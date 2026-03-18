# ============================================
# E8 -> E6 x A2 branching computation in Sage
# v2 - corrected subgroup name: "E6xA2"
# ============================================

from sage.all import WeylCharacterRing, branching_rule

E8 = WeylCharacterRing("E8", style="coroots")
E6xA2 = WeylCharacterRing("E6xA2", style="coroots")

b = branching_rule("E8", "E6xA2", "extended")
print("Branching rule:", b)
print()

# --- Verify with adjoint (248) first ---
# The 248 is E8(0,0,0,0,0,0,1,0) in Sage's coroot convention
adj = E8(0,0,0,0,0,0,1,0)
print(f"Adjoint rep dimension: {adj.degree()}")
print("248 branches as:")
adj_branched = adj.branch(E6xA2, rule=b)
print(adj_branched)
print()

# --- Now the 3875 ---
# Try E8(1,0,0,0,0,0,0,0) - should be 3875
rep = E8(1,0,0,0,0,0,0,0)
print(f"E8(1,0,0,0,0,0,0,0) dimension: {rep.degree()}")
print()

if rep.degree() == 3875:
    print("Confirmed: this is the 3875.")
else:
    print(f"WARNING: dimension is {rep.degree()}, not 3875!")
    print("Trying other fundamental reps to find 3875...")
    for i in range(8):
        label = [0]*8
        label[i] = 1
        r = E8(*label)
        d = r.degree()
        print(f"  E8({','.join(map(str,label))}): dim = {d}")
        if d == 3875:
            rep = r
            print(f"  ^^^ THIS IS THE 3875")
    print()

print(f"\n3875 of E8 branches under E6 x A2 as:")
result = rep.branch(E6xA2, rule=b)
print(result)
print()

# Print with dimensions of each component
print("Decomposed terms with dimensions:")
for term in result.support():
    coeff = result.coefficient(term)
    dim = E6xA2(term).degree()
    print(f"  {coeff} x {term}  (dim = {dim})")