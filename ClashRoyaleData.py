import APILaunch as api
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Specify the endpoint
endpoint = "/cards"

# Fetch data using the function from APILaunch
api.endpoint_data = api.fetch_endpoint_data(endpoint)

# Extract card names and elixir costs
card_names = []
elixir_costs = []
maxed_level = []

# Dictionaries to store totals
rarity_card_counts = {}
rarity_evolution_totals = {}

for card in api.endpoint_data['items']:
    card_names.append(card['name'])
    elixir_costs.append(card.get('elixirCost', 0))  # Some cards may not have elixir cost, use 0 as default
    rarity = card.get('rarity', 'Unknown')
    evolution_level = card.get('maxEvolutionLevel', 0)
    maxed_level.append(card.get('maxLevel', 0))
    # Update card count for this rarity
    rarity_card_counts[rarity] = rarity_card_counts.get(rarity, 0) + 1

    # Update evolution total for this rarity
    rarity_evolution_totals[rarity] = rarity_evolution_totals.get(rarity, 0) + evolution_level

# Prepare data for plotting
rarities = list(rarity_card_counts.keys())
card_counts = [rarity_card_counts[r] for r in rarities]
evolution_totals = [rarity_evolution_totals[r] for r in rarities]

# Combine card names and elixir costs into a list of tuples and sort by elixir cost
cards_sorted = sorted(zip(elixir_costs, card_names))

# Unpack the sorted data
elixir_costs_sorted, card_names_sorted = zip(*cards_sorted)

# Create a single figure with multiple subplots
fig, axs = plt.subplots(2, 2, figsize=(15, 10))  # 2 rows, 2 columns

# Plot 1: Card Elixir Costs
axs[0, 0].bar(card_names_sorted, elixir_costs_sorted, color='lightskyblue')
axs[0, 0].set_xticklabels(card_names_sorted, rotation=90, fontsize=8)
axs[0, 0].set_title('Card Elixir Costs', fontsize=14)
axs[0, 0].set_xlabel('Card Name', fontsize=10)
axs[0, 0].set_ylabel('Elixir Cost', fontsize=10)

# Plot 2: Number of Cards by Rarity
axs[0, 1].bar(rarities, card_counts, color='red')
axs[0, 1].set_title('Number of Cards by Rarity', fontsize=14)
axs[0, 1].set_xlabel('Rarity', fontsize=10)
axs[0, 1].set_ylabel('Number of Cards', fontsize=10)

# Plot 3: Total Evolutions by Rarity
axs[1, 0].bar(rarities, evolution_totals, color='orange')
axs[1, 0].set_title('Total Evolutions by Rarity', fontsize=14)
axs[1, 0].set_xlabel('Rarity', fontsize=10)
axs[1, 0].set_ylabel('Total Evolution Levels', fontsize=10)

# Plot 4: Cards by Maxed Level
axs[1, 1].bar(card_names, maxed_level, color='purple')
axs[1, 1].set_xticklabels(card_names, rotation=90, fontsize=8)
axs[1, 1].set_title('Cards by Maxed Level', fontsize=14)
axs[1, 1].set_xlabel('Card Name', fontsize=10)
axs[1, 1].set_ylabel('Maxed Level', fontsize=10)

# Adjust layout for better appearance
plt.tight_layout()

# Display the single window with all plots
plt.show()
