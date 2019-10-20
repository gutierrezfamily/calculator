passwordName = raw_input ("What is the password? ")

if passwordName == "":
    print "Processing Password....    "
    print "Access Accepted"

else:
    print "Processing Password....    "
    print "Access Denied"

firstNum = int(raw_input ("What is the first number? "))
secondNum = int(raw_input ("What is the second number? "))


calQuest = raw_input ("What operation do you want to use? ")

if calQuest == ("add"):
    x = (firstNum) + (secondNum)
    print (x)

elif calQuest == ("subtract"):
    x = (firstNum) - (secondNum)
    print (x)

elif calQuest == ("multiply"):
    x = (firstNum) * (secondNum)
    print (x)

elif calQuest == ("divide"):
    x = (firstNum) / (secondNum)
    print " is your answer."


else:
   print "That is not an operation that I know of."
