# Lorenz System

A Python simulation of the Lorenz system, a classic example of chaos.

The Lorenz equations were introduced by Edward Lorenz in 1963 as a simplified model of atmospheric convection:

```
dx/dt = σ (y − x)
dy/dt = x (ρ − z) − y
dz/dt = x y − β z
```

With the classic parameters σ = 10, ρ = 28 and β = 8/3, the system never settles down and never repeats. It traces out the butterfly-shaped **Lorenz attractor**.

## What it does

- Solves the equations numerically with `scipy.integrate.solve_ivp`
- Plots the trajectory in 3D with `matplotlib`

## Project structure

```
LorenzSystem/
├── core/
│   └── model.py      # Lorenz equations, solver and plot
├── pyproject.toml
└── README.md
```

## Setup and run

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/<your-username>/LorenzSystem.git
cd LorenzSystem
uv sync
uv run python core/model.py
```


