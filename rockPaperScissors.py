'''
Created on Sep 15, 2018

@author: ITAUser 
'''
#testme
#Loops the whole game 
keepPlaying= True
while(keepPlaying):
    print("Welcome to Rock Paper Scissors!")
    print("Best 2 out of 3. Press 'q' to quit.")
    #1 = Rock 
    #2 = Scissors 
    #3 = Paper
           
    
    #Selects a random integer between 1 and 3
    
    import random 
    
    
    humanScore = 0
    cpuScore = 0
    while(humanScore < 2 and cpuScore < 2):
        cpuChoice = random.randint(1,3)
        
            
            
        #asks user to select an option 
        choice = input("Please choose(Rock,Paper,Scissors:)")
            
        #checks if user wants to quit
        if(choice == 'q'or choice == 'Q'):
            keepPlaying = False 
            break 
        
           #checks for a draw 
        elif((choice.lower() == 'rock' and cpuChoice == 1)
            or (choice.lower() == 'scissors' and cpuChoice == 2)
            or (choice.lower()== 'paper' and cpuChoice == 3)):
            print("DRAW!!!")
            print("Human: " + str(humanScore), "CPU: " + str(cpuScore))
                  
           #checks if human wins 
        elif((choice.lower() == 'rock' and cpuChoice == 2)
            or (choice.lower() == 'scissors' and cpuChoice == 3)
            or (choice.lower()== 'paper' and cpuChoice == 1)):
            humanScore = humanScore + 1
            print("Human: " + str(humanScore), "CPU: " + str(cpuScore))
          
          #checks if cpu wins        
        elif((choice.lower() == 'rock' and cpuChoice == 3)
            or (choice.lower() == 'scissors' and cpuChoice == 1)
            or (choice.lower()== 'paper' and cpuChoice == 2)):
            cpuScore: cpuScore + 1
            print("Human: " + str(humanScore) , "CPU: " + str(cpuScore))
        else:
            print("Not an option, try again.")
             
    print("Thanks for Playing!")
    #These two conditions check who won the game
    if(humanScore == 2):
        print("WIINNERR!") 
    elif(cpuScore == 2):
        print("LOOOSSER!")
#This prints the final score
    print("Human:" + str(humanScore) , "CPU: " + str(cpuScore))                         
              
