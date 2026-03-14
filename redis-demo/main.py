from flask import Flask
from app.web.routes import task_bp

app = Flask(__name__)
app.register_blueprint(task_bp)

@app.route("/")
def home():
    return {
        "message": "Redis Task API berjalan",
        "endpoint_create": "POST /task",
        "endpoint_get": "GET /task/<id>"
    }

if __name__ == '__main__':
    print('Starting Flask app on http://127.0.0.1:5000')
    app.run(host='0.0.0.0', port=5000, debug=True)