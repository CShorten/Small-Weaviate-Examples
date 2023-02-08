```graphql
{
  Get {
    Summary (
      nearText: {
        concepts: ["What is Weaviate?"]
      },
      limit: 5
    ) {
      content
      _additional {
        generate (
          groupedResult: {
            task:"Please write a short explanation of the search results"
          }
        ){
          groupedResult
        }
      }
    }
  }
}
```
