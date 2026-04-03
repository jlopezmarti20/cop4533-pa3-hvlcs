from pathlib import Path
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
output_path = BASE_DIR / "output" / "timing_results.txt"

products, times = [], []
with open(output_path, "r") as f:
    for line in f:
        parts = line.split()
        time_ms = float(parts[0])
        len_a = int(parts[1])
        len_b = int(parts[2])
        products.append(len_a * len_b)
        times.append(time_ms)

# Sort by product
paired = sorted(zip(products, times))
products, times = zip(*paired)

plt.bar([str(p) for p in products], times)
plt.xlabel("|A| x |B|")
plt.ylabel("Time (ms)")
plt.title("MCSS Runtime by Input Size")
plt.tight_layout()
plt.savefig(BASE_DIR / "output" / "runtime_plot.png")