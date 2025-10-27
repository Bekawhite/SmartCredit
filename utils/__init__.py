"""
Utils package for KCB SmartCredit App

This package contains utility functions and helpers for the application.
"""

__version__ = "1.0.0"
__author__ = "KCB SmartCredit Team"
__description__ = "Utility functions for KCB SmartCredit Application"

# Import key functions to make them easily accessible
from .helpers import (
    generate_sample_borrowers,
    generate_sample_loans,
    calculate_risk_band,
    format_currency,
    calculate_debt_to_income,
    validate_loan_parameters
)

# List of available functions in this package
__all__ = [
    'generate_sample_borrowers',
    'generate_sample_loans', 
    'calculate_risk_band',
    'format_currency',
    'calculate_debt_to_income',
    'validate_loan_parameters'
]

# Package initialization
print(f"Initializing KCB SmartCredit Utils v{__version__}")
