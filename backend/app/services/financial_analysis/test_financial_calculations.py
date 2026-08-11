from financial_calculations import (
    calculate_annual_revenue,
    calculate_project_cost,
    calculate_payback_period,
    calculate_roi,
)


def test_financial_calculations():
    annual_energy_yield = 128450
    electricity_tariff = 9

    installed_capacity_mw = 1
    cost_per_mw = 42000000
    additional_installation_percentage = 0

    annual_revenue = calculate_annual_revenue(
        annual_energy_yield,
        electricity_tariff
    )

    project_cost = calculate_project_cost(
        installed_capacity_mw,
        cost_per_mw,
        additional_installation_percentage
    )

    payback_period = calculate_payback_period(
        project_cost,
        annual_revenue
    )

    roi = calculate_roi(
        project_cost,
        annual_revenue
    )

    print("Annual Revenue:", annual_revenue)
    print("Project Cost:", project_cost)
    print("Payback Period:", payback_period)
    print("ROI:", roi)


if __name__ == "__main__":
    test_financial_calculations()