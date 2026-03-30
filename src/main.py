def main():
    k = int(input().strip())

    letter_scores = {}

    for _ in range(k):
        letter, score = input().split()
        letter_scores[letter] = int(score)

    A = input().strip()
    B = input().strip()

    best_value = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                best_value[i][j] = best_value[i - 1][j - 1] + letter_scores[A[i - 1]]
            else:
                best_value[i][j] = max(best_value[i - 1][j], best_value[i][j - 1])

    i = len(A)
    j = len(B)
    picked_letters = []

    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            picked_letters.append(A[i - 1])
            i -= 1
            j -= 1
        elif best_value[i - 1][j] >= best_value[i][j - 1]:
            i -= 1
        else:
            j -= 1

    picked_letters.reverse()
    best_subsequence = "".join(picked_letters)

    print(best_value[len(A)][len(B)])
    print(best_subsequence)


if __name__ == "__main__":
    main()