import json
from pipeline.gemini_client import generate

def generate_schema(design):

    prompt = f"""
You are a Schema Generation Engine.

Convert the following architecture into JSON schemas.

Return ONLY valid JSON.

Format:

{{
    "ui_schema": {{}},
    "api_schema": {{}},
    "db_schema": {{}},
    "auth_schema": {{}}
}}

Architecture:

{json.dumps(design, indent=2)}
"""

    response = generate(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")

    return json.loads(response)