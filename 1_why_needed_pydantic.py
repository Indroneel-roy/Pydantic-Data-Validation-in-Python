#You have a web form or API where users submit data. You want to ensure the data is valid.

# without pytandic we do manually check everything
def valid_data(data):
    if "age" in data:
        try:
            age = int(data["age"])
        except ValueError:
            raise Exception("invalid age")
    else:
        raise Exception("missing age")    
    
# With Pydantic:
# It handles this automatically:    

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

data = {'name': 'Alice', 'age': '25'}  # '25' is a string

user = User(**data)
print(user.age)  # it converted automatically to to int
                
