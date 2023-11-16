from app import app


def test_text_generation():
    with app.test_client() as client:
        # Simulate a POST request with the word "test"
        response = client.post("/", data={"word": "apple"})
        content_generated=response.get_data(as_text=True)
        print(content_generated)
        # Your assertions go here
        assert "apple" in response.get_data(as_text=True)
    # assert True
