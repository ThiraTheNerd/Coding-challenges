# Create pig latin based on string inputted
def pig_it(text):
    #Initialize an empty string
    res = []
    #Loop through list converting each word 
    for i in text.split():
        #Check if all the characters in the text are letters
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        #If not an alphabet append without altering
        else:
            res.append(i)
            
    return ' '.join(res)