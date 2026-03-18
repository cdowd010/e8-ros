# WL2-A: Deriving n = 15 from First Principles
## The Number of Self-Referential Tower Levels

**Status:** In progress  
**Type:** Fix — Critical  
**Session:** March 2026  
**Goal:** Derive n = h∨(E₈)/2 = 15 as the number of tower levels *before* computing that it gives M_W, not after.

---

## 1. The Problem Stated Precisely

The paper claims:

> M_W = M_Pl / 12^{15}

The number 15 is identified with h∨(E₈)/2 = 30/2 = 15, and also with K(G₂) + K(F₄) = 5 + 10 = 15.

Both are real algebraic identities. Neither is a *derivation* of why the tower has 15 levels. Currently the logic is:

```
Observe: M_Pl / 12^n = M_W   (empirical)
Find: n = 15 ≈ h∨(E₈)/2       (post-hoc identification)
Claim: this is a prediction    (incorrect — it is a postdiction)
```

A genuine derivation would be:

```
From E₈ boundary theory alone, derive: tower has n levels
Compute: M_Pl / 12^n
Compare to observation
```

---

## 2. Direction 1 — Counting Conformal Embedding Steps

**The question:** Does the conformal embedding cascade E₈ ⊃ G₂×F₄ ⊃ ... ⊃ SM have exactly 15 independent steps?

### The cascade written out explicitly

Starting from (E₈)₁ at c = 8, the full chain to SM factors:

```
Level 0:  (E₈)₁                           c = 8

Level 1:  (G₂)₁ ⊗ (F₄)₁                  c = 14/5 + 26/5 = 8
          — one conformal embedding step

Level 2a: (G₂)₁ → SU(3)_fam ⊗ ???
          Under G₂ ⊃ SU(3): (G₂)₁ at k=1
          c(SU(3)_fam)₁ = 2
          Remaining: c = 14/5 - 2 = 4/5 ... 
```

Wait. The G₂ factor does NOT further embed into SU(3) as a *conformal embedding*. G₂ ⊃ SU(3) is a Lie group inclusion, but (G₂)₁ ⊃ (SU(3))_k is a conformal embedding only at specific k values. Let me check this carefully.

### Conformal embeddings: definition

A conformal embedding G ⊃ H₁ × H₂ at level k means:
```
c(G)_k = c(H₁)_{k₁} + c(H₂)_{k₂}
```
where k₁, k₂ are the induced levels. For the GUT cascade at k = 1 in the paper:

```
E₈ ⊃ SU(3)_fam × E₆:   c = 2 + 6 = 8   ✓   (at k_fam = 1, k_{E₆} = 1)
E₆ ⊃ SO(10) × U(1):    c = 5 + 1 = 6   ✓   (at k_{SO(10)} = 1, k_{U(1)} = 1)
SO(10) ⊃ SU(5) × U(1): c = 4 + 1 = 5   ✓   (at k_{SU(5)} = 1)
SU(5) ⊃ SU(3)×SU(2)×U(1): c = 2+1+1 = 4  ✓
```

**Separately:**
```
E₈ ⊃ G₂ × F₄:  c = 14/5 + 26/5 = 8  ✓
```

### Counting distinct conformal embedding steps

**In the GUT chain (the SM derivation chain):**

1. E₈ → G₂ × F₄ (Family × SM precursor split)
2. E₈ → SU(3)_fam × E₆ (Family × GUT)
3. E₆ → SO(10) × U(1)₁
4. SO(10) → SU(5) × U(1)₂
5. SU(5) → SU(3)_c × SU(2)_L × U(1)_Y

That's 5 conformal embedding steps in the main GUT chain, not 15.

**Verdict:** Direction 1 in its naive form does not give 15. The number of conformal embedding *steps* in the cascade is only 4-5, not 15.

So the cascade step count ≠ 15. We need a different interpretation.

---

## 3. Direction 2 — Reinterpreting What n Counts

### What does the self-referential tower actually do?

Each level of the tower integrates out Z = 12 states per Planck cell. This is a *holographic* UV/IR correspondence: boundary UV → bulk high-energy, boundary IR → bulk low-energy.

The number of integrations needed to go from M_Pl to M_W is:

```
n = log_{12}(M_Pl / M_W) = log_{12}(1.22×10¹⁸ / 80.4) = log_{12}(1.52×10¹⁶)
```

Compute:
```
log_{12}(1.52×10¹⁶) = ln(1.52×10¹⁶) / ln(12)
                     = 37.26 / 2.485
                     = 14.99 ≈ 15
```

**So n = 15 is exactly the observational statement that M_Pl/M_W = 12^{15}.**

This confirms the problem: n = 15 *is* log₁₂(M_Pl/M_W). It is defined empirically, not derived.

To derive n = 15, we need to derive M_W/M_Pl independently of the tower formula. But M_W/M_Pl *is* the hierarchy problem. We can't derive n without solving the hierarchy problem — unless we can derive n from the E₈ algebra independently of M_W.

### The algebraic route: n = h∨(E₈)/2

**Can we derive n = h∨(E₈)/2 = 15 from the self-referential structure?**

The dual Coxeter number h∨(E₈) = 30 appears throughout E₈ theory:
- It appears in the Killing form normalization
- In the one-loop level shift K = k + h∨
- In the Weyl denominator formula
- In the denominator of the central charge formula: c = k·dim(G)/(k+h∨)

**Specific question:** Is there a natural sense in which "the E₈ boundary theory has h∨(E₈)/2 = 15 natural scales"?

### Positive roots interpretation

h∨(E₈) = 30 is related to but not equal to the number of positive roots of E₈. E₈ has:
- Rank: 8
- Dim: 248
- Positive roots: (248 - 8)/2 = 120

So h∨ ≠ (number of positive roots). h∨ is the sum of the highest root coefficients when expressed in the simple root basis: for E₈, the highest root is 2α₁ + 3α₂ + 4α₃ + 5α₄ + 6α₅ + 4α₆ + 2α₇ + 3α₈, and the sum of coefficients is 2+3+4+5+6+4+2+3 = 29... hmm that gives 29, not 30. Let me recheck.

Actually: h∨(E₈) is defined as 1 + (sum of labels of the highest root in the Dynkin diagram). For E₈ with Bourbaki labeling, the highest root is 2α₁ + 3α₂ + 4α₃ + 6α₄ + 5α₅ + 4α₆ + 3α₇ + 2α₈. Sum = 2+3+4+6+5+4+3+2 = 29. Plus the 1: h∨ = 30. ✓

So h∨(E₈) = 30 = 1 + 29 where 29 = sum of Dynkin labels of the highest root.

**h∨/2 = 15** does not have an obvious combinatorial meaning as "number of scales." It is half the dual Coxeter number — a standard Lie algebraic quantity, but one whose factor of 1/2 doesn't have a natural physical interpretation in this context.

### K(G₂) + K(F₄) = 5 + 10 = 15

The effective levels of the two factors in E₈ = G₂ × F₄ at level 1:
```
K(G₂) = 1 + h∨(G₂) = 1 + 4 = 5
K(F₄) = 1 + h∨(F₄) = 1 + 9 = 10
K(G₂) + K(F₄) = 15
```

**Is this sum physically meaningful as a "number of levels"?**

**Attempt:** Each factor has an effective level K_i representing the "quantum depth" of that sector. The total quantum depth K(G₂) + K(F₄) = 15 could represent the total number of independent quantum scales in the boundary theory.

But this is heuristic. K(G₂) = 5 means SU(2) Chern-Simons at level 5 (corresponding to the Fibonacci category), not "5 levels of something." Similarly K(F₄) = 10. Their sum being 15 is a numerological coincidence unless we can give the sum a direct physical meaning.

---

## 4. Direction 3 — The Coxeter Plane and Root System

### A more promising approach: the Coxeter element and h∨

The Coxeter number h(E₈) = 30 (= h∨(E₈) for simply-laced E₈) has a geometric interpretation: the Coxeter element of the Weyl group has order h = 30, and the Coxeter plane shows the E₈ root system with 30-fold symmetry (actually the E₈ Coxeter plane has the symmetry of a regular 30-gon, showing the 240 roots arranged in 8 groups of 30).

**Key property:** The eigenvalues of the Coxeter element of E₈ are:
```
e^{2πi m_j / 30}   where m_j are the Coxeter exponents of E₈:
m_j = 1, 7, 11, 13, 17, 19, 23, 29
```

These are the 8 exponents of E₈. Note: all are odd (since E₈ is simply-laced, exponents come in pairs summing to h-1 = 29, with m_j and h-1-m_j). Wait, that's not right: 1+29=30, 7+23=30, 11+19=30, 13+17=30. Yes, they pair to h = 30.

**The h/2 = 15 interpretation:** The exponents come in pairs (m_j, h-m_j) = (m_j, 30-m_j). Each pair represents a *complex conjugate pair* of Coxeter eigenvalues. There are 8 exponents, giving 4 conjugate pairs. The "half" in h/2 = 15 reflects this pairing.

But this doesn't directly give "15 energy scales."

---

## 5. Direction 4 — The Refined Tower Interpretation

### What if the tower is not about iteration count but about RG flow?

**Alternative reading:** The tower formula M_W = M_Pl/12^{15} is not about 15 discrete steps. Instead:

```
M_W = M_Pl × exp(−n × ln 12) = M_Pl × exp(−L)
```

where L = n × ln 12 = 15 × ln 12 ≈ 37.3 ≈ ln(M_Pl/v).

The tower is a compact notation for:
```
ln(M_Pl/M_W) = n × ln Z = h∨(E₈)/2 × ln 12
```

This is a single equation with two ingredients:
- Z = 12: the microstate count per Planck cell (derived from j(i)^{1/3} = 12)
- h∨(E₈)/2 = 15: the "depth" of the E₈ self-referential structure

**The real question is then:** Can we derive ln(M_Pl/M_W) = (h∨(E₈)/2) × ln 12 from the E₈ boundary theory without knowing M_W?

Equivalently: can we derive M_W/M_Pl = 12^{-15}?

This is equivalent to deriving the electroweak hierarchy from first principles — which is exactly the hierarchy problem of the Standard Model. So the n = 15 derivation is as hard as solving the hierarchy problem.

---

## 6. A Possible Structural Argument

### The self-referential tower and the Jones tower

The Jones basic construction for a subfactor N ⊂ M produces a tower:
```
N ⊂ M ⊂ M₁ ⊂ M₂ ⊂ M₃ ⊂ ...
```
where each Mₙ = ⟨M_{n-1}, e_n⟩ is generated by M_{n-1} and the Jones projection e_n.

The Jones index [M:N] = φ² is constant at each level. After n steps, the relative size is φ^{2n}.

**Question:** Is there a natural termination condition that gives n = 15?

**Attempt:** The tower terminates when the algebra at level n becomes the full Type I factor B(H) — i.e., when the subfactor structure saturates. For the Fibonacci subfactor at index φ², the tower is the Temperley-Lieb algebra TL_n(δ), where δ = φ. The TL algebra has a quotient at n = h∨(E₈)/2... 

Actually: the Temperley-Lieb algebra TL_n(δ) has a non-trivial trace (the Markov trace) that terminates at specific n values related to the Jones index. For δ = φ (corresponding to index φ²), the TL representation theory has a natural termination at:

```
n = level of the associated quantum group = ???
```

For the Fibonacci anyons, the associated quantum group is SU(2) at level k = 3 (since the Fibonacci category is equivalent to the even part of SU(2)_{k=3} Chern-Simons theory). But k = 3 ≠ 15.

This approach doesn't immediately give 15.

---

## 7. The Most Promising Lead: WZW Level Counting

### Total effective levels in the boundary theory

The (E₈)₁ boundary theory, when decomposed into its SM factors via the conformal embedding cascade, has effective levels:

```
K(SU(3)_fam) = 4
K(SU(3)_c) = 4
K(SU(2)_L) = 3
K(U(1)_Y) = 1
K(U(1)_1) = 1
K(U(1)_2) = 1

Total K = 4 + 4 + 3 + 1 + 1 + 1 = 14  (not 15)
```

Or, using the G₂ × F₄ decomposition:
```
K(G₂) + K(F₄) = 5 + 10 = 15
```

The **G₂ × F₄ decomposition** gives 15. The **SM decomposition** gives 14.

**Hypothesis:** The relevant count is K(G₂) + K(F₄) = 15 because this is the first-level decomposition of (E₈)₁, before the SM cascade. The G₂ factor carries the Fibonacci structure (family + cosmological sector); the F₄ factor carries the SM gauge structure.

**Physical interpretation attempt:** Each unit of effective level K corresponds to one "quantum of holographic depth" — one iteration of the self-model. The total quantum depth of the (E₈)₁ boundary theory, as measured by its G₂ × F₄ primary decomposition, is K(G₂) + K(F₄) = 15. Therefore the tower has 15 levels.

**Problem with this interpretation:** K(G₂) = 5 means the G₂ Chern-Simons theory has level 5, which quantizes to 5 units of something. K(F₄) = 10 means the F₄ CS theory has level 10. Why does their *sum* correspond to the number of energy scales? This remains hand-wavy.

---

## 8. The Honest Assessment

### What we can say:

**Algebraic fact [T]:** K(G₂) + K(F₄) = 5 + 10 = h∨(E₈)/2 = 15. This is a real identity.

**Numerical fact [T]:** log₁₂(M_Pl/M_W) ≈ 14.99 ≈ 15. This is a real coincidence (or non-coincidence).

**Not yet derived:** Why the number of tower levels equals K(G₂) + K(F₄). All interpretations so far are heuristic:
- "Total quantum depth" — undefined term
- Jones tower termination — gives wrong number (3 or 30, not 15)
- Conformal embedding steps — gives 5, not 15
- Coxeter exponent pairing — gives structural insight but not physical mechanism

### What is needed for a genuine derivation:

A derivation would show, starting from the (E₈)₁ boundary theory alone, that:
1. The boundary theory produces a tower of nested subfactors
2. The tower terminates after exactly K(G₂) + K(F₄) = 15 levels
3. Each level reduces the energy scale by a factor of Z = 12
4. Therefore M_EW = M_Pl / 12^{15}

Step 2 is the missing piece. The termination condition for the Jones tower is not currently derived.

---

## 9. A New Approach: The Kac-Moody Vacuum Structure

### Irreducible representations of (E₈)₁

At level k = 1, (E₈)₁ has only ONE irreducible representation: the vacuum module (highest weight = 0). This is the defining feature of a holomorphic CFT.

The Virasoro algebra of (E₈)₁ has central charge c = 8. The vacuum module has L₀ eigenvalues:
```
h = 0, 1, 2, 3, ...  (integer, for a bosonic theory)
```

The first non-vacuum primary appears at h = 1 (the 248 dimension current J^a with h = 1).

**Under the G₂ × F₄ decomposition:**

The Fibonacci τ anyon has h_τ = 2/5 in (G₂)₁. The first "non-trivial" operator in the tower with h < 1 is h_τ = 2/5. 

The self-referential tower can be thought of as a sequence of "squeezing" operations, each reducing the conformal weight by a factor. The number of steps to go from the Planck-scale operator (h ~ 1) to the tachyonic operator (h = 2/5 < 1/2) through h∨/2 steps...

This line of reasoning is not yet developed enough to pursue further.

---

## 10. Summary and Status

### Current status: OPEN — partial progress

**What we know:**

1. The naive interpretation (15 conformal embedding steps) is wrong — the cascade has ~5 steps.

2. The formula M_W = M_Pl/12^{15} is equivalent to saying n = log₁₂(M_Pl/M_W) ≈ 15. It is currently an observation, not a derivation.

3. The best algebraic candidate for why n = 15 is K(G₂) + K(F₄) = 5 + 10 = 15, but the physical interpretation of this sum as "number of tower levels" is not yet derived.

4. The Jones tower for the Fibonacci subfactor does not naturally terminate at n = 15.

5. A genuine derivation would require deriving M_W/M_Pl from first principles — equivalent to solving the hierarchy problem.

### Honest assessment for the paper:

The paper should state:

> "The tower formula M_W = M_Pl/12^{h∨(E₈)/2} = M_Pl/12^{15} matches observation to 1.5%. The exponent h∨(E₈)/2 = K(G₂) + K(F₄) = 15 is a real algebraic identity of the (E₈)₁ boundary theory. However, a first-principles derivation of why the tower has h∨(E₈)/2 levels — as opposed to h∨(E₈) or h∨(G₂) or any other algebraic quantity — has not been achieved. The electroweak scale prediction should be regarded as an observation motivating such a derivation, not a parameter-free consequence of the framework."

### Required paper action:

Replace the current wording (which implies n = 15 is derived) with the honest statement above. The match M_W = M_Pl/12^{15} is still striking and worth reporting — but as an empirical observation supported by an algebraic identity, not a zero-parameter prediction.

---

## 11. New Direction: Can We Derive M_W from the Gauge Coupling Predictions?

### An indirect approach

The framework predicts:
- α₂(M_Z) → 1/α₂ = 29.57 (from the WZW boundary theory)
- M_Z from M_W and sin²θ_W

But M_W itself sets the EW scale — it is not derivable from gauge coupling predictions alone (those give dimensionless ratios, not mass scales).

**Unless:** the framework predicts v from the Fibonacci tachyon condensation, and M_W follows from M_W = g₂v/2.

The condensation potential for the τ anyon:
- V(τ) = m²|τ|² + λ|τ|⁴
- m² = −(16/25)H²
- Minimum at |τ|² = |m²|/(2λ) = (16/25)H²/(2λ)

The VEV |τ| at the minimum depends on λ. If λ is computable from the Fibonacci F-matrix (the quartic coupling from τ×τ fusion), this could fix v/H:

```
v = √(|m²|/λ) × (something from F-matrix)
  = (4/5)H × (something)
```

And v/M_Pl = v/(H × M_Pl/H) = (v/H) × (H/M_Pl).

At the Planck epoch H ~ M_Pl, so v/H ~ O(1). But the electroweak scale v = 246 GeV << M_Pl = 1.22×10¹⁸ GeV. So v/H ~ 10⁻¹⁶ at the Planck scale — the hierarchy is not solved by this argument.

**Conclusion:** The λ from the Fibonacci F-matrix sets v/H at the Planck scale, but the physical Higgs VEV at the electroweak scale requires understanding the RG flow of v from M_Pl to M_Z — which is the hierarchy problem. The tower (n = 15) is one way to encode this hierarchy, but deriving n from first principles requires solving the hierarchy problem.

---

## 12. Verdict

**WL2-A Status: Partial progress. Not closed.**

**Key finding:** The n = 15 derivation is harder than it appears — it is equivalent to solving the electroweak hierarchy problem from first principles. The algebraic identity K(G₂) + K(F₄) = h∨(E₈)/2 = 15 is real, but its interpretation as "number of tower levels" is not derived.

**What CAN be said:** The framework identifies a relationship between the E₈ algebraic structure and the observed hierarchy. This is a genuine structural observation, not mere numerology (the fact that exactly h∨/2 appears, not h∨ or dim(E₈) or anything else, is specific). But it is not yet a derivation.

**Recommended paper action:** Downgrade the M_W prediction from "zero-parameter" to "observation motivated by algebraic identity." This is honest and appropriate. The prediction is still striking.

**Recommended next research direction:** Investigate whether the Jones tower for index φ² has a natural "saturation" condition at n = 15 within the (E₈)₁ representation theory. Specifically: does the Temperley-Lieb quotient at level n = K(G₂) + K(F₄) have a special representation-theoretic significance for the Fibonacci category embedded in (E₈)₁?

---

## 13. New Direction (March 17, 2026): Coxeter Element as RG Operator

*Added from updated research plan after external review.*

### The idea

The Coxeter element w of the E₈ Weyl group has order h = 30. For simply-laced groups, w^{h/2} = −1 on the Cartan subalgebra (sends every root to its negative — charge conjugation).

**Hypothesis:** The tower from M_Pl to M_W corresponds to one half-rotation of the Coxeter element: w⁰ → w^{h/2} = w^{15}. The electroweak scale is where the self-model reaches its "antipodal" point (maximally different from the original). The second half (w^{15} → w^{30}) is excluded by the chiral boundary condition (anti-self-model).

### Why this is interesting

- Gives a representation-theoretic reason for h/2 specifically (not h, not h/3)
- The factor of 2 comes from chirality — the same chirality that selects the holomorphic (E₈)₁ over the non-chiral (E₈)₁ × (E₈)₁
- w^{h/2} = −1 is a theorem (for simply-laced groups), not a heuristic

### What needs to be checked

1. Does the Coxeter element have a well-defined action on the Jones tower for a Fibonacci subfactor?
2. Is there a representation-theoretic "termination" or "fixed point" at step h/2 in the tower?
3. Can the Coxeter rotation be interpreted as an RG flow step?
4. Does the chirality exclusion of the second half-rotation have a precise subfactor-theoretic meaning?

### Difficulty

Hard. Requires connecting Weyl group geometry to subfactor theory — two fields not usually in contact. But the question is mathematically precise and has a definite answer.

### Status: Not yet attempted.

---

## 14. Direction 13 — Coxeter Element as RG Operator: First Analysis

*Added March 17, 2026.*

### Established facts [T]

1. $w^{h/2} = w^{15} = -1$ on the E₈ root lattice (Bourbaki, Ch. 5 §6 Cor. 3).
2. The 240 roots of E₈ form 8 orbits of 30 under repeated Coxeter action.
3. $w^{15}$ maps every positive root $\alpha \mapsto -\alpha$ — all roots flip simultaneously.
4. This is a $\mathbb{Z}_2$ involution: the unique automorphism of the root system acting as $-1$ on all roots.
5. The (E₈)₁ character $\chi_0(\tau) = \Theta_{E_8}(\tau)/\eta(\tau)^8 = j(\tau)^{1/3}$ is **Coxeter-invariant**: the Weyl group $W$ acts as isometries on the root lattice and therefore permutes terms in $\Theta_{E_8}$ without changing the sum. The partition function is $W$-invariant.

### Physical picture [P]

The self-referential boundary tower starts at the Planck scale with (E₈)₁ in its "positive root vacuum" (UV: unbroken symmetry). Each RG step rotates the root configuration by $w$. After 15 steps:

- Every root has flipped: positive ↔ negative (all gauge bosons ↔ conjugates)
- $w^{15}$ acts on the current algebra as $J^\alpha \to -J^{-\alpha}$ — charge conjugation + Hermitian conjugation
- The holomorphic (chiral) boundary condition of (E₈)₁ identifies the antipodal theory as the charge-conjugate IR vacuum, not a new UV theory
- The tower terminates: step 15 is the last consistent chiral step

The second half-orbit $w^{15} \to w^{30} = \mathrm{id}$ is identified with the anti-holomorphic sector, which is excluded by the holomorphic boundary condition. This provides the first non-circular reason for $h/2$ specifically (rather than $h$ or $h/3$): it is the chirality of (E₈)₁ that cuts the orbit in half.

### The gap [⚠ GAP]

The argument requires: one RG step (integrating out one Planck shell, reducing energy by factor $Z = 12$) corresponds to one application of $w$ to the root configuration. This is **not established**. It requires connecting the WZW/holographic RG kernel for (E₈)₁ to the Weyl group action on the root lattice — two structures not usually in direct contact.

### Proposed next computation

Check whether the modular orbit $\tau_k = i + k/15$ in the $j$-function reproduces the energy sequence $M_k = M_\mathrm{Pl} \cdot 12^{-k}$. Specifically, does:

$$|j(i + k/15)|^{1/3} \stackrel{?}{=} 12^{15-k}$$

→ Carried out in §15; result is negative [F].

---

## 15. Direction 13 — Modular Orbit Ruled Out; Jones-Wenzl Singularity Identified

*Added March 17, 2026.*

### Modular orbit computation [F]

**Setup:** For $\tau_k = i + k/15$, the nome is $q_k = e^{2\pi i \tau_k} = e^{-2\pi} \cdot e^{2\pi ik/15}$. The modulus $|q_k| = e^{-2\pi} \approx 0.00187$ is **constant** along the entire orbit — only the phase rotates.

**Leading-order expansion** ($|q|$ small, convergent):

$$j(i + k/15) \approx 535.49\, e^{-2\pi ik/15} + 744 + 368\, e^{2\pi ik/15} + 75.2\, e^{4\pi ik/15} + \cdots$$

**Spot check at $k=1$** (with $\omega = e^{2\pi i/15}$, $\cos 24° = 0.9135$, $\sin 24° = 0.4067$):

- Real part: $535.49(0.9135) + 744 + 368(0.9135) + 75.2(0.6691) \approx 1619.7$
- Imaginary part: $535.49(-0.4067) + 368(0.4067) + 75.2(0.7431) \approx -12.1$
- $|j(i+1/15)|^{1/3} \approx 11.74$

**Result:** All values $|j(i+k/15)|^{1/3} \approx O(12)$ for all $k$. There is no geometric decrease by factor 12 between steps. The orbit produces values oscillating near 12, not the tower $12^{15}, 12^{14}, \ldots, 12^1$.

**Diagnosis:** The factor $Z = 12$ comes from $\mathrm{Im}(\tau) = 1$ via $j(i)^{1/3} = 12$. A geometric energy sequence $M_k = M_\mathrm{Pl} \cdot 12^{-k}$ would require $\mathrm{Im}(\tau_k)$ to increase with $k$ (moving upward in the upper half-plane, not sideways). The orbit $\tau = i + \mathrm{real}$ holds $\mathrm{Im}(\tau)$ constant. **The modular orbit approach is definitively ruled out [F].**

### Consequence for the Coxeter approach

The $W$-invariance of the (E₈)₁ partition function (§14 fact 5) further confirms this: the Coxeter element cannot generate non-trivial dynamics at the level of the character or partition function. The tower generates $\ln 12$ entropy per level by repeated evaluation at $\tau = i$, not by moving $\tau$ along a modular orbit.

The Coxeter element's physical content is confined to its action on the **current algebra** ($J^\alpha \to -J^{-\alpha}$ at step 15) — meaningful as a charge-conjugation statement [P], but not a derivation of $n=15$ without the missing RG↔Coxeter link.

### Jones-Wenzl singularities — new candidate [⚠ GAP]

For $\delta = \phi = 2\cos(\pi/5)$, the Jones-Wenzl projector $P_n \in TL_n(\phi)$ is singular when $\Delta_{n-1} = 0$, where $\Delta_n = \sin((n+1)\pi/5)/\sin(\pi/5)$. Singularities occur precisely at $n \in \{5, 10, 15, 20, \ldots\} = 5\mathbb{Z}_{>0}$.

| Singularity | $n$ | Algebraic coincidence |
|-------------|-----|----------------------|
| 1st | $5$ | $= K(G_2) = 1 + h^\vee(G_2)$ |
| 2nd | $10$ | $= K(F_4) = 1 + h^\vee(F_4)$ |
| **3rd** | **15** | $= K(G_2) + K(F_4) = h^\vee(E_8)/2$ |

**Hypothesis:** The Jones tower for the Fibonacci subfactor, embedded in (E₈)₁ via the $G_2 \times F_4$ decomposition, runs until the first Jones-Wenzl singularity that simultaneously engages both the $G_2$ and $F_4$ sectors. The first two singularities ($n=5$, $n=10$) correspond to the individual factor truncations; $n=15$ is the first singularity of the *combined* tower, which terminates it.

This is not circular: the singularity positions $\{5, 10, 15, \ldots\}$ are properties of $TL_n(\phi)$ with $\delta = \phi$ determined by the Jones index alone. The identification with $K(G_2)$, $K(F_4)$ is a consequence of the conformal embedding, not an input.

**What needs to be verified:**
1. That the Fibonacci subfactor tower in the (E₈)₁ context is governed by $TL_n(\phi)$ (rather than a more general planar algebra).
2. That the "simultaneous engagement" criterion is well-defined in the $G_2 \times F_4$ tensor product structure.
3. Literature check: Morrison-Peters-Snyder on Jones-Wenzl projectors in pivotal categories; Bigelow-Morrison-Peters on planar algebras. Check whether the $n=15$ singularity for the Fibonacci specialization has been noted.

### Status after this session

| Approach | Status |
|----------|--------|
| Modular orbit $\tau_k = i + k/15$ | **[F]** ruled out by explicit computation |
| Coxeter element / chirality termination | **[P]** physical argument; RG↔Coxeter link is [⚠ GAP] |
| Jones-Wenzl singularity at $n=15$ for $\delta=\phi$ | **[⚠ GAP]** best current candidate; requires subfactor literature check |

**Recommended next session:** Obtain and check Morrison-Peters-Snyder or equivalent reference. Verify whether $P_{15}(\phi)$ singularity has representation-theoretic significance in the context of the Fibonacci category embedded in a level-1 WZW model.

---

## 16. Jones-Wenzl Full Analysis — Results and Fundamental Blockage

*Added March 17, 2026.*

### TL singularity structure for $\delta = \phi$ [T]

With $\theta = \pi/5$, $\Delta_n = \sin((n+1)\pi/5)/\sin(\pi/5)$:

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|-----|---|---|---|---|---|---|---|---|---|---|----|----|----|----|-----|
| $\Delta_n$ | $1$ | $\phi$ | $\phi$ | $1$ | $0$ | $-1$ | $-\phi$ | $-\phi$ | $-1$ | $0$ | $1$ | $\phi$ | $\phi$ | $1$ | $0$ |

Period 10; zeros at $n = 4, 9, 14, 19, \ldots$ (i.e., $n \equiv 4 \pmod 5$). $P_n$ singular when $\Delta_{n-1} = 0$: at $n = 5, 10, 15, 20, \ldots$

The coincidences $K(G_2) = 5$, $K(F_4) = 10$, $K(G_2) + K(F_4) = 15$ matching the first three singularity positions are confirmed [T].

**Correction to §15:** The "simultaneous engagement" framing was imprecise. $\text{lcm}(5, 10) = 10$ is the first shared singularity, not 15. The sum $K(G_2) + K(F_4) = 15$ picks out the *third* singularity of the $G_2$ sequence, not a joint termination condition. The sum has no derived meaning as a termination criterion — it is a coincidence pointing at the right answer without explaining it.

### What the singularities do NOT give [F]

TL singularities are necessary but not sufficient for tower termination. The sequence continues at $n = 20, 25, 30, \ldots$ — all equally singular. The algebra has no internal mechanism to stop at $n=15$ rather than $n=20$.

The Graham-Lehrer cell theory and the Ridout-Saint-Aubin radical structure both confirm that the radical of $TL_n(\phi)$ grows at each resonance without bound. There is no "saturation" at $n=15$ visible in the algebra alone.

**The Morrison-Peters-Snyder reference flag from §15 is now moot:** their results on Jones-Wenzl projectors in pivotal categories will confirm the singularity positions but cannot supply the termination argument, since the algebra itself doesn't terminate.

### Fundamental blockage identified

All three approaches converge on the same obstruction:

| Approach | What it gives | What it cannot give |
|----------|--------------|-------------------|
| Coxeter element (§14) | $w^{15} = -1$ [T]; chirality argument [P] | Why one RG step = one Coxeter rotation |
| Modular orbit (§15) | Explicit computation | Ruled out [F] |
| Jones-Wenzl (§16) | Three [T] coincidences at $n = 5, 10, 15$ | Dynamical termination at $n=15$ |

The common failure mode: every approach identifies algebraic reasons why 15 is special, but none can derive that the tower *stops* there, because **the self-modeling map $\mathcal{S}$ is not defined precisely enough to be iterated and analyzed for fixed points or inconsistencies.**

### The self-modeling map: what is missing

The tower is described heuristically as: start with $(E_8)_1$, apply self-model construction, repeat $n$ times. A genuine derivation of $n=15$ requires:

1. **A precise definition** of $\mathcal{S}: \{\text{holomorphic CFTs at } c=8\} \to \{\text{holomorphic CFTs at } c=8\}$
2. **A proof** that $\mathcal{S}^{15}((E_8)_1)$ is a fixed point or an inconsistency
3. **A proof** that $\mathcal{S}^k((E_8)_1)$ for $k < 15$ is neither

Without (1), steps (2) and (3) are not well-posed. The algebraic coincidences at $n=15$ are consistent with the tower terminating there, and motivate the claim, but do not derive it. This is not a gap that more algebra will close — it requires a foundational definition.

### Revised status of the M_W prediction

```
[T] K(G₂) + K(F₄) = h∨(E₈)/2 = 15
[T] Third Jones-Wenzl singularity for δ=φ occurs at n=15
[T] w^{15} = −1 on E₈ root lattice
[T] These are three independent algebraic characterizations of 15 
    within the (E₈)₁ structure
[P] Together they suggest n=15 is the natural "depth" of the tower
[⚠ GAP] Termination at n=15 requires precise definition of S and a 
         fixed-point or inconsistency proof at iteration 15
```

The M_W prediction remains **Tier B**: motivated by a cluster of theorems pointing at $n=15$, but not a zero-parameter consequence of the framework. The cluster is now better documented and stronger than before this workstream, but the gap is also now more precisely located.

### What would close this workstream

**Option A — Define $\mathcal{S}$ precisely:**
If the self-modeling map can be defined as a concrete operation on modular tensor categories (e.g., as a specific functor, or as the Drinfeld center construction, or as a coset/extension operation), then the fixed-point question becomes tractable.

**Option B — Derive $v$ from the tachyon condensation:**
If the Fibonacci tachyon condensation (§11) can be made precise — computing $\lambda$ from the $F$-matrix and showing $v/M_\text{Pl} = 12^{-15}$ — this would bypass the tower count entirely and derive the EW scale directly.

**Option C — Accept as structural:**
Downgrade the prediction formally to [D] (derived with the assumption that the tower depth equals $K(G_2)+K(F_4)$), document the three [T] coincidences as motivation, and move on. Return to this when the theory's foundations are more developed.

**Recommendation: Option C now, with Option A as a long-term foundational goal.**
