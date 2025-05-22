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

from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class User(BaseModel):
    name: str
    age: int

data = {'name': 'Alice', 'age': '25'}  # '25' is a string

user = User(**data)
print(user.age)  # it converted automatically to to int
                
##

class Patient(BaseModel):
    name  : Annotated[str, Field(max_length=50, title="Name of the patient", description="Type the name of the patient")]
    age : int
    email: EmailStr
    linkedin_url: AnyUrl
    weight : float = Field(gt=0)
    married : bool = False
    allergies : Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details : Dict[str, str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    # print(patient.allergies)
    print(patient.married)
    print("inserted")
    
patient_info = {"name" : "Shishir", "age" : "30", 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', "weight" : 60.2, "married" : True, "allergies" : ["Pollen", "Dust"], 'contact_details':{'phone':'2353462'}}    

patient1 = Patient(**patient_info)
insert_patient_data(patient1)        