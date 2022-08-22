prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

#this is a while loop with user input, but it also uses a flag.
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

#We can write our programs so they run while the flag is set to True 
#and stop running when any of several events sets the value of the flag to False.
