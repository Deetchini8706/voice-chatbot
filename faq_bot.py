# chatbot.py
faq_responses = {
    "return policy": "Our return policy allows returns within 30 days of purchase.",
    "shipping": "We offer free shipping on orders above ₹999.",
    "support": "You can contact our support team 24/7 through the app.",
    "payment": "We accept credit cards, UPI, and net banking.",
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in faq_responses:
        if key in user_input:
            return faq_responses[key]
    return "Sorry, I didn't catch that. Could you please repeat your question?"