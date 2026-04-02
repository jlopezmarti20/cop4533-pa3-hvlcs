from time import perf_counter
from ..main import dp
from pathlib import Path

BASE_DIR = Path(__file__).parent
input_dir = BASE_DIR / "input"
output_dir = BASE_DIR / "output"

def time_test():
    results = []
    for i in range(1, 11):
        with open(f"{input_dir}/input_{i}.txt", 'r') as f:
            n = int(f.readline())
            letter_scores = {}
            for _ in range(n):
                line = f.readline().split()
                letter_scores[line[0]] = int(line[1])
            
            A = f.readline().strip()
            B = f.readline().strip()
            start = perf_counter()
            res, substr = dp(n, letter_scores, A, B)
            end = perf_counter()
            runtime_ms = (end - start) * 100
            results.extend([runtime_ms, A, B])
    with open(f"{output_dir}/timing_results.txt", "w"):
        pass
    for i in range(0, 30, 3):
        with open(f"{output_dir}/timing_results.txt", "a") as f:
            f.write(f"{results[i]} {len(results[i+1])} {len(results[i + 2])}\n")

def main():
    time_test()

if __name__ == "__main__":
    main()
