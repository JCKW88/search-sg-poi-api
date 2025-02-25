# Search Singapore Place of Interest (POI) API

## Overview
This API accepts a query string (i.e. 'q' as the parameter) containing specific requirements (e.g. "Muslim Friendly Salon", "Birthday Party Venues for children", "Fusion Peranakan Cuisine places") and returns a list of relevant results in JSON.

## Installation
To set up the project, clone the repository and install the required dependencies:

Flask==2.0.0
Werkzeug==2.0.0
flask_restful==0.3.10
python-dotenv==1.0.1
google-generativeai==0.8.4
requests==2.32.3

## Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| GEMINI_API_KEY | API key for Google's Gemini AI service. Obtain from Google AI Studio (https://aistudio.google.com/) | [AIzaSyB4J...] |
| GEMINI_MODEL_NAME | The name of the Gemini model to use | [gemini-2.0-flash] |

## API Usage
Using GET method (example):

    https://127.0.0.1:5000/api/search_sg_poi?q="hainan chicken rice"
