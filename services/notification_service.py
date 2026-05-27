def send_notification(complaint_id, status, contact="user"):

    # (For now we simulate instead of real SMS/email)
    print("NOTIFICATION SENT")
    print("Complaint:", complaint_id)
    print("New Status:", status)

    return True