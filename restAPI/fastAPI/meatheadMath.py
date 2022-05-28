def one_rep_max(reps: int, weight: float) -> float:
    """Calculate the one rep max
    TODO we should include the paper for the calibration factors in all the formulas somewhere.

    Args:
        reps (int): Number of reps
        weight (float): Weight of the lifts

    Returns:
        float: One rep max
    """
    return  weight / (1.0278 - 0.0278 * reps)


def relative_intensity(reps: int, weight: float, one_rm: float) -> float:
    """Calculate the relative intensity

    Args:
        reps (int): Number of reps
        weight (float): Weight of the lifts
        one_rm (float): One rep max

    Returns:
        float: relative intensity
    """
    max_weight = one_rm * (1.0278 - 0.0278 * reps)
    ai = (weight) / one_rm
    ri = ai / (max_weight / one_rm)
    return 100 * ri


def new_weight(reps: int, desired_ri: float, one_rm: float) -> int:
    """Calculate the new weight for a lift

    Args:
        reps (int): Number of reps
        desired_ri (float): Desired relative intensity
        one_rm (float): One rep max

    Returns:
        int: New weights
    """
    mi = 1.0278 - 0.0278 * reps
    new_ai = int(mi * (desired_ri)) / 100
    return int(new_ai * one_rm)
    