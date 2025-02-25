import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    enum = [],
    required = ["Search Results"],
    properties = {
      "Search Results": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.OBJECT,
          enum = [],
          required = ["Name", "Address", "Opening Hours", "Description", "Top Offerings", "Contact Number", "Images", "Sources"],
          properties = {
            "Name": content.Schema(
              type = content.Type.STRING,
            ),
            "Address": content.Schema(
              type = content.Type.STRING,
            ),
            "Opening Hours": content.Schema(
              type = content.Type.ARRAY,
              items = content.Schema(
                type = content.Type.OBJECT,
                enum = [],
                required = ["Day of Week", "Operating Hours"],
                properties = {
                  "Day of Week": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "Operating Hours": content.Schema(
                    type = content.Type.STRING,
                  ),
                },
              ),
            ),
            "Description": content.Schema(
              type = content.Type.STRING,
            ),
            "Top Offerings": content.Schema(
              type = content.Type.ARRAY,
              items = content.Schema(
                type = content.Type.OBJECT,
                enum = [],
                required = ["Offering", "Price"],
                properties = {
                  "Offering": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "Price": content.Schema(
                    type = content.Type.NUMBER,
                  ),
                },
              ),
            ),
            "Contact Number": content.Schema(
              type = content.Type.STRING,
            ),
            "Images": content.Schema(
              type = content.Type.ARRAY,
              items = content.Schema(
                type = content.Type.OBJECT,
                enum = [],
                required = ["Name"],
                properties = {
                  "Name": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                      type = content.Type.OBJECT,
                      enum = [],
                      required = ["URL", "Caption", "Hashtags"],
                      properties = {
                        "URL": content.Schema(
                          type = content.Type.STRING,
                        ),
                        "Caption": content.Schema(
                          type = content.Type.STRING,
                        ),
                        "Hashtags": content.Schema(
                          type = content.Type.STRING,
                        ),
                      },
                    ),
                  ),
                },
              ),
            ),
            "Sources": content.Schema(
              type = content.Type.ARRAY,
              items = content.Schema(
                type = content.Type.OBJECT,
                enum = [],
                required = ["Page Title", "URL"],
                properties = {
                  "Page Title": content.Schema(
                    type = content.Type.STRING,
                  ),
                  "URL": content.Schema(
                    type = content.Type.STRING,
                  ),
                },
              ),
            ),
          },
        ),
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name=os.getenv("GEMINI_MODEL_NAME"),
  generation_config=generation_config,      
  system_instruction="You are an experienced local guide in Singapore. Your task is to provide recommendations based on user requests for activities or places to visit. Please adhere to the following guidelines:\n\n1. Provide a list of recommended places or activities based on the user's input.\n2. Present the information in a structured JSON format and adhered to the following fields specification:\n- Name of the shop, place, or event.\n- Physical location address. For multiple locations, provide the one closest to central Singapore.\n- Opening hours in the 2400 format, structured as {\"Mon\": \"<start>-<end>\", ..., \"Sun\": \"<start>-<end>\"}. \n- Description of the location or event with the length between 350-400 characters.\n- Contact number in +65-XXXX-XXXX format (indicate as N/A if information not available).\n- Image url (indicate as N/A if information not available).\n- Image caption is <= 70 words, matching tone of official Singapore tourism website.\n- Hashtags related to the place of interest.\n- Sources of information including page title and URL.\n\n3. Ensure all information is factual and up-to-date. Do not generate fictitious information if information unavailable.\n4. Provide 3-5 recommendations per user request.",
)

chat_session = model.start_chat(
  history=[]
)

response = chat_session.send_message("laksa")

print(response.text)