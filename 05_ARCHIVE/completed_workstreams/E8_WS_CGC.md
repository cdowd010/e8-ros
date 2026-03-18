# E₈ Project — Workstream: CGC / Exotic 5̄ Mixing (WS-CGC)

**Status: COMPLETE — KC-g evaluated, escape route closed, F8 deepened**
**Session: 2026-03-17**

---

## Problem statement

Determine whether the mixing between the SM **5̄_A** (from the **16** of SO(10), inside the **27** of E₆) and the exotic **5̄_B** (from the **10** of SO(10), inside the same **27**) is:

- **Forced to zero** by E₈/E₆ group theory (KC-g triggers — escape route closed)
- **Nonzero and parameter-free** (KC-g does not trigger — V_CKM ≠ I recoverable)
- **Free parameter** (partial kill on minimality)

This directly evaluates **KC-g** and the escape route for **F8** (V_CKM = I in minimal Paper 2).

---

## Branching chain

### E₈ ⊃ E₆ × SU(3)_fam (Slansky Table 29)

```
248 → (78, 1) + (1, 8) + (27, 3) + (27̄, 3̄)
```

Three SM generations sit in three copies of **27** of E₆, transforming as a **3** of SU(3)_fam.

### E₆ ⊃ SO(10) × U(1)_ψ

```
27 → 16_{+1} + 10_{-2} + 1_{+4}
```

### SO(10) ⊃ SU(5) × U(1)_χ

```
16 → 10_{-1} + 5̄_{+3} + 1_{-5}
10 → 5_{-2}  + 5̄_{+2}
```

**Two 5̄-plets per generation:**
- **5̄_A** = 5̄_{+3} from **16** of SO(10) ← SM down-type quarks + charged leptons
- **5̄_B** = 5̄_{+2} from **10** of SO(10) ← exotic 5̄

SU(5) content of 27: **10 + 5̄ + 5 + 5̄ + 1 + 1** = 27 ✓ [code-verified]

---

## Key group-theory results

### SO(10) tensor products used [T — Slansky 1981]

| Product | Result |
|---------|--------|
| 16 × 16 (sym) | 10 + 126* |
| 16 × 16 (antisym) | 120 |
| 16 × 10 | 16 + 144 |
| 10 × 10 (sym) | 1 + 54 |
| 10 × 10 (antisym) | 45 |

Dimension checks: 10+120+126=256 ✓; 16+144=160 ✓; 1+45+54=100 ✓ [code-verified]

### E₆ cubic invariant

E₆ has **one independent cubic invariant**: the d-symbol d_{ABC} acting on **27 × 27 × 27** (symmetric). The operator **27 × 27 × 27̄** does **not** constitute a separate cubic invariant — verified by U(1)_ψ charge conservation: no (R_i, R_j, R̄_H) triple with R_i, R_j ∈ {16, 10, 1} and R̄_H ∈ {16̄, 10̄, 1̄} gives zero total U(1)_ψ charge [code-verified].

### Which SO(10) triples contribute to the d-symbol singlet?

Checked by explicit SO(10) product analysis [code-verified]:

| Triple (R₁, R₂, R₃) | Singlet in R₁×R₂×R₃? | Route |
|----------------------|----------------------|-------|
| (16, 16, 10) | **YES** ✓ | [16×16]_sym = 10+126*; 10×10 ⊃ 1 |
| (10, 10, 1)  | **YES** ✓ | [10×10]_sym = 1+54; ×1 = 1+54 |
| **(16, 10, 1)** | **NO** ✗ | 16×10 = 16+144; ×1 = 16+144, no singlet |
| (10, 10, 10) | NO ✗ | 1×10=10, 54×10=10+210+320, none singlet |
| (16, 16, 1)  | NO ✗ | 10+126* ×1, no singlet |

---

## KC-g verdict

### [D] Renormalizable E₆ level

The E₆ d-symbol contains **only** the (16, 16, 10_H) and (10, 10, 1_H) sectors. The **(16, 10, ...)** mixing sector is **group-theoretically absent** — no CGC connects them in 27³. This is a selection rule, not a fine-tuning.

Consequence for the mass matrix:
- **5̄_A** (from 16_i) couples only via 16_i × 16_j × 10_H
- **5̄_B** (from 10_i) couples only via 10_i × 10_j × 1_H
- The two sectors are **completely decoupled** at renormalizable level

### [D] E₈ cubic level

The E₈ cubic 248³ generates a **27 × 27̄ × 78** coupling (adjoint insertion). Under SO(10), 78 → 45₀ + 16_{+3} + 16̄_{-3} + 1₀. Analysis shows **16 × 10 × {any 78-component}** contains no SO(10) singlet (16×10 = 16+144, no singlet). The E₈ structure confirms the 16-10 decoupling.

### KC-g TRIGGERED ✓

**The 5̄_A/5̄_B mixing is forbidden by E₆ selection rules at renormalizable level.** The proposed escape route for F8 (exotic 5̄ mixing generating V_CKM ≠ I) is **CLOSED**.

---

## Escape routes evaluated

### E1 — SU(3)_fam breaking

The E₈ Yukawa from d^{E6}_{ABC} × ε^{SU3}_{ijk} gives Y_{ij} ~ ε_{ij} (antisymmetric, rank 2). Both M_u and M_d have **identical** SU(3)_fam structure from the single d-symbol operator → V_CKM = V_uL† V_dL = I. **[F] E1 does not rescue V_CKM ≠ I at leading order.**

### E2 — dim-5 operators

16_i × 10_j × 1_H × 1_H / M_* gives mixing suppressed by M_GUT/M_Pl ≈ 1.6×10⁻³. Cabibbo angle ~ 0.22, so this requires M_* ~ 10 × M_GUT ≪ M_Pl. [⚠ GAP — tuning of M_* needed]

### E3 — Kahler metric mixing

With E₆-symmetric Kahler metric: generation rotation only, no 5̄_A/5̄_B mixing within a generation. With non-minimal Kahler: reintroduces as free parameter. **[⚠] E3 minimal: no help. E3 non-minimal: new free param.**

---

## Bottom line on F8

[F] **F8 is confirmed and deepened.** V_CKM = I in minimal Paper 2 is not just a numerical coincidence — it is a structural consequence of E₆ selection rules. The minimal Paper 2 framework is **not dead**, but CKM generation requires extending the Higgs sector.

[P] **Most natural extension:** a second Higgs 27̄-plet transforming as **(27̄, 3̄)** under E₆ × SU(3)_fam (already present in the 248 as the (27̄, 3̄) component). This gives M_d ≠ M_u and can generate V_CKM ≠ I with **one additional parameter** (VEV ratio tan β = v₂₇/v₂₇̄). This is the **WS-CKM2** direction.

---

## Next workstream

**WS-CKM2**: With two Higgs sources — (27, 3) and (27̄, 3̄) from the 248 — derive the Yukawa matrix structure for M_u and M_d, compute V_CKM as a function of tan β, and determine whether any value of tan β reproduces observed CKM angles without introducing further free parameters.

*Workstream WS-CGC: COMPLETE. Archive after this session.*
