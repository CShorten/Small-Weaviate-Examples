import weaviate

client = weaviate.Client("http://localhost:8080")

schema = {
    "classes": [
        {
            "class": "TimeObj",
            "description": "A time object test.",
            "properties": [
                {
                    "dataType": ["date"],
                    "name": "timeEntered",
                    "description": "The time this data object was added to Weaviate.",
                },
                {
                    "dataType": ["int"],
                    "name": "idx",
                    "description": "idx used to test the time sorting"
                }
            ]
        }
    ]
}

client.schema.create(schema)

from datetime import datetime, timezone
import time
from weaviate.util import generate_uuid5

for x in range(5):
    datetime_now = datetime.now()
    datetime_now = datetime_now.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    client.data_object.create(
        data_object = {
            "timeEntered": datetime_now,
            "idx": x
        },
        uuid = generate_uuid5(x),
        class_name = "TimeObj"
    )
    time.sleep(2)

'''graphql
{
	Get {
    TimeObj (
     sort: [{
      path: ["timeEntered"],
      order: desc
    }] 
    ){
      idx
      timeEntered
    }
  }
}
'''