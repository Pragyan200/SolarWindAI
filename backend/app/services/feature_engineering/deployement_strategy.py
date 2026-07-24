def recommend_deployment(solar_class: str, wind_class: str) -> str:
    """
    Recommend the best deployment type based on solar and wind quality.
    """

    if solar_class == "Excellent" and wind_class == "Excellent":
        return "Hybrid"
    elif solar_class == "Excellent":
        return "Solar"
    elif wind_class == "Excellent":
        return "Wind"
    else:
        return "Hybrid"


def generate_reason(solar_class: str, wind_class: str) -> str:
    """
    Generate a human-readable explanation for the deployment recommendation.
    """

    if solar_class == "Excellent" and wind_class == "Excellent":
        return "High solar irradiance and consistently strong wind resource."
    elif solar_class == "Excellent":
        return "Excellent solar resource with limited wind potential."
    elif wind_class == "Excellent":
        return "Excellent wind resource with limited solar potential."
    else:
        return "Moderate renewable resources. A hybrid system can improve overall energy generation."


def confidence_score(solar_class: str, wind_class: str) -> int:
    """
    Return a confidence score (0-100) for the deployment recommendation.
    """

    if solar_class == "Excellent" and wind_class == "Excellent":
        return 91
    elif solar_class == "Excellent" or wind_class == "Excellent":
        return 85
    elif solar_class == "Good" or wind_class == "Good":
        return 75
    else:
        return 60


def get_deployment_recommendation(solar_class: str, wind_class: str) -> dict:
    """
    Generate the complete deployment recommendation.
    """

    deployment = recommend_deployment(solar_class, wind_class)
    confidence = confidence_score(solar_class, wind_class)
    reason = generate_reason(solar_class, wind_class)

    return {
        "deployment": deployment,
        "confidence": confidence,
        "reason": reason
    }