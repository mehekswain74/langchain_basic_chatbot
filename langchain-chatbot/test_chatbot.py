import requests
import json

def test_chatbot(query):
    url = "http://localhost:5000/chat"
    headers = {"Content-Type": "application/json"}
    data = {"query": query}

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    test_query = "What courses are available?"
    result = test_chatbot(test_query)
    print(f"Query: {test_query}")
    print(f"Response: {result}")

