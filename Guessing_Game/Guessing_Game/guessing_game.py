import random
from collections import Counter

def simulate_games(n=1000, low=1, high=100):
    """
    Run n simulations using binary-search guesses.
    Print per-number totals and average guesses per game to the console.
    Returns the Counter of total guesses per number.
    """
    counts = Counter()
    for _ in range(n):
        l, h = low, high
        target = random.randint(l, h)
        while True:
            guess = (l + h) // 2
            counts[guess] += 1
            if guess == target:
                break
            if guess > target:
                h = guess - 1
            else:
                l = guess + 1

    # Print CSV-like header and rows to console
    print("number,total_guesses,avg_per_game")
    for num in range(low, high + 1):
        total = counts.get(num, 0)
        avg = total / n
        print(f"{num},{total},{avg:.6f}")

    return counts

if __name__ == "__main__":
    simulate_games()
