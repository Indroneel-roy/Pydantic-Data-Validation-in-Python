from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):
        valid_email = ['student.edu.sust', 'plc.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_email:
            raise ValueError("not a valid email")
        return value
    
    @field_validator("name")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after') #field_validator has two mode after and before(preprocess value) by default mode is after
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    # print(patient.allergies)
    print(patient.married)
    print("inserted")
    
patient_info = {"name" : "Shishir", "age" : "30", 'email':'abc@plc.com', 'linkedin_url':'http://linkedin.com/1322', "weight" : 60.2, "married" : True, "allergies" : ["Pollen", "Dust"], 'contact_details':{'phone':'2353462'}}    

patient1 = Patient(**patient_info)
insert_patient_data(patient1)        