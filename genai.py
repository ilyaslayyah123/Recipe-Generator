import requests
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = "tgp_v1_kpN6r1tNqgrVrwosftbD3PSwnjx-DjVeNnaVCbKwF3k"  

headers = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

def recip(ingredients, preference="vegetarian"):
    prompt = (
        f"You are a professional chef.\n"
        f"Create a new {preference} recipe using the following ingredients: {ingredients}.\n"
        f"Include:\n"
        f"- Recipe Name\n"
        f"- List of Ingredients\n"
        f"- Step-by-step Cooking Instructions\n\n"
        f"Make the recipe detailed and delicious!"
    )

    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful recipe generator."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(TOGETHER_API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"API Error: {e}"
    except KeyError:
        return "Unexpected response format from API."
