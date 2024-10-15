
# Zip Radius Fetcher

Zip Radius Fetcher is a Python-based tool that allows users to fetch nearby zip codes within a given radius from a specified address. The program uses the Google Maps API for geocoding and pgeocode for postal code data. Additionally, the application creates an interactive map showing the specified radius around the address using Folium.

<div align="center">
    <img src="https://i.imgur.com/vwqNI8O.png" alt="Zip Fetcher Image" />
</div>

## Features

- Fetch latitude and longitude of an address using Google Maps API.
- Calculate nearby postal codes within a specified radius using pgeocode.
- Visualize the search area and nearby zip codes with an interactive map using Folium.
- Save the map and results in multiple formats: `.html` for maps, `.txt` or `.xlsx` for zip code results.
- Easy-to-use Graphical User Interface (GUI) built with `tkinter`.

### Prerequisites

- **Python 3.6+**: Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- **Google Maps Geocoding API Key**: To use this project, you will need a Google Maps API key with the Geocoding API enabled.

  #### Steps to enable and secure your API key:

  1. **Get a Google Cloud account**: If you don't have one, sign up at [Google Cloud Console](https://console.cloud.google.com/).
  2. **Create a new project**: Once logged in, create a new project or select an existing one.
  3. **Enable the Geocoding API**:
     - Go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard).
     - Click on `+ Enable APIs and Services`.
     - Search for "Geocoding API" and enable it for your project.
  4. **Create API credentials**:
     - Go to the [Credentials](https://console.cloud.google.com/apis/credentials) page and click on `+ Create Credentials`.
     - Choose **API key**.
     - Copy the API key that gets generated.
  5. **Set restrictions on the API key** (optional but recommended):
     - On the Credentials page, click on the **API key** you just created.
     - Under "Application restrictions," choose the appropriate restriction:
       - **HTTP referrers (websites)**: If you're using the key for a web application, specify the URLs where the key can be used.
       - **IP addresses**: If you're using it for a backend service, restrict it to specific IP addresses that will call the API.
     - Under "API restrictions," select **Geocoding API** to limit the key to this API only.

For more information, refer to the [Google API documentation](https://developers.google.com/maps/gmp-get-started).


### Python Packages

You'll need to install the following Python libraries to run this project:

```bash
pip install requests pgeocode geopy folium openpyxl pandas tkinter
```

## How to Use

1. Clone or download this repository to your local machine.
2. Install the required dependencies by either:
   - Running the command `pip install -r requirements.txt`, or
   - Running the provided `install_requirements.bat` file for automatic setup.
3. Run the script:
   - A graphical interface will pop up with the following fields:
     - **Google API Key**: Enter your Google Maps API key with Geocoding enabled.
     - **Address**: Enter the address for which you want to fetch nearby zip codes.
     - **Radius (km)**: Specify the radius in kilometers to search for nearby zip codes.
     - **Save Format**: Choose whether to save the results as a `.txt` or `.xlsx` file.
4. Click the **Fetch Zip Codes** button:
   - The program will fetch the latitude and longitude of the given address.
   - It will then calculate zip codes within the specified radius.
   - The results can be saved to a file, and a map with the radius will be generated and saved as an HTML file.


### Steps to Follow:

1. Enter your Google Maps API key.
2. Input the address and radius (in kilometers).
3. Click on `Fetch Zip Codes` to start the process.
4. The tool will display the nearby zip codes and create a radius map.
5. You can choose to save the results as `.txt` or `.xlsx`.

## Example

1. Input: `123 Main St, New York, NY` with a radius of `50 km`
2. Output: A list of zip codes within 50 km of the input address, and an interactive map showing the radius.

## Files

- `main.py`: The main Python file with all the logic and the GUI.
- `requirements.txt`: A list of required Python packages for easy setup.
- `install_requirements.bat`: A batch script to automatically install the required dependencies from `requirements.txt`.
- `README.md`: Project documentation with setup and usage instructions.
- `map_with_radius.html`: Generated map file showing the address and the radius, saved by the script (this is created after running the script).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

If you find this tool useful, consider starring it on GitHub!

## License

This project is licensed under the MIT License.
