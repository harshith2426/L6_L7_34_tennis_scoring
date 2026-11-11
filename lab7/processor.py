"""Tennis scoring processor with input validation (Lab 7 fixed version)."""

POINTS = ["0", "15", "30", "40"]


def _require_nonnegative_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def game_score(a, b):
    _require_nonnegative_integer(a, "a")
    _require_nonnegative_integer(b, "b")
    if a >= 3 and b >= 3:
        if a == b:
            return "deuce"
        if a - b >= 2:
            return "game A"
        if b - a >= 2:
            return "game B"
        if a > b:
            return "advantage A"
        return "advantage B"
    if a >= 4:
        return "game A"
    if b >= 4:
        return "game B"
    return POINTS[a] + "-" + POINTS[b]


def set_winner(a, b):
    _require_nonnegative_integer(a, "a")
    _require_nonnegative_integer(b, "b")
    if a >= 6 and a - b >= 2:
        return "A"
    if b >= 6 and b - a >= 2:
        return "B"
    if a == 7 and b == 6:
        return "A"
    if b == 7 and a == 6:
        return "B"
    return None


def match_status(sets_a, sets_b, best_of):
    _require_nonnegative_integer(sets_a, "sets_a")
    _require_nonnegative_integer(sets_b, "sets_b")
    if (
        isinstance(best_of, bool)
        or not isinstance(best_of, int)
        or best_of <= 0
        or best_of % 2 == 0
    ):
        raise ValueError("best_of must be a positive odd integer")
    needed = best_of // 2 + 1
    if sets_a == needed:
        return "A wins"
    if sets_b == needed:
        return "B wins"
    if sets_a == needed - 1 and sets_b == needed - 1:
        return "decider"
    return "in progress"


def main():
    print("Tennis scoring processor demonstration (validated version)")
    print(f"game_score(3, 3): {game_score(3, 3)}")
    print(f"set_winner(6, 2): {set_winner(6, 2)}")
    print(f"match_status(2, 1, 3): {match_status(2, 1, 3)}")
    try:
        game_score(True, 0)
    except (TypeError, ValueError) as error:
        print(f"invalid boolean score rejected: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
