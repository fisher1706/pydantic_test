from pydantic import BaseModel, ValidationError, Field, validator, root_validator


class City(BaseModel):
    city_id: int
    name: str = Field(alias='cityFullName')

    @validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError("Work with SPB!")
        return v

    @root_validator
    def val_root(cls, values):
        print('values:', values)
        return values


input_json = """
    {
        "city_id": "123", 
        "cityFullName": "SPB"
    }"""


try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception", e.json())
else:
    print(city)
    print(city.json())
    print(city.json(by_alias=True, exclude={"city_id"}))







