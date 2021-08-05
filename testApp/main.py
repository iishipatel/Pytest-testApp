from flask import Flask, jsonify, request
# import src.Controllers.student_controller as SC
from src.Services.student_service import create_tables

app = Flask(__name__)

import src.Controllers.student_data

if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=8000, debug=False)
