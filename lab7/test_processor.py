"""Hypothesis-based fuzz tests for the tennis scoring processor."""

import pytest
from hypothesis import given, settings, strategies as st

from processor import game_score, match_status, set_winner


non_integer = st.one_of(
    st.none(),
    st.booleans(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.text(),
    st.lists(st.integers()),
    st.dictionaries(st.text(), st.integers()),
)

fast_fuzz = settings(max_examples=60, deadline=None)


@fast_fuzz
@given(a=st.integers(min_value=0, max_value=30), b=st.integers(min_value=0, max_value=30))
def test_game_score_returns_a_valid_score_for_nonnegative_points(a, b):
    result = game_score(a, b)
    valid_results = {
        "0-0", "0-15", "0-30", "0-40", "15-0", "15-15", "15-30", "15-40",
        "30-0", "30-15", "30-30", "30-40", "40-0", "40-15", "40-30", "40-40",
        "deuce", "advantage A", "advantage B", "game A", "game B",
    }
    assert result in valid_results


@fast_fuzz
@given(value=non_integer)
def test_game_score_rejects_non_integer_points(value):
    with pytest.raises(TypeError, match="must be an integer"):
        game_score(value, 0)


@fast_fuzz
@given(value=st.integers(min_value=-1000, max_value=-1))
def test_game_score_rejects_negative_points(value):
    with pytest.raises(ValueError, match="must be non-negative"):
        game_score(value, 0)


@fast_fuzz
@given(a=st.integers(min_value=0, max_value=30), b=st.integers(min_value=0, max_value=30))
def test_set_winner_returns_a_valid_result_for_nonnegative_sets(a, b):
    assert set_winner(a, b) in {"A", "B", None}


@fast_fuzz
@given(value=non_integer)
def test_set_winner_rejects_non_integer_set_scores(value):
    with pytest.raises(TypeError, match="must be an integer"):
        set_winner(value, 0)


@fast_fuzz
@given(value=st.integers(min_value=-1000, max_value=-1))
def test_set_winner_rejects_negative_set_scores(value):
    with pytest.raises(ValueError, match="must be non-negative"):
        set_winner(value, 0)


@fast_fuzz
@given(
    sets_a=st.integers(min_value=0, max_value=10),
    sets_b=st.integers(min_value=0, max_value=10),
    best_of=st.sampled_from([1, 3, 5, 7, 9]),
)
def test_match_status_returns_a_valid_result_for_valid_inputs(sets_a, sets_b, best_of):
    assert match_status(sets_a, sets_b, best_of) in {
        "A wins", "B wins", "decider", "in progress"
    }


@fast_fuzz
@given(value=non_integer)
def test_match_status_rejects_non_integer_set_scores(value):
    with pytest.raises(TypeError, match="must be an integer"):
        match_status(value, 0, 3)


@fast_fuzz
@given(value=st.integers(min_value=-1000, max_value=-1))
def test_match_status_rejects_negative_set_scores(value):
    with pytest.raises(ValueError, match="must be non-negative"):
        match_status(value, 0, 3)


@fast_fuzz
@given(best_of=st.integers(min_value=-20, max_value=20).filter(lambda n: n <= 0 or n % 2 == 0))
def test_match_status_requires_positive_odd_best_of(best_of):
    with pytest.raises(ValueError, match="best_of must be a positive odd integer"):
        match_status(0, 0, best_of)
