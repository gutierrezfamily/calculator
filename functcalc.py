def addition (a,b):
    x = (a) + (b)
    return (x)

def subtraction (a,b):
    x = (a) - (b)
    return (x)

def multiplication (a,b):
    x = (a) * (b)
    return (x)

def division (a,b):
    x = (a) / (b)
    return (x)

print "________________________________"
print " THIS IS THE CALCULATOR PROGRAM"
print "________________________________"



firstNum = int(raw_input ("What is the first number? "))
secondNum = int(raw_input ("What is the second number? "))


calQuest = raw_input ("What operation do you want to use? ")

if calQuest == ("add"):
    answer = addition (firstNum,secondNum)

elif calQuest == ("subtract"):
    answer = subtraction (firstNum,secondNum)

elif calQuest == ("multiply"):
    answer = multiplication (firstNum,secondNum)

elif calQuest == ("divide"):
    answer = division (firstNum,secondNum)

else:
   print "That is not an operation that I know of."

print "The answer is:"
print(answer)
