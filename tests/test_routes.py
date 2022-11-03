from app.models.cat import Cat

def test_get_all_cats_returns_empty_list_when_db_is_empty(client):
    # act
    response = client.get("/cats")

    # assert
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_one_cat_returns_seeded_cat(client, one_cat):
    # act
    response = client.get(f"/cats/{one_cat.id}")
    response_body = response.get_json()

    # asserts
    assert response.status_code == 200
    assert response_body["id"] == one_cat.id
    assert response_body["name"] == one_cat.name
    assert response_body["color"] == one_cat.color
    assert response_body["personality"] == one_cat.personality

def test_create_cat_can_create_cat_in_empty_db(client):
    # arrange
    EXPECTED_CAT = {
        "name": "Luna",
        "color": "black",
        "personality": "wise"
    }
    # We can assume that ID is 1 because we started from an empty DB
    EXPECTED_ID = 1

    # act
    response = client.post("/cats", json=EXPECTED_CAT)
    response_body = response.get_data(as_text=True)

    actual_cat = Cat.query.get(EXPECTED_ID)

    # assert
    assert response.status_code == 201
    assert response_body == f"Cat {EXPECTED_CAT['name']} has been created"
    assert actual_cat.id == EXPECTED_ID
    assert actual_cat.name == EXPECTED_CAT["name"]
    assert actual_cat.color == EXPECTED_CAT["color"]
    assert actual_cat.personality == EXPECTED_CAT["personality"]