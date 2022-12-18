from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():

    db = SessionLocal() # pragma: no cover
    try: # pragma: no cover
        yield db # pragma: no cover
    finally: # pragma: no cover
        db.close() # pragma: no cover

@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client(client_id: int, db: Session = Depends(get_db)):
    
    db_client = crud.get_client_by_id(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_client
##
@app.get("/refuelings/", response_model=list[schemas.Refueling])
def read_refuelings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   
    refuelings = crud.get_refuelings(db, skip=skip, limit=limit)
    return refuelings


@app.get("/refuelings/{refueling_id}", response_model=schemas.Refueling)
def read_refueling(refueling_id: int, db: Session = Depends(get_db)):
    
    db_refueling = crud.get_refueling_by_id(db, refueling_id=refueling_id)
    if db_refueling is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_refueling
## 
@app.get("/firms/", response_model=list[schemas.Firm])
def read_firms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   
    firms = crud.get_firms(db, skip=skip, limit=limit)
    return firms


@app.get("/firms/{firm_id}", response_model=schemas.Firm)
def read_firm(firm_id: int, db: Session = Depends(get_db)):
    
    db_firm = crud.get_firm_by_id(db, firm_id=firm_id)
    if db_firm is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_firm
##
@app.get("/fuels/", response_model=list[schemas.Fuel])
def read_fuels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   
    fuels = crud.get_fuels(db, skip=skip, limit=limit)
    return fuels


@app.get("/fuels/{fuel_id}", response_model=schemas.Fuel)
def read_fuel(fuel_id: int, db: Session = Depends(get_db)):
    
    db_fuel = crud.get_fuel_by_id(db, fuel_id=fuel_id)
    if db_fuel is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_fuel
##
@app.get("/daily_sales/", response_model=list[schemas.Daily_sale])
def read_daily_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
   
    daily_sales = crud.get_daily_sales(db, skip=skip, limit=limit)
    return daily_sales


@app.get("/daily_sales/{daily_sale_id}", response_model=schemas.Daily_sale)
def read_daily_sale(daily_sale_id: int, db: Session = Depends(get_db)):
    
    db_daily_sale = crud.get_daily_sale_by_id(db, daily_sale_id=daily_sale_id)
    if db_daily_sale is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_daily_sale
###
@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_number_phone(db,number_phone = client.number_phone)
    if db_client:
        raise HTTPException(status_code=400, detail="Phone already registered")
    return crud.create_client(db=db, client=client)
##
@app.post("/firms/", response_model=schemas.Firm)
def create_firm(firm: schemas.FirmCreate, db: Session = Depends(get_db)):
    db_firm = crud.get_firm_by_number_firm(db,number_firm=firm.number_firm)
    if db_firm:
        raise HTTPException(status_code=400, detail="Phone already registered")
    return crud.create_firm(db=db, firm=firm)
##
@app.post("/fuels/", response_model=schemas.Fuel)
def create_fuel(fuel: schemas.FuelCreate, db: Session = Depends(get_db)):
    return crud.create_fuel(db=db, fuel=fuel)
###
@app.post("/refuelings/{firm_id}/firms/", response_model=schemas.Refueling)
def create_refueling_for_firm(
    firm_id: int, refueling: schemas.RefuelingCreate, db: Session = Depends(get_db)
    ):
    
    return crud.create_refueling(db=db, refueling=refueling, firm_id=firm_id)
##
@app.post("/daily_sales/{client_id}/{refueling_id}/{fuel_id}/", response_model=schemas.Daily_sale)
def create_daily_sale(
    client_id: int,refueling_id: int,fuel_id: int, daily_sale: schemas.Daily_saleCreate, db: Session = Depends(get_db)
    ):
    
    return crud.create_daily_sale(db=db, daily_sale=daily_sale, client_id=client_id, fuel_id=fuel_id, refueling_id=refueling_id)
