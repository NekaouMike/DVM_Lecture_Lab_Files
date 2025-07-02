import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('spotify-2023.csv', encoding='ISO-8859-1')

# Display basic info about the dataset
display(df.head())

# Visualizing distributions
fig, axes = plt.subplots(3, 2, figsize=(12, 12))
sns.histplot(df['bpm'], bins=30, kde=True, ax=axes[0, 0]).set_title("BPM Distribution")
sns.histplot(df['key'], bins=12, kde=False, discrete=True, ax=axes[0, 1]).set_title("Key Distribution")
sns.histplot(df['danceability_%'], bins=30, kde=True, ax=axes[1, 0]).set_title("Danceability Distribution")
sns.histplot(df['energy_%'], bins=30, kde=True, ax=axes[1, 1]).set_title("Energy Distribution")
sns.histplot(df['speechiness_%'], bins=30, kde=True, ax=axes[2, 0]).set_title("Speechiness Distribution")
sns.histplot(df['acousticness_%'], bins=30, kde=True, ax=axes[2, 1]).set_title("Acousticness Distribution")
plt.tight_layout()
plt.show()

# Identifying the most common characteristics
optimal_bpm = df['bpm'].mode()[0]
optimal_key = df['key'].mode()[0]
optimal_mode = df['mode'].mode()[0]
optimal_danceability = df['danceability_%'].median()
optimal_energy = df['energy_%'].median()
optimal_speechiness = df['speechiness_%'].median()
optimal_acousticness = df['acousticness_%'].median()

print(f"Optimal Values for a Smash Hit:")
print(f"BPM: {optimal_bpm}")
print(f"Key: {optimal_key}")
print(f"Mode: {optimal_mode}")
print(f"Danceability: {optimal_danceability:.2f}")
print(f"Energy: {optimal_energy:.2f}")
print(f"Speechiness: {optimal_speechiness:.2f}")
print(f"Acousticness: {optimal_acousticness:.2f}")

# Finding existing songs that match these optimal criteria
hit_songs = df[(df['bpm'] == optimal_bpm) &
               (df['key'] == optimal_key) &
               (df['mode'] == optimal_mode) &
               (df['danceability_%'].between(optimal_danceability - 0.05, optimal_danceability + 0.05)) &
               (df['energy_%'].between(optimal_energy - 0.05, optimal_energy + 0.05)) &
               (df['speechiness_%'].between(optimal_speechiness - 0.05, optimal_speechiness + 0.05)) &
               (df['acousticness_%'].between(optimal_acousticness - 0.05, optimal_acousticness + 0.05))]

# Display hit songs
if not hit_songs.empty:
    print("Songs that meet the optimal criteria:")
    display(hit_songs[['Artist', 'Title', 'bpm', 'key', 'mode', 'danceability', 'energy', 'speechiness', 'acousticness']])
else:
    print("No exact matches found.")
