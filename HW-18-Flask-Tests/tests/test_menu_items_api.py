from models import MenuItem


class TestMenuItemResource:
    def test_get_menu_items(self, test_app):
        response = test_app.test_client().get('/api/menu-items')
        assert response.status_code == 200
        
        expected_menu_items = []
        menu_items = MenuItem.query.all()
        for menu_item in menu_items:
            expected_menu_items.append(menu_item.serialize)
        assert response.json == expected_menu_items

    def test_post_menu_item(self, test_app):
        menu_item_data = {
            "name": "Test Item",
            "link": "/test"
        }
        response = test_app.test_client().post('/api/menu-items', json=menu_item_data)
        assert response.status_code == 200
        
        assert response.json['name'] == menu_item_data['name']
        assert response.json['link'] == menu_item_data['link']
        
        assert MenuItem.query.filter_by(name=menu_item_data['name']).first() is not None
