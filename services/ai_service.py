def predict_category_and_priority(text):

    text = text.lower()

    if "water" in text or "pipeline" in text:
        return {"category": "Water", "priority": "High"}

    if "road" in text or "pothole" in text:
        return {"category": "Infrastructure", "priority": "Medium"}

    if "light" in text or "electricity" in text:
        return {"category": "Electricity", "priority": "Medium"}

    return {"category": "Other", "priority": "Low"}