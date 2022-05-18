from fastapi import FastAPI
from meatheadMath import *

app = FastAPI()


@app.get("/max/{reps, weight}")
def get_rm(reps: int, weight: int):
    rm = int(one_rep_max(reps, weight))
    return {"oneRepMax": rm}


@app.get("/ri/{reps, weight, one_rm}")
def get_rel(reps: int, weight: int, one_rm: int):
    rel_int = int(relative_intensity(reps, weight, one_rm))
    return {"rel_int": rel_int}


@app.get("/ri/{reps, desired_ri, one_rm}")
def get_new_weight(reps: int, desired_ri: int, one_rm: int):
    weight = new_weight(reps, desired_ri, one_rm)
    return {"new_weight": weight}
