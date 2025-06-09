from flask import Flask, render_template, request
import os
import yfinance as yf
from datetime import datetime, timedelta
from dotenv import load_dotenv
import openai
from google import genai

# Load environment variables (like API keys) from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a Flask app instance
app = Flask(__name__)

# Route for the homepage (form page)
@app.route('/', methods=['GET', 'POST'])
def index():
    stock_summary = None

    if request.method == 'POST':
        ticker = request.form['ticker'].upper()

        try:
            # Fetch stock data for last 5 days to ensure we get at least 3 trading days
            end_date = datetime.now().date()
            start_date = end_date - timedelta(days=5)

            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)

            # Get last 3 trading days
            last_3_days = hist.tail(3)

            # Format into a readable string
            summary_text = f"Stock data for {ticker} (last 3 days):<br><br>"
            for date, row in last_3_days.iterrows():
                summary_text += f"{date.date()} - Open: {row['Open']:.2f}, High: {row['High']:.2f}, Low: {row['Low']:.2f}, Close: {row['Close']:.2f}, Volume: {int(row['Volume'])}<br>"

            # Send formatted stock data to OpenAI for summary
            prompt = f"Here is the stock data for {ticker} from the last 3 days:\n{summary_text}\n\nPlease summarize the stock's performance in a few sentences."

            client = client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )

            # Extract the response text
            ai_summary = response.text

            # Display both raw data and AI summary
            stock_summary = f"{summary_text}<br><br><strong>AI Summary:</strong><br>{ai_summary}"

        except Exception as e:
            stock_summary = f"Error fetching data for {ticker}: {e}"

    return render_template('index.html', summary=stock_summary)

# Run the app (only if this script is run directly, not imported)
if __name__ == '__main__':
    app.run(debug=True)
