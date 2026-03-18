# E₈ Workstream: WS-α₃ — Two-Stage RG for the Strong Coupling
## Priority 3 in Research Plan

**Status:** Stalled — two-stage WZW ruled out; all standard corrections wrong sign; doublet-triplet threshold is only candidate but M_T/M_GUT not derivable from current framework (see §4 Session 4); pending decision on Tier C demotion  
**Goal:** Apply the same two-stage WZW/RG treatment to α₃ that was done for α₂, reducing the 5.2% error.  
**Current prediction:** 1/α₃(M_Z) = 8.94 (observed 8.50, error +5.2%)

---

## 1. The Problem

The current α₃ derivation uses single-stage RG: bare value 1/α₃(M_Pl) = 16π, then SM running all the way to M_Z. But between M_Pl and M_GUT (≈ 5.7×10¹⁶ GeV), the full E₈ matter content is active, not just the SM. The α₂ derivation (Notebook 2, §3) showed this matters: the E₈ beta function for SU(2) is b₂^{WZW} = +38/3, dramatically different from the SM value b₂ = −19/6.

The same two-stage treatment should apply to SU(3)_c.

---

## 2. What Needs to Be Computed

### Step 1: Decompose 248 of E₈ under SU(3)_c

All SU(3)_c generators live in the F₄ sector (none in G₂ — see Notebook 2, §5/WL3-B). Need the SU(3)_c representation content of the full 248.

Under E₈ → SU(3)_fam × E₆ → SU(3)_fam × SU(3)_c × ...:

From the 78 of E₆ (gauge sector):
- Contains SU(3)_c gauge bosons (adjoint 8) and various representations

From the 3 × (27 + 27̄) of E₆ (matter sector, 3 families):
- Each 27 decomposes under SU(5) → SU(3)_c as: 10 → (3̄+3+1), 5̄ → (3̄+1+1), 1 → 1

**Need:** Total Dynkin index T_total for SU(3)_c from ALL 248 states.

### Step 2: Compute b₃^{WZW}

```
b₃^{WZW} = −(11/3) × C₂(SU(3)) + (2/3) × T_total
          = −(11/3)(3) + (2/3)(T_total)
          = −11 + (2/3)(T_total)
```

### Step 3: Run Stage 1 (M_Pl → M_GUT)

```
1/α₃(M_GUT) = 16π + (b₃^{WZW}/2π) × ln(M_Pl/M_GUT)
             = 50.27 + (b₃^{WZW}/2π) × 3.065
```

### Step 4: Run Stage 2 (M_GUT → M_Z)

```
1/α₃(M_Z) = 1/α₃(M_GUT) + (b₃^{SM}/2π) × ln(M_GUT/M_Z)
           = 1/α₃(M_GUT) + (−7/2π) × 34.08
           = 1/α₃(M_GUT) − 37.96
```

### Step 5: Add corrections

- Two-loop SM running: estimated +0.5 to +1.0
- GUT threshold corrections: estimated +0.5 to +1.5
- αs-specific: three-loop, matching conditions

---

## 3. Key Question: Is b₃^{WZW} Positive or Negative?

For α₂, the enormous E₈ fermionic content overwhelmed the gauge contribution, giving b₂^{WZW} = +38/3 > 0 (non-asymptotically free). The same likely holds for SU(3)_c because:

- SU(3)_c has C₂ = 3 (vs SU(2)'s C₂ = 2), so the gauge contribution is −11 (vs −22/3)
- But SU(3)_c sees MORE colored matter (triplets appear more frequently than doublets in E₈ decompositions)
- Expect T_total to be large, making b₃^{WZW} > 0

If b₃^{WZW} > 0, the coupling 1/α₃ INCREASES from M_Pl to M_GUT, which means 1/α₃(M_GUT) > 50.27, and after SM running down, the final 1/α₃(M_Z) will be LARGER than 8.94 — moving AWAY from the observed 8.50.

**This would be a problem.** Check the sign carefully.

Alternatively, if the E₈ threshold effect is smaller for SU(3) than for SU(2) (possible if SU(3) representations are more evenly distributed), the correction could be modest.

**[F] Session findings:** The sign concern was correct and severe. T_total(SU(3)_c) = 30 (same as SU(2) by SU(3)³ symmetry of E₆), giving b₃^{WZW} = +9. Two-stage result: 1/α₃(M_Z) = 16.70. Catastrophic.

**[F] Additionally:** Two-loop SM running (~+0.8) and standard GUT threshold corrections (+0.3 to +0.7) also go the wrong direction. The observed α₃ is *larger* than predicted (1/α₃ = 8.50 < 8.94), so the needed correction is *negative* (Δ ≈ −0.44). All standard corrections are positive.

**[D] WL3-B implication:** The two-stage WZW treatment does not apply to α₃. All SU(3)_c generators are in F₄ (none in G₂), so there is no structural analog to the α₂ mechanism. The gap must be closed by a negative GUT threshold from E₆ exotic colored triplets at M_T > M_GUT, motivated by doublet-triplet splitting / Casimir ordering. See §4.

---

## 4. Work Log

**[2026-03-17] Session 1 — T_total and b₃^{WZW}**

Decomposed 248 under SU(3)_c via E₈ → SU(3)_fam × E₆ → SU(3)_c × SU(3)_L × SU(3)_R:

| Source | SU(3)_c content | T contribution |
|--------|----------------|----------------|
| (1,78): (8,1,1) | one adjoint | 3 |
| (1,78): (3,3̄,3̄)+(3̄,3,3) | 9+9 triplets | 4.5+4.5 = 9 |
| 3×(3,27): (3,3̄,1)+(3̄,1,3) per 27 | 3+3 triplets × 3 copies | 9 |
| 3×(3̄,27̄) | same by conjugation | 9 |
| **Total** | | **T_total = 30** |

Note: T_total(SU(3)_c) = T_total(SU(2)_L) = 30. Not a coincidence — reflects the symmetric role of SU(3)_c and SU(2)_L in the SU(3)³ decomposition of E₆.

```
b₃^{WZW} = −(11/3)(3) + (2/3)(30) = −11 + 20 = +9
```

Two-stage result:
```
Stage 1: 1/α₃(M_GUT) = 50.27 + (9/2π)(3.065) = 54.66
Stage 2: 1/α₃(M_Z)   = 54.66 − 37.96 = 16.70
```

**[F] Two-stage WZW/RG gives 16.70 vs. observed 8.50. Ruled out.**

---

**[2026-03-17] Session 2 — Cross-reference with Notebook 2 §3 and §5**

Confirmed against Notebook 2 §3: same T_total = 30 methodology used for α₂. The α₂ WZW correction was structurally motivated by T₃'s dual role in G₂ (electromagnetic sector). Per WL3-B (Notebook 2 §5): all 8 SU(3)_c generators are in F₄ — none participate in G₂. The structural asymmetry that licensed the two-stage treatment for SU(2) does not exist for SU(3)_c.

**[D] The two-stage WZW treatment does not apply to α₃.**

---

**[2026-03-17] Session 3 — Sign analysis and correction directions**

Sign of discrepancy:
```
Predicted:  1/α₃(M_Z) = 8.94  →  α₃ = 0.1118
Observed:   1/α₃(M_Z) = 8.50  →  α₃ = 0.1176
```
The observed coupling is *stronger* than predicted. Need 1/α₃ to *decrease* by ~0.44.

Corrections surveyed:

| Correction | Direction | Magnitude | Status |
|-----------|-----------|-----------|--------|
| Two-loop SM running | increases 1/α₃ | ~+0.8 | Wrong sign |
| X/Y boson threshold | increases 1/α₃ | ~+0.2 to +0.3 | Wrong sign |
| Light colored triplet threshold | increases 1/α₃ | ~+0.1 | Wrong sign |
| E₆ exotic triplets at M_T > M_GUT | decreases 1/α₃ | ~−0.4 to −0.7 | **Right sign** |

All standard corrections worsen the prediction. The only candidate in the right direction: **negative threshold from E₆ exotic colored triplets with M_T > M_GUT**.

Physical motivation: Doublet-triplet splitting (Casimir ordering, Reference Core §1) naturally places colored triplet components of GUT Higgs/matter multiplets *above* M_GUT while electroweak doublets are below. If M_T ~ 1.5–2 × M_GUT, the threshold correction is:

```
Δ(1/α₃)^{triplet} = −(2/3)(T_triplet)/(2π) × ln(M_T/M_GUT)
```

For T_triplet from 3 families of exotic (3̄,1,3) states (T = 27/2 total) and ln(M_T/M_GUT) ~ 0.1–0.2:
```
Δ ≈ −(2/3)(13.5)/(2π) × 0.15 ≈ −0.22   [needs refinement]
```

Larger ln factor or fewer contributing states could give the full −0.44. **Explicit computation of M_T from Casimir ordering mechanism is the next step.**

Required bare shift check: if threshold gives the full correction,
```
49.83 = 50.27 + Δ_threshold  →  Δ_threshold = −0.44
```
Achievable for M_T/M_GUT ~ 1.5 with appropriate T_triplet. Plausible.

---

**[2026-03-17] Session 4 — M_T/M_GUT from Casimir Ordering**

Attempted three approaches to derive M_T/M_GUT from within the existing framework:

**Approach 1: Perturbative one-loop Casimir shift at M_GUT.**
The mass correction to a colored triplet from SU(3)_c at the GUT scale is δM_T²/M_GUT² ≈ (α_GUT/4π) × C₂(3̄) = (0.02153/4π) × (4/3) ≈ 0.00229, giving M_T/M_GUT ≈ 1.02. The threshold correction from this separation is < 0.01. **Insufficient.**

**Approach 2: RS bulk profiles from WZW conformal dimensions h_R = C₂(R)/[2(k+h∨)].**
Triplets in the 27 of E₆ under SU(3)_c at level k=1 have h = C₂(3̄)/(2×4) = (4/3)/8 = 1/6, giving bulk parameter c = 1/2 − 1/6 = 1/3, and 4D KK mass m_T ≈ M_Pl × exp(−(1/3)×36.1) ≈ 7×10¹² GeV. This is *below* M_GUT = 5.7×10¹⁶ GeV. **Wrong direction for M_T > M_GUT.**

For M_T > M_GUT, the approach would require c < 0 (UV-localized), placing the triplet above M_Pl. Unphysical.

**Approach 3: Matching to Paper 2 condensate parameter Q×L = 1.61.**
Identifying ξ × ΔC₂ × L = Q × L gives ξ = 0.0764 and M_T/M_GUT = exp(1.61 − 32.77) ≪ 1. The Q condensate governs intra-generation fermion mass ratios, not GUT-Higgs triplet masses. **Not the right identification.**

**Backward computation of required value:**
The threshold formula (from §3) with T_total = 9 (18 exotic triplets from 3×27 matter, each T=1/2, excluding SM quarks) and the required correction Δ(1/α₃) = −0.44:

```
−0.44 = −(2/3)(9)/(2π) × ln(M_T/M_GUT)
ln(M_T/M_GUT) = 0.461
M_T/M_GUT = 1.586
```

A separation of ~59% above M_GUT is physically plausible for a GUT-breaking spectrum but is not derivable from current RS/WZW inputs.

```
[F] None of the three approaches derives M_T/M_GUT > 1 from first principles within the
    current framework. The RS/WZW mechanism places exotic triplets below M_GUT, not above it.
[D] Required: M_T/M_GUT = 1.586 for full Δ(1/α₃) = −0.44 (backward-computed from T_total = 9).
[⚠ GAP] Dynamical origin of the ~59% mass separation above M_GUT is missing.
         Options: (i) explicit one-loop mass matrix for E₆ exotic spectrum from the
         GUT-breaking condensate; (ii) dedicated model of the GUT-breaking sector;
         (iii) accept as fitted parameter and demote α₃ prediction to Tier C.
[P] The required M_T/M_GUT = 1.59 is numerically plausible for O(1) loop corrections
    at the GUT breaking scale — not excluded, but not derived.
```

---

## 5. Dependencies

- 248 decomposition under SU(3)_c (standard representation theory) — **completed**
- M_GUT = 5.7×10¹⁶ GeV (from Reference Core) — **in use**
- ln(M_Pl/M_GUT) = 3.065 (from Reference Core) — **in use**
- **New (blocked):** M_T/M_GUT — mass of E₆ exotic colored triplets relative to M_GUT. Required value is M_T/M_GUT = 1.586 (backward-computed). Not derivable from existing RS/WZW inputs (see §4 Session 4). Requires an explicit one-loop mass matrix calculation for the E₆ exotic spectrum from the GUT-breaking condensate, or demotion of the α₃ prediction to Tier C with M_T/M_GUT as a fitted parameter.

---

*End of WS-α₃ workstream file.*
