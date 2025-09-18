"""Agent Manager Module

Manages 20+ AI agents across departments with coordination,
voting systems, and performance tracking.
"""

import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, asdict
from enum import Enum
import asyncio
import random

class AgentRole(Enum):
    DIRECTOR = "director"
    SENIOR = "senior"
    SPECIALIST = "specialist"
    ANALYST = "analyst"

class DepartmentType(Enum):
    MARKET_INTELLIGENCE = "market_intelligence"
    TRADE_OPERATIONS = "trade_operations" 
    RISK_CONTROL = "risk_control"
    PERFORMANCE_LAB = "performance_lab"
    COMMUNICATIONS = "communications"

@dataclass
class Agent:
    """AI Agent definition with personality and capabilities"""
    id: str
    name: str
    role: AgentRole
    department: DepartmentType
    personality_traits: Dict[str, float]
    expertise_areas: List[str]
    confidence_level: float
    learning_rate: float
    vote_weight: float
    created_at: datetime
    performance_score: float = 0.75
    active: bool = True

@dataclass
class AgentDecision:
    """Decision made by an agent"""
    agent_id: str
    timestamp: datetime
    decision_type: str
    recommendation: str
    confidence: float
    reasoning: str
    supporting_data: Dict[str, Any]
    vote_weight: float

class AgentManager:
    """Manages the 20+ agent AI firm ecosystem"""
    
    def __init__(self):
        self.agents = {}
        self.agent_registry = {}
        self.voting_sessions = []
        self.performance_tracker = AgentPerformanceTracker()
        
        # Initialize the 20+ agent firm
        self._initialize_ai_firm()
        
    def _initialize_ai_firm(self):
        """Initialize the complete 20+ agent AI firm structure"""
        
        # MARKET INTELLIGENCE DEPARTMENT (5 agents)
        self._create_agent(
            "Warren", AgentRole.DIRECTOR, DepartmentType.MARKET_INTELLIGENCE,
            {"risk_aversion": 0.8, "fundamentals_focus": 0.9, "patience": 0.9},
            ["value_investing", "fundamental_analysis", "risk_assessment"],
            0.85
        )
        
        self._create_agent(
            "Cathie", AgentRole.SENIOR, DepartmentType.MARKET_INTELLIGENCE,
            {"innovation_focus": 0.9, "growth_seeking": 0.8, "risk_tolerance": 0.7},
            ["growth_investing", "innovation_analysis", "sector_rotation"],
            0.80
        )
        
        self._create_agent(
            "Quant", AgentRole.SENIOR, DepartmentType.MARKET_INTELLIGENCE,
            {"mathematical_precision": 0.9, "pattern_recognition": 0.85, "objectivity": 0.9},
            ["quantitative_analysis", "statistical_modeling", "algorithmic_signals"],
            0.88
        )
        
        self._create_agent(
            "Data_Whisperer", AgentRole.SPECIALIST, DepartmentType.MARKET_INTELLIGENCE,
            {"pattern_detection": 0.9, "data_synthesis": 0.85, "market_intuition": 0.7},
            ["data_aggregation", "pattern_analysis", "market_context"],
            0.82
        )
        
        self._create_agent(
            "Macro_Monk", AgentRole.SPECIALIST, DepartmentType.MARKET_INTELLIGENCE,
            {"strategic_thinking": 0.85, "macro_vision": 0.9, "decision_clarity": 0.8},
            ["macro_analysis", "strategic_decisions", "market_timing"],
            0.79
        )
        
        # TRADE OPERATIONS DEPARTMENT (4 agents)
        self._create_agent(
            "Trade_Executor", AgentRole.DIRECTOR, DepartmentType.TRADE_OPERATIONS,
            {"execution_speed": 0.9, "accuracy": 0.9, "reliability": 0.85},
            ["order_execution", "market_microstructure", "slippage_minimization"],
            0.87
        )
        
        self._create_agent(
            "Portfolio_Optimizer", AgentRole.SENIOR, DepartmentType.TRADE_OPERATIONS,
            {"optimization_focus": 0.9, "balance_seeking": 0.8, "efficiency": 0.85},
            ["portfolio_construction", "asset_allocation", "rebalancing"],
            0.83
        )
        
        self._create_agent(
            "Liquidity_Hunter", AgentRole.SPECIALIST, DepartmentType.TRADE_OPERATIONS,
            {"market_timing": 0.8, "liquidity_awareness": 0.9, "adaptability": 0.75},
            ["liquidity_analysis", "market_impact", "execution_optimization"],
            0.78
        )
        
        self._create_agent(
            "Arbitrage_Scout", AgentRole.ANALYST, DepartmentType.TRADE_OPERATIONS,
            {"opportunity_detection": 0.85, "speed": 0.9, "precision": 0.8},
            ["arbitrage_opportunities", "price_discrepancies", "cross_market_analysis"],
            0.76
        )
        
        # RISK CONTROL DEPARTMENT (4 agents)
        self._create_agent(
            "Degen_Auditor", AgentRole.DIRECTOR, DepartmentType.RISK_CONTROL,
            {"risk_vigilance": 0.9, "skepticism": 0.8, "contrarian_thinking": 0.7},
            ["risk_validation", "audit_trails", "red_flag_detection"],
            0.84
        )
        
        self._create_agent(
            "VaR_Guardian", AgentRole.SENIOR, DepartmentType.RISK_CONTROL,
            {"mathematical_rigor": 0.9, "conservatism": 0.85, "model_accuracy": 0.8},
            ["value_at_risk", "stress_testing", "risk_modeling"],
            0.81
        )
        
        self._create_agent(
            "Correlation_Detective", AgentRole.SPECIALIST, DepartmentType.RISK_CONTROL,
            {"pattern_recognition": 0.85, "system_thinking": 0.8, "vigilance": 0.9},
            ["correlation_analysis", "systemic_risk", "portfolio_diversification"],
            0.77
        )
        
        self._create_agent(
            "Black_Swan_Sentinel", AgentRole.ANALYST, DepartmentType.RISK_CONTROL,
            {"paranoia": 0.8, "scenario_analysis": 0.85, "preparedness": 0.9},
            ["tail_risk", "scenario_planning", "crisis_preparation"],
            0.74
        )
        
        # PERFORMANCE LAB DEPARTMENT (4 agents)
        self._create_agent(
            "Performance_Analyst", AgentRole.DIRECTOR, DepartmentType.PERFORMANCE_LAB,
            {"analytical_precision": 0.9, "objectivity": 0.85, "insight_generation": 0.8},
            ["performance_attribution", "benchmarking", "metric_analysis"],
            0.86
        )
        
        self._create_agent(
            "Alpha_Hunter", AgentRole.SENIOR, DepartmentType.PERFORMANCE_LAB,
            {"alpha_detection": 0.9, "strategy_evaluation": 0.85, "optimization": 0.8},
            ["alpha_generation", "strategy_performance", "factor_analysis"],
            0.82
        )
        
        self._create_agent(
            "Backtesting_Engine", AgentRole.SPECIALIST, DepartmentType.PERFORMANCE_LAB,
            {"historical_analysis": 0.9, "simulation_accuracy": 0.85, "validation": 0.8},
            ["historical_testing", "strategy_validation", "simulation_modeling"],
            0.80
        )
        
        self._create_agent(
            "The_Ghost", AgentRole.ANALYST, DepartmentType.PERFORMANCE_LAB,
            {"meta_analysis": 0.8, "emergent_behavior": 0.9, "intuition": 0.7},
            ["emotional_intelligence", "meta_layer_analysis", "emergent_patterns"],
            0.75
        )
        
        # COMMUNICATIONS DEPARTMENT (3 agents)
        self._create_agent(
            "Report_Generator", AgentRole.DIRECTOR, DepartmentType.COMMUNICATIONS,
            {"communication_clarity": 0.9, "synthesis_ability": 0.85, "insight_presentation": 0.8},
            ["report_generation", "executive_summaries", "stakeholder_communication"],
            0.83
        )
        
        self._create_agent(
            "Market_Narrator", AgentRole.SENIOR, DepartmentType.COMMUNICATIONS,
            {"storytelling": 0.85, "market_interpretation": 0.8, "narrative_construction": 0.9},
            ["market_storytelling", "trend_narration", "insight_communication"],
            0.78
        )
        
        self._create_agent(
            "Alert_Coordinator", AgentRole.SPECIALIST, DepartmentType.COMMUNICATIONS,
            {"urgency_assessment": 0.9, "priority_management": 0.85, "notification_precision": 0.8},
            ["alert_management", "notification_systems", "escalation_protocols"],
            0.79
        )
        
    def _create_agent(self, name: str, role: AgentRole, department: DepartmentType,
                     personality: Dict[str, float], expertise: List[str], 
                     base_confidence: float) -> Agent:
        """Create and register a new agent"""
        
        agent_id = str(uuid.uuid4())
        
        # Calculate vote weight based on role and department
        vote_weights = {
            AgentRole.DIRECTOR: 1.0,
            AgentRole.SENIOR: 0.8,
            AgentRole.SPECIALIST: 0.6,
            AgentRole.ANALYST: 0.4
        }
        
        agent = Agent(
            id=agent_id,
            name=name,
            role=role,
            department=department,
            personality_traits=personality,
            expertise_areas=expertise,
            confidence_level=base_confidence,
            learning_rate=random.uniform(0.05, 0.15),
            vote_weight=vote_weights[role],
            created_at=datetime.now()
        )
        
        self.agents[agent_id] = agent
        self.agent_registry[name] = agent_id
        
        return agent
    
    def coordinate_decision_making(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Coordinate decision making across all agents"""
        
        # Get decisions from all active agents
        agent_decisions = []
        
        for agent_id, agent in self.agents.items():
            if agent.active:
                decision = self._get_agent_decision(agent, context)
                agent_decisions.append(decision)
        
        # Run voting session
        voting_result = self._conduct_voting_session(agent_decisions, context)
        
        # Track performance
        self.performance_tracker.record_coordination_session(agent_decisions, voting_result)
        
        return voting_result
    
    def _get_agent_decision(self, agent: Agent, context: Dict[str, Any]) -> AgentDecision:
        """Get decision from specific agent based on their personality and expertise"""
        
        # Simulate agent decision making based on personality and expertise
        decision_confidence = self._calculate_agent_confidence(agent, context)
        recommendation = self._generate_agent_recommendation(agent, context)
        reasoning = self._generate_agent_reasoning(agent, context, recommendation)
        
        decision = AgentDecision(
            agent_id=agent.id,
            timestamp=datetime.now(),
            decision_type=context.get('decision_type', 'trading'),
            recommendation=recommendation,
            confidence=decision_confidence,
            reasoning=reasoning,
            supporting_data=self._gather_supporting_data(agent, context),
            vote_weight=agent.vote_weight
        )
        
        return decision
    
    def _calculate_agent_confidence(self, agent: Agent, context: Dict[str, Any]) -> float:
        """Calculate agent confidence based on expertise and context"""
        base_confidence = agent.confidence_level
        
        # Boost confidence if context matches expertise
        context_type = context.get('market_type', 'general')
        expertise_match = any(exp in context_type for exp in agent.expertise_areas)
        
        if expertise_match:
            base_confidence *= 1.2
        
        # Adjust based on personality traits
        if 'risk_aversion' in agent.personality_traits:
            market_volatility = context.get('volatility', 0.1)
            if market_volatility > 0.3:
                base_confidence *= (1 - agent.personality_traits['risk_aversion'] * 0.2)
        
        return min(1.0, max(0.1, base_confidence))
    
    def _generate_agent_recommendation(self, agent: Agent, context: Dict[str, Any]) -> str:
        """Generate recommendation based on agent personality and role"""
        
        # Base recommendations based on agent characteristics
        if agent.name == "Warren":
            return "CONSERVATIVE_BUY" if context.get('pe_ratio', 20) < 15 else "HOLD"
        elif agent.name == "Cathie":
            return "GROWTH_BUY" if context.get('innovation_score', 0.5) > 0.7 else "RESEARCH"
        elif agent.name == "Quant":
            return "SIGNAL_BUY" if context.get('technical_score', 0.5) > 0.6 else "SIGNAL_SELL"
        elif agent.name == "Degen_Auditor":
            return "RISK_APPROVED" if context.get('risk_score', 0.5) < 0.3 else "RISK_WARNING"
        else:
            # Default behavior for other agents
            confidence = self._calculate_agent_confidence(agent, context)
            if confidence > 0.7:
                return "BUY"
            elif confidence > 0.4:
                return "HOLD"
            else:
                return "SELL"
    
    def _generate_agent_reasoning(self, agent: Agent, context: Dict[str, Any], recommendation: str) -> str:
        """Generate human-readable reasoning for agent decision"""
        
        reasoning_templates = {
            "Warren": f"Based on fundamental analysis, {recommendation.lower()} aligns with value investing principles.",
            "Cathie": f"Innovation metrics suggest {recommendation.lower()} for growth potential.",
            "Quant": f"Statistical models indicate {recommendation.lower()} based on technical signals.",
            "Degen_Auditor": f"Risk assessment results in {recommendation.lower()} recommendation."
        }
        
        return reasoning_templates.get(
            agent.name, 
            f"Based on {agent.department.value} analysis, recommending {recommendation.lower()}."
        )
    
    def _gather_supporting_data(self, agent: Agent, context: Dict[str, Any]) -> Dict[str, Any]:
        """Gather supporting data relevant to agent's decision"""
        
        supporting_data = {
            'agent_expertise': agent.expertise_areas,
            'confidence_factors': [],
            'context_relevance': 0.5
        }
        
        # Add department-specific data
        if agent.department == DepartmentType.MARKET_INTELLIGENCE:
            supporting_data['market_analysis'] = context.get('market_data', {})
        elif agent.department == DepartmentType.RISK_CONTROL:
            supporting_data['risk_metrics'] = context.get('risk_data', {})
        elif agent.department == DepartmentType.TRADE_OPERATIONS:
            supporting_data['execution_data'] = context.get('trade_data', {})
        
        return supporting_data
    
    def _conduct_voting_session(self, decisions: List[AgentDecision], context: Dict[str, Any]) -> Dict[str, Any]:
        """Conduct weighted voting session among agents"""
        
        vote_tally = {}
        total_weight = 0
        confidence_weighted_votes = {}
        
        # Collect votes with weights
        for decision in decisions:
            recommendation = decision.recommendation
            weight = decision.vote_weight * decision.confidence
            
            if recommendation not in vote_tally:
                vote_tally[recommendation] = 0
                confidence_weighted_votes[recommendation] = []
            
            vote_tally[recommendation] += weight
            total_weight += weight
            confidence_weighted_votes[recommendation].append({
                'agent_id': decision.agent_id,
                'confidence': decision.confidence,
                'weight': decision.vote_weight
            })
        
        # Determine winning recommendation
        winning_recommendation = max(vote_tally.items(), key=lambda x: x[1])
        
        # Calculate consensus metrics
        consensus_strength = winning_recommendation[1] / total_weight if total_weight > 0 else 0
        
        voting_result = {
            'winning_recommendation': winning_recommendation[0],
            'consensus_strength': consensus_strength,
            'vote_distribution': {k: v/total_weight for k, v in vote_tally.items()},
            'total_votes': len(decisions),
            'participating_agents': [d.agent_id for d in decisions],
            'session_timestamp': datetime.now(),
            'session_id': str(uuid.uuid4())
        }
        
        self.voting_sessions.append(voting_result)
        
        return voting_result
    
    def get_agent_status(self, agent_name: Optional[str] = None) -> Dict[str, Any]:
        """Get status of specific agent or all agents"""
        
        if agent_name:
            agent_id = self.agent_registry.get(agent_name)
            if agent_id and agent_id in self.agents:
                agent = self.agents[agent_id]
                return self._get_single_agent_status(agent)
            else:
                return {'error': f'Agent {agent_name} not found'}
        else:
            # Return status of all agents grouped by department
            status = {}
            for dept in DepartmentType:
                status[dept.value] = []
                
            for agent in self.agents.values():
                agent_status = self._get_single_agent_status(agent)
                status[agent.department.value].append(agent_status)
                
            return status
    
    def _get_single_agent_status(self, agent: Agent) -> Dict[str, Any]:
        """Get comprehensive status for single agent"""
        
        recent_performance = self.performance_tracker.get_agent_performance(agent.id)
        
        return {
            'name': agent.name,
            'role': agent.role.value,
            'department': agent.department.value,
            'active': agent.active,
            'confidence_level': agent.confidence_level,
            'performance_score': agent.performance_score,
            'expertise_areas': agent.expertise_areas,
            'personality_summary': self._summarize_personality(agent.personality_traits),
            'recent_performance': recent_performance,
            'vote_weight': agent.vote_weight,
            'created_at': agent.created_at.isoformat()
        }
    
    def _summarize_personality(self, traits: Dict[str, float]) -> str:
        """Create human-readable personality summary"""
        dominant_traits = sorted(traits.items(), key=lambda x: x[1], reverse=True)[:2]
        trait_descriptions = {
            'risk_aversion': 'Risk-averse',
            'innovation_focus': 'Innovation-focused', 
            'mathematical_precision': 'Analytically precise',
            'strategic_thinking': 'Strategic thinker',
            'execution_speed': 'Fast executor',
            'risk_vigilance': 'Risk-vigilant'
        }
        
        descriptions = [trait_descriptions.get(trait, trait.replace('_', ' ')) 
                       for trait, _ in dominant_traits]
        
        return ', '.join(descriptions)
    
    def update_agent_performance(self, agent_id: str, performance_data: Dict[str, Any]):
        """Update agent performance based on outcomes"""
        
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            
            # Update performance score with learning rate
            new_score = performance_data.get('score', agent.performance_score)
            agent.performance_score = (
                agent.performance_score * (1 - agent.learning_rate) +
                new_score * agent.learning_rate
            )
            
            # Adjust confidence based on recent performance
            if performance_data.get('accuracy', 0.5) > 0.8:
                agent.confidence_level = min(1.0, agent.confidence_level * 1.05)
            elif performance_data.get('accuracy', 0.5) < 0.3:
                agent.confidence_level = max(0.1, agent.confidence_level * 0.95)
            
            # Record in performance tracker
            self.performance_tracker.record_agent_performance(agent_id, performance_data)

class AgentPerformanceTracker:
    """Tracks agent performance and coordination metrics"""
    
    def __init__(self):
        self.performance_history = {}
        self.coordination_sessions = []
        
    def record_agent_performance(self, agent_id: str, performance_data: Dict[str, Any]):
        """Record individual agent performance"""
        
        if agent_id not in self.performance_history:
            self.performance_history[agent_id] = []
            
        performance_record = {
            'timestamp': datetime.now(),
            'data': performance_data
        }
        
        self.performance_history[agent_id].append(performance_record)
        
    def record_coordination_session(self, decisions: List[AgentDecision], result: Dict[str, Any]):
        """Record coordination session outcomes"""
        
        session_record = {
            'timestamp': datetime.now(),
            'decisions': [asdict(d) for d in decisions],
            'result': result,
            'consensus_strength': result.get('consensus_strength', 0)
        }
        
        self.coordination_sessions.append(session_record)
        
    def get_agent_performance(self, agent_id: str, days: int = 7) -> Dict[str, Any]:
        """Get recent performance metrics for agent"""
        
        if agent_id not in self.performance_history:
            return {'performance_records': 0, 'average_score': 0}
            
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_records = [
            r for r in self.performance_history[agent_id] 
            if r['timestamp'] > cutoff_date
        ]
        
        if not recent_records:
            return {'performance_records': 0, 'average_score': 0}
            
        scores = [r['data'].get('score', 0.5) for r in recent_records]
        
        return {
            'performance_records': len(recent_records),
            'average_score': sum(scores) / len(scores),
            'latest_score': scores[-1] if scores else 0,
            'trend': 'improving' if len(scores) > 1 and scores[-1] > scores[0] else 'stable'
        }
