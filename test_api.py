import requests

# Test the Welcome Route
response = requests.get('http://localhost:5000/')
print("---- Welcome Route Test ----")
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")
print()

# Test the About Route
response = requests.get('http://localhost:5000/about')
print("---- About Route Test ----")

if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print(f"Status Code: {response.status_code}")
    print("JSON Data:", data)

    # Print individual values
    for key, value in data.items():
        print(f"{key}: {value}")
else:
    print(f"Request failed with status code {response.status_code}")

print()

# Test the Greeting Route
name = "RK"  # change this to your actual name if you want
response = requests.get(f'http://localhost:5000/greet/{name}')

print("---- Greeting Route Test ----")
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

# Verify name is in response
if name in response.text:
    print("Name verification: PASSED")
else:
    print("Name verification: FAILED")

print()

# Test the Calculator Route
print("---- Calculator Route Test ----")

operations = [
    {"num1": 10, "num2": 5, "operation": "add"},
    {"num1": 10, "num2": 0, "operation": "divide"}  # will test division by zero
]

for op in operations:
    response = requests.get(
        f"http://localhost:5000/calculate?num1={op['num1']}&num2={op['num2']}&operation={op['operation']}"
    )

    print(f"Testing {op['operation']} with num1={op['num1']} and num2={op['num2']}")
    print(f"Status Code: {response.status_code}")

    try:
        data = response.json()
        print("Response JSON:", data)
    except Exception as e:
        print("Failed to parse JSON:", e)

    print()

# Test the Echo Route (POST)
print("---- Echo Route Test ----")

url = "http://localhost:5000/echo"
payload = {"message": "Hello Flask"}

response = requests.post(url, json=payload)
print(f"Status Code: {response.status_code}")

try:
    data = response.json()
    print("Response JSON:", data)

    # Verify "echoed" field
    if data.get("echoed") is True:
        print("Echo verification: PASSED")
    else:
        print("Echo verification: FAILED")
except Exception as e:
    print("Failed to parse JSON:", e)

print()

# Test Custom Headers
print("---- Custom Header Test ----")

response = requests.get("http://localhost:5000/")  # you can use any route

custom_header = response.headers.get("X-Custom-Header")
print(f"Status Code: {response.status_code}")
print(f"Custom Header: {custom_header}")

# Verify header is correct
if custom_header == "FlaskRocks":
    print("Custom header verification: PASSED")
else:
    print("Custom header verification: FAILED")

print()

# Test Error Handling (division by zero)
print("---- Error Handling Test ----")

response = requests.get(
    "http://localhost:5000/calculate?num1=10&num2=0&operation=divide"
)

print(f"Status Code: {response.status_code}")

try:
    data = response.json()
    print("Response JSON:", data)

    # Verify error message
    if "error" in data:
        print("Error handling verification: PASSED")
    else:
        print("Error handling verification: FAILED")
except Exception as e:
    print("Failed to parse JSON:", e)

print()
