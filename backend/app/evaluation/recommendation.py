def get_recommendation(score: float) -> str:
    """
    Convert a suitability score into a recommendation.
    """

    if score >= 85:
        return "Highly Suitable"
    elif score >= 70:
        return "Suitable"
    elif score >= 50:
        return "Moderately Suitable"
    else:
        return "Not Recommended"