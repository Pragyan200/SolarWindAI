"""
Energy Estimation Service
"""

OPERATING_HOURS = 8760  # Hours in one year


def estimate_solar_energy(
    installed_capacity: float,
    capacity_factor: float
) -> float:
    """
    Estimate annual solar energy generation.

    Formula:
    Annual Energy = Installed Capacity × Capacity Factor × 8760

    Args:
        installed_capacity: Capacity in MW (or kW if used consistently)
        capacity_factor: Decimal value (e.g. 0.20 for 20%)

    Returns:
        Estimated annual energy generation
    """
    return installed_capacity * capacity_factor * OPERATING_HOURS


def estimate_wind_energy(
    installed_capacity: float,
    capacity_factor: float
) -> float:
    """
    Estimate annual wind energy generation.

    Formula:
    Annual Energy = Installed Capacity × Capacity Factor × 8760

    Args:
        installed_capacity: Capacity in MW (or kW if used consistently)
        capacity_factor: Decimal value (e.g. 0.35 for 35%)

    Returns:
        Estimated annual energy generation
    """
    return installed_capacity * capacity_factor * OPERATING_HOURS


def estimate_energy(
    site_result: str,
    deployment_type: str,
    installed_capacity: float,
    solar_capacity_factor: float = 0.20,
    wind_capacity_factor: float = 0.35,
):
    """
    Estimate annual energy generation for Solar, Wind, or Hybrid deployments.

    Args:
        site_result: Site evaluation result (e.g. "Suitable")
        deployment_type: "Solar", "Wind", or "Hybrid"
        installed_capacity: Installed capacity
        solar_capacity_factor: Solar capacity factor
        wind_capacity_factor: Wind capacity factor

    Returns:
        Dictionary containing estimated annual energy values.
    """

    solar_energy = 0.0
    wind_energy = 0.0

    deployment = deployment_type.lower()

    if deployment == "solar":
        solar_energy = estimate_solar_energy(
            installed_capacity,
            solar_capacity_factor
        )

    elif deployment == "wind":
        wind_energy = estimate_wind_energy(
            installed_capacity,
            wind_capacity_factor
        )

    elif deployment == "hybrid":
        solar_energy = estimate_solar_energy(
            installed_capacity,
            solar_capacity_factor
        )
        wind_energy = estimate_wind_energy(
            installed_capacity,
            wind_capacity_factor
        )

    total_energy = solar_energy + wind_energy

    return {
        "site_result": site_result,
        "deployment_type": deployment_type,
        "installed_capacity": installed_capacity,
        "estimated_annual_solar_energy": round(solar_energy, 2),
        "estimated_annual_wind_energy": round(wind_energy, 2),
        "total_estimated_annual_energy": round(total_energy, 2),
    }