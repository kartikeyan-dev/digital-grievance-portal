from datetime import datetime
from config import complaints_collection
from services.notification_service import send_notification

def create_complaint(complaint):
    now = datetime.utcnow()

    complaint["created_at"] = now
    complaint["updated_at"] = now
    complaint["priority"] = "Medium"

    complaint["history"] = [
        {
            "status": "Pending",
            "timestamp": now,
            "updated_by": "system"
        }
    ]

    complaints_collection.insert_one(complaint)


def get_complaint_by_id(complaint_id):
    return complaints_collection.find_one({"complaint_id": complaint_id})


def get_all_complaints():
    return list(complaints_collection.find())


def update_status(complaint_id, new_status, updated_by="admin"):

    now = datetime.utcnow()

    complaint = get_complaint_by_id(complaint_id)

    if not complaint:
        return

    history_entry = {
        "status": new_status,
        "timestamp": now,
        "updated_by": updated_by
    }

    complaints_collection.update_one(
        {"complaint_id": complaint_id},
        {
            "$set": {
                "status": new_status,
                "updated_at": now
            },
            "$push": {
                "history": history_entry
            }
        }
    )

    # 🔔 TRIGGER NOTIFICATION
    send_notification(complaint_id, new_status)


def delete_complaint(complaint_id):
    complaints_collection.delete_one({"complaint_id": complaint_id})

def get_analytics():
    complaints = list(complaints_collection.find())

    total = len(complaints)

    status_count = {
        "Pending": 0,
        "In Progress": 0,
        "Resolved": 0
    }

    category_count = {}
    priority_count = {
        "Low": 0,
        "Medium": 0,
        "High": 0,
        "Critical": 0
    }

    for c in complaints:

        # status
        if c.get("status") in status_count:
            status_count[c["status"]] += 1

        # category
        cat = c.get("category", "Other")
        category_count[cat] = category_count.get(cat, 0) + 1

        # priority
        pr = c.get("priority", "Low")
        priority_count[pr] = priority_count.get(pr, 0) + 1

    return {
        "total": total,
        "status_count": status_count,
        "category_count": category_count,
        "priority_count": priority_count
    }
from datetime import datetime, timedelta

def check_sla(complaint):

    created = complaint.get("created_at")

    if not created:
        return "OK"

    now = datetime.utcnow()

    # SLA rule: 3 days max for normal complaints
    if now - created > timedelta(days=3):
        return "ESCALATE"

    return "OK"