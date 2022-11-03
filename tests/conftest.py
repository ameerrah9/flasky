import pytest
from app import create_app, db
from app.models.cat import Cat
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    # Hack to make sure DB stays up to date
    @request_finished.connect_via(app)
    def expire_session(send, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_cat(app):
    cat = Cat(
        name="Foo",
        color="black",
        personality="sleepy"
    )
    db.session.add(cat)
    db.session.commit()
    db.session.refresh(cat, ["id"])
    return cat