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
<br />
<br />
```graphql
{
  Get {
    Summary (
      where: {
        path: ["podNum"]
        operator:Equal
        valueInt: 35
      }
    ) {
      content
      _additional {
        generate (
          groupedResult: {
            task:"Please write a summary of the content in all of the search results. Please make it exciting!"
          }
        ){
          groupedResult
        }
      }
    }
  }
}
```
