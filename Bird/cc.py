import openai
openai.api_key = "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"

def generate_response(user_query):
    prompt = "User: {}\nChatbot:".format(user_query)
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        
    )  
    chatbot_response = generate_response(user_query)
    print(chatbot_response)
    return response.choices[0].text.strip()
