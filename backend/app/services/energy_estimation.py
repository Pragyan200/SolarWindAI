"""
Energy Yield Estimation Service

Provides modular estimation of annual energy generation
for solar, wind, and hybrid renewable energy systems.
"""

OPERATING_HOURS = 8760


def _validate_inputs(
    installed_capacity: float,
    capacity_factor: float,
    system_efficiency: float
) -> None:
    """Validate common energy estimation inputs."""

    if installed_capacity < 0:
        raise ValueError("Installed capacity cannot be negative.")

    if not 0 <= capacity_factor <= 1:
        raise ValueError("Capacity factor must be between 0 and 1.")

    if not 0 < system_efficiency <= 1:
        raise ValueError(
            "System efficiency must be greater than 0 and at most 1."
        )


def estimate_solar_energy(
    installed_capacity: float,
    capacity_factor: float,
    system_efficiency: float = 0.90
) -> float:
    """
    Estimate annual solar energy generation.

    Returns energy in MWh/year when capacity is provided in MW.
    """

    _validate_inputs(
        installed_capacity,
        capacity_factor,
        system_efficiency
    )

    return (
        installed_capacity
        * capacity_factor
        * system_efficiency
        * OPERATING_HOURS
    )


def estimate_wind_energy(
    installed_capacity: float,
    capacity_factor: float,
    system_efficiency: float = 0.90
) -> float:
    """
    Estimate annual wind energy generation.

    Returns energy in MWh/year when capacity is provided in MW.
    """

    _validate_inputs(
        installed_capacity,
        capacity_factor,
        system_efficiency
    )

    return (
        installed_capacity
        * capacity_factor
        * system_efficiency
        * OPERATING_HOURS
    )


def estimate_hybrid_energy(
    solar_installed_capacity: float,
    wind_installed_capacity: float,
    solar_capacity_factor: float = 0.20,
    wind_capacity_factor: float = 0.35,
    system_efficiency: float = 0.90
) -> dict:
    """
    Estimate annual energy generation for a hybrid
    solar-wind system.
    """

    solar_energy = estimate_solar_energy(
        solar_installed_capacity,
        solar_capacity_factor,
        system_efficiency
    )

    wind_energy = estimate_wind_energy(
        wind_installed_capacity,
        wind_capacity_factor,
        system_efficiency
    )

    return {
        "solar_energy": round(solar_energy, 2),
        "wind_energy": round(wind_energy, 2),
        "total_energy": round(
            solar_energy + wind_energy,
            2
        )
    }


def estimate_energy(
    site_result: str,
    deployment_type: str,
    installed_capacity: float,
    solar_capacity_factor: float = 0.20,
    wind_capacity_factor: float = 0.35,
    system_efficiency: float = 0.90,
    solar_capacity_share: float = 0.50
) -> dict:
    """
    Estimate annual energy generation for Solar, Wind,
    or Hybrid deployment.
    """

    if not 0 <= solar_capacity_share <= 1:
        raise ValueError(
            "Solar capacity share must be between 0 and 1."
        )

    deployment = deployment_type.lower()

    solar_energy = 0.0
    wind_energy = 0.0

    if deployment == "solar":

        solar_energy = estimate_solar_energy(
            installed_capacity,
            solar_capacity_factor,
            system_efficiency
        )

    elif deployment == "wind":

        wind_energy = estimate_wind_energy(
            installed_capacity,
            wind_capacity_factor,
            system_efficiency
        )

    elif deployment == "hybrid":

        solar_capacity = (
            installed_capacity * solar_capacity_share
        )

        wind_capacity = (
            installed_capacity * (1 - solar_capacity_share)
        )

        hybrid_result = estimate_hybrid_energy(
            solar_installed_capacity=solar_capacity,
            wind_installed_capacity=wind_capacity,
            solar_capacity_factor=solar_capacity_factor,
            wind_capacity_factor=wind_capacity_factor,
            system_efficiency=system_efficiency
        )

        solar_energy = hybrid_result["solar_energy"]
        wind_energy = hybrid_result["wind_energy"]

    else:
        raise ValueError(
            "deployment_type must be Solar, Wind, or Hybrid."
        )

    total_energy = solar_energy + wind_energy

    return {
        "site_result": site_result,
        "deployment_type": deployment_type,
        "installed_capacity": installed_capacity,
        "system_efficiency": system_efficiency,
        "estimated_annual_solar_energy": round(
            solar_energy, 2
        ),
        "estimated_annual_wind_energy": round(
            wind_energy, 2
        ),
        "total_estimated_annual_energy": round(
            total_energy, 2
        )
    }