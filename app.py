from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Api Developed by @YuvrajMODZ

@app.route('/api', methods=['GET'])
def currency_conversion():
    # Check if 'dollar' or 'inr' parameter is provided
    dollar_amount = request.args.get('usd')
    inr_amount = request.args.get('inr')
    
    if dollar_amount:
        # Construct the Google search URL for dollar to INR conversion
        search_url = f"https://www.google.com/search?q={dollar_amount}+dollar+to+inr"
    elif inr_amount:
        # Construct the Google search URL for INR to dollar conversion
        search_url = f"https://www.google.com/search?q={inr_amount}+inr+to+dollar"
    else:
        return jsonify({"error": "Either 'dollar' or 'inr' parameter is required"}), 400
    
    # Make a request to the Google search URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    
    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    try:
        # Find the data values in the specific tags
        data = soup.select_one("span.DFlfde.SwHCTb").text
        formatdata = soup.select_one("span.MWvIVe").text
        
        # Return the data in JSON format
        return jsonify({
            "input_amount": dollar_amount if dollar_amount else inr_amount,
            "converted_value": data,
            "currency": formatdata
        })
    except AttributeError:
        # Handle cases where the conversion data isn't found
        return jsonify({"error": "Could not retrieve conversion data"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5030))
    app.run(host='0.0.0.0', port=port, debug=True)