                "Check the API key, model name, quota, and hosting logs."
            ),
        )

    try:
        parsed = parse_groq_response(response)
    except ValueError as exc:
        logger.exception("Groq response parsing failed")
        raise HTTPException(status_code=502, detail=str(exc)) from exc

    job_summary = parsed.get("job_summary")
    model_candidates = parsed.get("candidates")

    if not isinstance(job_summary, dict) or not isinstance(model_candidates, list):
        raise HTTPException(
            status_code=502,
            detail="AI response is missing the job_summary or candidates list. Please retry.",
        )

    required_skills = safe_string_list(job_summary.get("required_skills"), limit=40, item_limit=100)
    # Remove duplicate skill labels without changing their order.
    required_skills = list(dict.fromkeys(required_skills))

    candidates_by_id: dict[str, dict[str, Any]] = {}
    for item in model_candidates:
        if isinstance(item, dict):
            candidate_id = clean_text(item.get("candidate_id"), 40)
            if candidate_id:
                candidates_by_id[candidate_id] = item

    final_candidates = []
    for index, resume in enumerate(resumes, start=1):
        model_candidate = candidates_by_id.get(resume["candidate_id"])
        if model_candidate is None:
            # Do not fabricate a 75% result. Report the incomplete AI response.
            raise HTTPException(
                status_code=502,
                detail=f"AI did not return a result for {resume['filename']}. Please retry.",
            )

        final_candidates.append(
            build_candidate(
                model_candidate=model_candidate,
                resume=resume,
                required_skills=required_skills,
                job_description=jd,
                rank=index,
            )
        )

    final_candidates.sort(key=lambda candidate: candidate["similarity_score"], reverse=True)
    for index, candidate in enumerate(final_candidates, start=1):
        candidate["rank"] = index

    score_values = [candidate["similarity_score"] for candidate in final_candidates]
    classifications = Counter(candidate["classification"] for candidate in final_candidates)
    skills_counter = Counter(
        skill
        for candidate in final_candidates
        for skill in candidate["matched_skills"]
    )

    result = {
        "job_summary": {
            "title": clean_text(job_summary.get("title"), 150) or "Position",
            "required_skills": required_skills,
            "preferred_skills": safe_string_list(
                job_summary.get("preferred_skills"), limit=30, item_limit=100
            ),
            "experience_required": clean_text(
                job_summary.get("experience_required"), 200
            ) or "Not specified",
            "education_required": clean_text(
                job_summary.get("education_required"), 200
            ) or "Not specified",
        },
        "candidates": final_candidates,
        "statistics": {
            "total_processed": len(final_candidates),
            "shortlisted": classifications.get("Shortlisted", 0),
            "under_review": classifications.get("Under Review", 0),
            "rejected": classifications.get("Rejected", 0),
            "average_score": round(sum(score_values) / len(score_values))
            if score_values else 0,
            "top_skills_found": [
                skill for skill, _ in skills_counter.most_common(10)
            ],
        },
        "file_errors": file_errors,
        "scoring_method": {
            "weights": {
                "skills": 40,
                "experience": 30,
                "education": 15,
                "keywords": 15,
            },
            "thresholds": {
                "shortlisted": "75-100",
                "under_review": "50-74",
                "rejected": "0-49",
            },
        },
    }
    return JSONResponse(content=result)


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port)
