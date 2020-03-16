# flask_web/app.py

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')