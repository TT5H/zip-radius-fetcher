import tkinter as tk
from tkinter import messagebox, filedialog
import pandas as pd
import requests
import pgeocode
import openpyxl  
import geopy.distance  
from geopy.geocoders import Nominatim
import folium  # For creating maps

# Function to get latitude and longitude using Google Maps API
def get_lat_long_from_address(address, google_api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            messagebox.showerror("Error", f"No results found for the address: {address}")
    else:
        messagebox.showerror("Error", f"Error fetching data from Google API: {response.status_code}")
    return None, None

# Function to get zip codes within a radius using pgeocode
def get_zip_codes_within_radius(lat, lng, radius_km):
    nomi = Nominatim(user_agent="my_geocoder")

    # Get the location details using reverse geocoding
    location = nomi.reverse((lat, lng), exactly_one=True)

    if location is None or 'postcode' not in location.raw['address']:
        messagebox.showerror("Error", "Could not find postal code for the given latitude and longitude.")
        return []

    current_postal_code = location.raw['address']['postcode']  # Extract postal code
    geo_locator = pgeocode.Nominatim('us')

    # Get the current postal code latitude and longitude
    current_zip_info = geo_locator.query_postal_code(current_postal_code)

    if current_zip_info is None or current_zip_info.empty:
        messagebox.showerror("Error", "Could not find information for the current postal code.")
        return []

    current_lat = current_zip_info.latitude
    current_lng = current_zip_info.longitude

    if pd.isna(current_lat) or pd.isna(current_lng):
        messagebox.showerror("Error", "Invalid coordinates for current postal code.")
        return []

    nearby_zip_codes = []
    for postal_code in range(90001, 96162):  # Adjust range based on postal codes in your area
        postal_data = geo_locator.query_postal_code(postal_code)

        if postal_data is not None and not postal_data.empty:
            postal_lat = postal_data.latitude
            postal_lng = postal_data.longitude

            if pd.isna(postal_lat) or pd.isna(postal_lng):
                continue

            distance = geopy.distance.distance((current_lat, current_lng), (postal_lat, postal_lng)).km
            if distance <= radius_km:
                nearby_zip_codes.append(postal_code)

    return nearby_zip_codes

# Function to create a map with a radius circle
def create_map_with_radius(lat, lng, radius_km, address):
    map_center = [lat, lng]
    m = folium.Map(location=map_center, zoom_start=12)

    folium.Circle(
        location=map_center,
        radius=radius_km * 1000,  # Radius in meters
        color='blue',
        fill=True,
        fill_opacity=0.3,
        popup=f'{radius_km} km radius around {address}'
    ).add_to(m)

    folium.Marker(location=map_center, tooltip=address).add_to(m)

    map_file = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
    if map_file:
        m.save(map_file)
        messagebox.showinfo("Success", f"Map with radius saved as {map_file}")

# Function to save results to a file
def save_results(addresses_results):
    file_format = format_var.get()
    filename = filedialog.asksaveasfilename(defaultextension=f".{file_format}", filetypes=[(f"{file_format.upper()} files", f"*.{file_format}")])
    if file_format == "txt":
        with open(filename, 'w') as file:
            for address, zip_codes in addresses_results.items():
                file.write(f"{address}: {zip_codes}\n")
        messagebox.showinfo("Success", f"Results saved to {filename}")
    elif file_format == "xlsx":
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Address", "Nearby Zip Codes"])
        for address, zip_codes in addresses_results.items():
            sheet.append([address, ", ".join(map(str, zip_codes))])
        workbook.save(filename)
        messagebox.showinfo("Success", f"Results saved to {filename}")


def process_address():
    address = address_entry.get()
    radius_km = int(radius_entry.get())
    google_api_key = api_key_entry.get()

    lat, lng = get_lat_long_from_address(address, google_api_key)
    if lat and lng:
        nearby_zip_codes = get_zip_codes_within_radius(lat, lng, radius_km)
        addresses_results = {address: nearby_zip_codes}

        create_map_with_radius(lat, lng, radius_km, address)

        save_option = messagebox.askyesno("Save Results", "Do you want to save the results?")
        if save_option:
            save_results(addresses_results)

# GUI
app = tk.Tk()
app.title("Zip Radius Fetcher")

tk.Label(app, text="Google API Key:").grid(row=0, column=0)
api_key_entry = tk.Entry(app, width=50)
api_key_entry.grid(row=0, column=1)

tk.Label(app, text="Address:").grid(row=1, column=0)
address_entry = tk.Entry(app, width=50)
address_entry.grid(row=1, column=1)

tk.Label(app, text="Radius (km):").grid(row=2, column=0)
radius_entry = tk.Entry(app, width=50)
radius_entry.grid(row=2, column=1)

tk.Button(app, text="Fetch Zip Codes", command=process_address).grid(row=3, column=1)

# Dropdown for save file format
format_var = tk.StringVar(app)
format_var.set("txt")  # Default value
tk.Label(app, text="Save Format:").grid(row=4, column=0)
tk.OptionMenu(app, format_var, "txt", "xlsx").grid(row=4, column=1)

app.mainloop()
