```graphql
{
  Get {
    Author(where: {
      path: ["wroteArticles"],
      operator: GreaterThanEqual,
      valueInt: 2
    }) {
      name
      wroteArticles {
        ... on Article {
          title
        }
      }
    }
  }
}
```
