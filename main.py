# main.py

import matplotlib.pyplot as plt
from src.exposure.montecarlo_forward_simulator import simulate_forward_paths, calculate_expected_exposure
from src.credit.cva_dva_calculator import (
    bootstrap_survival_curve,
    compute_discount_factors,
    compute_cva,
    compute_dva
)

# Parameters
S0 = 100             # Initial asset value
mu = 0.01            # Drift (risk-free rate / forward rate)
sigma = 0.2          # Volatility
T = 1.0              # Maturity in years
r = 0.01             # Risk-free rate
hazard_rate = 0.02   # Flat hazard rate
lgd = 0.6            # Loss given default

# Simulate exposure
paths, time_grid = simulate_forward_paths(S0=S0, mu=mu, sigma=sigma, T=T)
exposure_df = calculate_expected_exposure(paths)

# Compute survival curve and discount factors
survival_probs = bootstrap_survival_curve(hazard_rate, time_grid)
discount_factors = compute_discount_factors(r, time_grid)

# Calculate CVA and DVA
cva = compute_cva(
    epe=exposure_df["EPE"].values,
    survival_probs=survival_probs,
    discount_factors=discount_factors,
    lgd=lgd
)

dva = compute_dva(
    ene=exposure_df["ENE"].values,
    survival_probs=survival_probs,
    discount_factors=discount_factors,
    lgd=lgd
)

# Output results
print("Counterparty Credit Risk Results")
print("----------------------------------")
print(f"CVA: {cva:.4f}")
print(f"DVA: {dva:.4f}")

# Plot expected exposure profile
plt.figure(figsize=(10, 6))
plt.plot(time_grid, exposure_df["EPE"], label="EPE (Expected Positive Exposure)", color="green")
plt.plot(time_grid, exposure_df["ENE"], label="ENE (Expected Negative Exposure)", color="red")
plt.plot(time_grid, exposure_df["EE"], label="EE (Expected Exposure)", color="gray", linestyle="--")
plt.xlabel("Time (Years)")
plt.ylabel("Exposure Value")
plt.title("Simulated Exposure Profiles")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and show plot
plt.savefig("exposure_profiles.png", dpi=300)
print("Exposure profile plot saved as exposure_profiles.png")
plt.show()
