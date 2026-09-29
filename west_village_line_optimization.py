import random
import matplotlib.pyplot as plt

NUM_STUDENTS = 100


def current_line():
    """Current dining hall setup"""
    total_wait = 0

    for _ in range(NUM_STUDENTS):
        total_wait += random.randint(4, 10)

    return total_wait / NUM_STUDENTS


def second_serving_station():
    """Adds another serving station"""
    total_wait = 0

    for _ in range(NUM_STUDENTS):
        total_wait += random.randint(2, 7)

    return total_wait / NUM_STUDENTS


def express_line():
    """Separate line for quick meals"""
    total_wait = 0

    for _ in range(NUM_STUDENTS):
        total_wait += random.randint(1, 6)

    return total_wait / NUM_STUDENTS


results = {
    "Current Line": current_line(),
    "Second Station": second_serving_station(),
    "Express Line": express_line(),
}

print("\nWest Village Lunch Line Simulation")
print("-" * 40)

for option, wait_time in results.items():
    print(f"{option}: {wait_time:.1f} minutes")

best_option = min(results, key=results.get)

print("\nBest Option:")
print(f"{best_option} ({results[best_option\]:.1f} minutes)")

# Create chart
plt.figure(figsize=(8, 5))

plt.bar(
    results.keys(),
    results.values(),
    color=["red", "orange", "green"]
)

plt.title("West Village Lunch Line Optimization")
plt.ylabel("Average Wait Time (
