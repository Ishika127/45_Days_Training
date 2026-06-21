#Question 1  Explain the difference between the following data types with examples: 
 #Integer:An integer is a whole number that can be postive , negative or zero .
a=10
b =-5
print(a)
print(type(a))
print(b)
print(type(b))
#Float:A float is a number that has a decimal point or is in exponential form.
c=3.89
print(c)
print(type(c))
#String :A string is a sequence of characters enclosed in quotes (single,double    or triple).
d="Hello world"
print(d)
print(type(d))
e='Python programming'
print(e)
print(type(e))
f='''This is a multi-line string.'''
print(f)
print(type(f))
#Boolean:A boolean is a data type that can have one of two values :true or false.
g=True
h=False
print(g)
print(type(g))
print(h)
print(type(h))

#Queestion 2 Write a Python program to create three variables: name,age,city
name="Ishika"
age=20
city="New York"
print(name)
print(age)
print(city)

#Question 3  Write a Python program that:Takes a user's name as input.  
#Prints the name in uppercase.  
#Prints the total number of characters in the name.
name = input("Enter your name: ")
print(name.upper())
print(len(name))

#Question 4 4. Explain any five commonly used string methods in Python with examples:
#1.upper():This method converts all characters in a string to uppercase.
name="Hello"
print(name.upper())
#2.lower():This methos converts all character in a string to lowercase.
name ="World"
print(name.lower())
#3.strip():this method removes any leading and trailing whitespace from a string.
name="    Python"
print(name.strip())
#4.replace():This method replace a specified value with another value in a string.
name="Hirat"
print(name.replace("Hirat", "Ishika"))
#5.find():This method searches for a specified value in a string and returns the position of where it was found.
name="Hello, welcome to my world."
print(name.find("welcome"))

#Question 5  Create a list containing the names of five fruits.
#Print the complete list.  
# Print the first and last element.  
# Print the total number of items in the list.
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits)
print(fruits[0])
print(fruits[-1])
print(len(fruits))


# Question 6. Write a Python program to: 
# Create a list of numbers [10, 20, 30, 40, 50]  
#Add 60 to the list.  
#Remove 20 from the list.  
#Print the updated list.
numbers=[10,20,30,40,50]
print(numbers)
numbers.append(60)
numbers.remove(20)
print(numbers)


#Question 7.What is Artificial Intelligence (AI)? Explain its importance and mention any four real-life applications of AI.

#                     ARTIFICIAL INTELLIGENCE (AI)

# DEFINITION:
# Artificial Intelligence is the ability of machines (especially computers)
# to simulate human-like thinking — such as learning, reasoning,
# problem-solving, understanding language, and making decisions.

# In simple terms: AI makes machines "smart" enough to perform tasks
# that would normally require a human brain.

# The term was coined by John McCarthy in 1956, who defined it as:
# "The science and engineering of making intelligent machines."

#                         HOW DOES AI WORK?


# AI systems learn from DATA. The more data they process, the smarter they get.
# The core process looks like this:
#
#   Data Input  →  Learning (Training)  →  Pattern Recognition  →  Output


# KEY TECHNOLOGIES THAT POWER AI:

# 1. Machine Learning (ML)
#    Learns from data without being explicitly programmed
#
# 2. Deep Learning
#     neural networks to mimic the human brain
#
# 3. Natural Language Processing (NLP)
#    Enables machines to understand human language
#
# 4. Computer Vision
#     Enables machines to interpret images and video

#                         IMPORTANCE OF AI

# 1. SAVES TIME & BOOSTS EFFICIENCY
#    AI automates repetitive tasks, freeing humans to focus on
#      creative and strategic work.

# 2. REDUCES HUMAN ERROR
#     Machines don't get tired or distracted.
#    AI delivers consistent, accurate results — especially critical
#      in healthcare and finance.

# 3. HANDLES BIG DATA
#     AI can analyze massive datasets in seconds —
#      something impossible for humans alone.

# 4. AVAILABLE 24/7
#    →Unlike humans, AI systems never need sleep or breaks,
#      ensuring round-the-clock service.

# 5. DRIVES INNOVATION
#     AI is powering breakthroughs in medicine, climate science,
#      space exploration, and more.



#                   FOUR REAL-LIFE APPLICATIONS OF AI


# APPLICATION 1: HEALTHCARE — Disease Diagnosis
# AI analyzes medical scans (X-rays, MRIs) to detect diseases like
#   cancer earlier and more accurately than traditional methods.
# Example: Google's DeepMind AI detects eye diseases from retinal scans.


# APPLICATION 2: E-COMMERCE — Recommendation Systems
# AI studies your browsing and purchase history to suggest products
#   you are likely to buy.
# Example: Amazon's "Customers who bought this also bought..."
#   feature is powered by AI.


# APPLICATION 3: TRANSPORTATION — Self-Driving Cars
# AI uses sensors, cameras, and real-time data to navigate roads,
#   avoid obstacles, and make driving decisions autonomously.
# Example: Tesla's Autopilot and Waymo's self-driving taxis.


# APPLICATION 4: COMMUNICATION — Virtual Assistants

#  AI-powered assistants understand voice commands and natural language
#   to answer questions, set reminders, and control smart devices.
# Example: Siri, Alexa, and Google Assistant.

# CONCLUSION:
# AI is no longer the future — it is the PRESENT,
# quietly powering the tools and services we use every single day.

#Question 8.# IDENTIFYING WHETHER THE FOLLOWING ARE EXAMPLES OF AI


# 1. ChatGPT
# IS IT AI?  YES
#  Built on a Large Language Model (LLM) called GPT.
#  Uses Natural Language Processing (NLP) and Deep Learning.
#  Trained on massive text data to understand and reply like a human.
#  Does NOT follow fixed rules — it thinks and generates new responses.
# Learns from data — a core feature of AI.


# 2. Google Maps Route Prediction
# IS IT AI? YES
#  Uses Machine Learning to predict traffic and suggest best routes.
#  Learns from real-time data of millions of users.
#  Uses Pattern Recognition to detect traffic and estimate arrival time.
# A basic GPS is NOT AI — but Google Maps learns and predicts, so it IS AI.


# 3. Calculator
# IS IT AI?  NO
#  Only follows fixed, pre-programmed math rules.
#  Does NOT learn from data or improve over time.
#  Always gives the same output for the same input.
#  Example: 2 + 2 = 4 (always, no thinking involved)
# It is just a fixed logic tool — NOT Artificial Intelligence.


# 4. Netflix Recommendations
# IS IT AI?  YES
#  Uses a Machine Learning based Recommendation System.
#  Analyzes your watch history, ratings, and viewing habits.
#  Compares your behavior with millions of other users.
#  The more you use Netflix, the smarter its suggestions become.
#  Personalizes content for every user — a great real-life AI example.


# 5. Voice Assistants (Alexa / Siri)
# IS IT AI? YES
#  Uses Natural Language Processing (NLP) to understand your words.
#  Uses Speech Recognition to convert voice into text.
#  Uses Machine Learning to learn your accent and preferences.
#  Adapts and gets smarter with use.
# Example: "Hey Siri, set an alarm" — it understands and acts.