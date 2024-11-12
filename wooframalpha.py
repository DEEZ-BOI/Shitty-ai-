def wolframalpha(query):
    import wolframalpha
    client = wolframalpha.Client('T7WG97-H9UQ349YHA')
    res = client.query(query)
    return(next(res.results).text)
    