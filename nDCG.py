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
