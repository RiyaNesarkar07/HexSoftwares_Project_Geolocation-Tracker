# 🌍 Geolocation Tracker using Python

A simple Python project that fetches your **geolocation using your IP address** and displays it on an **interactive map**.

---

## 🧭 Features
- Detects your **public IP address** automatically.
- Fetches **city, region, country, latitude, and longitude**.
- Displays your location on an interactive map using **Folium (Leaflet.js)**.
- Opens the map automatically in your default browser.

---

## 🛠️ Technologies Used
- **Python 3**
- **Requests** (for API call)
- **Folium** (for map visualization)
- **ipapi.co** (free IP geolocation API)

---

## 📦 Installation

1. Clone this repository or download the script:
   ```bash
   git clone https://github.com/yourusername/geolocation-tracker.git
   cd geolocation-tracker
   
2. Install the required Python libraries:
   '''bash
   pip install requests folium
   
# ▶️ Usage

Run the script:
python geolocation_tracker.py


# Example Output:

📍 IP Address: 106.203.18.47
🏙️  Location: Pune, Maharashtra, India
🌐 Coordinates: (18.5204, 73.8567)
🗺️  Map generated: user_location_map.html


The map will automatically open in your default web browser showing your location.


# 📄 Code Overview

import requests
import folium
import webbrowser
Fetches IP-based geolocation from ipapi.co
Extracts latitude, longitude, and address details.
Creates a Folium map centered at your coordinates.
Saves the map as an HTML file and opens it automatically.

# 🧩 Example Map

When you run the script, a file user_location_map.html will be created and opened automatically in your browser:

📍 Marker: Your detected city
🗺️ Map: Interactive (zoom in/out, move around)

# 🧠 Learning Highlights

Working with APIs in Python
Handling JSON data
Integrating visualization using Folium
Real-world application of IP-based geolocation

