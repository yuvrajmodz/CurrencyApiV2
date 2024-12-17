# Developed By @YUVRAJMODZ [𝐌𝐀𝐓𝐑𝐈𝐗] 

# Currency Conversion API

This Flask API allows users to convert currency values between US dollars (USD) and Indian Rupees (INR) using web scraping techniques to fetch real-time conversion rates from Google.

## Features

- Convert from USD to INR or INR to USD.
- Simple JSON response with conversion results.

## Endpoints

### `GET /api`

#### Query Parameters
- `usd`: Amount in US dollars to convert to Indian Rupees.
- `inr`: Amount in Indian Rupees to convert to US dollars.

#### Example Requests
- To convert USD to INR:

#### Example Endpoint Request

### /api?usd=200

### /api?inr=200




#### Example Response

```json
{
  "input_amount": "100",
  "converted_value": "7500",
  "currency": "INR"
}