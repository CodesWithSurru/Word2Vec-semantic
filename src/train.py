import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec

nltk.download('punkt')

# Load dataset with proper encoding
news_dataset = pd.read_csv("../data/FA-KES-Dataset.csv", encoding='latin1')

# Extract article content
article_corpus = news_dataset['article_content'].astype(str)

# Text preprocessing pipeline
def preprocess_article(article):
    article = article.lower()
    article = re.sub(r'[^a-zA-Z ]', '', article)
    return word_tokenize(article)

# Process all articles
print("Processing articles...")
tokenized_corpus = [preprocess_article(article) for article in article_corpus]

# Build Word2Vec embeddings
print("Building semantic embeddings...")
semantic_model = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=100,
    window=5,
    min_count=2,
    workers=4
)

# Persist model
semantic_model.save("../models/word2vec.model")

print("Complete. Model saved to ../models/word2vec.model")