'''
pseudocode:
define a function for the vector:
    define a list, and for the element in a range from 0 to ten, insert in a variable di input (int to transofm the element in numbers). Add each element to the list and print it
define a function for the avarage:
    sum each element of the list and divide for the lenght of the list. Put the operetion in a variable and print it.

For the average of the vector inserted form users, the function of the vector has to be the argument of the function for the average.
'''
vect = []
def vectors(vector):
    for i in range(0,10):
        vec = int(input('Write a number here: '))
        vector.append(vec)
    return vector

def average(list):
    average_list = sum(list)/len(list)
    print ('The avarage is:', average_list)

average(vectors(vect))

   

