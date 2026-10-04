import pandas as pd


def calculate_clearing_price(
    period_data: pd.DataFrame,
    demand: float,
) -> float:
    """
    Return the marginal bid price required to meet demand
    for a single trading period.

    period_data must contain:
        - cumulative_bid_volume
        - bid_price
    """

    # Prevent empty input df
    if period_data.empty:
        raise ValueError("Offer stack is empty.")
    # Prevent invalid demand
    if demand < 0:
        raise ValueError("Demand must be greater than zero.")
    # prevent 
    if not period_data[
        "cumulative_bid_volume"
    ].is_monotonic_increasing:
        raise ValueError(
            "Cumulative bid volume must be increasing."
        )

    total_capacity = period_data[
        "cumulative_bid_volume"
    ].max()

    if demand > total_capacity:
        raise ValueError(
            f"Demand ({demand:.2f} MW) exceeds total offered "
            f"capacity ({total_capacity:.2f} MW)."
        )

    marginal_bid = period_data.loc[
        period_data["cumulative_bid_volume"] >= demand
    ].iloc[0]

    return float(marginal_bid["bid_price"])