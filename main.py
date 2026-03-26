import asyncio
import aiohttp
import os
import json
from dotenv import load_dotenv

print("✅ Imports working fine")

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")


# Async function to fetch weather
async def fetch_weather(session, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        async with session.get(url) as response:
            data = await response.json()

            if response.status != 200:
                raise Exception(data.get("message", "Error"))

            weather = data["weather"][0]["main"]
            return weather

    except Exception as e:
        print(f"❌ Error fetching {city}: {e}")
        return None


# ✅ AI-style apology function (OUTSIDE loop)
def generate_apology(customer, city, weather):
    return f"Hi {customer}, we regret to inform you that your delivery to {city} is delayed due to {weather.lower()} conditions. Thank you for your patience and understanding."


# Main processing function
async def process_orders():
    # Read orders.json
    with open("orders.json", "r") as f:
        orders = json.load(f)

    async with aiohttp.ClientSession() as session:
        tasks = []

        # Create async tasks
        for order in orders:
            city = order["city"]
            tasks.append(fetch_weather(session, city))

        # Run all API calls in parallel
        results = await asyncio.gather(*tasks)

    # Apply logic
    for order, weather in zip(orders, results):

        # Add weather
        order["weather"] = weather

        # Check delay condition
        if weather in ["Rain", "Snow", "Extreme","Clouds"]:
            order["status"] = "Delayed"

            message = generate_apology(order["customer"], order["city"], weather)
            order["message"] = message

            print(f"⚠️ {message}")

        else:
            order["message"] = "No delay expected"

        # Extra logging (optional but good)
        print(f"📦 Order {order['order_id']} → {order['status']}")

    # Save updated JSON
    with open("updated_orders.json", "w") as f:
        json.dump(orders, f, indent=2)

    print("\n✅ Updated orders saved to updated_orders.json")


# Run the program
asyncio.run(process_orders())