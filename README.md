# Semantic Vector Search

A machine learning application that builds word embeddings from newstext data, enabling semantic similarity queries and vector-based word analogies.

## What Does It Do?

This utility trains a Word2Vec model on a collection of news articles, then lets you search for words based on semantic meaning rather than text matching. It demonstrates the power of distributed word representations in capturing contextual relationships.

**Key Ability**: Find semantically related terms instantly, or compute word analogies through vector arithmetic (e.g., "king - man + woman").

## Quick Start

### Installation

```bash
cd semantic-vector-search
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Build the Embeddings

```bash
cd src
python train.py
```

This processes the news dataset and creates the model file.

### Interactive Search

```bash
python inference.py
```

Type any word to see semantically related terms.

---

## Technical Approach

The project follows a three-stage pipeline:

1. **Data Preparation**: Raw news articles are tokenized and cleaned using NLTK
2. **Model Training**: Gensim's Word2Vec learns distributed representations (100-dim vectors)
3. **Similarity Queries**: Uses cosine distance to find nearest neighbors in embedding space

The underlying principle: Words that appear in similar contexts get similar vector representations.

## Project Layout

```
.
├── src/
│   ├── train.py         # Build embeddings from dataset
│   ├── inference.py     # Search interface
│   ├── check.py         # Data inspection utility
├── models/              # Compiled Word2Vec model
├── data/                # News dataset
├── requirements.txt
└── README.md
```

## Usage Examples

### Finding Similar Terms

```
Enter search term: attack

Matching terms:
  - suspected (0.814)
  - bombing (0.802)
  - exploded (0.781)
  - incident (0.776)
  - assault (0.769)
```

### Word Arithmetic

The model supports analogy resolution:

```
king - man + woman = ?
Result: ['queen', 'princess', 'court', 'duchess', 'lady']
```

## Requirements

- Python 3.7+
- pandas (data handling)
- gensim (Word2Vec)
- nltk (text processing)

See `requirements.txt` for exact versions.

## Data

Uses a fake news classification dataset in CSV format with article content. Ensure the data file is placed in `../data/FA-KES-Dataset.csv` relative to scripts.

## Utilities

**check.py**: Inspects the dataset structure and shows available fields before training.

---

*Built with Gensim, NLTK, and Pandas*
