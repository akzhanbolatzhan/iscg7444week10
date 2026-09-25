import json

from flask import Flask

# 初始化 Flask 应用程序
app = Flask(__name__)

@app.route("/")
def home():
    return json.dumps({})

@app.route("/test")
def test_api():
    return json.dumps({"message": "success"})

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')