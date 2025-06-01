# src/exposure/montecarlo_forward_simulator.py

import numpy as np
import pandas as pd

def simulate_forward_paths(
    S0, mu, sigma, T, num_paths=10000, num_steps=250, seed=None
):
    """
    Simulates forward exposure paths using Geometric Brownian Motion (GBM).

    Parameters:
    - S0: initial value (e.g., FX rate or interest rate)
    - mu: drift (risk-free rate or forward rate)
    - sigma: volatility
    - T: maturity in years
    - num_paths: number of simulation paths
    - num_steps: time steps (e.g., 250 = daily)
    - seed: random seed for reproducibility

    Returns:
    - paths: (num_paths x num_steps+1) matrix of simulated values
    - time_grid: (num_steps+1,) array of time points
    """
    if seed is not None:
        np.random.seed(seed)

    dt = T / num_steps
    time_grid = np.linspace(0, T, num_steps + 1)

    paths = np.zeros((num_paths, num_steps + 1))
    paths[:, 0] = S0

    randn = np.random.normal(0, 1, size=(num_paths, num_steps))

    for t in range(1, num_steps + 1):
        paths[:, t] = paths[:, t - 1] * np.exp(
            (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * randn[:, t - 1]
        )

    return paths, time_grid


def calculate_expected_exposure(paths):
    """
    Computes Expected Exposure (EE) and Expected Positive/Negative Exposure.

    Returns:
    - DataFrame with EE, EPE, ENE over time
    """
    exposure = pd.DataFrame(paths)
    ee = exposure.mean(axis=0)
    epe = exposure.clip(lower=0).mean(axis=0)
    ene = exposure.clip(upper=0).mean(axis=0)
    return pd.DataFrame({
        "EE": ee,
        "EPE": epe,
        "ENE": ene
    })
