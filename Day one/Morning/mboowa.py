#if condition1;
#print(True if the condition is true)

#elif condition 2;
#print(True if the condition is true)

#else;
#print(False if the condition is false)

#EXAMPLE 1
#age<18,print ur under age
#age>18 and age <=65 ,print ur adult
#print your senior adult

#Solution
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


 #Exceptional handling
#try:
#print(x)
#except:
print("An exception occurred")
  #we have try, then use either of the two ;except  and finally

  #EXAMPLE 1
try:
    print(1/0)
except ZeroDivisionError:
    print("you can't divide by zero")
finally:
    print("this will always run")

    #EXAMPLE 2
#try:
   # print(1/0)
#except ZeroDivisionError:
   # print("you can't divide by zero")
#except Exception as e:
    #print(e)

#example 5
#Dict as a dictionary

#emotion ={
#    "happy":"Im happy always",
 #   "sad":"Im sad always",
#    "angry":"Im angry always"
#}

    #prompt user to enter emotions
#user_emotion =input("How are u feeling dearie?")

#if user_emotion in emotion:
 #   print(emotion[user_emotion])

#else:
   # print( "Im sorry, i cant relate")

    #WRITE A PROGRAM TO ASK STUDENTS ABOUT THEIR MENTAL HEALTH
    #prompt students on a scale of 1 to 10 to rate their mental health
    #if the student rates the mental health above 6, print ur mental health is good
    #if the student rates the mental health below 6, print ur mental health is bad
    #if the student rates the mental health between 6and 10, print ur mental health is okay


#EXERCISE
emotion ={
    "happy":"Im happy always",
    "sad":"Im sad always",
    "angry":"Im angry always"
}

    #prompt user to enter emotions
rating=int(input("On a scale of 1 to 10 ,How are u feeling dearie?"))

    
if rating > 10 or rating < 1:
     print("Invalid rating. Please rate your mental health between 1 and 10.")
elif rating > 6:
     print("Your mental health is good.")
elif rating < 6:
     print("Your mental health is bad.")
else:
    print("Your mental health is okay.")

 




    

   

