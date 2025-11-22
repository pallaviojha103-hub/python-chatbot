'''import openai  

openai.api_key="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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )  

    return response.choices[0].message.content.strip() 

if __name__=="__main__":
    while True: 
        user_input=input("you: ")
        if user_input.lower() in ["quit","exit","bye"]:
            break

        response  = chat_with_gpt(user_input) 
        print("chatbot: ", response)'''



    
