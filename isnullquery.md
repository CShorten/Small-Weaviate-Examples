```graphql
{
	Aggregate {
    PodClip (
      where: {
        path: ["summary"]
        operator: IsNull
        valueBoolean: false
      }
    ) {
      meta {
        count
      }
    }
  }
}
```
