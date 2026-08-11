def calculate_annual_revenue(
    annual_energy_yield: float,
    electricity_tariff: float
) -> float:
    """
    Calculate estimated annual revenue.

    Annual Revenue = Annual Energy Yield × Electricity Tariff
    """

    if annual_energy_yield < 0:
        raise ValueError("Annual energy yield cannot be negative.")

    if electricity_tariff < 0:
        raise ValueError("Electricity tariff cannot be negative.")

    return annual_energy_yield * electricity_tariff


def calculate_project_cost(
    installed_capacity_mw: float,
    cost_per_mw: float,
    additional_installation_percentage: float = 0.0
) -> float:
    """
    Calculate estimated total project cost.
    """

    if installed_capacity_mw <= 0:
        raise ValueError("Installed capacity must be greater than zero.")

    if cost_per_mw < 0:
        raise ValueError("Cost per MW cannot be negative.")

    if additional_installation_percentage < 0:
        raise ValueError(
            "Additional installation percentage cannot be negative."
        )

    base_cost = installed_capacity_mw * cost_per_mw

    additional_cost = (
        base_cost * additional_installation_percentage / 100
    )

    return base_cost + additional_cost


def calculate_payback_period(
    total_project_cost: float,
    annual_revenue: float
) -> float:
    """
    Calculate estimated payback period in years.
    """

    if total_project_cost < 0:
        raise ValueError("Total project cost cannot be negative.")

    if annual_revenue <= 0:
        raise ValueError("Annual revenue must be greater than zero.")

    return total_project_cost / annual_revenue


def calculate_roi(
    total_project_cost: float,
    annual_revenue: float
) -> float:
    """
    Calculate Return on Investment (ROI) as a percentage.
    """

    if total_project_cost <= 0:
        raise ValueError("Total project cost must be greater than zero.")

    return (annual_revenue / total_project_cost) * 100