from flask import Flask, request
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/")
def home():
    # Google App Engine provides user email in headers
    user_email = request.headers.get("X-Appengine-User-Email", "Guest")

    # Get timezone (example: based on user preference or default)
    timezone_name = "Asia/Kolkata"
    timezone = pytz.timezone(timezone_name)

    current_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <h2>Google Account Based Clock</h2>
    <p><b>User:</b> {user_email}</p>
    <p><b>Time Zone:</b> {timezone_name}</p>
    <p><b>Current Time:</b> {current_time}</p>
    """

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
