#functia ce alege contextul ai ului in functie de optiune
def context_social(varianta,input1, input2, input3, input4, input5, input6,nr_tokens):
    raspuns_context_ai=''
    raspuns_context_user = ''
    eroare_context=''
    if varianta =='Caption':
        raspuns_context_ai = 'You are a profesional social media Captions text generator.'
        raspuns_context_user='Write a social media caption with hashtags with main ideea '+input1+' which contain following details: '+input2+', '+input3+', '+input4+'. Generate the phrase with '+nr_tokens+' words'
    elif varianta == 'Bio':
        raspuns_context_ai = 'You are a profesional social media Bio text generator.'
        raspuns_context_user = 'Write a social media Bio caption without hashtags with main ideea '+input1+' which contain following details: '+input2+', '+input3+', '+input4+' Generate the phrase with '+nr_tokens+' words'
    elif varianta == 'Testimonial':
        raspuns_context_ai = 'You are a profesional social media testimonial text generator. Like exemple: Happy handwritten thank you notes… I just wanted to let you know that it is been great working with you.'
        raspuns_context_user ='Write a social media testimonial text on subject '+input1+' user liked this company or this services provider beacause '+input2+' '+input3+'. Generate the phrase with '+nr_tokens+' words'
    elif varianta == 'Tips & Tricks':
        raspuns_context_ai = 'You are a profesional Tips & Tricks text generator.'
        raspuns_context_user = 'Give me one cool tips & Tricks about '+input1
    elif varianta == 'Giveaway':
        raspuns_context_ai = 'You are a profesional social media Giveaway text generator.'
        raspuns_context_user = 'Write an text for a Giveaway available '+input4+' for product: '+input1+' organized by: '+input2+' the product have following characteristics: '+input3+' conditions of participation '+input5+' the winner will be chose '+input6
    elif varianta == 'Collaboration message':
        raspuns_context_ai = 'You are a profesional social media Collaboration message generator.'
        raspuns_context_user = 'Write for me, my name is: '+input2+' and i represent company: '+input4+ 'a formal collaboration text, to the recipient '+input1+' the purpose of the collaboration: '+input3
    else:
        eroare_context= 'Nu sa ales o varianta valida'
        raspuns_context_ai= 'Explain to the user that he doesnt chose an option'
    return raspuns_context_ai, raspuns_context_user, eroare_context

# varianta='Caption'
# rezult,err=context_chose(varianta)
# print(rezult,err)
