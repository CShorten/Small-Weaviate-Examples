import weaviate

client = weaviate.Client("http://localhost:8080")

updated_schema = {
    "name": "J. Kantor"
}

# Update only the properties in variable "updated_schema"
client.data_object.update(
    updated_schema,
    class_name="Author",
    "36ddd591-2dee-4e7e-a3cc-eb86d30a4303"
    consistency_level=weaviate.data.replication.ConsistencyLevel.ALL,  # default QUORUM
)
