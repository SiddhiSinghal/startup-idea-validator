from flask import Flask, render_template, request, jsonify
import json
import random
from datetime import datetime

app = Flask(__name__)

# Sample data for domains and startup ideas
DOMAINS = {
    "finance": {
        "name": "Finance",
        "description": "Financial Solutions & Services",
        "ideas": [
            "AI-powered personal finance advisor",
            "Blockchain-based micro-lending platform",
            "Cryptocurrency portfolio management tool",
            "Digital banking for small businesses",
            "Automated investment portfolio rebalancer"
        ]
    },
    "healthcare": {
        "name": "Healthcare",
        "description": "Health & Medical Innovation",
        "ideas": [
            "Telemedicine platform for rural areas",
            "AI diagnostic tool for medical imaging",
            "Mental health chatbot companion",
            "Wearable health monitoring device",
            "Personalized nutrition planning app"
        ]
    },
    "education": {
        "name": "Education",
        "description": "Learning & Development",
        "ideas": [
            "Personalized learning AI tutor",
            "Virtual reality classroom experiences",
            "Skill-based job matching platform",
            "Gamified coding education app",
            "Language learning with AI conversation partners"
        ]
    },
    "shopping": {
        "name": "Shopping",
        "description": "Online Retail & Commerce",
        "ideas": [
            "AR-powered virtual try-on platform",
            "Sustainable product marketplace",
            "Social commerce integration tool",
            "AI-powered inventory management",
            "Subscription box curation service"
        ]
    },
    "realestate": {
        "name": "Real Estate",
        "description": "Property & Housing Solutions",
        "ideas": [
            "Smart home automation platform",
            "Real estate investment analyzer",
            "Virtual property tour creator",
            "Rental property management system",
            "AI-powered property valuation tool"
        ]
    },
    "food": {
        "name": "Food",
        "description": "Food & Dining Solutions",
        "ideas": [
            "AI-powered recipe recommendation app",
            "Food waste reduction platform",
            "Smart kitchen inventory management",
            "Plant-based meal planning service",
            "Restaurant reservation and management system"
        ]
    },
    "retail": {
        "name": "Retail",
        "description": "Store & Shopping Innovation",
        "ideas": [
            "Smart inventory prediction system",
            "Customer behavior analytics platform",
            "Automated checkout solution",
            "Personalized shopping assistant",
            "Supply chain optimization tool"
        ]
    },
    "workplace": {
        "name": "Workplace",
        "description": "HR & Team Management",
        "ideas": [
            "AI-powered recruitment platform",
            "Employee engagement analytics",
            "Skills development tracking system",
            "Remote team management tool",
            "Automated performance review system"
        ]
    },
    "delivery": {
        "name": "Delivery",
        "description": "Logistics & Transportation",
        "ideas": [
            "Route optimization platform",
            "Fleet management system",
            "Last-mile delivery solution",
            "Supply chain visibility tool",
            "Automated warehouse management"
        ]
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/domains')
def domains():
    return render_template('domains.html', domains=DOMAINS)

@app.route('/validate')
def validate():
    return render_template('validate.html')

@app.route('/api/validate-idea', methods=['POST'])
def validate_idea():
    data = request.json
    idea = data.get('idea', '')
    
    # Simulate AI-powered validation (replace with actual GPT-4 API call)
    validation_result = {
        "idea": idea,
        "problem": f"The current market lacks efficient solutions for {idea.lower()}, creating friction for users who need streamlined access to this service.",
        "solution": f"Our {idea} platform leverages AI and modern technology to provide a seamless, user-friendly experience that addresses the core pain points in this market.",
        "target_audience": "Tech-savvy millennials and Gen-Z users aged 25-40 who value efficiency and digital-first solutions.",
        "competitors": ["Competitor A", "Competitor B", "Competitor C"],
        "market_demand": random.choice(["High", "Medium", "Low"]),
        "viability_score": random.randint(65, 95),
        "recommendations": [
            "Focus on user experience and interface design",
            "Build strong partnerships in the industry",
            "Consider freemium pricing model for initial traction",
            "Invest in robust security and data protection"
        ]
    }
    
    return jsonify(validation_result)

@app.route('/api/get-domain-ideas/<domain>')
def get_domain_ideas(domain):
    if domain in DOMAINS:
        return jsonify(DOMAINS[domain])
    return jsonify({"error": "Domain not found"}), 404

@app.route('/api/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.json
    # Here you would save feedback to database
    # For now, we'll just return a success response
    return jsonify({"status": "success", "message": "Feedback submitted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
