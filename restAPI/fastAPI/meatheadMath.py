import math


def one_rep_max(reps, weight):
    rm = weight / (1.0278 - 0.0278 * reps)
    return rm


def relative_intensity(reps, weight, one_rm):
    max_weight = one_rm * (1.0278 - 0.0278 * reps)
    ai = (weight) / one_rm
    ri = ai / (max_weight / one_rm)
    return 100 * ri


def new_weight(reps, desired_ri, one_rm):
    mi = 1.0278 - 0.0278 * reps
    new_ai = math.floor(mi * (desired_ri)) / 100
    new_weight = int(new_ai * one_rm)
    return new_weight
