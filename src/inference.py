from gensim.models import Word2Vec

# Initialize embedding model
semantic_model = Word2Vec.load("../models/word2vec.model")

vocab_size = len(semantic_model.wv.index_to_key)
print(f"Loaded vocabulary with {vocab_size} terms")
print(f"Sample terms: {semantic_model.wv.index_to_key[:30]}\n")

# Retrieve semantically similar terms
def get_similar_terms(search_term):
    if search_term not in semantic_model.wv:
        return f"'{search_term}' not found in model vocabulary"
    
    similar_matches = semantic_model.wv.most_similar(search_term, topn=5)
    
    formatted_results = []
    for term, similarity_score in similar_matches:
        formatted_results.append(f"{term} ({similarity_score:.3f})")
    
    return formatted_results

# Perform vector-based word analogies
def compute_analogy(base_word, exclude_word, target_word):
    try:
        analogy_results = semantic_model.wv.most_similar(
            positive=[base_word, target_word], 
            negative=[exclude_word], 
            topn=5
        )
  Main CLI loop
if __name__ == "__main__":
    print("Semantic Search Interface")
    print("=" * 40)
    
    while True:
        search_query = input("\nEnter search term (type 'quit' to exit): ").strip().lower()
        
        if search_query == "quit":
            break
        
        matching_terms = get_similar_terms(search_query)

        print("\nMatching terms:")
        
        if isinstance(matching_terms, str):
            print(f"  {matching_terms}")
        else:
            for match in matching_terms:
                print(f"  - {match}")

    print("\n[Vector Analogy Example]")
    print("king - man + woman = ?")
    analogy_result = compute_analogy("king", "man", "woman")
    print(f"Result: {analogy_result}"

    print("\n📌 Vector Example:")
    print("king - man + woman =")
    print(word_math("king", "man", "woman"))
    