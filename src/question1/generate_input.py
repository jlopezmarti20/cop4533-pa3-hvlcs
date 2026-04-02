import random
from pathlib import Path

random.seed(42)

BASE_DIR = Path(__file__).parent
input_dir = BASE_DIR / "input"
input_dir.mkdir(parents=True, exist_ok=True)

POSSIBLE_CHARS = ['a', 'b', 'c', 'd', 'e']
SIZES = [25, 28, 32, 35, 38, 42, 48, 55, 65, 80]


def generate_test(i: int) -> None:
    weights = {char: random.randint(0, 100) for char in POSSIBLE_CHARS}

    len_s1 = SIZES[i - 1]
    len_s2 = SIZES[i - 1] + random.randint(-3, 3)

    s1 = ''.join(random.choices(POSSIBLE_CHARS, k=len_s1))
    s2 = ''.join(random.choices(POSSIBLE_CHARS, k=len_s2))

    with open(input_dir / f"input_{i}.txt", 'w') as file:
        file.write(f"{len(POSSIBLE_CHARS)}\n")
        for char in POSSIBLE_CHARS:
            file.write(f"{char} {weights[char]}\n")
        file.write(f"{s1}\n")
        file.write(s2)


if __name__ == "__main__":
    for i in range(1, 11):
        generate_test(i)