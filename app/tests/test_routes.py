from app.models.dog_model import Dog

def test_get_all_dogs_with_empty_db_return_empty_list(client):
    # 'client' is the fixture we registered from the conftest.py, 
    # pytest automatically tries to match each test parameter to a 
    # fixture with the same name.

    response = client.get('/dogs')

    response_body = response.get_json()

    assert response_body == []
    assert response.status_code == 200

def test_get_one_dog(client, two_saved_dogs):
    # Act
    response = client.get("/dogs/1")
    response_body = response.get_json()

    dog1 = {
        "id": 1,
        "age": 2,
        "breed": "terrier",
        "gender": "female",
        "name": "Winston"
    }

    # Assert
    assert response.status_code == 200
    # another way of writing the assert with a dictionary literal
    # assert response_body == {
    #     "id": 1,
    #     "age": 2,
    #     "breed": "terrier",
    #     "gender": "female",
    #     "name": "Winston"
    # }
    assert response_body == dog1