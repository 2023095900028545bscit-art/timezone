pip install pytz
from datetime import datetime
import pytz

# Choose location
timezone = pytz.timezone("Asia/Kolkata")   # India
# timezone = pytz.timezone("America/New_York")  # USA

current_time = datetime.now(timezone)

print("Current Time:", current_time.strftime("%H:%M:%S"))
