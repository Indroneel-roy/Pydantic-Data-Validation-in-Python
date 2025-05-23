from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
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
    
    @model_validator(mode="after") # valided with more variable use model_validator method
    def valided_emergency_contact(cls, model):
        if model.age > 50 and "emergency" not in model.contact_details:
            raise ValueError("If age is more than 50 please add an emergecy contact")
        return model
        
    


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    # print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print("inserted")
    
patient_info = {"name" : "Shishir", "age" : "60", 'email':'abc@plc.com', 'linkedin_url':'http://linkedin.com/1322', "weight" : 60.2, "married" : True, "allergies" : ["Pollen", "Dust"], 'contact_details':{"emergency" : "0192345", 'phone':'2353462'}}    

patient1 = Patient(**patient_info)
insert_patient_data(patient1)        