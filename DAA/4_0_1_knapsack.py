def knapsack():
    n = int(input("Number of items: "))
    items = [tuple(map(int, input(f"Item {i+1} (weight value): ").split())) for i in range(n)]
    W = int(input("Maximum capacity: "))

    dp = [0] * (W + 1)

    for w, v in items:
        for j in range(W, w - 1, -1):
            dp[j] = max(dp[j], dp[j - w] + v)

    print("Maximum profit:", dp[W])

if __name__ == "__main__":
    knapsack()
