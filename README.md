# Weather-Based Order Tracking System 🌦️📦

## Overview

This project is an automated system that checks weather conditions for delivery locations and flags potential delays. It uses asynchronous API calls and displays results in a dynamic dashboard.

---

## Features

* ⚡ Parallel API calls using asyncio
* 🌧️ Weather-based delay detection
* ❌ Error handling for invalid cities
* 🤖 AI-style apology message generation
* 📊 Interactive dashboard with charts
* 🔍 Search and filter functionality

---

## Tech Stack

* Python (asyncio, aiohttp)
* OpenWeatherMap API
* HTML, CSS, JavaScript
* Chart.js

---

## How to Run

### Backend

```bash
pip install -r requirements.txt
python main.py
```

### Frontend

* Open `ui/index.html` using Live Server

---

## Sample Output

* Orders marked as **Delayed** if weather conditions are severe
* Dashboard shows real-time insights

---

## AI Log

* Used prompts to generate async logic and apology messages
