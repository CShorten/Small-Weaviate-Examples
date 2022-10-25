<h1> GraphQL Notepad </h1>
<br />
<h4>Super useful for debugging and monitoring importing large numbers of vectors to Weaviate! </h4>

```graphql
Aggregate {
  Product {
    meta {
      count
    }
  }
}

```
<br />
<h4>Wikipedia and Weaviate - Article, Paragraph </h4>

```graphql
{
  Get {
    Paragraph(
      nearText: {
        concepts: ["What was Obama's legacy?"],
      }
      where: {
        operator: Equal
        path: ["inArticle", "Article", "title"]
        valueString: "Barack Obama"
    ){
    content
    order
    title
    }
}

```
