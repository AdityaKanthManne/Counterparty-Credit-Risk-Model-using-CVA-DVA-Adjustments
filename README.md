# Counterparty Credit Risk Model using CVA and DVA Adjustments

This project models counterparty credit risk for over-the-counter (OTC) derivative contracts by estimating Credit Valuation Adjustment (CVA) and Debit Valuation Adjustment (DVA). The framework simulates forward exposure paths, derives survival probabilities from credit spreads or hazard rates, and discounts expected losses over time using risk-neutral valuation.

---

## Objectives

- Simulate potential exposure profiles (EE, EPE, ENE) for derivatives such as FX Forwards and Interest Rate Swaps
- Compute CVA as the discounted expected loss from counterparty default
- Compute DVA as the adjustment for the user's own credit risk
- Use bootstrapped survival curves from credit default swap (CDS) spreads
- Account for ISDA netting, threshold/collateral agreements

---

## Key Components

| Component           | Description                                                      |
|--------------------|------------------------------------------------------------------|
| Exposure Simulation | Monte Carlo paths of mark-to-market values                      |
| CVA Calculation     | Expected exposure × default probability × loss given default     |
| DVA Calculation     | Symmetric method for user's own credit risk                     |
| Discounting         | Continuous discounting using risk-free rate curves              |
| Survival Curves     | Derived from hazard rates or bootstrapped CDS spreads           |

---

## Use Cases

- Measuring credit risk impact of derivatives on balance sheets
- Enhancing pricing models for OTC contracts
- Stress testing counterparty risk under correlation/volatility shocks

---

## Tech Stack

- Python (NumPy, pandas, matplotlib)
- Scipy (for integration, interpolation, bootstrapping)
- Free/Mock CDS data and discount curves
- Optional: Streamlit dashboard for visualization

---

## Run Instructions

```bash
git clone https://github.com/AdityaKanthManne/Counterparty-Credit-Risk-Model-using-CVA-DVA-Adjustments.git
cd Counterparty-Credit-Risk-Model-using-CVA-DVA-Adjustments
pip install -r requirements.txt
python main.py
```

---

## Output

- Time-bucketed exposure profiles (EE, EPE, ENE)
- CVA and DVA values over tenor
- Risk driver sensitivities (credit spread, correlation, LGD)
- Exposure vs survival probability plots

---

## License

MIT License © 2025 Aditya Kanth Manne  
https://github.com/AdityaKanthManne

---

## Contributions

Suggestions and pull requests are welcome. Extend this model for XVA, WWR, collateralization, or Basel III CCR compliance.
