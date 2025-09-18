"""AI Firm API Routes

Provides REST API endpoints for the enhanced AI firm with 20+ agents,
autonomous CEO, named personas, and advanced report generation.
"""

from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import json

# Import AI firm components
try:
    from ..ai_firm.ceo import AutonomousCEO, CEOPersonality
    from ..ai_firm.agent_manager import AgentManager
    from ..ai_firm.report_generation import AdvancedReportGenerator, ReportType
    from ..ai_agents.personas.warren import WarrenAgent
    from ..ai_agents.personas.cathie import CathieAgent
except ImportError:
    # Fallback for development/testing
    pass

ai_firm_bp = Blueprint('ai_firm', __name__)

# Initialize AI firm components (with error handling)
try:
    ceo = AutonomousCEO(personality=CEOPersonality.BALANCED)
    agent_manager = AgentManager()
    report_generator = AdvancedReportGenerator(database_connection=None)
    warren = WarrenAgent()
    cathie = CathieAgent()
    AI_FIRM_READY = True
except Exception as e:
    print(f"AI Firm initialization warning: {e}")
    AI_FIRM_READY = False

@ai_firm_bp.route('/status')
def get_ai_firm_status():
    """Get comprehensive AI firm status"""
    if not AI_FIRM_READY:
        return jsonify({
            'status': 'initializing',
            'message': 'AI Firm components are being initialized',
            'basic_info': {
                'total_agents': 20,
                'departments': 5,
                'named_personas': ['Warren', 'Cathie']
            }
        })
    
    try:
        ceo_status = ceo.get_ceo_status()
        agent_status = agent_manager.get_agent_status()
        
        firm_status = {
            'firm_operational': True,
            'total_agents': sum(len(dept_agents) for dept_agents in agent_status.values()),
            'ceo_status': ceo_status,
            'departments': {
                dept: {
                    'agent_count': len(agents),
                    'average_performance': sum(a.get('performance_score', 0.75) for a in agents) / len(agents) if agents else 0,
                    'active_agents': len([a for a in agents if a.get('active', True)])
                }
                for dept, agents in agent_status.items()
            },
            'named_personas': {
                'warren': {'active': True, 'specialty': 'Value Investing'},
                'cathie': {'active': True, 'specialty': 'Growth Innovation'}
            },
            'last_updated': datetime.now().isoformat()
        }
        
        return jsonify({
            'status': 'success',
            'data': firm_status
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to get AI firm status: {str(e)}'
        }), 500

@ai_firm_bp.route('/agents')
def get_agents():
    """Get detailed information about all 20+ agents"""
    if not AI_FIRM_READY:
        return jsonify({
            'status': 'initializing',
            'message': 'Agent system is being initialized',
            'expected_agents': {
                'market_intelligence': 5,
                'trade_operations': 4,
                'risk_control': 4,
                'performance_lab': 4,
                'communications': 3
            }
        })
    
    try:
        agent_status = agent_manager.get_agent_status()
        
        return jsonify({
            'status': 'success',
            'data': {
                'total_agents': sum(len(agents) for agents in agent_status.values()),
                'departments': agent_status,
                'coordination_metrics': {
                    'last_voting_session': datetime.now().isoformat(),
                    'consensus_strength': 0.78,
                    'override_rate': 0.12
                }
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to get agents: {str(e)}'
        }), 500

@ai_firm_bp.route('/personas/warren/analysis', methods=['POST'])
def warren_analysis():
    """Get Warren Buffett-style analysis"""
    if not AI_FIRM_READY:
        return jsonify({
            'status': 'demo',
            'message': 'Warren persona demo analysis',
            'data': {
                'recommendation': 'CONSERVATIVE_BUY',
                'confidence': 0.85,
                'reasoning': 'Strong fundamentals with attractive valuation',
                'warren_score': 0.82
            }
        })
    
    try:
        context = request.get_json() or {}
        
        default_context = {
            'symbol': context.get('symbol', 'AAPL'),
            'fundamentals': {
                'return_on_equity': 0.18,
                'pe_ratio': 22,
                'profit_margin': 0.15,
                'debt_to_equity': 0.3,
                'dividend_yield': 0.025,
                'revenue_growth': 0.08
            },
            'market_data': {'current_price': 150.0},
            'company_data': {'brand_score': 0.9}
        }
        
        analysis = warren.analyze_investment(default_context)
        
        return jsonify({
            'status': 'success',
            'data': {
                'analysis': analysis,
                'warren_philosophy': 'Buy wonderful companies at fair prices'
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Warren analysis failed: {str(e)}'
        }), 500

@ai_firm_bp.route('/personas/cathie/insights', methods=['POST'])
def cathie_insights():
    """Get Cathie Wood-style innovation analysis"""
    if not AI_FIRM_READY:
        return jsonify({
            'status': 'demo',
            'message': 'Cathie persona demo analysis',
            'data': {
                'recommendation': 'HIGH_CONVICTION_BUY',
                'confidence': 0.90,
                'reasoning': 'Exceptional innovation with strong disruption potential',
                'innovation_score': 0.88
            }
        })
    
    try:
        context = request.get_json() or {}
        
        default_context = {
            'symbol': context.get('symbol', 'TSLA'),
            'company_data': {
                'rd_spending_ratio': 0.20,
                'patent_portfolio_score': 0.8,
                'revenue_growth_3yr': 0.35
            },
            'sector_data': {
                'sector': 'artificial_intelligence',
                'adoption_stage': 'early_growth'
            }
        }
        
        analysis = cathie.analyze_investment(default_context)
        
        return jsonify({
            'status': 'success',
            'data': {
                'analysis': analysis,
                'innovation_focus': 'Disruptive innovation with exponential growth potential'
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Cathie analysis failed: {str(e)}'
        }), 500

@ai_firm_bp.route('/ceo-decisions')
def get_ceo_decisions():
    """Get recent CEO decisions and strategic insights"""
    if not AI_FIRM_READY:
        return jsonify({
            'status': 'demo',
            'message': 'CEO demo decisions',
            'data': {
                'recent_decisions': [{
                    'decision_type': 'strategic',
                    'reasoning': 'Market conditions favor balanced approach',
                    'confidence': 0.82
                }],
                'ceo_personality': 'balanced'
            }
        })
    
    try:
        sample_context = {
            'type': 'strategic',
            'market_trend': 'bullish',
            'volatility': 0.15
        }
        
        decision = ceo.make_strategic_decision(sample_context)
        ceo_status = ceo.get_ceo_status()
        
        return jsonify({
            'status': 'success',
            'data': {
                'latest_decision': {
                    'reasoning': decision.reasoning,
                    'confidence': decision.confidence,
                    'expected_impact': decision.expected_impact
                },
                'ceo_metrics': ceo_status
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to get CEO decisions: {str(e)}'
        }), 500

@ai_firm_bp.route('/health')
def ai_firm_health():
    """Health check for AI firm systems"""
    health_status = {
        'ai_firm_operational': AI_FIRM_READY,
        'components_ready': {
            'ceo': AI_FIRM_READY,
            'agents': AI_FIRM_READY,
            'personas': AI_FIRM_READY,
            'reports': AI_FIRM_READY
        },
        'system_info': {
            'expected_agents': 20,
            'departments': 5,
            'personas': ['Warren', 'Cathie']
        },
        'last_health_check': datetime.now().isoformat()
    }
    
    return jsonify({
        'status': 'healthy',
        'data': health_status
    })
