from app import app, db
import json

def test_get_itineraries():
    # Create a test client
    client = app.test_client()

    # Ensure the database is in a clean state
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Test GET request to /itineraries
    response = client.get('/itineraries')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 0  # Check if there are no itineraries in the response

    # Test POST request to create an itinerary
    itinerary_data = {
        "destination_id": 1,
        "activity": "Visit Eiffel Tower"
    }
    response = client.post('/itineraries', json=itinerary_data)
    assert response.status_code == 200  # Check if the response status code is 200 (OK)

    # Test GET request to /itineraries again
    response = client.get('/itineraries')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 1  # Check if there is one itinerary in the response

if __name__ == '__main__':
    test_get_itineraries()
