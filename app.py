from flask import Flask
from config import SECRET_KEY

# Blueprints
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp

# Create app
app = Flask(__name__)

# Config
app.config["SECRET_KEY"] = SECRET_KEY

# Register Blueprints
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


# Health check route (important for deployment)
@app.route("/health")
def health():
    return {"status": "running", "message": "Grievance system active"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)