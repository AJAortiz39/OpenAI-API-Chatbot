# Importing class OpenAI from module openai 
from openai import OpenAI 
# Importing function process_request from processRequest file
from processRequest import process_request

def main():
    # Instantiate object client using the OpenAI class
    # Typically the API key will go inside OpenAI()
    # Please set up your API key enviornment variable
    # For setting up an API key Enviornment variable visit https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
    client = OpenAI()

    # Setting chat variable to True to initiate while loop in code below
    chat = True
    # Taking in user prompt into variable user_prompt
    user_prompt = input("Please enter your prompt: ")
    print("\n")
    # List that contains and will continue to contain dictionaries of our 'message' argument inorder to continue to chat with openai
    saved_messages = [
        {
            "role" : "user",
            "content" : user_prompt
        }
    ]

    # While loop that will take the user's prompt, display the content of the message and append the assistant role and assistant's response to saved_messages by utilizing the process_request function
    # OpenAI will continue to take prompts until the user decides.(using if statements to check user's response)
    while chat == True:
        response = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages = saved_messages
        )
        saved_messages.append(process_request(response))
        chat_continuation = input("Would you like to continue? (Y/N) : ")
        print("\n")
        if str(chat_continuation.lower()) == 'n' :
            print("Thank you for visiting, GoodBye")
            chat = False
        elif str(chat_continuation.lower()) != 'n' and str(chat_continuation.lower()) != 'y' :
            print("Sorry, incorrect input, ending program.")
            chat = False
        elif str(chat_continuation.lower()) == 'y':
            user_prompt = input("Please enter your next prompt, OpenAI has retained your last prompt in order to better serve you. : ")
            print("\n")
            saved_messages.append({"role":"user", "content":user_prompt})



if __name__ == "__main__":
    main()