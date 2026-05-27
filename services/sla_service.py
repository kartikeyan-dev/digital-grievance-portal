from datetime import datetime, timedelta

def calculate_sla(priority, created_at):

    # 🔥 FIX 1: handle missing date
    if not created_at:
        return "NO SLA DATA"

    # 🔥 FIX 2: ensure datetime format
    if isinstance(created_at, str):
        created_at = datetime.fromisoformat(created_at)

    now = datetime.utcnow()

    if priority == "High":
        limit = 2
    elif priority == "Medium":
        limit = 4
    else:
        limit = 7

    # 🔥 SAFE COMPARISON
    try:
        if now > created_at + timedelta(days=limit):
            return "OVERDUE"
    except Exception:
        return "INVALID DATE"

    return "ACTIVE"