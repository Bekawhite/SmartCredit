import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st

def generate_sample_borrowers(count=100):
    """Generate sample borrower data for testing and demonstration"""
    segments = ['SME', 'Consumer', 'Agriculture', 'Corporate']
    employment_types = ['Salaried', 'Business Owner', 'Self-Employed', 'Contractor']
    income_bands = ['Low (<50K)', 'Medium (50K-150K)', 'High (150K-500K)', 'Very High (>500K)']
    regions = ['Nairobi', 'Coast', 'Central', 'Rift Valley', 'Western', 'Eastern']
    
    borrowers = []
    for i in range(count):
        income_band = np.random.choice(income_bands)
        base_income = {
            'Low (<50K)': np.random.randint(20000, 50000),
            'Medium (50K-150K)': np.random.randint(50000, 150000),
            'High (150K-500K)': np.random.randint(150000, 500000),
            'Very High (>500K)': np.random.randint(500000, 1000000)
        }[income_band]
        
        borrowers.append({
            'borrower_id': f'BORR{i+1:03d}',
            'first_name': f'FirstName{i+1}',
            'last_name': f'LastName{i+1}',
            'email': f'borrower{i+1}@kcb.com',
            'phone': f'+2547{np.random.randint(10000000, 99999999)}',
            'segment': np.random.choice(segments),
            'employment_type': np.random.choice(employment_types),
            'income_band': income_band,
            'monthly_income': base_income,
            'region': np.random.choice(regions),
            'credit_score': np.random.randint(300, 850),
            'registration_date': datetime.now() - timedelta(days=np.random.randint(1, 1000))
        })
    
    return pd.DataFrame(borrowers)

def generate_sample_loans(count=200):
    """Generate sample loan data for testing and demonstration"""
    products = ['Personal Loan', 'Business Loan', 'Mortgage', 'Auto Loan', 'SME Credit', 'Emergency Loan']
    statuses = ['Active', 'Delinquent', 'Restructured', 'Closed', 'Written Off']
    risk_bands = ['Low', 'Medium', 'High', 'Critical']
    
    loans = []
    for i in range(count):
        loan_amount = np.random.uniform(50000, 5000000)
        status = np.random.choice(statuses, p=[0.75, 0.10, 0.05, 0.08, 0.02])
        
        loans.append({
            'loan_id': f'LOAN{i+1:03d}',
            'borrower_id': f'BORR{np.random.randint(1, 101):03d}',
            'product_type': np.random.choice(products),
            'loan_amount': loan_amount,
            'outstanding_balance': loan_amount * np.random.uniform(0.1, 1.0),
            'interest_rate': np.random.uniform(8.0, 25.0),
            'term_months': np.random.choice([12, 24, 36, 48, 60]),
            'days_past_due': np.random.randint(0, 120) if status in ['Delinquent', 'Restructured'] else 0,
            'status': status,
            'risk_band': np.random.choice(risk_bands, p=[0.60, 0.25, 0.10, 0.05]),
            'collateral_value': loan_amount * np.random.uniform(0.5, 1.5),
            'origination_date': datetime.now() - timedelta(days=np.random.randint(1, 365*3))
        })
    
    return pd.DataFrame(loans)

def calculate_risk_band(score):
    """Calculate risk band from numerical score (0-100)"""
    if score >= 80:
        return "Critical"
    elif score >= 60:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"

def format_currency(amount, currency="KES"):
    """Format currency amount with proper formatting"""
    if amount >= 1000000:
        return f"{currency} {amount/1000000:.2f}M"
    elif amount >= 1000:
        return f"{currency} {amount/1000:.1f}K"
    else:
        return f"{currency} {amount:,.0f}"

def calculate_debt_to_income(monthly_debt, monthly_income):
    """Calculate debt-to-income ratio"""
    if monthly_income == 0:
        return float('inf')
    return (monthly_debt / monthly_income) * 100

def validate_loan_parameters(loan_amount, income, existing_debt=0, term_months=12):
    """Validate loan parameters and return approval recommendation"""
    dti = calculate_debt_to_income(existing_debt + (loan_amount / term_months), income)
    
    if dti > 60:
        return {
            "approved": False,
            "reason": "Debt-to-income ratio too high",
            "dti_ratio": f"{dti:.1f}%",
            "suggestion": "Reduce loan amount or increase income"
        }
    elif loan_amount > income * 12:
        return {
            "approved": False,
            "reason": "Loan amount exceeds annual income",
            "suggestion": "Reduce loan amount"
        }
    elif term_months > 60:
        return {
            "approved": False,
            "reason": "Loan term too long",
            "suggestion": "Maximum term is 60 months"
        }
    else:
        return {
            "approved": True,
            "dti_ratio": f"{dti:.1f}%",
            "message": "Loan parameters are acceptable"
        }

def get_risk_color(risk_band):
    """Get color code for risk bands"""
    color_map = {
        'Low': '#28a745',
        'Medium': '#ffc107', 
        'High': '#fd7e14',
        'Critical': '#dc3545'
    }
    return color_map.get(risk_band, '#6c757d')

def calculate_affordability(monthly_income, monthly_expenses, proposed_payment):
    """Calculate affordability metrics"""
    disposable_income = monthly_income - monthly_expenses
    affordability_ratio = (proposed_payment / disposable_income) * 100 if disposable_income > 0 else 100
    
    if affordability_ratio <= 30:
        status = "Excellent"
        color = "green"
    elif affordability_ratio <= 50:
        status = "Good" 
        color = "blue"
    elif affordability_ratio <= 70:
        status = "Fair"
        color = "orange"
    else:
        status = "Poor"
        color = "red"
    
    return {
        "disposable_income": disposable_income,
        "affordability_ratio": affordability_ratio,
        "status": status,
        "color": color
    }

def generate_portfolio_summary(loans_df):
    """Generate portfolio summary statistics"""
    total_loans = len(loans_df)
    total_outstanding = loans_df['outstanding_balance'].sum()
    avg_loan_size = loans_df['outstanding_balance'].mean()
    
    npl_loans = loans_df[loans_df['days_past_due'] > 90]
    npl_ratio = (len(npl_loans) / total_loans) * 100 if total_loans > 0 else 0
    
    risk_distribution = loans_df['risk_band'].value_counts().to_dict()
    
    return {
        "total_loans": total_loans,
        "total_outstanding": total_outstanding,
        "average_loan_size": avg_loan_size,
        "npl_ratio": npl_ratio,
        "npl_count": len(npl_loans),
        "risk_distribution": risk_distribution,
        "product_distribution": loans_df['product_type'].value_counts().to_dict()
    }

def create_sample_npl_trend():
    """Create sample NPL trend data"""
    months = pd.date_range('2023-01-01', periods=12, freq='M')
    return pd.DataFrame({
        'month': months,
        'npl_ratio': [8.5, 8.2, 7.9, 7.7, 7.8, 8.1, 8.4, 8.6, 8.3, 8.0, 7.8, 7.6],
        'portfolio_value': [200, 210, 215, 220, 225, 230, 235, 238, 240, 242, 244, 245.7]
    })
