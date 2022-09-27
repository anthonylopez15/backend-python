from faker import Faker

from .user_repository import UserRepository
from ..config import DBConnectionHandler

faker = Faker()
user_repository = UserRepository()
db_connection = DBConnectionHandler()


def test_insert_user():
    name = faker.name()
    password = faker.password()
    engine = db_connection.get_engine()

    new_user = user_repository.insert_user(name, password)
    query_user = engine.execute(
        "SELECT * FROM users WHERE id='{}';".format(new_user.id)
    ).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}';".format(new_user.id))

    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.password == query_user.password
