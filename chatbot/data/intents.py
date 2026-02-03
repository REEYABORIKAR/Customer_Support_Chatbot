INTENTS = [
    {
        "intent": "greeting",
        "patterns": [
            "hi", "hello", "hey", "hello bot",
            "good morning", "good afternoon", "good evening",
            "is anyone there"
        ],
        "responses": [
            "Hello! How can I assist you today?",
            "Hi there! How may I help you?",
            "Hello! I am here to help with orders, products, or support.",
            "Welcome! How can I assist you right now?",
            "Hi! Let me know what you’d like help with today."
        ],
        "priority": 1,
        "escalate": False
    },

    {
        "intent": "complaint",
        "patterns": [
            "im unhappy", "i am unhappy",
            "bad service", "this is frustrating",
            "worst experience", "not satisfied",
            "very disappointed"
        ],
        "responses": [
            "I’m really sorry for the inconvenience ",
            "I understand your frustration. Let me help resolve this.",
            "Your experience matters to us. Let’s fix this.",
            "I apologize for the trouble. Would you like me to connect you to support?"
        ],
        "priority": 2,
        "escalate": True
    },

    {
        "intent": "refund_policy",
        "patterns": [
            "refund", "return", "money back",
            "cancel order", "cancel my order",
            "refund not received", "return request",
            "return my product", "i want to return my product"
        ],
        "responses": [
            "Refunds are processed within 5–7 business days after approval.",
            "You can request a refund within 10 days of delivery.",
        ],
        "priority": 3,
        "escalate": True
    },

    {
        "intent": "order_status",
        "patterns": [
            "order status", "where is my order",
            "track my order", "order tracking",
            "order not delivered", "my order is delayed",
            "check my order", "when will my order arrive"
        ],
        "responses": [
            "Please provide your order ID to check the status.",
            "I’ll help you check your order status.",
            "Once you share your order ID, I can look into it."
        ],
        "priority": 4,
        "escalate": False
    },

    {
        "intent": "shipping_info",
        "patterns": [
            "shipping charges", "delivery time",
            "how long does shipping take",
            "shipping cost", "delivery charges"
        ],
        "responses": [
            "Shipping usually takes 3–5 business days.",
            "Delivery time depends on your location, typically 3–7 days.",
            "Shipping charges vary based on location and order value."
        ],
        "priority": 5,
        "escalate": False
    },

    {
        "intent": "working_hours",
        "patterns": [
            "working hours", "when are you open",
            "support timings", "office hours"
        ],
        "responses": [
            "Our support team is available Monday to Friday, 9 AM to 6 PM.",
            "We’re open from 9 AM to 6 PM on weekdays.",
            "Customer support operates during standard business hours (9 AM – 6 PM)."
        ],
        "priority": 6,
        "escalate": False
    },

    {
        "intent": "product_info",
        "patterns": [
            "product", "products",
            "what do you sell", "features",
            "product details", "specification",
            "do you have specification"
        ],
        "responses": [
            "Our products are built with high quality standards. Please tell me which product you're interested in.",
            "You can find detailed product information on our official website.",
            "Could you please specify which product you’re looking for?",
            "I can help with features, pricing, or availability."
        ],
        "priority": 7,
        "escalate": False
    },

    {
        "intent": "confirmation",
        "patterns": [
            "ok", "okay", "yes", "sure",
            "sounds good", "alright",
            "no", "not really"
        ],
        "responses": [
            "Alright  Let me know how I can help you further.",
            "Okay! If you need anything else, just tell me.",
            "Got it. What would you like to do next?",
            "No problem. Let me know if you change your mind."
        ],
        "priority": 8,
        "escalate": False
    },

    {
        "intent": "thank_you",
        "patterns": [
            "thanks", "thank you",
            "thank you so much", "appreciate it"
        ],
        "responses": [
            "You're welcome! ",
            "Happy to help!",
            "Glad I could assist you.",
            "Anytime! Let me know if you need anything else."
        ],
        "priority": 9,
        "escalate": False
    },

    {
        "intent": "goodbye",
        "patterns": [
            "bye", "goodbye", "see you",
            "thats all", "ok bye", "see ya"
        ],
        "responses": [
            "Thank you for chatting with us. Goodbye!",
            "Goodbye! Feel free to reach out anytime.",
            "Have a wonderful day ahead!"
        ],
        "priority": 10,
        "escalate": False
    }
]
