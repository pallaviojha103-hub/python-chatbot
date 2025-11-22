import openai  

openai.api_key="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"
def chat_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )  

    return response.choices[0].message.content.strip() 

if __name__=="__main__":
    while True: 
        input_user=input("you: ")
        if input_user.lower() in ["quit","exit","bye"]:
            break

        response  = chat_bot(input_user) 
        print("chatbot: ", response)



    
