"""
Author : Arief Muhammad Lubis
Created on 11 Apr 2020
Code for adder two number using quantum computing
"""
from FullAdder import FullAdder

def main():
    # Before you can use the jobs API, you need to set up an access token.
    # Log in to the Quantum Experience. Under "Account", generate a personal 
    # access token. Replace 'PUT_YOUR_API_TOKEN_HERE' below with the quoted
    # token string. Uncomment the APItoken variable, and you will be ready to go.

    APItoken = 'You can get in https://quantum-computing.ibm.com/account and copy your token'
    firstNumber = int(input("Enter your first number : "))
    secondNumber = int(input("Enter your second number : "))
    notUsingIBMExperience = FullAdder(firstNumber, secondNumber)
    print("Testing full adder not using IBM Experience")
    print(notUsingIBMExperience)
    
    """if you use IBMQ Experience add API TOken to Fulladdder
    usingIBMExperience = FullAdder(firstNumber, secondNumber, yourAPIToken)
    print("Testing full adder using IBM Experience")
    print(usingIBMExperience)    
    """
if __name__ == '__main__':
    main()

