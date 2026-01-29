# Customer Support Chatbot 🤖

A lightweight, rule-based customer support chatbot built with **FastAPI**. This bot uses keyword matching and logical triggers to assist users with common inquiries like order status, refunds, shipping, and general support.

## 🚀 Features

* **Rule-Based Intent Recognition:** Matches user input against predefined intents (orders, refunds, shipping, etc.).
* **Order Tracking Simulation:** Handles multi-turn logic to request and validate order IDs.
* **Text Preprocessing:** Normalizes text, removes special characters, and corrects common spelling mistakes.
* **Web-Based Interface:** Simple and clean UI built with HTML/CSS and JavaScript for real-time interaction.
* **Custom Exception Handling & Logging:** Robust error management and session-based logging for debugging.

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **Templating:** [Jinja2](https://jinja.palletsprojects.com/)
* **Spelling Correction:** [pyspellchecker](https://pypi.org/project/pyspellchecker/)
* **Frontend:** HTML5, CSS3, JavaScript

## 📋 Prerequisites

* Python 3.8+
* `pip` (Python package manager)

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/REEYABORIKAR/Customer_Support_Chatbot.git](https://github.com/REEYABORIKAR/Customer_Support_Chatbot.git)
    cd Customer_Support_Chatbot
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    uvicorn app:app --reload
    ```

5.  **Access the Chatbot:**
    Open your browser and navigate to `http://127.0.0.1:8000`.

## 💬 Supported Scenarios

The bot is currently programmed to handle the following topics:
* **Greetings:** Hello, Hi, Hey.
* **Order Status:** Tracking and checking order delivery (Requires a valid 5–20 character ID).
* **Refunds:** Information on refund policies and processing times.
* **Shipping:** Delivery charges and estimated times.
* **Complaints:** Handling unhappy customer feedback.
* **General:** Working hours, product info, and support contact.

## 📁 Project Structure

```text
├── app.py                # FastAPI application entry point
├── chatbot/
│   ├── core/             # Chatbot logic and intent matching
│   ├── config/           # Static configurations and messages
│   ├── data/             # Predefined intent patterns and responses
│   ├── exception/        # Custom exception handling
│   ├── logging/          # Logging configuration
│   └── utils/            # Text cleaning and validation utilities
├── static/               # CSS and JavaScript files
├── templates/            # HTML templates (Jinja2)
└── requirements.txt      # Project dependencies