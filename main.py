import os
import uvicorn
from fastapi import FastAPI, HTTPException
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the Numbers API base URL
NUMBERS_API_URL = "http://numbersapi.com/"

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

@app.get("/api/classify-number")
def classify_number(number: int):
    properties = []
    
    # Check if prime
    if is_prime(number):
        properties.append("prime")

    # Check if perfect
    if is_perfect(number):
        properties.append("perfect")

    # Check if Armstrong
    if is_armstrong(number):
        properties.append("armstrong")

    # Check if even or odd
    properties.append("even" if number % 2 == 0 else "odd")

    # Calculate digit sum
    digit_sum = get_digit_sum(number)

    # Get fun fact
    fun_fact = get_fun_fact(number)

    return {
        "number": number,
        "is_prime": "prime" in properties,
        "is_perfect": "perfect" in properties,
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    }

# Ensure the app runs on Railway
PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)

