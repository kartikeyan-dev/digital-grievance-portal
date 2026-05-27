import uuid

def generate_complaint_id():
    return "CIV-" + str(uuid.uuid4().hex)[:8].upper()