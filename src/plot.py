import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Output directory
plot_dir = Path("plots")
plot_dir.mkdir(exist_ok=True)  # Folder create karega agar exist nahi karta

# Data generate karna (Sine wave + Noise)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(scale=0.2, size=len(x))

# Plot create karna
plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Sine Wave with Noise", color="blue", linestyle="--")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Random Sine Wave Plot")
plt.legend()
plt.grid(True)

# Save the plot
plot_path = plot_dir / "plot.png"
plt.savefig(plot_path)
plt.show()

print(f"Plot saved at: {plot_path}")
