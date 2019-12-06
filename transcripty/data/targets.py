"""
This file contains the calibration targets that we will use to find
the "optimal" parameters for the model
"""
import numpy as np

from collections import namedtuple


CPMParams = namedtuple("CPMParams", ["p", "sigma"])
HPMParams = namedtuple("HPMParams", ["gamma_min", "gamma_1", "gamma_2", "sigma"])


class CalibrationTargets(object):
    """
    This holds the calibration targets used for calibrating the model

    Parameters
    ----------
    credit_corr : float64
        The correlation between the credits earned in years 1 and 2
    y2_deciles_by_quartile : np.array((9, 5), float64)
        The 20/50/80 percent quantiles of total credits earned after
        two years for each gpa quartile

    Attributes
    ----------
    See parameters
    """
    def __init__(self, credit_corr, y2_deciles):
        self.credit_corr = credit_corr
        self.y2_deciles = y2_deciles

    def compare_results(self, gpa, credits, corrmult=25.0, normalize=False):
        """
        Compares the credit simulation results with the calibration
        targets

        Parameters
        ----------
        gpa : np.array((N,), float64)
            A simulation of gpa of N individuals
        credits : np.array((N, T_c), float64)
            A simulation of credits earned by N individuals over T_c
            periods
        corrmult : float64, optional(25.0)
            A multiplier used to scale the importance of the correlation
            between years 1 and 2
        normalize : bool, optional(false)
            If normalize is true then computes the percent difference
            in targets rather than absolute differences

        Returns
        -------
        diff : float64
            The 'score' of a particular simulation. The higher the
            score, the less we believe the parameters that generated
            the score
        """
        # Pull out the y1/y2 credits and compute total credits after
        # 2 years
        y1_credits = credits[:, 0]
        y2_credits = credits[:, 1]
        total_credits = y1_credits + y2_credits

        # Get the relevant moments from simulation data
        credit_corr_sim = np.corrcoef(y1_credits, y2_credits)[0, 1]
        y2_deciles_sim = np.quantile(total_credits, np.linspace(0.1, 0.9, 9))

        diff = 0.0
        if normalize:
            diff += corrmult*((100*credit_corr_sim/self.credit_corr) - 100.0)**2
            diff += np.sum(((100*y2_deciles_sim/self.y2_deciles) - 100.0)**2)
        else:
            diff += corrmult*((credit_corr_sim - self.credit_corr))**2
            diff += np.sum((y2_deciles_sim - self.y2_deciles)**2)

        return diff


HL_OPT_PARAMS = HPMParams(0.35, 0.6778, 1.0556, 0.0)

CREDIT_CORR_Y1Y2 = 0.4799253

Y2_DECILES = np.array([
    29.0, 41.0, 48.0, 53.37, 57.0, 60.0, 62.97, 66.0, 72.0
])

CT = CalibrationTargets(CREDIT_CORR_Y1Y2, Y2_DECILES)

