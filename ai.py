from google import genai

client = genai.Client(api_key="AIzaSyBGIqjFQn8TxQ0u3tD0vVkugbcjMbo6jas")

def get_ai_response(user_input):
    prompt = f"""
You are a smart recommendation AI.

User question: {user_input}

Give helpful, short, clear recommendations.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text