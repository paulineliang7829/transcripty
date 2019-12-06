import numpy as np
import scipy.optimize as opt

from hyperopt import fmin, tpe, Trials
from hyperopt import hp
from functools import partial

from .targets import CalibrationTargets, CT, CPMParams, HPMParams, HL_OPT_PARAMS
from ..probabilitymodels import (
    CommonProbabilityModel, HeterogeneousProbabilityModel
)


def CPMobjective(params, target):
    # Create and simulate the model to get samples of gpa and credits
    model = CommonProbabilityModel(*params, 6, 12, 3, 125)
    a_i, gpa_i, credits = model.simulate(25000)
    return target.compare_results(gpa_i, credits, corrmult=0.25, normalize=True)


def calibrateCPM(target=CT, nevals=500):
    f = partial(CPMobjective, target=CT)
    space = [
        hp.uniform("p", 0.01, 0.99),
        hp.uniform("sigma", 1e-4, 2.0)
    ]
    tpe_trials = Trials()
    parameters = fmin(
        fn=f, space=space, algo=tpe.suggest, trials=tpe_trials, max_evals=nevals
    )

    return parameters, tpe_trials


def HPMobjective(params, target):
    model = HeterogeneousProbabilityModel(*params, 6, 12, 3, 125)
    a_i, gpa_i, credits = model.simulate(25000)
    return target.compare_results(gpa_i, credits, corrmult=1.00, normalize=True)


def calibrateHPM(target=CT, nevals=500):
    f = partial(HPMobjective, target=CT)
    space = [
        hp.uniform("gamma_min", 0.05, 0.60),
        hp.uniform("gamma_1", 0.20, 2.5),
        hp.uniform("gamma_2", 0.20, 2.5),
        hp.uniform("sigma", 1e-4, 1.0)
    ]
    tpe_trials = Trials()
    parameters = fmin(
        fn=f, space=space, algo=tpe.suggest, trials=tpe_trials, max_evals=nevals
    )

    return parameters, tpe_trials

