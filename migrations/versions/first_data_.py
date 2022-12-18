"""empty message

Revision ID: first_data
Revises: f696148fd045
Create Date: 2022-12-12 20:21:28.881715

"""
from alembic import op
from sqlalchemy import orm
from src.models import Client, Fuel, Refueling, Firm, Daily_sale



# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = 'f696148fd045'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    Client1 = Client(name = "Dima", address = "gogolya 151", number_phone = "89638664896")
    Client2 = Client(name = "Nedima", address = "negogolya 151", number_phone = "ne89638664896")
    
    session.add_all([Client1, Client2])
    session.flush()

    Fuel1 = Fuel(kind = "100", unit = "litr", price = "60")
    Fuel2 = Fuel(kind = "92", unit = "litr", price = "42")
    
    session.add_all([Fuel1, Fuel2])
    session.flush()

    Firm1 = Firm(legal_address = "da", number_firm = "88005553535")
    Firm2 = Firm(legal_address = "net", number_firm = "ne88005553535")

    session.add_all([Firm1, Firm2])
    session.flush()
    
    Refueling1 = Refueling(title = "100-A", address_firms = "Studencheskaya 7, 410", firm_id = Firm1.id)
    Refueling2 = Refueling(title = "Ros", address_firms = "neStudencheskaya 7, 410", firm_id = Firm2.id)
    
    session.add_all([Refueling1, Refueling2])
    session.commit()



    Daily_sale1 = Daily_sale(date_of_sale = "segodnya", amount = "20", client_id = Client1.id, refueling_id = Refueling1.id, fuel_id = Fuel2.id)
    Daily_sale2 = Daily_sale(date_of_sale = "20:48", amount = "40", client_id = Client2.id, refueling_id = Refueling2.id, fuel_id = Fuel1.id)

    session.add_all([Daily_sale1, Daily_sale2])
    session.commit()


def downgrade() -> None:
    pass
