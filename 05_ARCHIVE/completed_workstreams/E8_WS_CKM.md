# E₈ Workstream: PRED-A — CKM Matrix from Paper 2 Parameters
## Priority 2 in Research Plan

**Status:** Closed — partial kill condition on minimal Paper 2  
**Goal:** Compute the CKM matrix from the already-fitted Paper 2 mass parameters with zero additional freedom.  
**Success criterion:** Wolfenstein parameters (λ, A, ρ, η) match observation to reasonable precision.  
**Failure criterion:** CKM angles wildly wrong → constrains (G₂)₆ model.

---

## 1. The Setup

Paper 2 fits 6 mass ratios (3rd/2nd and 2nd/1st in each charge sector) to determine P×L and Q×L for up-type and down-type quarks:

| Sector | P×L (stored in §6) | Q×L (stored in §6) | P×L (consistent with Tier C) | Q×L (consistent with Tier C) |
|--------|---------------------|---------------------|-------------------------------|-------------------------------|
| Up quarks | 2.71 | 1.61 | **5.401** | **3.188** |
| Down quarks | 0.80 | 0.68 | **3.533** | **1.498** |

**[⚠ GAP — parameter inconsistency]** The stored §6 values give m_t/m_u = 292 and m_b/m_d = 6.6 (code-verified). Tier C entries say 84,455 and 836. Inconsistent by factors ~290× and ~130×. The right column above shows parameters consistent with Tier C. The §6 table must be audited before any Paper 2 quantitative prediction.

The mass matrices for up-type and down-type quarks are diagonalized by unitary matrices U_u and U_d respectively. The CKM matrix is:

```
V_CKM = U†_u × U_d
```

---

## 2. What Needs to Be Computed

### Step 1: Write the full 3×3 mass matrices

The bulk mass parameters for each family in each sector:

**Up-type quarks (from two copies of 10 in Yukawa):**
```
c₃^u = c₀^u + P_u        where P_u × L = 5.401  [corrected]
c₂^u = c₀^u − P_u/2 + Q_u   where Q_u × L = 3.188  [corrected]
c₁^u = c₀^u − P_u/2 − Q_u
```

**Down-type quarks (from 10 + 5̄ in Yukawa):**
```
c₃^d = c₀^d + P_d        where P_d × L = 3.533  [corrected]
c₂^d = c₀^d − P_d/2 + Q_d   where Q_d × L = 1.498  [corrected]
c₁^d = c₀^d − P_d/2 − Q_d
```

The effective Yukawa matrix in family space combines the antisymmetric ε_ijk (from Paper 1) with the symmetric/adjoint condensate corrections (from Paper 2).

### Step 2: Diagonalize each mass matrix — RESOLVED (structural result)

See §5 Work Log. The diagonalization is not necessary: V_CKM = I exactly in minimal Paper 2 for structural reasons proved in §5.

---

## 3. Key Question: What Is the Exact Form of M_ij?

**Resolved in §5.** The key issue is not the form of M_ij but whether the mass eigenbases for up and down sectors can differ at all.

**Proved:** With the Paper 2 condensates S and A, U_u = U_d exactly, giving V_CKM = I. See §5 for the proof.

---

## 4. Simplified First Pass — Superseded

The simplified RS form with varying H direction was computed numerically. Results:

- **[T] Antisymmetric matrix theorem** (code-verified): Any 3×3 antisymmetric M has MM† eigenvalues {0, λ, λ}. Both massive generations degenerate. This is the known F1 failure. Paper 2 condensates are required to lift degeneracy.

- **Numerical scan over all H directions** (code-verified, N=100×100 grid): Best achievable |V_us| = 0.21 (observed 0.225) with |V_cb| = 0.069 (observed 0.042) at an unrelated H direction. These cannot be simultaneously optimized. However, this analysis is moot — see §5.

---

## 5. Work Log

### Session 2026-03-17 (all computations code-verified with Python/numpy)

---

**[⚠ GAP] Finding 1: Parameter table inconsistency**

Reference Core §6 parameters give (code-verified):
```
m_t/m_u = exp(3*Pu_L/2 + Qu_L) = exp(5.675) = 292    [Tier C says 84,455]
m_b/m_d = exp(3*Pd_L/2 + Qd_L) = exp(1.880) = 6.6     [Tier C says 836]
```
Inconsistent by factors of ~290× and ~130×. Parameters that reproduce Tier C values:
```
P_u×L = 5.401,  Q_u×L = 3.188   [from inverting ln(m_t/m_u)=11.289, ln(m_t/m_c)=4.913]
P_d×L = 3.533,  Q_d×L = 1.498   [from inverting ln(m_b/m_d)=6.797, ln(m_b/m_s)=3.801]
```
PDG 2024 masses used: m_u=2.16 MeV, m_c=1.27 GeV, m_t=172.7 GeV, m_d=4.67 MeV, m_s=93.4 MeV, m_b=4.18 GeV.

---

**[T] Finding 2: Antisymmetric matrix degeneracy theorem (code-verified)**

For any 3×3 antisymmetric M = [[0,a,b],[−a,0,c],[−b,−c,0]]:
```
MM^T eigenvalues = {0,  a²+b²+c²,  a²+b²+c²}
```
Checked numerically for (a,b,c) = (1,2,3), (0.5,0.1,0.7), (10,1,0.1) — exact degeneracy in all cases. Therefore ε_ijk Yukawa alone gives m_t = m_c and m_b = m_s exactly (F1 — known). Paper 2 condensates S and A resolve this by making the three c_i distinct.

---

**[F] Finding 3: V_CKM = I exactly in minimal Paper 2 — structural proof**

The proof proceeds in three steps.

**Step 3a:** In Paper 2, the mass eigenbasis is determined by the condensates. In the condensate-defined family basis:
```
S = r × diag(1, −1/2, −1/2)    [symmetric tensor — breaks SU(3)_fam → SU(2)×U(1)]
A = a × diag(0,  1,   −1)       [adjoint — breaks residual SU(2)]
```
Both S and A are diagonal in the same basis. Therefore [S, A] = 0 (confirmed numerically). Their eigenbases are identical.

**Step 3b:** E₆ representation theory forces η_10 = η_5̄.

The E₆ → SO(10) branching is: 27 = 16(+1) + 10(−2) + 1(+4). Three SM generations come from 16_1, 16_2, 16_3. Under SO(10) → SU(5): 16 = 10 + 5̄ + 1. The SU(5) 10-plet and 5̄-plet for generation i both live inside 16_i. SU(3)_fam acts on the generation index i — identically for both 10 and 5̄. Therefore η_10 = η_5̄ is not a free parameter; it is forced by the representation structure.

**Step 3c:** With S and A diagonal in the same basis, and η_10 = η_5̄:
```
c_i^u = c_0^u + η_10 × (S+A)_ii
c_i^d = c_0^d + η_10 × (S+A)_ii    [same η, same diagonal entries]
```
The eigenbasis that diagonalizes c_i^u is identical to the one diagonalizing c_i^d. Therefore U_u = U_d and V_CKM = U_u† U_d = I exactly.

This is not a numerical discrepancy. It is an exact structural result. No choice of parameters in the current framework can give V_CKM ≠ I.

---

**Escape route: exotic 5̄ mixing**

The 10 of SO(10) in the 27 decomposes under SU(5) as 10 = 5 + 5̄. This exotic 5̄ is in a *different* SO(10) multiplet from the SM 5̄ (which is in the 16). If the physical SM 5̄ mass eigenstate mixes with this exotic 5̄, the effective SU(3)_fam action on the SM 5̄ fields is rotated relative to the 10-plet fields. This introduces a misalignment between U_u and U_d, generating V_CKM ≠ I.

This mixing is not currently specified in Paper 2. Whether it is forced by the E₈ structure (and is therefore parameter-free) or requires new input is precisely the WS-CGC question. If the E₆ Clebsch-Gordan coefficients force a specific mixing angle, V_CKM becomes a prediction. If they allow free mixing, it is a new parameter.

---

**Classification:**

| Scope | Verdict |
|-------|---------|
| Minimal Paper 2 (no exotic 5̄ mixing) | **[F] Kill condition** — V_CKM = I proved |
| Broader framework (exotic 5̄ mixing from E₈) | **[⚠ GAP — severe]** — not yet a kill condition; unblocked by WS-CGC |

---

## 6. Dependencies

- Paper 2 fitted parameters (in Reference Core §6) — ⚠ inconsistent, needs audit
- E₆ CGC values for exotic 5̄ mixing (WS-CGC — **now priority-blocking**)
- Standard RS mass matrix formalism (Grossman-Neubert 2000, Gherghetta-Pomarol 2000)

---

*End of PRED-A workstream file.*
