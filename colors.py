!pip install sentence-transformers umap-learn hdbscan > /dev/null

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

# would like to have this a text file separate by \n
# f = open("colors.txt")
# colors = f.readlines()
# that would take you right to the for color in colors:

'''
{
  "color": "Red",
  "rgb_vector": (255,255,0),
  "SentenceTransformer": {
    "model_name": "all-MiniLM-L6-v2",
    "vector": [0.3, 0.5, ..., 1.6],
    "UMAP-3D-vector": [1.7, 2.7, 8.1],
    "UMAP-2D-vector": [8.5, 11.7],
   },
   "SentenceTransformer": {
    "model_name": "paraphrase-MiniLM-L6-v2",
    "vector": [1.4, 0.02, ..., 0.08],
    "UMAP-3D-vector": [1.708, 9.7, 8.9],
    "UMAP-2D-vector": [10.5, 0.7],
   }
  ...
}
'''


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
