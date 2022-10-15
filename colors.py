!pip install sentence-transformers umap-learn hdbscan > /dev/null

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# would like to have this a text file separate by \n
# f = open("colors.txt")
# colors = f.readlines()
# that would take you right to the for color in colors:

colors = [
    {
        "color": "red",
        "vector": []
    },
    {
        "color": "blue",
        "vector": []
    },{
        "color": "green",
        "vector": []
    }
]

for color in colors:
  color["vector"] = model.encode(["vector"]) 

import matplotlib.pyplot as plt

# hit this with HDBSCAN as well, lmao
