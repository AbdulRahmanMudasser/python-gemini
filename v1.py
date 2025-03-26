import google.generativeai as genai
from config import API_KEY

# Configure the API key
genai.configure(api_key=API_KEY)

def main():
    # Initialize the model (using Gemini Pro)
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    print("Welcome to Gemini Chat!")
    print("Type 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            response = model.generate_content(user_input)
            print("\nGemini:", response.text, "\n")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()