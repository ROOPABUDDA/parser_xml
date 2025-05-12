import matplotlib.pyplot as plt
import numpy as np

def draw_water_level_gauge(level_ft, min_ft=900, max_ft=1200):
    fig, ax = plt.subplots(figsize=(6, 4), subplot_kw={'projection': 'polar'})
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Hide the frame
    ax.set_frame_on(False)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    # Value normalization
    level = np.clip(level_ft, min_ft, max_ft)
    norm_level = (level - min_ft) / (max_ft - min_ft)

    # Tick marks
    num_ticks = 50
    ticks = np.linspace(0, np.pi, num_ticks)
    ax.bar(ticks, np.ones(num_ticks) * 1.0, width=0.015, bottom=1.5, color='black')

    # Gauge segments
    zones = [
        (0.0, 0.1, '#ff4c4c', 'DEAD POOL'),       # red
        (0.1, 0.25, '#ff9900', 'MIN POWER POOL'), # orange
        (0.25, 0.85, '#66c2ff', ''),              # blue
        (0.85, 1.0, '#4caf50', 'FULL POOL')       # green
    ]
    
    for start, end, color, label in zones:
        angles = np.linspace(start * np.pi, end * np.pi, 100)
        ax.bar(angles, np.ones_like(angles) * 1.0, width=0.02, bottom=1.5, color=color, edgecolor='none')

    # Water level needle
    level_angle = norm_level * np.pi
    ax.bar(level_angle, 1.2, width=0.03, bottom=1.5, color='navy', zorder=5)

    # Text labels
    ax.text(0, 0.5, f'{int(level_ft)} ft', ha='center', va='center', fontsize=18, fontweight='bold', color='navy')
    ax.text(0, 2.8, 'LAKE MEAD', ha='center', va='center', fontsize=14, fontweight='bold', color='lightblue')

    # Zone labels
    ax.text(np.pi * 0.07, 2.3, 'DEAD\nPOOL', ha='center', va='center', fontsize=9, color='black')
    ax.text(np.pi * 0.18, 2.4, 'MIN\nPOWER\nPOOL', ha='center', va='center', fontsize=8, color='black')
    ax.text(np.pi * 0.93, 2.4, 'FULL\nPOOL', ha='center', va='center', fontsize=9, color='black')

    plt.tight_layout()
    plt.show()

# Example usage
draw_water_level_gauge(1060)
