# src/credit/cva_dva_calculator.py

import numpy as np

def bootstrap_survival_curve(hazard_rate, time_grid):
    """
    Computes survival probabilities from a flat hazard rate.

    Parameters:
    - hazard_rate: flat hazard rate (e.g., 0.02 for 2%)
    - time_grid: array of time points

    Returns:
    - survival_probs: array of survival probabilities
    """
    return np.exp(-hazard_rate * time_grid)


def compute_discount_factors(r, time_grid):
    """
    Computes discount factors using a flat risk-free rate.

    Parameters:
    - r: risk-free rate (e.g., 0.01 for 1%)
    - time_grid: array of time points

    Returns:
    - discount_factors: array of discount factors
    """
    return np.exp(-r * time_grid)


def compute_cva(epe, survival_probs, discount_factors, lgd=0.6):
    """
    Computes Credit Valuation Adjustment (CVA) as a discounted sum of
    exposure × default probability × LGD.

    Parameters:
    - epe: expected positive exposure (array)
    - survival_probs: array of survival probabilities
    - discount_factors: array of discount factors
    - lgd: loss given default (typically 0.6)

    Returns:
    - CVA value
    """
    default_probs = -np.diff(survival_probs, prepend=1.0)
    cva = np.sum(epe * default_probs * discount_factors) * lgd
    return cva


def compute_dva(ene, survival_probs, discount_factors, lgd=0.6):
    """
    Computes Debit Valuation Adjustment (DVA) using own ENE.

    Parameters:
    - ene: expected negative exposure (array)
    - survival_probs: array of survival probabilities
    - discount_factors: array of discount factors
    - lgd: assumed loss given default of the firm

    Returns:
    - DVA value
    """
    default_probs = -np.diff(survival_probs, prepend=1.0)
    dva = np.sum(np.abs(ene) * default_probs * discount_factors) * lgd
    return dva
