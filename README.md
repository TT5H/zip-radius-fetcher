# Zip Radius Fetcher

Welcome to the **Zip Radius Fetcher** project! This Python application allows you to fetch nearby zip codes based on given addresses within a specified radius. You can choose the radius in various units (kilometers, miles, or meters) and save the results to a text file or Excel sheet.

## Features

- **Fetch Latitude and Longitude**: Uses the Google Maps API to convert addresses into geographical coordinates.
- **Zip Code Retrieval**: Retrieves nearby zip codes within a specified radius using the `pgeocode` library.
- **Multiple Address Support**: Input multiple addresses to retrieve zip codes for all of them.
- **Flexible Radius Units**: Choose the radius in kilometers, miles, or meters.
- **Save Results**: Save the results to a plain text file or an Excel spreadsheet.
- **User Control Options**: Pause or stop the process at any time during execution.

## Requirements

Before running the application, make sure you have the following:

- Python 3.x installed on your machine.
- An active Google Maps API key. (Replace `YOUR_GOOGLE_API_KEY` in the code with your actual API key.)
- Required Python libraries: `requests`, `pgeocode`, and `openpyxl`.

You can install the required libraries using pip:

```bash
pip install requests pgeocode openpyxl
```

## How to Use

1. Clone the repository or download the source code.
2. Open the `app.py` file and replace `YOUR_GOOGLE_API_KEY` with your actual Google Maps API key.
3. Run the application:

   ```bash
   python app.py
   ```

4. Follow the prompts to:
   - Enter the radius for searching (e.g., 5 for 5 kilometers).
   - Choose the unit for the radius (km for kilometers, mi for miles, m for meters).
   - Input the addresses (type 'done' when finished).
   - Optionally pause, stop, or save the results.

5. Check the output file for the zip codes retrieved.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please create a pull request.

## Acknowledgements

- [Google Maps API](https://developers.google.com/maps/documentation/geocoding/start)
- [pgeocode](https://pypi.org/project/pgeocode/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

If you find this project helpful, please consider starring it on GitHub!
