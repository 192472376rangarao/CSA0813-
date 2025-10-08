#Loops : loops are used to Exucute A block of code repeatedly as long a certain condition is true or for a specific number of iterations.
# Types : 1.While 2.for loop
# while Loop :it continously Checks Theondition before each iteration and stops when the Condition Becomes fakse.
#syntax :while condition :
# For Loop : A for loop is a way to repeat a block of code for each item in a collection (like a list) or for a specificc range of numbers.
# syntax : fir variable in range(start,stop,step):
# 
candies=10
for i in range(0,candies):
    print("give to my friend")


#BREAK : if during the Execution of the loop python intrpeter Encounters break,it immediately stops the loop execution and exits out of it
#Syntax : while condition :
#         if some_condition
#           break

candies=10
for i in range(candies):
    print("Chocolate given to my frineds")

    if candies- i == 5:
        print("Only 5 left")
        break

# Continue: Continue Statement is used to skip the rest of the current iteration in a loop and move to the next iteration 

candies=10
for i in range(candies):
    print("Chocolate given to my frineds")

    if candies- i == 5:
        print("Only 5 left")
        continue
    print("Giving to my frined :")