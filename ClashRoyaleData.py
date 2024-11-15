import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open("mykey.txt") as f:
    my_key = f.read().strip()

base_url = "https://api.clashroyale.com/v1"
endpoint = "/cards"


# Prepare the request with the Authorization header (fixing the dictionary issue)
headers = {
    "Authorization": f"Bearer {my_key}"
}

# Construct the request with the proper headers
request = urllib.request.Request(
    base_url + endpoint, headers=headers
)

# Send the request and get the response
response = urllib.request.urlopen(request).read().decode("utf-8")
#print(response)

data = json.loads(response)

# Write the data to a JSON file using UTF-8 encoding
with open("ClashRoyaleView.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)


# Load the data from the JSON file
with open("ClashRoyaleView.json", "r", encoding="utf-8") as json_file:
    cards_data = json.load(json_file)

# Extract card names and elixir costs
card_names = []
elixir_costs = []

# Dictionaries to store totals
rarity_card_counts = {}
rarity_evolution_totals = {}

for card in cards_data['items']:
    card_names.append(card['name'])
    elixir_costs.append(card.get('elixirCost', 0))  # Some cards may not have elixir cost, use 0 as default
    rarity = card.get('rarity', 'Unknown')
    evolution_level = card.get('maxEvolutionLevel', 0)
    
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
elixir_costs_sorted, card_names_sorted= zip(*cards_sorted)

# Create a vertical bar chart using matplotlib
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.bar(card_names_sorted, elixir_costs_sorted, color='lightskyblue')

# Rotate the card names on the x-axis for readability
ax1.set_xticklabels(card_names_sorted, rotation=90, fontsize=10)

# Set chart title and labels
ax1.set_title('Card Elixir Costs', fontsize=16)
ax1.set_xlabel('Card Name', fontsize=12)
ax1.set_ylabel('Elixir Cost', fontsize=12)

# Create bar charts
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.bar(rarities, card_counts, color='red')
ax2.set_title('Number of Cards by Rarity', fontsize=16)
ax2.set_xlabel('Rarity', fontsize=12)
ax2.set_ylabel('Number of Cards', fontsize=12)

fig, ax3 = plt.subplots(figsize=(10, 6))
ax3.bar(rarities, evolution_totals, color='orange')
ax3.set_title('Total Evolutions by Rarity', fontsize=16)
ax3.set_xlabel('Rarity', fontsize=12)
ax3.set_ylabel('Total Evolution Levels', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()