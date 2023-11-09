from app import app, db
import json

def test_get_expenses():
    # Create a test client
    client = app.test_client()

    # Ensure the database is in a clean state
    with app.app_context():
        db.drop_all()
        db.create_all()

    # Test GET request to /expenses
    response = client.get('/expenses')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 0  # Check if there are no expenses in the response

    # Test POST request to create an expense
    expense_data = {
        "destination_id": 1,
        "category": "Food",
        "amount": 50.0
    }
    response = client.post('/expenses', json=expense_data)
    assert response.status_code == 200  # Check if the response status code is 200 (OK)

    # Test GET request to /expenses again
    response = client.get('/expenses')
    assert response.status_code == 200  # Check if the response status code is 200 (OK)
    data = json.loads(response.data)
    assert len(data) == 1  # Check if there is one expense in the response

if __name__ == '__main__':
    test_get_expenses()
