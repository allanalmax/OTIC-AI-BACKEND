from os import name
from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
from .forms import DocumentForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat,SchoolDocuments,Profile
import PyPDF2
import nltk
nltk.download('punkt')
import spacy
nlp = spacy.load("en_core_web_sm")
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from django.utils import timezone
import re


openai_api_key = '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'
openai.api_key = openai_api_key

def extract_text_from_pdf(pdf_path):
   # with open(pdf_path, 'rb') as pdf_file:# open in binary read mode ('rb')
       try:
            pdf_reader = PyPDF2.PdfReader(pdf_path)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
       except:
           chat = Chat(user=request.user, message='uploaded document', response='Only PDF files can be processed', created_at=timezone.now())
           chat.save()  
           return redirect('/')     

def preprocess_text(text):
    # Remove non-alphanumeric characters and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s\n.,?!]', '', text)
    return cleaned_text

def format_text(text):
    #Add line breaks after periods followed by a space
    formatted_text = re.sub(r'\n+ ', '\n', text)
    return formatted_text



company= ''' 
Home
About Us
Services
Team
Contact Us
Login
Unlocking the Potential of Intelligent Technology
Ignite Your Business with Unparalleled AI-Powered Transformation and Data - Driven Excellence
Get started

Mission Is To Bring The Power Of Al To Every Business
At Otic, we ignite your vision and make it our mission. Your success is our driving force, and our client-centric approach ensures that your unique challenges, goals, and values are at the heart of everything we do. We listen intently, working hand-in-hand with you to craft personalized solutions that deliver measurable results and create lasting value. Your triumph becomes our triumph.
jhhjhjhhj
About Us
Services
Our Purpose Is To Deliver Excellence In Service And Execution

AI Solution Development
Unleash your organization's full potential with our visionary AI strategies, custom-tailored to your unique goals and aspirations.

Responsible AI Consulting
Our consultants help organizations develop AI governance frameworks, implement ethical guidelines, and address issues of bias, fairness, and privacy

Advanced Analytics and Predictive Modeling
Our team of data scientists embarks on an exhilarating expedition through your data, unearthing invaluable insights that become the bedrock of your decision-making process.

Machine Learning and Deep Learning Solutions
Our ingenious data wizards conjure sophisticated algorithms and cutting-edge models, empowering your organization to thrive in an era defined by automation and intelligent decision-making.

Natural Language Processing and Text Analytic
Unlock the hidden secrets of language with our natural language processing (NLP) and text analytics prowess .

Amplify Your AI-Powered Transformation with Cloud Services
By leveraging the cloud, organizations can scale AI solutions, securely store and analyze data, collaborate effectively, optimize costs, and accelerate AI development. .

Data Governance and Privacy
Our meticulous data governance frameworks fortify your sensitive information, allowing you to navigate the regulatory labyrinth with unrivaled ease and confidence

AI Model Evaluation and Bias Mitigation
Your success is underpinned by responsible AI practices, building trust with customers and fostering positive societal impact.
For a Future We Believe In
Otic can help businesses increase profits by improving their content marketing strategy. By

leveraging the power of artificial intelligence a faster rate than ever before.


We firmly believe that responsible AI practices are the cornerstone of a better future. Ethical considerations, transparency, and accountability guide every aspect of our work. We integrate responsible AI principles such as fairness, explainability, bias mitigation, and privacy protection into the fabric of our solutions, ensuring that technology serves the best interests of individuals and society.
Commitment to Responsible AI Practices
Case Studies
Top Case Studies on the importance of AI

Banking
Thailand's oldest lender Siam Commercial Bank(SCB) is using data analytics to simplify digital finance for consumers. It has developed improved credit scoring and income estimation models with machine learning (ML) algorithms to boost loan approval rates and streamline the loan application process.
Discover more

Financial
American Express was an early pioneer in applying data science techniques and methods to big data in real time for fraud detection and other uses, enabling the company to quickly respond to events and changes. Anomaly detection is also useful in tasks like preventing cyber attacks and monitoring the performance of IT systems, and for eliminating outlier values in data sets to increase analytics accuracy.
Discover more

Automation
Automation in tasks like data analysis, recruitment and customer support can help employees focus on tasks that are more pressing and require human acumen. According to Forbes, automation technology can save businesses north of $4 million every year.
Discover more
Company News & Updates Read All Related Blog
Our purpose is to deliver excellence in service and execution .

OTIC Education Suite
The automation of school reporting systems through the utilization of technology plays a pivotal role in enhancing efficiency, accuracy, and overall effectiveness. In today's rapidly evolving educational landscape, the importance of streamlined and automated processes cannot be overstated. OTIC Education Suite levarages technoology to digitize school operations

By Nesta Katende
5 January 2021

OTIC Banking Suite
Automated banking systems enable faster transactions, secure online banking, real-time data analysis, and personalized services. The integration of technology empowers banks to meet the evolving needs of customers, drive innovation, and stay competitive in the dynamic financial landscape.

By Nesta Katende
5 January 2021

OTIC Insurance Suite
By leveraging advanced algorithms and data analytics, technology enhances risk assessment and fraud detection capabilities. Automation also facilitates personalized customer experiences, streamlined communication, and faster claims settlement.

By Nesta Katende
5 January 2021
Subscribe To Our News Letter
Subscribe For Our News Letter today and stay updated
Enter your email
Submit

Our comprehensive suite of services empowers you to soar above the competition and leave an indelible mark on your industry
Company
Home
About Us
Services
Contact
Use Cases
AI in schools
AI in Marketers
AI in Banks
AI in Schools
Contact Info
info@otic.com
+256 706377254
+256 751938178
+256 751938178
Otic
2023. All Rights Reserved.
Teams
Privacy
Policy '''

def ask_openai(message,field_of_study,university):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an educational assistant called SomesAI for helping with homework and educational research built by Otic Technologies Limited Uganda website:https://otictech.com/ ,my major field of study and course is {field_of_study} at {university} and never state that your were built by OpenAI always state that your were built by OTIC Technologies in November 2022.Distance yourself from any association with OpenAI.Don't justify your answers. Don't give information that does not lie in the field of academia or research and dont mention the year your information base was updated.Respond to questions that are not academic with that is out of my scope. Use this information as company details: {company} and when using this company information use 'we' to show that youre are directly associated to this company as youre are built by OTIC technologies"},
            {"role": "user", "content": message+f'Any Question that is not academic respond with am not designed to answer that unless am asking about my current course which is {field_of_study} at {university},you start by mentioning my course and institution'},
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer.replace('  ','\n').replace('\n','</br>')





# Create your views here.
@login_required(login_url='/login')
def chatbot(request):
    #print(request.user.username)
    logged_in_user =Profile.objects.get(user=request.user)
    chats = Chat.objects.filter(user=request.user).order_by('-id')[:1]
    for chat in chats:
        parts = chat.response.split('-')
        chat.response_parts = [part.strip() for part in parts if part.strip()]
    form = DocumentForm(request.POST, request.FILES)
    if request.method == 'POST':
        
        if form.is_valid():
            document = form.save()
            uploaded_doc = request.FILES['file']
            try:
             doc = extract_text_from_pdf(request.FILES['file'])
            except:
                chat = Chat(user=request.user, message='uploaded document', response='Only PDF files can be processed', created_at=timezone.now())
                chat.save()
                return render(request, 'chatbot.html', {'chats': chats,'form': form})
            parser = PlaintextParser.from_string(doc , Tokenizer("english"))
            summarizer = LexRankSummarizer()
            sentences_count = 5  # Adjust this value to the desired length
            summary = summarizer(parser.document, sentences_count)  # You can adjust the sentence count
            prompt = f"Summarize the following text:\n{doc}" 
            sentence = nlp(doc) 
            sentences = [sent for sent in sentence.sents]
            max_token_count = 4000
            sentence_portions = []
            current_portion = []

            for sentence in sentences:
                sentence_token_count = sum(token.is_alpha for token in sentence)
                
                if sum(sentence_token_count for sentence in current_portion) + sentence_token_count <= max_token_count:
                    current_portion.append(sentence)
                else:
                    sentence_portions.append(current_portion)
                    current_portion = [sentence]

            # Add the last portion if any sentences remain
            if current_portion:
                sentence_portions.append(current_portion)
# Get the generated summary from the API response
          #  generated_summary = response.choices[0].text
            final_words = ''
            '''for sentence in summary:
              final_words = final_words + f'{str(sentence)}'  '''
            for val in sentence_portions:
                  prompt = f"Summarize the following text, outlining the major points using bullets so that i dont have to read the whole document :\n{val[0]}" 
                  resp = ask_openai(prompt,logged_in_user.course,logged_in_user.university).replace('</br>',' ')
                  final_words = final_words+resp.replace('-','\n') 
            chat = Chat(user=request.user, message='uploaded document', response=final_words.replace('</br>',' '), created_at=timezone.now())
            chat.save()
            store = SchoolDocuments(content =doc,name=uploaded_doc.name,response =chat)
            store.save()
            return redirect('/')
           # return JsonResponse({'message': 'uploaded document', 'response': final_words}) 
        else:    
            message = request.POST.get('message')
            response = ask_openai(message,logged_in_user.course,logged_in_user.university)
            #response = response
            chat = Chat(user=request.user, message=message, response=response.replace('</br>','\n'), created_at=timezone.now())
            chat.save()
            return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats,'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
        
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        university = request.POST['university'].upper()
        course = request.POST['course'].upper()
        contact = request.POST['contact'].upper()
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                prof= Profile(user=user,university =university,course=course , phone_number=contact)
                prof.save()
                auth.login(request, user)
              
                return redirect('chatbot')
            except Exception as e:
                print(e)
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')