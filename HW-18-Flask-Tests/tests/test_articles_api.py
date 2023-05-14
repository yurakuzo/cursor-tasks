from app import db
from models import Article


class TestArticleResource:
    def test_get_articles(self, test_app):
        response = test_app.test_client().get('/api/articles')
        assert response.status_code == 200
        
        expected_articles = []
        articles = Article.query.all()
        for article in articles:
            expected_articles.append(article.serialize)
        assert response.json == expected_articles

    def test_post_article(self, test_app):
        article_data = {
            "title": "Test Article",
            "body": "This is a test article"
        }
        response = test_app.test_client().post('/api/articles', json=article_data)
        assert response.status_code == 200
        
        assert response.json['title'] == article_data['title']
        assert response.json['body'] == article_data['body']
        
        assert Article.query.filter_by(title=article_data['title']).first() is not None

class TestArticleSingleResource:
    def test_get_article(self, test_app):
        article = Article(title="Test Article", body="This is a test article")
        db.session.add(article)
        db.session.commit()
        response = test_app.test_client().get(f'/api/articles/{article.id}')
        assert response.status_code == 200
        
        assert response.json['title'] == article.title
        assert response.json['body'] == article.body

    def test_put_article(self, test_app):
        article = Article(title="Test Article", body="This is a test article")
        db.session.add(article)
        db.session.commit()
        updated_data = {
            "title": "Updated Article",
            "body": "This is an updated article"
        }
        response = test_app.test_client().put(f'/api/articles/{article.id}', json=updated_data)
        assert response.status_code == 200
        
        updated_article = Article.query.get(article.id)
        assert updated_article.title == updated_data['title']
        assert updated_article.body == updated_data['body']

    def test_delete_article(self, test_app):
        article = Article(title="Test Article", body="This is a test article")
        db.session.add(article)
        db.session.commit()
        response = test_app.test_client().delete(f'/api/articles/{article.id}')
        assert response.status_code == 204
        
        assert Article.query.get(article.id) is None


