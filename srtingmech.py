
from sentence_transformers import SentenceTransformer, util

# Load pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example "typical" queries to serve as class representatives
wolfram_examples = ["What is the distance to Mars?", "Calculate 5+5", "What is the temperature today?"]
wikipedia_examples = ["Who was Albert Einstein?",'India', "Explain photosynthesis.", "What is climate change?"]
creative_examples = ["Write a story about a dragon.","Improve this", "Imagine a futuristic city.", "Describe a fantasy world."]

# Encode example sentences
wolfram_emb = model.encode(wolfram_examples, convert_to_tensor=True).mean(dim=0)
wikipedia_emb = model.encode(wikipedia_examples, convert_to_tensor=True).mean(dim=0)
creative_emb = model.encode(creative_examples, convert_to_tensor=True).mean(dim=0)

def classify_query(query):
    # Encode the query
    query_emb = model.encode(query, convert_to_tensor=True)

    # Calculate cosine similarities
    wolfram_score = util.pytorch_cos_sim(query_emb, wolfram_emb).item()
    wikipedia_score = util.pytorch_cos_sim(query_emb, wikipedia_emb).item()
    creative_score = util.pytorch_cos_sim(query_emb, creative_emb).item()

    # Determine which category has the highest similarity
    scores = {"wolfram_alpha": wolfram_score, "wikipedia": wikipedia_score, "creative": creative_score}
    return max(scores, key=scores.get)


