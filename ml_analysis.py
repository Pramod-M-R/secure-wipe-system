def compute_recoverability_score(before_count, after_count, hash_changed):
    if before_count == 0:
        return 0, "NO DATA", "UNKNOWN"

    # Score calculation
    score = (before_count - after_count) / before_count

    # Security level
    if score > 0.8:
        level = "HIGH SECURITY"
    elif score > 0.5:
        level = "MEDIUM SECURITY"
    else:
        level = "LOW SECURITY"

    # Prediction (ML-style classification)
    if after_count == 0 and hash_changed:
        prediction = "NOT RECOVERABLE"
    elif after_count < before_count:
        prediction = "PARTIALLY RECOVERABLE"
    else:
        prediction = "RECOVERABLE"

    return round(score, 2), level, prediction