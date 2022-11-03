from app.models.cat import Cat

def test_get_all_cats_with_no_records(client):
    # Act
    response = client.get("/cats")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200 
    assert response_body == []

def test_get_one_cat_returns_cat(client, one_saved_cat):
    # act
    response = client.get("/cats/1")
    response_body = response.get_json()

    # assert 
    assert response.status_code == 200 
    assert response_body["id"] == one_saved_cat.id
    assert response_body["name"] == one_saved_cat.name
    assert response_body["color"] == one_saved_cat.color
    assert response_body["personality"] == one_saved_cat.personality

def test_create_cat_happy_path(client):
    # arrange
    EXPECTED_CAT = {
        "name": "Mittens",
        "color": "gray with white socks",
        "personality": "wise"
    }
    
    response = client.post("/cats", json=EXPECTED_CAT)
    response_body = response.get_data(as_text=True)
    actual_cat = Cat.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Cat {EXPECTED_CAT['name']} successfully created"
    assert actual_cat.name == EXPECTED_CAT["name"]
    assert actual_cat.color == EXPECTED_CAT["color"]
    assert actual_cat.personality == EXPECTED_CAT["personality"]