from time import perf_counter
from main import dp
from pathlib import Path

BASE_DIR = Path(__file__).parent
input_dir = BASE_DIR / "input"

def time_test(i):
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

    with open(f"src/output/timing_results.txt", "a") as f:
        f.write(f"{runtime_ms} {len(A)} {len(B)}\n")

def main():
    for i in range(1, 11):
        time_test(i)

if __name__ == "__main__":
    main()
