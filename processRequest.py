# Function that takes in 1 argument.
# It will print the content from that request.
# It will return a dictionary containg the key:value pairs (role and content) inorder to keep the AI assistant up to date with the user's prompts.
# This is known as system prompting.
# The AI tool will be able to keep up with the ongoing context or instructions of the user's prompts.
def process_request(request):
    message = request.choices[0].message
    print(message.content, "\n")

    return {
        "role" : message.role,
        "content" : message.content
    }