"""
This file contains the calibration targets that we will use to find
the "optimal" parameters for the model
"""
import numpy as np

from collections import namedtuple


HBMParams = namedtuple("HBMParams", ["gamma_min", "gamma_1", "gamma_2"])


class CalibrationTargets(object):
    def __init__(self, credit_corr, y2_deciles):
        self.credit_corr = credit_corr
        self.y2_deciles = y2_deciles

    def compare_results(self, sims, corrmult=25.0, normalize=False):
        """
        """
        # Pull out the y1/y2 credits and compute total credits after
        # 2 years
        y1_credits = sims[:, 0]
        y2_credits = sims[:, 1]
        total_credits = y1_credits + y2_credits

        # Get the relevant moments from simulation data
        credit_corr_sim = np.corrcoef(y1_credits, y2_credits)[0, 1]
        y2_deciles_sim = np.quantile(total_credits, np.linspace(0.1, 0.9, 9))

        diff = 0.0
        if normalize:
            diff += ((100*credit_corr_sim/self.credit_corr) - 100.0)**2
            diff += np.sum(((100*y2_deciles_sim/y2_deciles) - 100.0)**2)
        else:
            diff += (corrmult*(credit_corr_sim - self.credit_corr))**2
            diff += np.sum((y2_deciles_sim - self.y2_deciles)**2)

        return diff


HL_OPT_PARAMS = HBMParams(0.35, 0.6778, 1.0556)

CREDIT_CORR_Y1Y2 = 0.4799253

Y2_DECILES = np.array([
    29.0, 41.0, 48.0, 53.37, 57.0, 60.0, 62.97, 66.0, 72.0
])

CT = CalibrationTargets(CREDIT_CORR_Y1Y2, Y2_DECILES)

