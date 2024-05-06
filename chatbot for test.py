import gradio

from openai import OpenAI

client = OpenAI(api_key="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")

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]


def CustomChatGPT(user_input):
    messages.append({"role":"user","content":user_input})

    response= client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    stream=True,
    )
#
    chat_gpt_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": chat_gpt_reply})

    return chat_gpt_reply

#
demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)






