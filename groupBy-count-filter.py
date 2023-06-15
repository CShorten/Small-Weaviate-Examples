import weaviate

client = weaviate.Client("http://localhost:8080")

aggregate_demo = """
{
	Aggregate {
    PodClip (
      groupBy: ["speaker"]
    ){
      groupedBy {
    		path
        value
    	}
      meta {
        count
      }
    }
  }
}
"""

results = client.query.raw(aggregate_demo)["data"]["Aggregate"]["PodClip"]

parsed_results = []
for res in results:
    print(res.keys())
    if res["meta"]["count"] > 10:
        parsed_results.append(res)

print(parsed_results)