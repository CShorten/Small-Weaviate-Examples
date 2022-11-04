# Calculate nDCG

# DCG = 2^rel[i] - 1 / log(i + 1)

# IDCG is this calculation with the labels

'''
Example from ritvikmath - https://www.youtube.com/watch?v=BvRMAgx0mvA

Ground Truth - (d3, d1, d2) d3 = 2, d1 = 1, d2 = 0
Ranking A - (d1, d2, d3) - so labels; d1 = 1; d2 = 0; d3 = 2

DCG Ranking A
2^1 - 1 / log(2)
+ 2^0 - 1 / log(3)
+ 2^2 - 1 / log(4)


'''
Binary case -- 1 positive doc

DCG = wherever the rank 1 doc has been put, i.e. rank 3

--> then DCG = 2^1 - 1 / log (3 + 1)

Because rel[3] is 1, the only 1 label

IDCG in this case is just 2^1 - 1 / log(2)
'''

'''
Binary case -- multiple positive docs

DCG = where the rank 1 docs have been put, i.e. ranks 1, 3, 5, 6

--> then DCG = 1 / log(2) + 1 / log(4) + 1 / log(6) + 1 / log(7) ...

IDCG = 1 / log(2) + 1 / log(3) + 1 / log(4) + 1 / log(5)
'''

# Ok so need to change how the query matching dict is setup

import math
def get_dense_performance(dense_model, vector_index, query_match_dict, index_to_query_id):
  dense_only_hits_at_1 = 0
  dense_only_hits_at_5 = 0
  dense_only_mrr = 0

  nDCG = 0

  for query in query_match_dict.keys():
    query_doc_match_set = set(query_match_dict[query]) # will need to change this when there is an order to the ranks -- or could just have a relevance_dict
    query_vector = dense_model.encode([query])
    _, results = vector_index.search(query_vector, 10)
    DCG = 0
    for rank, index in enumerate(results[0]):
      query_id = index_to_query_id[index]
      # change to in set, good thing we didn't have the break in here haha
      if query_id in query_doc_match_set:
        # hits at 1 and hits at 5 lose meaning with multiple #1 ranked documents
        if rank == 0: # I guess this still has some meaning
          dense_only_hits_at_1 += 1
        if rank < 5: # will have multiple docs in the top 5 so this metric os ruined
          dense_only_hits_at_5 += 1
        dense_only_mrr += 1 / (rank+1) # mrr may need additional normalization -- another metric ruined by multiple positive docs
        # Calculate nDCG
        # The binary relevance scores with only 1 positive label simplifies this a lot
        DCG += 1 / math.log(rank+2) # extra add 1 because of the 0 indexing in the loop

    # pretty much loop through the length of the set with binary relevance
    IDCG = 0
    print(len(query_doc_match_set))
    print(query)
    for pos_doc_counter in range(len(query_doc_match_set)):
      IDCG += 1 / math.log(pos_doc_counter+2) # 2 for the 0 indexing
    nDCG += DCG/IDCG
      
  dense_only_mrr /= len(query_match_dict.keys())
  nDCG /= len(query_match_dict.keys())

  print(f"Hits at 1 = {dense_only_hits_at_1}\nHits at 5 = {dense_only_hits_at_5}\nMRR = {dense_only_mrr}\nnDCG = {nDCG}")
