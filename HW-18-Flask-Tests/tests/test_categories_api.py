from models import Category


class TestCategoryResource:
    def test_get_categories(self, test_app):
        response = test_app.test_client().get('/api/categories')
        assert response.status_code == 200
        
        expected_categories = []
        categories = Category.query.all()
        for category in categories:
            expected_categories.append(category.serialize)
        assert response.json == expected_categories
