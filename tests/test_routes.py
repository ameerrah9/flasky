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