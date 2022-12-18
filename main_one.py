# https://www.youtube.com/watch?v=dOO3GmX6ukU

from pydantic import BaseModel, ValidationError
from typing import List


class Tag(BaseModel):
    id: int
    tag: str


class City(BaseModel):
    city_id: int
    name: str
    tags: List[Tag]


input_json = """
    {
        "city_id": "123", 
        "name": "Moscow", 
        "tags": [
            {"id": 1, "tag": "capital"},
            {"id": 2, "tag": "big_city"}
        ]
        
        "tags": [
            {"id": 1, "tag": "capital"},
            {"id": 2, "tag": "big_city"}
        ]
    }
    """


try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception", e.json())
# else:
#     print(city)
#     tag = city.tags[0]
#     print(tag)
#     print(tag.json())






