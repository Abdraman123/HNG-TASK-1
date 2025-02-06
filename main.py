import os
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

NUMBERS_API_URL = "http://numbersapi.com/"

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
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def get_digit_sum(n: int) -> int:
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def get_fun_fact(n: int) -> str:
    """Fetch a fun fact about a number from the Numbers API."""
    try:
        response = requests.get(f"{NUMBERS_API_URL}{n}")
        if response.status_code == 200:
            return response.text
        return "No fun fact available."
    except:
        return "Error fetching fun fact."

from fastapi import Query

@app.get("/api/classify-number")
def classify_number(number: int = Query(..., description="Enter a valid integer")):
    """Classifies a number and returns its properties in JSON format."""

    try:
        # Ensure input is an integer
        number = int(number)
    except ValueError:
        raise HTTPException(status_code=400, detail={"number": number, "error": True})

    # Determine number properties
    properties = []
    if is_prime(number):
        properties.append("prime")
    if is_perfect(number):
        properties.append("perfect")
    if is_armstrong(number):
        properties.append("armstrong")

    # Add odd/even classification
    properties.append("even" if number % 2 == 0 else "odd")

    # Create the response JSON
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "digit_sum": get_digit_sum(number),
        "fun_fact": get_fun_fact(number)
    }
    
    return result


from fastapi.middleware.cors import CORSMiddleware

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

PORT = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=PORT)