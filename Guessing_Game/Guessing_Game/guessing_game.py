# python
import random
import os
import statistics
from collections import Counter
import math

def play():
    """Original interactive game kept intact."""
    low, high = 1, 100
    rand_value = random.randint(low, high)

    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
        except ValueError:
            print("Please enter an integer.")
            continue

        if guess < low or guess > high:
            print(f"Guess out of range. Enter a number between {low} and {high}.")
            continue

        if guess == rand_value:
            print("correct")
            break
        elif guess > rand_value:
            print("guess greater than value")
            high = guess - 1
        else:
            print("guess smaller than value")
            low = guess + 1

        print(f"New range: {low} to {high}")

        if low > high:
            print(f"No valid numbers left. The number was {rand_value}.")
            break

def simulate_games(n=1000, low=1, high=100, out_file='Guessing_Game/results_binary.txt'):
    """Simulate games using binary-search guesses and records in binary."""
    out_dir = os.path.dirname(out_file)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    results = []
    for _ in range(n):
        l, h = low, high
        target = random.randint(l, h)
        attempts = 0

        while True:
            guess = (l + h) // 2  # binary search: pick middle
            attempts += 1

            if guess == target:
                break
            elif guess > target:
                h = guess - 1
            else:
                l = guess + 1

            if l > h:
                # Defensive: should not happen with valid ranges
                break

        results.append(attempts)

    with open(out_file, 'w', encoding='utf-8') as f:
        for count in results:
            f.write(bin(count)[2:] + "\n")

    counts = Counter(results)
    max_expected = math.ceil(math.log2(high - low + 1))  # for 1..100 this is 7

    print(f"Wrote {len(results)} binary results to `Guessing_Game/results_binary.txt`.")
    print(f"Summary: avg={statistics.mean(results):.2f}, min={min(results)}, max={max(results)}")

    for i in range(1, max_expected + 1):
        print(f"Guesses = {i}: {counts.get(i, 0)}")

if __name__ == "__main__":
    simulate_games()
