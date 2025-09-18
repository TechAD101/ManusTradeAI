"""AI Firm Architecture Module

Sophisticated 20+ agent AI firm structure with autonomous CEO,
multi-department coordination, and advanced report generation.
"""

# This file makes the ai_firm directory a Python package
# Required for proper import resolution

__version__ = "1.0.0"
__author__ = "YantraX AI Team"

try:
    from .ceo import AutonomousCEO, CEOPersonality
    from .agent_manager import AgentManager, DepartmentType
    from .report_generation import AdvancedReportGenerator, ReportType
    
    __all__ = [
        'AutonomousCEO',
        'CEOPersonality', 
        'AgentManager',
        'DepartmentType',
        'AdvancedReportGenerator',
        'ReportType'
    ]
    
except ImportError as e:
    print(f"Warning: AI Firm components import failed: {e}")
    __all__ = []
