import gradio as gr
import openai
from refrazat import rearanjare

#creierul
def contacteaza_ai(input1, input2, input3, input4, input5, input6, varianta,nr_tokens):
    from Alegere_Context import context_social
    #se alege contextul care va fi radacina case-ului
    context_ales_ai, context_ales_user, error_ch = context_social(varianta,input1, input2, input3, input4, input5, input6,nr_tokens)
    #de criptat key-ul
    openai.api_key = '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'
    message_history = [{"role": "user",
                        "content": context_ales_ai},
                       {"role": "assistant", "content": f"OK"}, {"role": "user",
                                                                 "content": f"{context_ales_user}"}]
    completion = openai.ChatCompletion.create \
            (
            model="gpt-3.5-turbo",
            messages=message_history
            )
    reply_content = completion.choices[0].message.content
    # print(reply_content)
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    response = [(message_history[i]["content"], message_history[i + 1]["content"])
                for i in range(2, len(message_history) - 1, 2)]  # convert to tuples of list
    #il trimitem in refrazare
    #reply_refrazat=rearanjare(reply_content)
    return reply_content, error_ch
