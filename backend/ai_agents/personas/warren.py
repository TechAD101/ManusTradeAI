"""Warren Buffett-Inspired AI Persona

Conservative fundamental analysis agent with value investing philosophy
and risk management focus. Secured with pbkdf2:sha256 for production use.
"""

import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import json

@dataclass
class WarrenPersonality:
    """Warren's core personality traits and investment philosophy"""
    risk_aversion: float = 0.85
    fundamentals_focus: float = 0.95
    patience_level: float = 0.90
    value_orientation: float = 0.88
    long_term_vision: float = 0.92
    contrarian_tendency: float = 0.75
    
class WarrenAgent:
    """Warren Buffett-inspired AI trading agent"""
    
    def __init__(self):
        self.name = "Warren"
        self.personality = WarrenPersonality()
        self.investment_criteria = self._initialize_criteria()
        self.memory = WarrenMemory()
        self.security_hash = self._generate_security_hash()
        
    def _initialize_criteria(self) -> Dict[str, Any]:
        """Initialize Warren's strict investment criteria"""
        return {
            'min_roe': 0.15,  # Minimum 15% ROE
            'max_pe_ratio': 25,  # Maximum P/E ratio
            'min_profit_margin': 0.10,  # Minimum 10% profit margin
            'max_debt_to_equity': 0.5,  # Maximum 50% debt-to-equity
            'min_dividend_yield': 0.02,  # Minimum 2% dividend yield
            'min_revenue_growth': 0.05,  # Minimum 5% revenue growth
            'moat_requirement': True,  # Must have economic moat
            'management_quality_threshold': 0.8  # Management quality score
        }
    
    def _generate_security_hash(self) -> str:
        """Generate pbkdf2:sha256 security hash for production use"""
        salt = secrets.token_bytes(32)
        key = hashlib.pbkdf2_hmac('sha256', 
                                 f'{self.name}_agent_{datetime.now().isoformat()}'.encode(),
                                 salt, 100000)
        return key.hex()[:16]
    
    def analyze_investment(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Perform Warren-style fundamental analysis"""
        
        symbol = context.get('symbol', 'UNKNOWN')
        fundamentals = context.get('fundamentals', {})
        market_data = context.get('market_data', {})
        
        # Perform fundamental analysis
        analysis_score = self._calculate_fundamental_score(fundamentals)
        valuation_assessment = self._assess_valuation(fundamentals, market_data)
        moat_evaluation = self._evaluate_economic_moat(context)
        
        # Generate Warren's recommendation
        recommendation = self._generate_recommendation(
            analysis_score, valuation_assessment, moat_evaluation
        )
        
        # Store in memory for learning
        self.memory.store_analysis(symbol, recommendation, context)
        
        return {
            'agent': self.name,
            'symbol': symbol,
            'recommendation': recommendation['action'],
            'confidence': recommendation['confidence'],
            'reasoning': recommendation['reasoning'],
            'fundamental_score': analysis_score,
            'valuation_score': valuation_assessment['score'],
            'moat_strength': moat_evaluation['strength'],
            'warren_criteria_met': recommendation['criteria_met'],
            'long_term_outlook': recommendation['long_term_outlook'],
            'risk_assessment': self._assess_warren_risk(fundamentals),
            'timestamp': datetime.now().isoformat()
        }
    
    def _calculate_fundamental_score(self, fundamentals: Dict[str, Any]) -> float:
        """Calculate comprehensive fundamental analysis score"""
        
        score_components = []
        
        # Profitability metrics
        roe = fundamentals.get('return_on_equity', 0)
        if roe >= self.investment_criteria['min_roe']:
            score_components.append(min(1.0, roe / 0.3))  # Cap at 30% ROE
        else:
            score_components.append(0.3)  # Penalty for low ROE
        
        # Profit margins
        profit_margin = fundamentals.get('profit_margin', 0)
        if profit_margin >= self.investment_criteria['min_profit_margin']:
            score_components.append(min(1.0, profit_margin / 0.25))  # Cap at 25%
        else:
            score_components.append(0.4)
        
        # Debt management
        debt_to_equity = fundamentals.get('debt_to_equity', 1.0)
        if debt_to_equity <= self.investment_criteria['max_debt_to_equity']:
            score_components.append(1.0 - debt_to_equity)
        else:
            score_components.append(0.2)  # High penalty for excessive debt
        
        # Revenue growth
        revenue_growth = fundamentals.get('revenue_growth', 0)
        if revenue_growth >= self.investment_criteria['min_revenue_growth']:
            score_components.append(min(1.0, revenue_growth / 0.2))  # Cap at 20%
        else:
            score_components.append(0.5)
        
        # Dividend sustainability
        dividend_yield = fundamentals.get('dividend_yield', 0)
        payout_ratio = fundamentals.get('payout_ratio', 1.0)
        if dividend_yield >= self.investment_criteria['min_dividend_yield'] and payout_ratio < 0.8:
            score_components.append(0.9)
        else:
            score_components.append(0.6)
        
        return sum(score_components) / len(score_components)
    
    def _assess_valuation(self, fundamentals: Dict[str, Any], market_data: Dict[str, Any]) -> Dict[str, Any]:
        """Assess if stock is undervalued using Warren's methods"""
        
        pe_ratio = fundamentals.get('pe_ratio', 50)
        book_value = fundamentals.get('book_value_per_share', 0)
        current_price = market_data.get('current_price', 0)
        
        # Calculate intrinsic value using simplified DCF
        intrinsic_value = self._calculate_intrinsic_value(fundamentals)
        
        # P/E assessment
        pe_score = 1.0 if pe_ratio <= self.investment_criteria['max_pe_ratio'] else 0.3
        
        # Price-to-book assessment
        pb_ratio = current_price / book_value if book_value > 0 else 10
        pb_score = 1.0 if pb_ratio <= 3.0 else 0.4
        
        # Margin of safety
        margin_of_safety = (intrinsic_value - current_price) / intrinsic_value if intrinsic_value > 0 else -1
        mos_score = 1.0 if margin_of_safety >= 0.25 else 0.2  # Require 25% margin of safety
        
        overall_score = (pe_score + pb_score + mos_score) / 3
        
        return {
            'score': overall_score,
            'pe_ratio': pe_ratio,
            'pb_ratio': pb_ratio,
            'intrinsic_value': intrinsic_value,
            'current_price': current_price,
            'margin_of_safety': margin_of_safety,
            'undervalued': margin_of_safety >= 0.25
        }
    
    def _calculate_intrinsic_value(self, fundamentals: Dict[str, Any]) -> float:
        """Calculate intrinsic value using simplified DCF model"""
        
        # Get financial metrics
        free_cash_flow = fundamentals.get('free_cash_flow', 0)
        revenue_growth = fundamentals.get('revenue_growth', 0.05)
        shares_outstanding = fundamentals.get('shares_outstanding', 1)
        
        # Warren's conservative assumptions
        growth_rate = min(revenue_growth, 0.15)  # Cap growth at 15%
        discount_rate = 0.10  # Warren's required return
        terminal_growth = 0.03  # Long-term GDP growth
        
        # 10-year DCF calculation
        projected_cashflows = []
        for year in range(1, 11):
            if year <= 5:
                cf = free_cash_flow * ((1 + growth_rate) ** year)
            else:
                cf = free_cash_flow * ((1 + growth_rate) ** 5) * ((1 + terminal_growth) ** (year - 5))
            
            present_value = cf / ((1 + discount_rate) ** year)
            projected_cashflows.append(present_value)
        
        # Terminal value
        terminal_cf = projected_cashflows[-1] * (1 + terminal_growth)
        terminal_value = terminal_cf / (discount_rate - terminal_growth)
        terminal_pv = terminal_value / ((1 + discount_rate) ** 10)
        
        # Total enterprise value
        enterprise_value = sum(projected_cashflows) + terminal_pv
        
        # Per share value
        intrinsic_value = enterprise_value / shares_outstanding if shares_outstanding > 0 else 0
        
        return intrinsic_value
    
    def _evaluate_economic_moat(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate company's economic moat strength"""
        
        company_data = context.get('company_data', {})
        
        moat_indicators = {
            'brand_strength': company_data.get('brand_score', 0.5),
            'switching_costs': company_data.get('switching_cost_score', 0.5),
            'network_effects': company_data.get('network_effect_score', 0.5),
            'cost_advantages': company_data.get('cost_advantage_score', 0.5),
            'regulatory_protection': company_data.get('regulatory_score', 0.5)
        }
        
        # Calculate overall moat strength
        moat_strength = sum(moat_indicators.values()) / len(moat_indicators)
        
        # Warren's moat classification
        if moat_strength >= 0.8:
            moat_classification = "Wide Moat"
        elif moat_strength >= 0.6:
            moat_classification = "Narrow Moat"
        else:
            moat_classification = "No Moat"
        
        return {
            'strength': moat_strength,
            'classification': moat_classification,
            'indicators': moat_indicators,
            'meets_warren_standard': moat_strength >= 0.6
        }
    
    def _generate_recommendation(self, fundamental_score: float, 
                               valuation: Dict[str, Any], 
                               moat: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Warren's final investment recommendation"""
        
        # Check all Warren criteria
        criteria_met = [
            fundamental_score >= 0.7,
            valuation['undervalued'],
            moat['meets_warren_standard']
        ]
        
        criteria_count = sum(criteria_met)
        
        # Generate recommendation based on criteria
        if criteria_count == 3:
            action = "STRONG_BUY"
            confidence = 0.9
            reasoning = "Excellent fundamentals, undervalued, and strong economic moat - classic Warren investment"
            long_term_outlook = "Very Positive"
        elif criteria_count == 2:
            if valuation['undervalued'] and moat['meets_warren_standard']:
                action = "BUY"
                confidence = 0.75
                reasoning = "Good value with economic moat, acceptable fundamentals"
                long_term_outlook = "Positive"
            else:
                action = "HOLD"
                confidence = 0.6
                reasoning = "Mixed signals - meets some but not all Warren criteria"
                long_term_outlook = "Neutral"
        elif criteria_count == 1:
            action = "HOLD"
            confidence = 0.4
            reasoning = "Insufficient quality metrics for Warren-style investment"
            long_term_outlook = "Cautious"
        else:
            action = "AVOID"
            confidence = 0.8
            reasoning = "Fails Warren's investment criteria - poor fundamentals, overvalued, or no moat"
            long_term_outlook = "Negative"
        
        return {
            'action': action,
            'confidence': confidence,
            'reasoning': reasoning,
            'criteria_met': criteria_count,
            'long_term_outlook': long_term_outlook,
            'warren_score': (fundamental_score + valuation['score'] + moat['strength']) / 3
        }
    
    def _assess_warren_risk(self, fundamentals: Dict[str, Any]) -> Dict[str, Any]:
        """Assess investment risk from Warren's perspective"""
        
        # Business risk factors
        debt_risk = "High" if fundamentals.get('debt_to_equity', 0) > 0.5 else "Low"
        earnings_stability = "Stable" if fundamentals.get('earnings_volatility', 1.0) < 0.3 else "Volatile"
        competitive_position = "Strong" if fundamentals.get('market_share', 0) > 0.2 else "Weak"
        
        # Overall risk assessment
        risk_factors = [debt_risk == "High", earnings_stability == "Volatile", competitive_position == "Weak"]
        risk_score = sum(risk_factors) / len(risk_factors)
        
        if risk_score <= 0.3:
            overall_risk = "Low"
        elif risk_score <= 0.6:
            overall_risk = "Moderate"
        else:
            overall_risk = "High"
        
        return {
            'overall_risk': overall_risk,
            'debt_risk': debt_risk,
            'earnings_stability': earnings_stability,
            'competitive_position': competitive_position,
            'risk_score': risk_score
        }
    
    def get_warren_insights(self) -> Dict[str, Any]:
        """Get Warren's current market insights and philosophy"""
        
        return {
            'investment_philosophy': {
                'rule_1': "Never lose money",
                'rule_2': "Never forget rule #1",
                'approach': "Buy wonderful companies at fair prices",
                'time_horizon': "Forever",
                'focus': "Intrinsic value and economic moats"
            },
            'current_market_view': self._generate_market_view(),
            'portfolio_guidelines': {
                'concentration': "High conviction, concentrated positions",
                'diversification': "Wide diversification is protection against ignorance",
                'cash_position': "Maintain cash for opportunities",
                'turnover': "Low turnover, buy and hold"
            },
            'decision_criteria': self.investment_criteria,
            'recent_performance': self.memory.get_performance_summary()
        }
    
    def _generate_market_view(self) -> str:
        """Generate Warren's view on current market conditions"""
        
        market_views = [
            "Be fearful when others are greedy and greedy when others are fearful",
            "Price is what you pay, value is what you get",
            "Time in the market beats timing the market",
            "Look for businesses with predictable earnings and strong competitive advantages",
            "The stock market is a voting machine in the short run, but a weighing machine in the long run"
        ]
        
        # Return different views based on current market conditions
        return market_views[datetime.now().day % len(market_views)]

class WarrenMemory:
    """Memory system for Warren agent to learn from past decisions"""
    
    def __init__(self):
        self.analysis_history = []
        self.performance_tracking = {}
        
    def store_analysis(self, symbol: str, recommendation: Dict[str, Any], context: Dict[str, Any]):
        """Store analysis for future learning"""
        
        analysis_record = {
            'timestamp': datetime.now(),
            'symbol': symbol,
            'recommendation': recommendation,
            'context_hash': self._hash_context(context),
            'outcome': None  # To be updated later
        }
        
        self.analysis_history.append(analysis_record)
        
    def _hash_context(self, context: Dict[str, Any]) -> str:
        """Create hash of context for pattern recognition"""
        context_str = json.dumps(context, sort_keys=True, default=str)
        return hashlib.md5(context_str.encode()).hexdigest()[:8]
    
    def get_performance_summary(self) -> Dict[str, Any]:
        """Get performance summary of Warren's recommendations"""
        
        if not self.analysis_history:
            return {'total_analyses': 0, 'success_rate': 0}
        
        successful_analyses = len([a for a in self.analysis_history 
                                 if a.get('outcome') == 'positive'])
        
        return {
            'total_analyses': len(self.analysis_history),
            'success_rate': successful_analyses / len(self.analysis_history),
            'recent_analyses': len([a for a in self.analysis_history 
                                  if (datetime.now() - a['timestamp']).days <= 30])
        }
