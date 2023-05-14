import pytest
from app import app, db
from models import Category, MenuItem


@pytest.fixture(scope="session")
def test_app():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_test.db"
    app.config["TESTING"] = True

    with app.app_context():
        db.drop_all()
        db.create_all()
        
        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture(scope="session")
def test_client(test_app):
    with test_app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def init_database(test_app):
    with test_app.app_context():
        from models import Article, User

        user = User(email="test@example.com", password="password", first_name="John", last_name="Doe")
        article = Article(title="Test Article", body="This is a test article", user_id=user.id)
        init_categories()
        init_menu_items()

        db.session.add(user)
        db.session.add(article)
        
        db.session.commit()

        yield db


def init_categories():
    category1 = Category(name="Test Category 1", slug="test-category-1")
    category2 = Category(name="Test Category 2", slug="test-category-2")
    
    db.session.add_all((category1, category2))
    
    db.session.commit()
    
    
def init_menu_items():
    menu_item1 = MenuItem(name="Create New Article", link="/article/create")
    menu_item2 = MenuItem(name="Home", link="/")
    menu_item3 = MenuItem(name="Create Category", link="/category/create")

    db.session.add_all((menu_item1, menu_item2, menu_item3))
    
    db.session.commit()
