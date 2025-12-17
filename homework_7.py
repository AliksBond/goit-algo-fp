import random
import matplotlib.pyplot as plt

def monte_carlo_dice(num_simulations):
    sums_count = {i:0 for i in range(2,13)}
    
    for _ in range(num_simulations):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        s = die1 + die2
        sums_count[s] += 1
    
    probabilities = {s: count/num_simulations for s, count in sums_count.items()}
    return sums_count, probabilities

def analytical_probabilities():
    probabilities = {2:1/36, 3:2/36, 4:3/36, 5:4/36, 6:5/36, 7:6/36,
                     8:5/36, 9:4/36, 10:3/36, 11:2/36, 12:1/36}
    return probabilities

def plot_probabilities(mc_probs, analytical_probs):
    sums = list(range(2,13))
    mc_values = [mc_probs[s] for s in sums]
    analytical_values = [analytical_probs[s] for s in sums]
    
    plt.figure(figsize=(10,6))
    plt.bar(sums, mc_values, color='skyblue', label='Monte Carlo', alpha=0.7)
    plt.plot(sums, analytical_values, color='red', marker='o', linestyle='-', label='Analytical')
    plt.xlabel('Sum of two dice')
    plt.ylabel('Probability')
    plt.title('Probabilities of sums for two dice: Monte Carlo vs Analytical')
    plt.xticks(sums)
    plt.legend()
    plt.show()

num_simulations = 100000
sums_count, mc_probs = monte_carlo_dice(num_simulations)
analytical_probs = analytical_probabilities()

print("Monte Carlo Probabilities:")
for s in range(2,13):
    print(f"Sum {s}: {mc_probs[s]:.4f}")

print("\nAnalytical Probabilities:")
for s in range(2,13):
    print(f"Sum {s}: {analytical_probs[s]:.4f}")

plot_probabilities(mc_probs, analytical_probs)
