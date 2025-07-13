from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os

# Import blueprints for API routes
from .api.auth_routes import auth_bp
from .api.trading_routes import trading_bp
from .api.simulator_routes import simulator_bp
from .api.strategy_routes import strategy_bp
from .api.journal_routes import journal_bp
from .api.ai_firm_routes import ai_firm_bp

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

# Load configuration from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "super-secret-key")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")

jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(trading_bp, url_prefix="/api/trading")
app.register_blueprint(simulator_bp, url_prefix="/api/simulator")
app.register_blueprint(strategy_bp, url_prefix="/api/strategy")
app.register_blueprint(journal_bp, url_prefix="/api/journal")
app.register_blueprint(ai_firm_bp, url_prefix="/api/ai-firm")

@app.route("/")
def hello_world():
    return jsonify(message="Welcome to TradeSmartAI Backend!")

if __name__ == "__main__":
    app.run(debug=True)


