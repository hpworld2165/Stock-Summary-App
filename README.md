# 📈 Stock Summary App

A simple Flask web application that:
- Takes a stock ticker as input (e.g., AAPL, TSLA)
- Fetches the last 3 days of stock data using `yfinance`
- Uses **Gemini API** to generate a natural language summary of the stock performance

---

## 💡 Features

- Real-time stock data from Yahoo Finance
- AI-generated summary using `gemini` model via Google Generative AI API
- Clean and beginner-friendly Flask backend
- Secure API key handling using `.env` file

Setup Instructions - 

	1.	Get your Gemini API key from Google AI Studio
 	2.	Create a .env file in your project root
  	3. 	Store your Api key in a variable in the .env file.
  	4.	Run the Flask app: "python app.py" 
