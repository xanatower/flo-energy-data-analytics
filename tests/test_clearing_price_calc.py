import pandas as pd
import pytest

from src.market_clearing_calculation import calculate_clearing_price


@pytest.fixture
def period_data():
    return pd.DataFrame(
        {
            "cumulative_bid_volume": [
                100.0,
                300.0,
                600.0,
                1000.0,
            ],
            "bid_price": [
                -100.0,
                0.0,
                50.0,
                200.0,
            ],
        }
    )


def test_clearing_price_within_tranche(period_data):
    result = calculate_clearing_price(
        period_data=period_data,
        demand=450.0,
    )

    assert result == 50.0


def test_clearing_price_on_exact_boundary(period_data):
    result = calculate_clearing_price(
        period_data=period_data,
        demand=300.0,
    )

    assert result == 0.0


def test_demand_above_total_capacity_raises(period_data):
    with pytest.raises(
        ValueError,
        match="exceeds total offered capacity",
    ):
        calculate_clearing_price(
            period_data=period_data,
            demand=1100.0,
        )


@pytest.mark.parametrize(
    "demand",
    [0.0, -100.0],
)
def test_non_positive_demand_raises(
    period_data,
    demand,
):
    with pytest.raises(
        ValueError,
        match="Demand must be greater than zero",
    ):
        calculate_clearing_price(
            period_data=period_data,
            demand=demand,
        )


def test_empty_offer_stack_raises():
    with pytest.raises(
        ValueError,
        match="Offer stack is empty",
    ):
        calculate_clearing_price(
            period_data=pd.DataFrame(),
            demand=100.0,
        )


def test_non_monotonic_cumulative_volume_raises():
    invalid_period_data = pd.DataFrame(
        {
            "cumulative_bid_volume": [
                100.0,
                600.0,
                300.0,
            ],
            "bid_price": [
                -100.0,
                50.0,
                100.0,
            ],
        }
    )

    with pytest.raises(
        ValueError,
        match="Cumulative bid volume must be increasing",
    ):
        calculate_clearing_price(
            period_data=invalid_period_data,
            demand=250.0,
        )