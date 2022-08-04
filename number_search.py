'''
1. Understand the Problem Statement Correctly/Clearly.Identify the i/p & o/p format.
2.Come up with some example inputs & outputs. Try to cover all edge cases.
3.Come up with a correct solution for the problem. State it in plain English.
4.Implement the solution and test it using example inputs. Fix bugs, if any.
5.Analyze the algorithm's complexity and identify inefficiencies, if any.
6.Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.
'''

'''
QUESTION: Alice has some cards with numbers written on them. She arranges the cards in decreasing order,
and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing
a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
'''

'''
STEP-1
In this case, for instance, we can represent the sequence of cards as a list of numbers. 
Turning over a specific card is equivalent to accessing the value of the number at the corresponding position the list.
New Problem Statement: We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. 
We also need to minimize the number of times we access elements from the list.

Input:
cards: A list of numbers sorted in decreasing order. E.g. [13, 11, 10, 7, 4, 3, 1, 0]
number: A number, whose position in the array is to be determined. E.g. 7
Output
position: The position of query in the list cards. E.g. 3 in the above case (counting from 0)
'''

def locate_card(cards,number):
    pass

'''
STEP-2
Before we start implementing our function, it would be useful to come up with some example inputs and
outputs which we can use later to test out problem.
Ex: cards = [13, 11, 10, 7, 4, 3, 1, 0] ,number = 7, output = 3

We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function.
For example, the above test case can be represented as follows:
'''

test={
    "input":{
        "cards":[13, 11, 10, 7, 4, 3, 1, 0],
        "number":7
    },
    "output":3
}

locate_card(**test["input"])==test["output"]

print(2+2)