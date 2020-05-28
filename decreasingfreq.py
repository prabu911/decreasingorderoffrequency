frequency = {} 
def most_frequent(word):                                          
    for i in word: 
        if i in frequency: 
            frequency[i] += 1                                      
        else: 
            frequency[i] = 1
most_frequent("Mississippi")    
sorted_frequency = dict(sorted(frequency.items(),reverse=True))          
print("The decreasing order of the frequency : ",sorted_frequency)               




#OUTPUT SCREEN
#The decreasing order of the frequency :  {'s': 4, 'p': 2, 'i': 4, 'M': 1}
