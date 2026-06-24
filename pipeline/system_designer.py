import json
from pipeline.gemini_client import generate

def design_system(intent):

    prompt = f"""
You are a Software Architect.

Convert this application intent into a software architecture.

Return ONLY valid JSON.

Format:

{{
    "pages": [],
    "tables": [],
    "apis": [],
    "workflows": []
}}

Intent:

{json.dumps(intent, indent=2)}
"""

    response = generate(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "")

    return json.loads(response)