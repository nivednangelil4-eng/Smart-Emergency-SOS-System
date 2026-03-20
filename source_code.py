cont=['Father : 9784758223','Mother : 9847599221','Friend : 8547632345']

def Alert():
  print("-----------------------------------------------------------------------")
  print("                     Sending SOS Alert!                                ")
  print("-----------------------------------------------------------------------")
  for i in cont:
    print("Alert sent to ",i)
    
  print("Location: [Simulated Location]")
  print("Help is on the way!")
  print("-----------------------------------------------------------------------")


def SafetyTips():
    print("-----------------------------------------------------------------------")
    print("                     Safety Instructions                               ")
    print("-----------------------------------------------------------------------")
    print("1. Stay calm and find a safe place.")
    print("2. Call local emergency number(Dial 112).")
    print("3. Share your location with trusted person.")
    print("4. Avoid panic and follow safety procedures.")
    print("-----------------------------------------------------------------------")

#Main 
print("-----------------------------------------------------------------------")
print("                     Smart Emergency SOS System                        ")
print("-----------------------------------------------------------------------")
ch='y'
while ch=='y':
    print("1. Send SOS Alert")
    print("2. View Safety Tips")
    print("3. Exit")
    print("-----------------------------------------------------------------------")
    
    c=int(input("Enter your choice: "))
    
    if c==1:
        Alert()
        SafetyTips()
    elif c==2:
        SafetyTips()
    elif c==3:
        print("-----------------------------------------------------------------------")
        print("Exiting system. Stay safe!")
        print("-----------------------------------------------------------------------")
        break
    else:
        print("Invalid choice. Try again.")
    ch=input("Do you want to continue(y/n): ")
    if ch=='n':
      print("-----------------------------------------------------------------------")
      print("Exiting system. Stay safe!")
      print("-----------------------------------------------------------------------")
