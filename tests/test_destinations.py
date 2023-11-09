from app import app, db
import json

def test_get_destinations():
    # Create a test client
    client = app.test_client()

    # Ensure the database is in a clean state
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Test GET request to /destinations
    response = client.get('/destinations')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 0  # Check if there are no destinations in the response

    # Test POST request to create a destination
    destination_data = {
        "name": "Paris",
        "description": "The City of Love",
        "location": "France"
    }
    response = client.post('/destinations', json=destination_data)
    assert response.status_code == 200  # Check if the response status code is 200 (OK)

    # Test GET request to /destinations again
    response = client.get('/destinations')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 1  # Check if there is one destination in the response

if __name__ == '__main__':
    test_get_destinations()
