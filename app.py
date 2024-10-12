import requests
import pgeocode
import time
import openpyxl 
import os

def get_lat_long_from_address(address, google_api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={google_api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"No results found for the address: {address}")
    else:
        print(f"Error fetching data from Google API: {response.status_code}")
    return None, None


def get_zip_codes_within_radius(lat, lng, radius_km):
    nomi = pgeocode.Nominatim('us')  # country code for the USA
    zip_codes = nomi.query_postal_code_radius(lat, lng, radius_km)
    return zip_codes['postal_code']

def save_results(addresses_results, filename="results.txt", format="txt"):
    if format == "txt":
        with open(filename, 'w') as file:
            for address, zip_codes in addresses_results.items():
                file.write(f"{address}: {zip_codes}\n")
        print(f"Results saved to {filename}")
    elif format == "xlsx":
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(["Address", "Nearby Zip Codes"])
        for address, zip_codes in addresses_results.items():
            sheet.append([address, ", ".join(zip_codes)])
        workbook.save(filename)
        print(f"Results saved to {filename}")

def main():
    print("Welcome to the Zip Radius Fetcher!")
    print("If you find this project helpful, please consider starring it on GitHub!")
    
    google_api_key = "YOUR_GOOGLE_API_KEY"  # your Google API key
    
    radius = float(input("Enter the radius for searching (e.g., 5 for 5 kilometers): "))
    unit = input("Choose the unit for radius (km for kilometers, mi for miles, m for meters): ").lower()
    
    if unit == 'km':
        radius_km = radius
    elif unit == 'mi':
        radius_km = radius * 1.60934 
    elif unit == 'm':
        radius_km = radius / 1000  
    else:
        print("Invalid unit selected. Defaulting to kilometers.")
        radius_km = radius
    
    addresses = []
    addresses_results = {}
    

    while True:
        address = input("Enter an address (or type 'done' to finish): ")
        if address.lower() == 'done':
            break
        addresses.append(address)

    remaining_requests = 20000  # Google API quota (adjust based on your limits)
    
    for address in addresses:
        if remaining_requests <= 0:
            print("API request limit reached.")
            break
        

        lat, lng = get_lat_long_from_address(address, google_api_key)

        if lat and lng:
            print(f"Latitude: {lat}, Longitude: {lng}")
            nearby_zip_codes = get_zip_codes_within_radius(lat, lng, radius_km)
            if nearby_zip_codes is not None:
                addresses_results[address] = nearby_zip_codes
                print(f"Nearby zip codes within {radius_km} km: {nearby_zip_codes}")
            else:
                addresses_results[address] = []
            remaining_requests -= 1
            print(f"Remaining API calls: {remaining_requests}")
        else:
            addresses_results[address] = []

        # pause or stop
        option = input("Enter 'p' to pause, 's' to stop, or press Enter to continue: ")
        if option.lower() == 'p':
            input("Paused. Press Enter to continue.")
        elif option.lower() == 's':
            print("Stopping the process.")
            break
    
    # Save results
    save_option = input("Do you want to save the results? (y/n): ")
    if save_option.lower() == 'y':
        file_format = input("Enter file format (txt/xlsx): ").lower()
        filename = f"results.{file_format}"
        save_results(addresses_results, filename=filename, format=file_format)
    else:
        print("Results were not saved.")

if __name__ == "__main__":
    main()
