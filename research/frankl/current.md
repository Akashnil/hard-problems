# Frankl — current status

## Constant
Frankl's union-closed sets conjecture, max element bias. Entropy method.
- Record (lower bound): **0.38271** (Liu, arXiv:2306.08824). Target 1/2 (OPEN).
- `held` (reviewer-verified this run): no bound improvement. Verified deliverable =
  rigorous impossibility analysis of the Frankl-file "perturb uniform A to force
  H[C] > H[A]" program (the goal's explicit honest fallback).

## Status: obstruction verified (no bound improvement — none available)

## Progress log
- R1: VERIFIED obstruction — Theorem 1 (H[C] <= H[A] for any supp(C) ⊆ F, hypothesis-free, Gibbs/KL) re-derived from scratch; Avenue A H''(1) = -(1/ln2)·Σ(dP/dt)²/Pᵢ < 0 confirmed (closed form == finite-diff, -2.1518 on nondistributive lattice); Avenue B collapse C→A confirmed; certificate reproduced (exit 0) and shown non-vacuous (perturbing core checks → exit 1). Record 0.38271 (Liu) stands, correctly cited not improved.
