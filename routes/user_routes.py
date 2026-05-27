from flask import Blueprint, render_template, request
from datetime import datetime
import uuid

from config import db
from services.ai_service import predict_category_and_priority

user_bp = Blueprint("user", __name__)

complaints = db["complaints"]


@user_bp.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "POST":

        name = request.form["name"]
        location = request.form["location"]
        description = request.form["description"]

        ai_result = predict_category_and_priority(description)

        complaint_id = str(uuid.uuid4().hex)[:8]

        complaint = {
            "complaint_id": complaint_id,
            "name": name,
            "location": location,
            "description": description,

            # AI OUTPUT (SAFE)
            "category": ai_result.get("category", "Other"),
            "priority": ai_result.get("priority", "Low"),

            # SYSTEM FIELDS
            "status": "Pending",
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),

            # NOTIFICATIONS
            "notifications": [
                {
                    "message": "Complaint submitted successfully",
                    "time": datetime.utcnow()
                }
            ]
        }

        complaints.insert_one(complaint)

        return render_template("submit.html", complaint_id=complaint_id)

    return render_template("submit.html")


@user_bp.route("/")
def home():

    all_complaints = list(complaints.find())

    notifications = []

    for c in all_complaints:
        for n in c.get("notifications", []):
            notifications.append(n)

    notifications = sorted(
        notifications,
        key=lambda x: x.get("time", ""),
        reverse=True
    )

    return render_template("home.html", notifications=notifications)