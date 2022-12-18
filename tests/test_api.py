from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению

def test_create_client():
    response = client.post(
        "/clients/",
        json={"name": "testing", "address": "ad", "number_phone" : "89638664896"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "testing"

def test_create_exist_client():
    response = client.post(
        "/clients/",
        json={"name": "testing", "address": "ad", "number_phone" : "89638664896"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Phone already registered"

def test_read_clients():
    response = client.get("/clients/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "testing"

def test_get_client_by_id():
    response = client.get("/clients/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "testing"

def test_client_not_found():
    response = client.get("/clients/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"

def test_get_client_by_phone():
    response = client.get("/clients/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["number_phone"] == "89638664896"
## 
def test_create_firm():
    response = client.post(
        "/firms/",
        json={"legal_address": "1", "number_firm": "2"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["legal_address"] == "1"

def test_create_exist_firm():
    response = client.post(
        "/firms/",
        json={"legal_address": "1", "number_firm": "2"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Phone already registered"

def test_read_firms():
    response = client.get("/firms/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["legal_address"] == "1"

def test_get_firm_by_id():
    response = client.get("/firms/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["legal_address"] == "1"

def test_firm_not_found():
    response = client.get("/firms/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"
##
def test_create_refueling():
    response = client.post(
        "/refuelings/1/firms/",
        json={"title": "100", "address_firms": "200", "firm_id": 1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "100"
    assert data["address_firms"] == "200"
    assert data["firm_id"] == 1

def test_read_refuelings():
    response = client.get("/refuelings/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["title"] == "100"
    assert data[0]["address_firms"] == "200"
    assert data[0]["firm_id"] == 1

def test_get_refueling_by_id():
    response = client.get("/refuelings/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "100"

def test_refueling_not_found():
    response = client.get("/refuelings/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"
## 
def test_create_fuel():
    response = client.post(
        "/fuels/",
        json={"kind": "12", "unit": "21", "price": "121"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["kind"] == "12"

def test_read_fuels():
    response = client.get("/fuels/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["kind"] == "12"

def test_get_fuel_by_id():
    response = client.get("/fuels/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["kind"] == "12"

def test_fuel_not_found():
    response = client.get("/fuels/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"
## 
def test_create_daily_sale():
    response = client.post(
        "/daily_sales/1/1/1/",
        json={"date_of_sale": "100", "amount": "200", "client_id": 1, "refueling_id": 1, "fuel_id": 1}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["date_of_sale"] == "100"
    assert data["amount"] == "200"
    assert data["client_id"] == 1
    assert data["refueling_id"] == 1
    assert data["fuel_id"] == 1

def test_read_daily_sales():
    response = client.get("/daily_sales/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["date_of_sale"] == "100"
    assert data[0]["amount"] == "200"
    assert data[0]["client_id"] == 1
    assert data[0]["refueling_id"] == 1
    assert data[0]["fuel_id"] == 1

def test_get_daily_sale_by_id():
    response = client.get("/daily_sales/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["date_of_sale"] == "100"

def test_daily_sale_not_found():
    response = client.get("/daily_sales/2")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "User not found"

