def recommend_deployment(site_score, solar_score, wind_score):
    """
    Recommend Solar, Wind, or Hybrid deployment.
    """

    if solar_score >= 80 and wind_score >= 80:
        return "Hybrid Deployment"
    elif solar_score >= wind_score:
        return "Solar Deployment"
    else:
        return "Wind Deployment"





def recommend_capacity(land_area, resource_score):
    """
    Estimate recommended installation capacity (MW).
    """

    if land_area >= 100 and resource_score >= 80:
        return 100
    elif land_area >= 50 and resource_score >= 70:
        return 50
    elif land_area >= 20:
        return 20
    else:
        return 5



def recommend_capacity(land_area, resource_score):
    """
    Estimate recommended installation capacity (MW).
    """

    if land_area >= 100 and resource_score >= 80:
        return 100
    elif land_area >= 50 and resource_score >= 70:
        return 50
    elif land_area >= 20:
        return 20
    else:
        return 5


def expansion_feasibility(land_area, available_land):
    """
    Determine whether the site can be expanded in the future.
    """

    if available_land >= land_area * 0.5:
        return "Expandable"
    elif available_land >= land_area * 0.2:
        return "Limited Expansion"
    else:
        return "Not Expandable"


def generate_deployment_plan(site_score, solar_score, wind_score, land_area, available_land):
    """
    Generate complete deployment plan.
    """

    technology = recommend_deployment(
        site_score,
        solar_score,
        wind_score
    )

    if technology == "Solar Deployment":
        resource_score = solar_score
    elif technology == "Wind Deployment":
        resource_score = wind_score
    else:
        resource_score = max(solar_score, wind_score)

    capacity = recommend_capacity(
        land_area,
        resource_score
    )

    expansion = expansion_feasibility(
        land_area,
        available_land
    )

    remarks = (
        f"Recommended {technology} with {capacity} MW capacity. "
        f"Future expansion status: {expansion}."
    )

    return {
        "recommended_technology": technology,
        "recommended_capacity": capacity,
        "expansion_status": expansion,
        "optimization_remarks": remarks
    }