from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

# Initialize the Flask app
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres-db-service/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Initialize Prometheus Metrics
metrics = PrometheusMetrics(app)

# Route for index page
@app.route('/')
def index():
    return "Welcome to the Simple Web App!"

# Define a route for exposing metrics (Prometheus will scrape this)
@app.route('/metrics')
def metrics_view():
    return metrics.expose()

# Import routes and models
from app import routes, models
