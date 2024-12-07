import requests

base_url = "http://localhost:5000/get_form"

def test_request():
    data = {
        "phone_field": "+7 123 456 78 90",
        "email_field": "test@example.com",
        "text_field": "Some text"
    }
    response = requests.post(base_url, data=data)
    print(response.json())

if __name__ == "__main__":
    test_request()
