import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# ============================================================================
# SIMULATION 4.1: COMPARATIVE PROJECTILE TRAJECTORIES (IDEAL VS DRAG)
# ============================================================================

def ideal_projectile(v0, angle_deg, g=9.81):
    """
    Analytical solution for ideal projectile motion (no drag)
    Returns x, y coordinates
    """
    angle = np.radians(angle_deg)
    v0x = v0 * np.cos(angle)
    v0y = v0 * np.sin(angle)
    
    # Time of flight
    t_flight = 2 * v0y / g
    t = np.linspace(0, t_flight, 500)
    
    # Position equations
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    
    return x, y

def projectile_with_drag(state, t, g, c_over_m):
    """
    System of ODEs for projectile motion with quadratic drag
    state = [x, y, vx, vy]
    """
    x, y, vx, vy = state
    
    # Speed
    v = np.sqrt(vx**2 + vy**2)
    
    # Accelerations with drag
    ax = -c_over_m * v * vx
    ay = -g - c_over_m * v * vy
    
    return [vx, vy, ax, ay]

def simulate_drag_projectile(v0, angle_deg, c_over_m=0.01, g=9.81):
    """
    Numerical solution for projectile with drag using odeint (similar to ode45)
    """
    angle = np.radians(angle_deg)
    v0x = v0 * np.cos(angle)
    v0y = v0 * np.sin(angle)
    
    # Initial state: [x0, y0, vx0, vy0]
    state0 = [0, 0, v0x, v0y]
    
    # Time array (simulate longer than ideal case)
    t = np.linspace(0, 2 * v0y / g, 1000)
    
    # Solve ODE
    solution = odeint(projectile_with_drag, state0, t, args=(g, c_over_m))
    
    x = solution[:, 0]
    y = solution[:, 1]
    
    # Truncate when projectile hits ground
    valid_idx = y >= 0
    x = x[valid_idx]
    y = y[valid_idx]
    
    return x, y

# ============================================================================
# SIMULATION 4.3: CAMERA SMOOTHING WITH DIFFERENT DAMPING CONSTANTS
# ============================================================================

def camera_smoothing(target, initial_pos, k, dt, duration):
    """
    Simulate exponential camera smoothing
    dy/dt = k(target - y)
    Solution: y(t) = target + (y0 - target) * exp(-kt)
    """
    steps = int(duration / dt)
    t = np.linspace(0, duration, steps)
    
    # Analytical solution
    y_analytical = target + (initial_pos - target) * np.exp(-k * t)
    
    # Numerical simulation (discrete game loop)
    y_numerical = np.zeros(steps)
    y_numerical[0] = initial_pos
    
    for i in range(1, steps):
        y_numerical[i] = y_numerical[i-1] + k * (target - y_numerical[i-1]) * dt
    
    return t, y_analytical, y_numerical

# ============================================================================
# PLOTTING ALL SIMULATIONS
# ============================================================================

# Create figure with subplots
fig = plt.figure(figsize=(18, 13))
fig.suptitle('Section 4: Results of Simulations - Numerical Implementation and Performance Analysis', 
             fontsize=16, fontweight='bold', y=0.98)

# ------------------------------------------------------------------------
# PLOT 1: Projectile Trajectories (Ideal vs Drag)
# ------------------------------------------------------------------------
ax1 = plt.subplot(2, 2, 1)

# Parameters
v0 = 50  # m/s
angle = 45  # degrees
g = 9.81
c_over_m = 0.02  # drag coefficient

# Calculate trajectories
x_ideal, y_ideal = ideal_projectile(v0, angle, g)
x_drag, y_drag = simulate_drag_projectile(v0, angle, c_over_m, g)

# Plot
ax1.plot(x_ideal, y_ideal, 'b-', linewidth=2.5, label='Ideal (No Drag) - Analytical')
ax1.plot(x_drag, y_drag, 'r--', linewidth=2.5, label='With Drag - Numerical (RK4)')
ax1.scatter([x_ideal[-1]], [0], color='blue', s=100, marker='o', zorder=5)
ax1.scatter([x_drag[-1]], [0], color='red', s=100, marker='s', zorder=5)

ax1.set_xlabel('Horizontal Distance (m)', fontsize=11, fontweight='bold')
ax1.set_ylabel('Vertical Height (m)', fontsize=11, fontweight='bold')
ax1.set_title('Simulation 4.1: Comparative Projectile Trajectories\n(Ideal vs. Aerodynamic Drag)', 
              fontsize=11, fontweight='bold', pad=10)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=10)
ax1.set_xlim(left=0)
ax1.set_ylim(bottom=0)

# Add annotations
max_range_ideal = x_ideal[-1]
max_range_drag = x_drag[-1]
reduction = (1 - max_range_drag/max_range_ideal) * 100

ax1.text(0.5, 0.92, f'Range Reduction: {reduction:.1f}%\nIdeal: {max_range_ideal:.1f}m | Drag: {max_range_drag:.1f}m',
         transform=ax1.transAxes, fontsize=9, verticalalignment='top',
         bbox={'boxstyle': 'round', 'facecolor': 'wheat', 'alpha': 0.5})

# ------------------------------------------------------------------------
# PLOT 2: Multiple Drag Coefficients
# ------------------------------------------------------------------------
ax2 = plt.subplot(2, 2, 2)

drag_coeffs = [0.0, 0.01, 0.02, 0.04]
colors = ['blue', 'green', 'orange', 'red']

for c, color in zip(drag_coeffs, colors):
    if c == 0:
        x, y = ideal_projectile(v0, angle, g)
        label = f'c/m = {c:.2f} (Ideal)'
        style = '-'
    else:
        x, y = simulate_drag_projectile(v0, angle, c, g)
        label = f'c/m = {c:.2f}'
        style = '--'
    
    ax2.plot(x, y, color=color, linestyle=style, linewidth=2, label=label)

ax2.set_xlabel('Horizontal Distance (m)', fontsize=11, fontweight='bold')
ax2.set_ylabel('Vertical Height (m)', fontsize=11, fontweight='bold')
ax2.set_title('Effect of Varying Drag Coefficients\n(Long-Range Ballistics - PUBG/Battlefield)', 
              fontsize=11, fontweight='bold', pad=10)
ax2.grid(True, alpha=0.3)
ax2.legend(loc='upper right', fontsize=9)
ax2.set_xlim(left=0)
ax2.set_ylim(bottom=0)

# ------------------------------------------------------------------------
# PLOT 3: Camera Smoothing with Different K Values
# ------------------------------------------------------------------------
ax3 = plt.subplot(2, 2, 3)

# Parameters
target = 100  # Target position
initial_pos = 0  # Starting camera position
dt = 0.016  # 60 FPS
duration = 3  # seconds

k_values = [0.5, 2.0, 5.0, 10.0]
colors_k = ['blue', 'green', 'orange', 'red']

for k, color in zip(k_values, colors_k):
    t, y_analytical, y_numerical = camera_smoothing(target, initial_pos, k, dt, duration)
    ax3.plot(t, y_analytical, color=color, linewidth=2.5, label=f'k = {k:.1f}')

# Add target line
ax3.axhline(y=target, color='black', linestyle=':', linewidth=1.5, label='Target Position')

ax3.set_xlabel('Time (seconds)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Camera Position', fontsize=11, fontweight='bold')
ax3.set_title('Simulation 4.3: Real-Time Camera Smoothing\nExponential Decay with Varying Damping Constants (k)', 
              fontsize=11, fontweight='bold', pad=10)
ax3.grid(True, alpha=0.3)
ax3.legend(loc='lower right', fontsize=9)
ax3.set_xlim(0, duration)
ax3.set_ylim(0, target * 1.1)

# Add annotation
ax3.text(0.97, 0.25, 'dy/dt = k(target - y)\n\nSmaller k → Smoother\nLarger k → Faster',
         transform=ax3.transAxes, fontsize=9, verticalalignment='top',
         horizontalalignment='right',
         bbox={'boxstyle': 'round', 'facecolor': 'lightblue', 'alpha': 0.7})

# ------------------------------------------------------------------------
# PLOT 4: Numerical Integration Method Comparison
# ------------------------------------------------------------------------
ax4 = plt.subplot(2, 2, 4)

# Simple harmonic oscillator to compare methods
def explicit_euler(y0, v0, omega, dt, steps):
    y = np.zeros(steps)
    v = np.zeros(steps)
    y[0], v[0] = y0, v0
    
    for i in range(1, steps):
        y[i] = y[i-1] + v[i-1] * dt
        v[i] = v[i-1] - omega**2 * y[i-1] * dt
    
    return y, v

def semi_implicit_euler(y0, v0, omega, dt, steps):
    y = np.zeros(steps)
    v = np.zeros(steps)
    y[0], v[0] = y0, v0
    
    for i in range(1, steps):
        v[i] = v[i-1] - omega**2 * y[i-1] * dt
        y[i] = y[i-1] + v[i] * dt  # Use updated velocity
    
    return y, v

def analytical_solution(y0, v0, omega, t):
    A = y0
    B = v0 / omega
    return A * np.cos(omega * t) + B * np.sin(omega * t)

# Parameters for oscillator
y0, v0 = 1.0, 0.0
omega = 2 * np.pi  # 1 Hz
dt = 0.05
duration = 5
steps = int(duration / dt)
t = np.linspace(0, duration, steps)

# Compute solutions
y_explicit, _ = explicit_euler(y0, v0, omega, dt, steps)
y_semi_implicit, _ = semi_implicit_euler(y0, v0, omega, dt, steps)
y_analytical = analytical_solution(y0, v0, omega, t)

# Plot
ax4.plot(t, y_analytical, 'k-', linewidth=2.5, label='Analytical Solution', alpha=0.7)
ax4.plot(t, y_explicit, 'r--', linewidth=2, label='Explicit Euler (Unstable)', alpha=0.8)
ax4.plot(t, y_semi_implicit, 'b:', linewidth=2.5, label='Semi-Implicit Euler (Stable)', alpha=0.8)

ax4.set_xlabel('Time (seconds)', fontsize=11, fontweight='bold')
ax4.set_ylabel('Position', fontsize=11, fontweight='bold')
ax4.set_title('Simulation 4.2: Numerical Integration Scheme Comparison\nSimple Harmonic Oscillator (ω = 2π, dt = 0.05s)', 
              fontsize=11, fontweight='bold', pad=10)
ax4.grid(True, alpha=0.3)
ax4.legend(loc='upper right', fontsize=9)
ax4.set_xlim(0, duration)

# Add performance table
table_data = [
    ['Method', 'Order', 'Stability', 'Cost'],
    ['Explicit Euler', '1st', 'Low', 'O(n)'],
    ['Semi-Implicit', '1st', 'High', 'O(n)'],
    ['Velocity Verlet', '2nd', 'High', 'O(n)'],
    ['RK4', '4th', 'V.High', '4×O(n)']
]

table_text = '\n'.join([f'{row[0]:16s} | {row[1]:4s} | {row[2]:8s} | {row[3]:6s}' 
                        for row in table_data])

ax4.text(0.02, 0.05, table_text, transform=ax4.transAxes, fontsize=7,
         verticalalignment='bottom', family='monospace',
         bbox={'boxstyle': 'round', 'facecolor': 'lightyellow', 'alpha': 0.8})

plt.tight_layout(rect=(0, 0, 1, 0.96))
plt.show()

print("=" * 80)
print("SIMULATION RESULTS SUMMARY - SECTION 4")
print("=" * 80)
print("\n4.1 PROJECTILE MOTION:")
print(f"  • Ideal range (no drag): {max_range_ideal:.2f} m")
print(f"  • Range with drag: {max_range_drag:.2f} m")
print(f"  • Range reduction: {reduction:.1f}%")
print(f"  • Method: High-order adaptive Runge-Kutta (odeint/ode45)")
print("\n4.2 NUMERICAL INTEGRATION:")
print("  • Semi-Implicit Euler: Industry standard (Unity, Unreal)")
print("  • Symplectic property ensures energy conservation")
print("  • Trade-off: Speed & Stability > Theoretical Accuracy")
print("\n4.3 CAMERA SMOOTHING:")
print("  • Exponential decay: y(t) = target + (y₀ - target)e^(-kt)")
print("  • Smaller k → Smoother, cinematic motion")
print("  • Larger k → Faster, responsive tracking")
print("  • Standard in all major game engines")
print("\n" + "=" * 80)