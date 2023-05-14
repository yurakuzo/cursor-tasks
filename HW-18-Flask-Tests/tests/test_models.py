def test_user_model(init_database):
    from models import User

    user = User(email="test_user_model@example.com", password="password", first_name="John", last_name="Doe")
    init_database.session.add(user)
    init_database.session.commit()

    assert user.id is not None
    assert user.email == "test_user_model@example.com"
    assert user.password == "password"
    assert user.first_name == "John"
    assert user.last_name == "Doe"


def test_article_model(init_database):
    from models import Article, User

    user = User(email="test_article_model@example.com", password="password", first_name="John", last_name="Doe")
    article = Article(title="Test Article", body="This is a test article", user_id=user.id)
    
    init_database.session.add(user)
    init_database.session.add(article)
    init_database.session.commit()

    assert article.id is not None
    assert article.title == "Test Article"
    assert article.body == "This is a test article"
    # assert article.user_id == user.id


def test_category_model(init_database):
    from models import Category

    category1 = Category.query.get(1)
    category2 = Category.query.get(2)

    assert category1.id is not None
    assert category2.id is not None
    
    assert category1.name == "Test Category 1"
    assert category2.name == "Test Category 2"
    
    assert category1.slug == "test-category-1"
    assert category2.slug == "test-category-2"
