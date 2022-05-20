from fastapi import FastAPI
import meatheadMath as mm

app = FastAPI()


@app.get("/max/{reps, weight}")
def get_rm(reps: int, weight: float) -> dict:
    """Calculate the max weight for one rep

    Args:
        reps (int): Number of reps
        weight (float): Weight of the lifts

    Returns:
        dict: dictionary of the one rep max
    """
    rm = int(mm.one_rep_max(reps, weight))
    return {"oneRepMax": rm}


@app.get("/ri/{reps, weight, one_rm}")
def get_rel(reps: int, weight: float, one_rm: float) -> dict:
    """Calculate the relative intensity

    Args:
        reps (int): Number of reps
        weight (float): Weigt of the lifts
        one_rm (float): One rep max

    Returns:
        dict: dictionary of the relative intensity
    """

    rel_int = int(mm.relative_intensity(reps, weight, one_rm))
    return {"rel_int": rel_int}


@app.get("/ri/{reps, desired_ri, one_rm}")
def get_new_weight(reps: int, desired_ri: float, one_rm: float) -> dict:
    """Calculate the new weight for a lift

    Args:
        reps (int): Number of reps
        desired_ri (float): Desired relative intensity
        one_rm (float): One rep max

    Returns:
        dict: dictionary of the new weight
    """

    weight = mm.new_weight(reps, desired_ri, one_rm)
    return {"new_weight": weight}
