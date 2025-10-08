import requests
import folium
import webbrowser

def get_ip_location():
    try:
        # Fetch geolocation data using a free API
        response = requests.get("https://ipapi.co/json/")
        data = response.json()

        # Extract relevant fields
        ip = data.get("ip", "N/A")
        city = data.get("city", "N/A")
        region = data.get("region", "N/A")
        country = data.get("country_name", "N/A")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        print(f"📍 IP Address: {ip}")
        print(f"🏙️  Location: {city}, {region}, {country}")
        print(f"🌐 Coordinates: ({latitude}, {longitude})")

        return latitude, longitude, city, region, country

    except Exception as e:
        print("Error fetching location:", e)
        return None, None, None, None, None


def show_location_on_map(lat, lon, city, region, country):
    if lat is None or lon is None:
        print("Could not determine location.")
        return

    # Create a folium map centered on user's location
    user_map = folium.Map(location=[lat, lon], zoom_start=10)

    # Add a marker
    folium.Marker(
        [lat, lon],
        popup=f"{city}, {region}, {country}",
        tooltip="You are here 📍",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(user_map)

    # Save map to an HTML file
    map_file = "user_location_map.html"
    user_map.save(map_file)

    # Open map in browser
    print(f"🗺️  Map generated: {map_file}")
    webbrowser.open(map_file)


if __name__ == "__main__":
    lat, lon, city, region, country = get_ip_location()
    show_location_on_map(lat, lon, city, region, country)
