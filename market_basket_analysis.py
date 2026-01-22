import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import combinations

# -------------------------------
# STEP 2: Read Data
# -------------------------------

df = pd.read_csv("transactions.csv")
print(df.head())

# -------------------------------
# STEP 3: Split Items
# -------------------------------

df["Items"] = df["Items"].apply(lambda x: x.split(","))

# -------------------------------
# STEP 4: Count Each Item
# -------------------------------

all_items = []

for basket in df["Items"]:
    for item in basket:
        all_items.append(item)

item_count = Counter(all_items)

count_df = pd.DataFrame(item_count.items(), columns=["Item","Count"])
count_df = count_df.sort_values(by="Count", ascending=False)

print(count_df)

# -------------------------------
# STEP 5: Bar Chart (Items)
# -------------------------------

plt.figure()
plt.bar(count_df["Item"], count_df["Count"])
plt.title("Item Sales Frequency")
plt.xlabel("Items")
plt.ylabel("Count")
plt.show()

# -------------------------------
# STEP 6: Item Pairs
# -------------------------------

pair_list = []

for basket in df["Items"]:
    pairs = combinations(basket, 2)
    for pair in pairs:
        pair_list.append(pair)

pair_count = Counter(pair_list)

pair_df = pd.DataFrame(pair_count.items(), columns=["Item Pair","Count"])
pair_df = pair_df.sort_values(by="Count", ascending=False)

pair_df["Pair"] = pair_df["Item Pair"].apply(lambda x: x[0] + " & " + x[1])

print(pair_df.head())

# -------------------------------
# STEP 7: Bar Chart (Pairs)
# -------------------------------

plt.figure()
plt.bar(pair_df["Pair"].head(10), pair_df["Count"].head(10))
plt.xticks(rotation=45)
plt.title("Top 10 Frequently Bought Together")
plt.xlabel("Item Pairs")
plt.ylabel("Count")
plt.show()
