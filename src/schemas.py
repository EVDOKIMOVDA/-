from pydantic import BaseModel

class Daily_saleBase(BaseModel):
    date_of_sale: str
    amount: str
    

class Daily_saleCreate(Daily_saleBase):
    pass

class Daily_sale(Daily_saleBase):
    id: int
    client_id: int
    refueling_id: int
    fuel_id: int

    class Config:
        orm_mode = True
# 
class ClientBase(BaseModel):
    name: str
    address: str
    number_phone: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    daily_sale: list[Daily_sale]=[]

    class Config:
        orm_mode = True
# 
class RefuelingBase(BaseModel):
    title: str
    address_firms: str
    

class RefuelingCreate(RefuelingBase):
    pass

class Refueling(RefuelingBase):
    id: int
    firm_id: int
    daily_sale: list[Daily_sale]=[]

    class Config:
        orm_mode = True
# 
class FirmBase(BaseModel):
    legal_address: str
    number_firm: str
    

class FirmCreate(FirmBase):
    pass

class Firm(FirmBase):
    id: int

    refueling: list[Refueling]=[]

    class Config:
        orm_mode = True
# 
class FuelBase(BaseModel):
    kind: str
    unit: str
    price: str
    

class FuelCreate(FuelBase):
    pass

class Fuel(FuelBase):
    id: int

    daily_sale: list[Daily_sale]=[]

    class Config:
        orm_mode = True
# 

