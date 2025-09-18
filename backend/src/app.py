from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
import sys
import traceback

# Import blueprints for API routes with error handling
blueprints_loaded = {}

try:
    from .api.auth_routes import auth_bp
    blueprints_loaded['auth'] = True
except Exception as e:
    print(f"Failed to import auth_routes: {e}")
    blueprints_loaded['auth'] = False
    auth_bp = None

try:
    from .api.trading_routes import trading_bp
    blueprints_loaded['trading'] = True
except Exception as e:
    print(f"Failed to import trading_routes: {e}")
    blueprints_loaded['trading'] = False
    trading_bp = None

try:
    from .api.simulator_routes import simulator_bp
    blueprints_loaded['simulator'] = True
except Exception as e:
    print(f"Failed to import simulator_routes: {e}")
    blueprints_loaded['simulator'] = False
    simulator_bp = None

try:
    from .api.strategy_routes import strategy_bp
    blueprints_loaded['strategy'] = True
except Exception as e:
    print(f"Failed to import strategy_routes: {e}")
    blueprints_loaded['strategy'] = False
    strategy_bp = None

try:
    from .api.journal_routes import journal_bp
    blueprints_loaded['journal'] = True
except Exception as e:
    print(f"Failed to import journal_routes: {e}")
    blueprints_loaded['journal'] = False
    journal_bp = None

# AI Firm Routes - Critical Import
try:
    from .api.ai_firm_routes import ai_firm_bp
    blueprints_loaded['ai_firm'] = True
    print("✅ Successfully imported ai_firm_routes blueprint")
except Exception as e:
    print(f"❌ Failed to import ai_firm_routes: {e}")
    print(f"❌ Traceback: {traceback.format_exc()}")
    blueprints_loaded['ai_firm'] = False
    ai_firm_bp = None

app = Flask(__name__)
CORS(app) # Enable CORS for all origins

# Load configuration from environment variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "super-secret-key")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")

jwt = JWTManager(app)

# Register blueprints with error handling
blueprints_registered = {}

if auth_bp:
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    blueprints_registered['auth'] = True
    print("✅ Registered auth blueprint at /api/auth")
else:
    blueprints_registered['auth'] = False

if trading_bp:
    app.register_blueprint(trading_bp, url_prefix="/api/trading")
    blueprints_registered['trading'] = True
    print("✅ Registered trading blueprint at /api/trading")
else:
    blueprints_registered['trading'] = False

if simulator_bp:
    app.register_blueprint(simulator_bp, url_prefix="/api/simulator")
    blueprints_registered['simulator'] = True
    print("✅ Registered simulator blueprint at /api/simulator")
else:
    blueprints_registered['simulator'] = False

if strategy_bp:
    app.register_blueprint(strategy_bp, url_prefix="/api/strategy")
    blueprints_registered['strategy'] = True
    print("✅ Registered strategy blueprint at /api/strategy")
else:
    blueprints_registered['strategy'] = False

if journal_bp:
    app.register_blueprint(journal_bp, url_prefix="/api/journal")
    blueprints_registered['journal'] = True
    print("✅ Registered journal blueprint at /api/journal")
else:
    blueprints_registered['journal'] = False

# AI Firm Blueprint Registration - Critical
if ai_firm_bp:
    try:
        app.register_blueprint(ai_firm_bp, url_prefix="/api/ai-firm")
        blueprints_registered['ai_firm'] = True
        print("✅ Successfully registered ai_firm blueprint at /api/ai-firm")
        print("✅ AI Firm endpoints should be available at:")
        print("   • /api/ai-firm/status")
        print("   • /api/ai-firm/health")
        print("   • /api/ai-firm/agents")
        print("   • /api/ai-firm/debug-imports")
    except Exception as e:
        blueprints_registered['ai_firm'] = False
        print(f"❌ Failed to register ai_firm blueprint: {e}")
else:
    blueprints_registered['ai_firm'] = False
    print("❌ AI Firm blueprint not available for registration")

@app.route("/")
def hello_world():
    return jsonify(
        message="YantraX RL Backend API - Production Ready",
        version="3.0.0",
        environment="production",
        features=[
            "Multi-asset market data (FREE APIs)",
            "AI agent coordination", 
            "Real-time portfolio management",
            "Professional error handling",
            "Production monitoring"
        ],
        blueprints_status=blueprints_registered,
        ai_firm_status={
            'loaded': blueprints_loaded.get('ai_firm', False),
            'registered': blueprints_registered.get('ai_firm', False),
            'expected_endpoints': [
                '/api/ai-firm/status',
                '/api/ai-firm/health', 
                '/api/ai-firm/agents',
                '/api/ai-firm/debug-imports'
            ] if blueprints_registered.get('ai_firm') else []
        }
    )

@app.route("/debug")
def debug_info():
    """Debug endpoint to check system status"""
    return jsonify({
        'python_version': sys.version,
        'python_path': sys.path[:5],  # First 5 paths
        'current_directory': os.getcwd(),
        'blueprints_loaded': blueprints_loaded,
        'blueprints_registered': blueprints_registered,
        'flask_app_name': app.name,
        'registered_routes': [str(rule) for rule in app.url_map.iter_rules()],
        'ai_firm_investigation': {
            'ai_firm_bp_exists': ai_firm_bp is not None,
            'ai_firm_routes_count': len([rule for rule in app.url_map.iter_rules() if '/api/ai-firm' in str(rule)]),
            'all_api_routes': [str(rule) for rule in app.url_map.iter_rules() if '/api/' in str(rule)]
        }
    })

# Fallback AI firm status endpoint if blueprint fails
@app.route("/api/ai-firm-fallback/status")
def ai_firm_fallback_status():
    """Fallback AI firm status when blueprint import fails"""
    return jsonify({
        'status': 'fallback',
        'message': 'AI Firm blueprint failed to load - using fallback endpoint',
        'blueprint_loaded': blueprints_loaded.get('ai_firm', False),
        'blueprint_registered': blueprints_registered.get('ai_firm', False),
        'troubleshooting': {
            'check_imports': 'AI firm components may have import errors',
            'check_dependencies': 'Missing packages may prevent initialization',
            'check_file_paths': 'Module paths may not be resolving correctly'
        },
        'expected_functionality': {
            'total_agents': 20,
            'departments': 5,
            'personas': ['Warren', 'Cathie'],
            'autonomous_ceo': True
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
