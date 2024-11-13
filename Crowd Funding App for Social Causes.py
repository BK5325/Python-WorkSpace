from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import stripe

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crowdfunding.db"
db = SQLAlchemy(app)
stripe.api_key = "YOUR_STRIPE_API_KEY"

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    goal = db.Column(db.Float)

@app.route("/projects", methods=["POST"])
def create_project():
    data = request.get_json()
    project = Project(title=data["title"], description=data["description"], goal=data["goal"])
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created successfully"}), 201

@app.route("/donate", methods=["POST"])
def donate():
    data = request.get_json()
    project_id = data["project_id"]
    amount = data["amount"]
    stripe.Charge.create(
        amount=amount,
        currency="usd",
        source=data["stripe_token"],
        description=f"Donation to project {project_id}"
    )
    return jsonify({"message": "Donation successful"})