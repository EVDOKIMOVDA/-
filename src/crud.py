from sqlalchemy.orm import Session

from src import models, schemas


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
# 
def create_refueling(db: Session, refueling: schemas.RefuelingCreate, firm_id: int):
    db_refueling = models.Refueling(**refueling.dict(), firm_id=firm_id)
    db.add(db_refueling)
    db.commit()
    db.refresh(db_refueling)
    return db_refueling
# 
def create_daily_sale(db: Session, daily_sale: schemas.Daily_sale, fuel_id: int, refueling_id: int, client_id: int):
    db_daily_sale = models.Daily_sale(**daily_sale.dict(), fuel_id=fuel_id, refueling_id=refueling_id, client_id=client_id)
    db.add(db_daily_sale)
    db.commit()
    db.refresh(db_daily_sale)
    return db_daily_sale
# /# 
def get_client_by_number_phone(db: Session, number_phone: str):
    return db.query(models.Client).filter(models.Client.number_phone == number_phone).first()
# 
def get_firm_by_number_firm(db: Session, number_firm: str):
    return db.query(models.Firm).filter(models.Firm.number_firm == number_firm).first()
# 
def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()
# 
def get_refuelings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Refueling).offset(skip).limit(limit).all()
#   
def get_firms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Firm).offset(skip).limit(limit).all()
# 
def get_fuels(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Fuel).offset(skip).limit(limit).all()
# 
def get_daily_sales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Daily_sale).offset(skip).limit(limit).all()  
# /
def create_firm(db: Session, firm: schemas.FirmCreate):
    db_firm = models.Firm(**firm.dict())
    db.add(db_firm)
    db.commit()
    db.refresh(db_firm)
    return db_firm
# 
def create_fuel(db: Session, fuel: schemas.FuelCreate):
    db_fuel = models.Fuel(**fuel.dict())
    db.add(db_fuel)
    db.commit()
    db.refresh(db_fuel)
    return db_fuel

##
def get_client_by_id(db: Session, client_id: int):

    return db.query(models.Client).filter(models.Client.id == client_id).first()
# 
def get_refueling_by_id(db: Session, refueling_id: int):

    return db.query(models.Refueling).filter(models.Refueling.id == refueling_id).first()
# 
def get_firm_by_id(db: Session, firm_id: int):

    return db.query(models.Firm).filter(models.Firm.id == firm_id).first()
# 
def get_fuel_by_id(db: Session, fuel_id: int):

    return db.query(models.Fuel).filter(models.Fuel.id == fuel_id).first()
# 
def get_daily_sale_by_id(db: Session, daily_sale_id: int):

    return db.query(models.Daily_sale).filter(models.Daily_sale.id == daily_sale_id).first()