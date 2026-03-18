# PARAMETER_REGISTRY.md
## Constants, Couplings, and Parameters

**Last updated:** 2026-03-17 (ROS v2 Session 1 — initial population from Reference Core §2, §5, §6)

---

## Fundamental Constants (Theory-Derived)

| Symbol | Value | Origin | Status |
|--------|-------|--------|--------|
| φ = (1+√5)/2 | 1.6180339887... | Jones index n=5 | [✓] Exact |
| Z = j(i)^{1/3} | 12 exactly | Modular j-invariant | [✓] Exact |
| s₀ = ln(12) | 2.48490665... nats | Z'(i)=0 saddle point | [✓] Exact |
| n (tower height) | 15 | K(G₂)+K(F₄) = h∨(E₈)/2 | [D] Not derived |

## Dual Coxeter Numbers

| Group | h∨ | K = 1+h∨ |
|-------|-----|-----------|
| E₈ | 30 | 31 |
| E₆ | 12 | 13 |
| SO(10) | 8 | 9 |
| SU(5) | 5 | 6 |
| F₄ | 9 | 10 |
| G₂ | 4 | 5 |
| SU(3) | 3 | 4 |
| SU(2) | 2 | 3 |

## Experimental Inputs (PDG)

| Quantity | Value | Source |
|----------|-------|--------|
| M_Pl | 1.22 × 10¹⁸ GeV | Standard |
| M_Z | 91.1876 GeV | PDG |
| M_W (obs) | 80.377 GeV | PDG |
| m_H (obs) | 125.1 GeV | PDG |
| m_t (pole) | 173 GeV | PDG |
| m_u | 2.0 MeV | PDG (MS-bar, 2 GeV) |
| m_d | 5.0 MeV | PDG (MS-bar, 2 GeV) |
| m_b | 4.18 GeV | PDG (MS-bar) |
| 1/α_em(M_Z) | 128.9 | PDG |
| 1/α₃(M_Z) obs | 8.50 | PDG |
| v (EW VEV) obs | 246.22 GeV | PDG |

## Planck-Scale Couplings (Predicted)

| Coupling | Formula | Value | Status |
|----------|---------|-------|--------|
| 1/α₃(M_Pl) | 4π × K(SU(3)) = 16π | 50.27 | [✓] |
| 1/α₂(M_Pl) | 4π × K(SU(2)) = 12π | 37.70 (bare) | [✓] |
| 1/α₁^GUT(M_Pl) | 4π × (5/3) | 20π/3 = 20.94 | [✓] |
| 1/α_em(M_Pl) | 4π × K(G₂) × ΣQ² = 100π/3 | 104.72 | [✓] |

## M_Z-Scale Couplings (Predicted)

| Coupling | Value | Observed | Match | Status |
|----------|-------|----------|-------|--------|
| 1/α_em(M_Pl) | 104.72 | 104.94 | 0.2% | [✓] |
| 1/α₂(M_Z) | 29.45 | 29.57 | 0.4% | [✓] ⚠×3 |
| 1/α₁(M_Z) | 61.33 | 59.00 | 3.9% | [✓] |
| 1/α₃(M_Z) bare | 8.90 | 8.50 | 4.7% → fitted | [✓] |
| sin²θ_W | 0.230 | 0.231 | 0.3% | [✓] |

## RG Beta Coefficients (SM)

| Coefficient | Value | Status |
|-------------|-------|--------|
| b₃ | −7 | [✓] |
| b₂ | −19/6 | [✓] |
| b₁ | +41/6 | [✓] |
| b₂^WZW | +38/3 | [⚠ unverified origin] |

## Paper 2 Parameters (§6)

| Parameter | Stored (inconsistent) | Tier-C-consistent | Status |
|-----------|----------------------|-------------------|--------|
| P_u × L | 2.71 | 5.401 | [⚠ F7] |
| Q_u × L | 1.61 | 3.188 | [⚠ F7] |
| P_d × L | 0.80 | 3.533 | [⚠ F7] |
| Q_d × L | 0.68 | 1.498 | [⚠ F7] |
| L = ln(M_Pl/v) | 36.14 | 36.14 | [✓] |

## Scales

| Scale | Value | Status |
|-------|-------|--------|
| M_GUT (used) | 5.7 × 10¹⁶ GeV | [⚠ input, not self-consistent] |
| M_GUT (WZW crossing) | 2.2 × 10¹⁶ GeV | [✓ computed] |
| M_T/M_GUT | 1.586 | [fitted for α₃] |
| 12¹⁵ | 1.541 × 10¹⁶ | [✓] |

---

*Update when new parameters are derived, corrected, or verified. Flag inconsistencies explicitly.*
