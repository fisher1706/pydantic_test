from pydantic import BaseModel, ValidationError, Field


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')


input_json = """
    {
        "city_id": "123", 
        "cityFullName": "Moscow"
    }"""


try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)
    print(city.json())
    print(city.json(by_alias=True, exclude={"city_id"}))







