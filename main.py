from flask import Flask, Response
import asyncio

from src.helpers.response_helper import format_error_response
from src.helpers.custom_exception_helper import CustomErrorException

app = Flask(__name__)

@app.route("/")
async def home():
    await asyncio.sleep(1)  # Simulasi proses async
    return "Hello, Async Flask!"

@app.route("/test_404")
async def test404():
    raise CustomErrorException(description="Unauthorized access", code=425, data={"error_code": 423, "message": "entity too large"})

# Error handler untuk 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return format_error_response(code=404, message="Resource not found")

# Error handler untuk 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return format_error_response(code=500, message="Internal server error")

# Error handler untuk 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return format_error_response(code=400, message="Bad request")

if __name__ == "__main__":
    app.run(debug=True)
