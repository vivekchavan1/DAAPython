def fractional_knapsack():
    n = int(input("Enter number of items: "))
    items = [tuple(map(float, input(f"Item {i+1} (weight value): ").split())) for i in range(n)]
    capacity = float(input("Enter knapsack capacity: "))

    # Sort items by value-to-weight ratio (descending)
    items.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_value = 0.0
    print("\nItem selection process:")

    for weight, value in items:
        if capacity == 0:
            break
        take = min(weight, capacity)
        total_value += take * (value / weight)
        print(f"  Took {take} weight from item (weight={weight}, value={value})")
        capacity -= take

    print(f"\nMaximum value in knapsack = {total_value:.2f}")

if __name__ == "__main__":
    fractional_knapsack()
