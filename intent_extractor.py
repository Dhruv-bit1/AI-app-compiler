import json
from pipeline.gemini_client import generate

def extract_intent(user_prompt):

    prompt = f"""
You are an Intent Extraction Engine.

Convert the following software requirement into JSON.

Return ONLY valid JSON.

Format:

{{
    "app_name": "",
    "features": [],
    "roles": [],
    "entities": [],
    "business_rules": []
}}

Requirement:

{user_prompt}
"""

    response = generate(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")

    return json.loads(response)