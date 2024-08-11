import google.generativeai as genai

API_KEY = "AIzaSyA7IzBS4cqt3xGsOKmxOYz8JGZ0pTPTpsI"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

user_input = input("Enter Your Prompt = ")
output = getResponseFromModel(user_input)
print(output)
