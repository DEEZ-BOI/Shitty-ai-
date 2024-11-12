    ##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
def creative_answer(query):    
    from langchain_groq import ChatGroq as cgq
    llm = cgq(groq_api_key = "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", model_name = "gemma-7b-it")
    response = llm.invoke(query)
    return response.content

