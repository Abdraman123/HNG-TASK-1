# HNG-TASK-1 - Number Classification API
## Project Description
This is a simple API that classifies a number and returns interesting mathematical properties about it, such as whether it is prime, perfect, or Armstrong. It also provides a fun fact about the number from the Numbers API.

## Setup Instructions

### 1. Clone the repository
To run the project locally, clone the repository:
```bash
git clone https://github.com/Abdraman123/HNG-TASK-1.git
cd your-repository
```

### 2. Install dependencies
Make sure you have Python 3.7+ installed. Then, install the required dependencies:
```
pip install -r requirements.txt
```
### 3. Run the application
Run the FastAPI app locally:
```
uvicorn main:app --reload
```

### 4. Open in your browser
Visit http://127.0.0.1:8000 in your browser.

### API Documentation
Endpoint
GET /api/classify-number

### Query Parameters
number: The number you want to classify (required).
Response Format (200 OK)
```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
Response Format (400 Bad Request)
If the input is invalid (non-integer):
```
{
  "number": "alphabet",
  "error": true
}
```
### Example Usage
Example Request:
```
curl "http://127.0.0.1:8000/api/classify-number?number=371"
```
Example Response:
```
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
### Deployment
This API is deployed on Railway. You can access the live API at the following URL:
```
https://your-railway-url/api/classify-number?number=371
```
### Additional Notes
For more information about Numbers API, visit:
http://numbersapi.com/#42

### **Step 7: Final Deployment to Railway**

Now that everything is set up, let’s deploy it to **Railway** again with the updated documentation.

1. **Push the changes to GitHub**:
   If you haven't already, add your `README.md` file to the GitHub repository:
   ```bash
   git add README.md
   git commit -m "Add README documentation"
   git push origin main
Redeploy on Railway: After pushing the changes, go to your Railway project dashboard and trigger a redeploy to make sure the latest changes are applied.

Test the live API: Once the deployment is successful, test the API using the live URL from Railway:

https://your-railway-url/api/classify-number?number=371
