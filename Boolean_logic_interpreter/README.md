# A Boolean logic interpreter.

## Requirements

This Boolean Logic Interpreter has been implemented using Python Programming Language. 
 
## Introduction 
Boolean logic is form of simple algebra centered from three operators; **AND, OR , NOT**.  

Boolean compares the relationship between two components and checks whether they relate. This means that an expression 2 + 8 is not a boolean logic since it is not compared with something else. An example of boolean logic is 6 + 4 = 3 + 7. The results are calculated as either *True or False* and can not take any other value. 

Booleanlogic can also be used to check whether two strings are equal.Example: "This Is A Coding Interview" = "This is a coding interview" results to False. On the left hand side of the logic, the first letter of each word in the sentence is capitalized while the on the right hand side, only the first letter of the first word is capitalized. A more detailed explanation on boolean logic is found on the link:[What Boolean Logic Is & How It’s Used In Programming](https://www.codecademy.com/resources/blog/what-is-boolean-logic/).

[Boolean Operators](https://www.scribbr.com/working-with-sources/boolean-operators/#:~:text=Boolean%20operators%20are%20specific%20words,parentheses%20()%2C%20and%20asterisks%20*.) are commonly used to expand search when using databases since databases do not understand natural language. They are:

| Operators | Symbol |
| ---------- | ------- |
| AND | ∧ . |
| OR | ∨ + |
| NOT | ! ¬ | 
| Parentheses | () | 
| quotation marks | "" | 
| asterisk | * |

- AND(∧,.) - used to confirm that both or two keywords are true.
- OR (∨, +)  -  used to confirm either one or both conditions are met.
- NOT(!, ¬) - this condition takes only one arguement. It tests whether a value is False or not. 
- Parentheses(()) - allows grouping together keywords and control the order in which the terms will be searched. Keywords and Boolean operators within parentheses will be searched first, followed by keywords outside parentheses.
- Quotation marks("") - Used when you want results that contain a precise keyword or keywords.
- Asterisk (*) - Use this when you want results that contain the keyword that you entered or other words that begin with those letters.

## What the application does

 This program is a Boolean logic interpreter that can evaluate simple expressions, for example:

**OR** 

λ> T ∨ F

T

The `or_operator` uses addition in the background . 

True is assigned a value of 1 and False is assigned a value of 0. 
T ∨ F. In the case of True or False, our mathematical expression is 1 + 0 which yields 1 which is True. In the case of F ∨ F, the result yields a 0. This is because 0 + 0 = 0 
If we have multiple operators and the result of the computation is greater than one, the result is considered True.


**AND**

λ> T ∧ F

F

The `and_operator` computes the expression in the background through multiplication. 
Just like the `or_operator`, True is assigned 1 and False is assigned 0. 
The result of the computation is True(1) if both conditions are true. 
1 * 1 results to  True

1 *  0 and 0 * 0 results to False

 T ∧ F
 
**Parentheses**

λ> (T ∧ F)

T

The parentheses operator is solved by the `evaluate_with_brackets` function. 
First check whether input string contains parentheses. 
If present, the string is compressed to a form that eliminates spaces for ease of computation. 
We get the expression inside the bracket and solve it which gives the bracket_result.
Replace the contents of the bracket, the  with the bracket_result from the step above.
The bracket_result is simplified, which is then evaluated to boolean form.

** Equality**
T = F
This works by simply checking if the string representations of the inputs match
if they match it returns true otherwise it will return false

### Operator Precedence
Operator precedence is implemented through order of function calls
The first function to be called is the `evaluate_with_equality_check`. This 

## Technologies you used
1. Python - it is a coincise language easy to learn and has wide support
2. Flask - It provides easy support ofr creating a webpage
3. Docker & Docker Compose - Allows us to run the application quickly independent of OS
   

### How ro run
1. Ensure docker is imstalled
2. Run `docker-compose up --build -d`
3. Navigate to your browser and visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

### Current limitations
1. No supoort for complex expressions e.g. multiple brackets
   
## Future improvements
1. Make the UI more intuitive
2. Support for more complex expressions e.g. multiple brackets

## Include Credits
