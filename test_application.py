from application import application

def test_get_all_heroes():
    response = application.test_client().get("/")
    
    assert response.status_code == 200
    assert "0" in response.get_json()

def test_get_hero_by_id():
    response = application.test_client().get("/0")
    
    assert response.status_code == 200
    assert response.get_json()["name"] == "A-Bomb"

def test_get_hero_by_id_not_found():
    response = application.test_client().get("/9999")
    
    assert response.status_code == 404