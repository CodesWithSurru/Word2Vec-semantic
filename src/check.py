import pandas as pd

# Load and inspect dataset
news_data = pd.read_csv("../data/FA-KES-Dataset.csv", encoding='latin1')

print("Dataset Preview:")
print("=" * 50)
print(news_data.head())

print("\n\nAvailable Fields:")
print("=" * 50)
for idx, field in enumerate(news_data.columns, 1):
    print(f"{idx}. {field}")