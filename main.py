import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi import Query
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the Numbers API base URL
NUMBERS_API_URL = "http://numbersapi.com/"


def get_fun_fact(number: int):
    try:
        url = f"http://numbersapi.com/{number}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error fetching fun fact: " + str(e))


def get_fun_fact(number: int) -> str:
    """Fetch a fun fact about a number from the Numbers API."""
    try:
        response = requests.get(f"{NUMBERS_API_URL}{number}")
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except:
        return "Error fetching fun fact."

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    """Check if a number is perfect (sum of divisors equals the number)."""
    if n < 2:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    # Check if the number is negative
    if n < 0:
        return False  # Armstrong numbers are not defined for negative numbers

    digits = [int(digit) for digit in str(n)]
    num_digits = len(digits)
    return sum(digit ** num_digits for digit in digits) == n

def get_digit_sum(n: int) -> int:
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

from fastapi import HTTPException

@app.get("/api/classify-number")
def classify_number(number: int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Number cannot be negative.")
    
    if not isinstance(number, int):  # If it's not an integer
        raise HTTPException(status_code=400, detail="Input must be an integer.")

    # Your classification logic here...
    properties = []
    # Example logic for prime check
    if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)):
        properties.append("prime")
    
    # Continue with the rest of the logic...
@app.get("/api/classify-number/{number}")
def classify_number(number: int):
    if number == 0:  # This is just an example to simulate something not found
        raise HTTPException(status_code=404, detail="Number not found.")
    # Rest of the code...

@app.get("/api/classify-number")
def classify_number(number: int):
    try:
        # Example: Attempt to get a fun fact about the number
        fun_fact = get_fun_fact(number)  # Function call that might fail
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error: " + str(e))

    # Continue with your logic and return the result...

@app.get("/api/classify-number")
def classify_number(number: int):
    print(f"Received number: {number}")  # Debugging line

    properties = []
    
    # Check if prime
    if number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)):
        properties.append("prime")

    # Check if even or odd
    properties.append("even" if number % 2 == 0 else "odd")

    # Calculate digit sum
    digit_sum = sum(int(digit) for digit in str(abs(number)))

    # Get fun fact
    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": "prime" in properties,
        "is_perfect": number == sum(i for i in range(1, number) if number % i == 0),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

    print(f"Response: {response}")  # Debugging line
    return response


# Ensure the app runs on Railway
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

