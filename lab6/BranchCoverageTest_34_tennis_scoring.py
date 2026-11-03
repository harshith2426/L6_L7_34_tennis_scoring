"""Tests covering both outcomes of decisions in tennis_scoring."""

import pytest

from tennis_scoring import game_score, match_status, set_winner


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0, 0, "0-0"),
        (1, 2, "15-30"),
        (3, 2, "40-30"),
        (2, 3, "30-40"),
        (3, 3, "deuce"),
        (4, 3, "advantage A"),
        (3, 4, "advantage B"),
        (5, 3, "game A"),
        (3, 5, "game B"),
        (4, 0, "game A"),
        (0, 4, "game B"),
    ],
)
def test_game_score_branches(a, b, expected):
    assert game_score(a, b) == expected


@pytest.mark.parametrize("a,b", [(-1, 0), (0, -1)])
def test_game_score_negative_input_branches(a, b):
    with pytest.raises(ValueError, match="negative points"):
        game_score(a, b)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 0, "A"),
        (0, 6, "B"),
        (7, 6, "A"),
        (6, 7, "B"),
        (6, 5, None),
        (5, 6, None),
        (4, 4, None),
    ],
)
def test_set_winner_branches(a, b, expected):
    assert set_winner(a, b) == expected


@pytest.mark.parametrize(
    "sets_a,sets_b,best_of,expected",
    [
        (2, 0, 3, "A wins"),
        (0, 2, 3, "B wins"),
        (1, 1, 3, "decider"),
        (0, 0, 3, "in progress"),
    ],
)
def test_match_status_branches(sets_a, sets_b, best_of, expected):
    assert match_status(sets_a, sets_b, best_of) == expected
