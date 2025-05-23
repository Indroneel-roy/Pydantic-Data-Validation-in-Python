from pydantic import BaseModel, EmailStr, AnyUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: str
    age: int
    email: EmailStr
    linkedin_url: AnyUrl
    weight: float #kg
    height : float #meters
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height**2), 2)
        return bmi
        
        
    


def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.allergies)
    # print(patient.allergies)
    print(patient.married)
    print(patient.contact_details)
    print("BMI : ", patient.bmi)
    print("inserted")
    
patient_info = {"name" : "Shishir", "age" : "60", 'email':'abc@plc.com', 'linkedin_url':'http://linkedin.com/1322', "weight" : 60.2, "height" : 1.6, "married" : True, "allergies" : ["Pollen", "Dust"], 'contact_details':{"emergency" : "0192345", 'phone':'2353462'}}    

patient1 = Patient(**patient_info)
insert_patient_data(patient1)        