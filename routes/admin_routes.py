from flask import Blueprint, render_template, request, session, redirect, url_for
from datetime import datetime

from config import db
from services.sla_service import calculate_sla

admin_bp = Blueprint("admin", __name__)

complaints = db["complaints"]


@admin_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["admin"] = True
            return redirect(url_for("admin.dashboard"))

        return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")


@admin_bp.route("/admin")
def dashboard():

    if not session.get("admin"):
        return redirect(url_for("admin.login"))

    complaints_list = list(complaints.find())

    status_counts = {
        "Pending": 0,
        "In Progress": 0,
        "Resolved": 0
    }

    category_counts = {}

    for c in complaints_list:

        status = c.get("status", "Pending")
        status_counts[status] = status_counts.get(status, 0) + 1

        category = c.get("category", "Other")
        category_counts[category] = category_counts.get(category, 0) + 1

        c["sla_status"] = calculate_sla(
            c.get("priority", "Low"),
            c.get("created_at")
        )

    analytics = {
        "total": len(complaints_list),
        "status_count": status_counts
    }

    return render_template(
        "admin.html",
        complaints=complaints_list,
        analytics=analytics,
        status_counts=status_counts,   # 🔥 REQUIRED
        category_counts=category_counts # 🔥 REQUIRED
    )


@admin_bp.route("/update_status/<cid>", methods=["POST"])
def update_status(cid):

    new_status = request.form["status"]

    complaints.update_one(
        {"complaint_id": cid},
        {
            "$set": {
                "status": new_status,
                "updated_at": datetime.utcnow()
            },
            "$push": {
                "notifications": {
                    "message": f"Status updated to {new_status}",
                    "time": datetime.utcnow()
                }
            }
        }
    )

    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/delete/<cid>", methods=["POST"])
def delete(cid):

    complaints.delete_one({"complaint_id": cid})
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("admin.login"))