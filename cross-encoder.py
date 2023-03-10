!pip install sentence-transformers > /dev/null

from sentence_transformers.cross_encoder import CrossEncoder
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

# all this comes from Weaviate
# so say these are the top 100 vector search results that are meh quality

ids = [5, 10]
query = "How do I get to New York from Boston"
documents = [
    "The amtrak train can take you from South Station Boston to New York",
    "Dogs are good pets."
]

cross_inps = [[query, document] for document in documents]
scores = cross_encoder.predict(cross_inps)

# now they are super high quality thanks to the cross encoder!

id_score_dict = {}
for idx, score in enumerate(scores):
  id_score_dict[ids[idx]] = score

# should the sorting happen here in Python?, if so here is how to do it
id_score_dict = sorted(id_score_dict.items(), key = lambda item: item[1], reverse=True)
print(id_score_dict)
