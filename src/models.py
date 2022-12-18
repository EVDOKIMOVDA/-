from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>" # pragma: no cover

class Client(BaseModel):
    __tablename__ = "clients"

    name = Column(String)
    address = Column(String)
    number_phone = Column(String, unique = True)

    daily_sale = relationship("Daily_sale", back_populates="client")


class Refueling(BaseModel):
    __tablename__ = "refuelings"

    title = Column(String)
    address_firms = Column(String)

    firm_id = Column(Integer, ForeignKey("firms.id"))
    firm = relationship("Firm", back_populates="refueling")

    daily_sale = relationship("Daily_sale", back_populates="refueling")
    

class Firm(BaseModel):
    __tablename__ = "firms"

    legal_address = Column(String)
    number_firm = Column(String, unique = True)

    refueling = relationship("Refueling", back_populates="firm")

class Fuel(BaseModel):
    __tablename__ = "fuels"

    kind = Column(String)
    unit = Column(String)
    price = Column(String)

    daily_sale = relationship("Daily_sale", back_populates="fuel")

class Daily_sale(BaseModel):
    __tablename__ = "daily_sales"

    date_of_sale = Column(String)
    amount = Column(String)

    client_id = Column(Integer, ForeignKey("clients.id"))
    refueling_id = Column(Integer, ForeignKey("refuelings.id"))
    fuel_id = Column(Integer, ForeignKey("fuels.id"))

    client = relationship("Client", back_populates="daily_sale")
    refueling = relationship("Refueling", back_populates="daily_sale")
    fuel = relationship("Fuel", back_populates="daily_sale")
    

