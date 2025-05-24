from pydantic import BaseModel

class address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : address
    
address_dict = {'city': 'San Francisco', 'state': 'California', 'pin': '94103'}
Address1 = address(**address_dict)
patient_dict = {'name': 'Shishir', 'gender': 'male', 'age': 35, 'address': Address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.address.pin)
print(patient1.address.city)

# Convert to Dictionary (Serialization):
print(patient1.model_dump())

#Convert to json
print(patient1.model_dump_json())
