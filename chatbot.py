
import datetime
import time

name= input("Welcome, Enter your name :")
presentHour= datetime.datetime.now().hour

if 5<= presentHour <=12:
    print("Good morning", name)
elif 12<= presentHour <=16:
    print("Good afternoon", name)
else:
    print("Good evening", name)




print("\nHELLO! Welcome to NayePankh Foundation Chat Assistant")
print("How can I help you?,Type bye to exit")

responses = {

    "hello":"Hi, How can I help you?",

    "What is NayePankh Foundation?":"NayePankh Foundation is an non profitable NGO working for social welfare.",
    
    "What does NayePankh do?":"It supports education, healthcare, food, and basic needs.",
    
    "When was NayePankh started?":"It started in 2021.",
    
    "How can I volunteer?":"You can join as a volunteer through the NGO website.",
    
    "Can students volunteer?":"Yes, students can volunteer.",
    
    "How can I donate?":"You can donate through the official website.",
    
    "Does NayePankh provide education support?":" Yes, it supports education.",
    
    "Does NayePankh distribute food?":"Yes, it provides food support.",
    
    "Does NayePankh help women?":"Yes, through awareness and support programs.",
    
    "Can I donate clothes?":"Yes, useful items can be donated.",
    
    "Do you provide certificates?":"Volunteer certificates may be provided.",
    
    "How can I contact NayePankh?":"Contact details are available on the website.",
    
    "What is the email?":"contact@nayepankh.com",
    
    "What is the contact number?":"+91-8318500748",
    
    "Where is NayePankh located?":"Kanpur, Uttar Pradesh.",
    
    "Do you provide internships?":"Yes,Contact the NGO for internship details.",
    
    "How can I support the NGO?":"Donate, volunteer, or spread awareness.",
    
    "Thank you":"You're welcome!",
    
    "Is NayePankh a non-profit organization?":"Yes, it is an NGO.",
    
    "How can I join NayePankh?":"You can join as a volunteer.",
    
    "Can I work with NayePankh?":"Yes, through volunteering",
    
    "Are volunteers needed?":"Yes, volunteers are welcome.",
    
    "What skills are needed for volunteering?":"Any helpful skills are welcome.",
    
    "Can I volunteer online?":"Contact the NGO for opportunities.",
    
    "Can college students join?":"Yes, students can join.",
    
    "Can I volunteer on weekends?":"Yes, based on requirements.",
    
    "Do you organize events?":"Yes, NGO activities are organized.",
    
    "How can I participate in events?":"Join as a volunteer.",
    
    "How can I help children?":"Support education programs.",
    
    "Do you provide medical support?":"Yes, healthcare support is provided.",
    
    "Can I donate monthly?":" Yes, regular support helps.",
    
    "Is every donation useful?":" Yes, every contribution helps.",
    
    "Can I donate books?":"Yes, useful items can help.",
    
    "Can I donate food?":"Yes, food support is useful.",
    
    "How can companies help?":"Through CSR and donations.",
    
    "Do you accept partnerships?":"Yes, partnerships are welcome.",
    
    "How can I collaborate?":"Contact the NGO team.",
    
    "Is there a donation receipt?":"Yes, eligible donations get receipts.",
    
    "Where can I find more information?":"Visit the official website.",
    
    "Who can contact for queries?":"Contact the NGO team.",
    
    "I need help.":"Please contact the NGO for support.",
    
    "I want to complain.":"Please share your concern with the team.",
    
    "I have a suggestion.":"We appreciate your feedback.",
    
    "Good morning.":"Good morning! How can I help?",
    

  }

def getResponseOfBot(userQuestion):

    userQuestion = userQuestion.lower()

    answer = []

    for key in responses:
        if key in userQuestion:
            answer.append(responses[key])

    if answer:
        return "\n".join(answer)

    return "Sorry, I can't help. Please ask again."

while True:
    userInput= input("\nPlease ask your question:")

    if "Bye" in userInput.lower():
        print("Bot: Thank you for connecting with NayePankh Foundation!")
        break

    reply= getResponseOfBot(userInput)

    print("Bot:", reply)

