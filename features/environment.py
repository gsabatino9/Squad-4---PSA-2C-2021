import os
import tempfile
import requests_mock
from behave import fixture, use_fixture
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db import crud, database, schemas
from app.main import app, get_db
from app.config import settings

# from ..database import Base
# from ..main import app, get_db

MOCK_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
MOCK_DATA = [
    {
        'title': 'Test Ticket 1',
        'description': 'Tiket for testing number 1',
        'product_id': 1,
        'ticket_type': 'BUG',
        'severity': 1,
        'employee_id': 1,
    }
]
MOCK_PRODUCTS_NAMES = ['PSA_ORM', 'PSA_BI', 'PSA_CRM']
MOCK_REQUESTS = {
    settings.clients_url: [{"id":1,"razon social":"FIUBA","CUIT":"20-12345678-2"},{"id":2,"razon social":"FSOC","CUIT":"20-12345678-5"},{"id":3,"razon social":"Macro","CUIT":"20-12345678-3"}],
    settings.employee_url: [{"id":1,"name":"Joaquín MOCKED","last_name":"Betz Rivera"},{"id":2,"name":"Joaquín","last_name":"Fontela"},{"id":3,"name":"Guido","last_name":"Movia"},{"id":4,"name":"Christian","last_name":"Bravo"}]
}


def get_override_get_db(TestingSessionLocal):
    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()
    return override_get_db


def mock_database():
    engine = create_engine(
        MOCK_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)
    database.Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = get_override_get_db(TestingSessionLocal)
    return TestingSessionLocal

def clean_mocked_database():
    engine = create_engine(
        MOCK_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine)
    database.Base.metadata.drop_all(bind=engine)

def add_mock_data(db: Session):
    for i in range(5):
        for name in MOCK_PRODUCTS_NAMES:
            db.execute("INSERT INTO products(name, version) VALUES ('{}', {})".format(name, i))
    for mock in MOCK_DATA:
        crud.create_ticket(db, schemas.TicketCreate(**mock))


# flaskr is the sample application we want to test
@fixture
def fastapi_test_client(context, *args, **kwargs):
    sessionLocal = mock_database()
    context.client = TestClient(app)
    db = sessionLocal()
    add_mock_data(db)
    context.db = db

@fixture
def mock_request(context, *args, **kwargs):
    with requests_mock.Mocker() as m:
        for url_to_mock in MOCK_REQUESTS:
            m.get(url_to_mock, json=MOCK_REQUESTS[url_to_mock])


def before_all(context):
    # -- HINT: Recreate a new flaskr client before each feature is executed.
    use_fixture(fastapi_test_client, context)

def after_all(context):
    clean_mocked_database()
