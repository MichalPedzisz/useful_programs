"""Generuje wykresy do raportu o rzucie ukośnym.

Uruchom z dowolnego katalogu: python generuj_wykresy.py
Wymaga pakietów numpy i matplotlib.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent / "files" / "rzut_ukosny"
OUT.mkdir(parents=True, exist_ok=True)

G = 9.81
V0 = 36.0
ALPHA_DEG = 46.0
ALPHA = np.deg2rad(ALPHA_DEG)
MASS = 0.145
RHO = 1.225
CD = 0.47
RADIUS = 0.0366
AREA = np.pi * RADIUS**2
BETA = 0.15
K_QUAD = RHO * CD * AREA / (2 * MASS)
DT = 0.002

COLORS = {"Bez oporu": "#2463A6", "Liniowy": "#D47722", "Kwadratowy": "#168578"}
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.2,
        "lines.linewidth": 2.2,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def przyspieszenie(vx, vy, model):
    """Zwraca składowe przyspieszenia dla wybranego modelu oporu."""
    speed = np.hypot(vx, vy)
    if model == "Bez oporu":
        ax = 0.0
        ay = -G
    elif model == "Liniowy":
        ax = -BETA * vx
        ay = -G - BETA * vy
    elif model == "Kwadratowy":
        ax = -K_QUAD * speed * vx
        ay = -G - K_QUAD * speed * vy
    else:
        raise ValueError(f"Nieznany model oporu: {model}")
    return ax, ay


def pochodna(stan, model):
    x, y, vx, vy = stan
    ax, ay = przyspieszenie(vx, vy, model)
    return np.array([vx, vy, ax, ay], dtype=float)


def krok_rk4(stan, dt, model):
    k1 = pochodna(stan, model)
    k2 = pochodna(stan + 0.5 * dt * k1, model)
    k3 = pochodna(stan + 0.5 * dt * k2, model)
    k4 = pochodna(stan + dt * k3, model)
    return stan + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)


def symuluj(model, alpha=ALPHA, dt=DT):
    """Całkuje ruch do chwili powrotu na poziom wyrzutu."""
    stan = np.array([0.0, 0.0, V0 * np.cos(alpha), V0 * np.sin(alpha)])
    czas = 0.0
    czasy = [czas]
    stany = [stan.copy()]
    limit = 30.0

    while czas < limit:
        poprzedni = stan
        nastepny = krok_rk4(poprzedni, dt, model)
        czas_nastepny = czas + dt
        if nastepny[1] < 0.0 and czas_nastepny > 0.0:
            udzial = poprzedni[1] / (poprzedni[1] - nastepny[1])
            stan = poprzedni + udzial * (nastepny - poprzedni)
            czas += udzial * dt
            czasy.append(czas)
            stany.append(stan.copy())
            break
        stan = nastepny
        czas = czas_nastepny
        czasy.append(czas)
        stany.append(stan.copy())
    else:
        raise RuntimeError(f"Nie znaleziono lądowania dla modelu: {model}")

    return np.asarray(czasy), np.asarray(stany)


def zapisz(fig, nazwa):
    fig.savefig(OUT / f"{nazwa}.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


modele = ["Bez oporu", "Liniowy", "Kwadratowy"]
wyniki = {model: symuluj(model) for model in modele}

# Kontrola numeryczna: rozwiązanie RK4 w próżni zgadza się ze wzorami.
t_vac, stan_vac = wyniki["Bez oporu"]
czas_teor = 2 * V0 * np.sin(ALPHA) / G
zasieg_teor = V0**2 * np.sin(2 * ALPHA) / G
wysokosc_teor = (V0 * np.sin(ALPHA)) ** 2 / (2 * G)
assert abs(t_vac[-1] - czas_teor) < 2 * DT
assert abs(stan_vac[-1, 0] - zasieg_teor) < 0.1
assert abs(np.max(stan_vac[:, 1]) - wysokosc_teor) < 0.1

# Trajektorie na wspólnych osiach.
fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
for model, (t, s) in wyniki.items():
    ax.plot(s[:, 0], s[:, 1], color=COLORS[model], label=model)
ax.set(
    xlabel="Położenie poziome x [m]",
    ylabel="Wysokość y [m]",
    title=f"Tor ruchu: v₀ = {V0:g} m/s, α = {ALPHA_DEG:g}°",
)
ax.set_ylim(bottom=0)
ax.legend()
zapisz(fig, "trajektorie")

# Składowe położenia i prędkości w funkcji czasu.
fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=False, layout="constrained")
for model, (t, s) in wyniki.items():
    axes[0].plot(t, s[:, 0], color=COLORS[model], label=f"x(t), {model}")
    axes[0].plot(t, s[:, 1], color=COLORS[model], ls="--", label=f"y(t), {model}")
    axes[1].plot(t, s[:, 2], color=COLORS[model], label=f"vₓ(t), {model}")
    axes[1].plot(t, s[:, 3], color=COLORS[model], ls="--", label=f"vᵧ(t), {model}")
axes[0].set(ylabel="Położenie [m]", title="Składowe położenia")
axes[1].set(xlabel="Czas t [s]", ylabel="Prędkość [m/s]", title="Składowe prędkości")
for ax in axes:
    ax.legend(ncol=2, fontsize=8)
zapisz(fig, "polozenie_predkosc")

# Przyspieszenia z uwzględnieniem grawitacji i oporu.
fig, axes = plt.subplots(2, 1, figsize=(9, 6.5), sharex=False, layout="constrained")
for model, (t, s) in wyniki.items():
    przyspieszenia = np.asarray(
        [przyspieszenie(vx, vy, model) for vx, vy in s[:, 2:4]]
    )
    axes[0].plot(t, przyspieszenia[:, 0], color=COLORS[model], label=model)
    axes[1].plot(t, przyspieszenia[:, 1], color=COLORS[model], label=model)
axes[0].set(ylabel="Przyspieszenie aₓ [m/s²]", title="Składowa pozioma")
axes[1].set(xlabel="Czas t [s]", ylabel="Przyspieszenie aᵧ [m/s²]",
            title="Składowa pionowa")
for ax in axes:
    ax.legend()
zapisz(fig, "przyspieszenie")

# Energia mechaniczna; w modelach z oporem jej ubytek odpowiada pracy oporu.
fig, ax = plt.subplots(figsize=(9, 4.5), layout="constrained")
for model, (t, s) in wyniki.items():
    energia = 0.5 * MASS * (s[:, 2] ** 2 + s[:, 3] ** 2) + MASS * G * s[:, 1]
    ax.plot(t, energia, color=COLORS[model], label=model)
ax.set(xlabel="Czas t [s]", ylabel="Energia mechaniczna [J]")
ax.set_title("Zmiana energii mechanicznej podczas lotu")
ax.legend()
zapisz(fig, "energia")

# Wartości końcowe służą do tabeli wyników w raporcie.
print(f"g = {G:.2f} m/s^2, v0 = {V0:.1f} m/s, alpha = {ALPHA_DEG:.1f} deg")
print(f"m = {MASS:.3f} kg, rho = {RHO:.3f} kg/m^3, Cd = {CD:.2f}")
print(f"A = {AREA:.6f} m^2, beta = {BETA:.3f} 1/s, k = {K_QUAD:.6f} 1/m")
for model, (t, s) in wyniki.items():
    print(
        f"{model}: czas lotu = {t[-1]:.3f} s, "
        f"zasięg = {s[-1, 0]:.3f} m, maks. wysokość = {np.max(s[:, 1]):.3f} m"
    )
print(f"Zapisano 4 wykresy w: {OUT}")
