# -*- coding: utf-8 -*-
"""lab_asssignment02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fd3QMjiou50PcvSNlFYJkewLgYlNgBZJ

Question#01
"""

product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice # here we give keys to their value that user entered.


while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])

    else:
        print("This product is not found in dictionary")
        break


print(my_dict)

"""Question#02"""

my_dict ={'fuel': '160','milk':'120','cycle':'6000'}
amount =eval(input("Enter Amount: $"))
for key ,values in my_dict.items():
    if  int(values) < amount:
        print (key)

"""Question#03"""

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}
                                      ###Part A
user_input= input("Enter Name of a month: ")
for key, values in year.items():
     if user_input == key: 
        print( values)
        


                                      #Part B
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

                                        ##Part C
for keys,values in year.items():
    if int(values) == 31:

      print(keys)

"""Question#04"""

user_dict ={"Talha":"1234","rehan":"5678","Rafay":"91011",'humam':"12131415"}
def login_system(id,pas):
    for keys ,values in user_dict.items():
        if keys == id  and pas == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



id = input("Enter Username: ")    
pas = input("Enter Your Password ")
print(login_system(id,pas))

"""Question#05"""

def scoreinfo():
   num_of_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_of_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})# here simply we update the win and losses that user enter into the of value of keys
       
   return team_dict

print(scoreinfo())

"""Question#06"""

matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def List():
    matrix_dict={}
    for number in range(len(matrix_5)):
        key = matrix_5[number]#here we simply assign keys to number that are present in the matrix
        value = matrix_5.count(key)# here  firstly  we count how many  time  a number occur in matrix than asssign to the  values according the statement 
        matrix_dict.update({key:value})# here we make the dictionary and update their key and value 
    return matrix_dict



print(List())

"""Question#07"""

import random

all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3 #every player have 3 cards
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))#here it simple choice the cards randomaly from the dictionary values
    c2= random.choice(list(all_card.values()))# same as aboe
    player1Card.append(c1)# now we have to add these selcted cards into list of playerscard
    player2Card.append(c2)
print(player1Card,player2Card)
# here we simply print that who win the game by that points
if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))

"""Question#08"""

d=[{'name':'Talha', 'phone':'000000', 'email':'talha@gmail.com'},
{'name':'ahsna', 'phone':'11118', 'email':'ahsan@gmail.com'},
{'name':'javed', 'phone':'222', 'email':''},
{'name':'rehan', 'phone':'33338', 'email':'rehan@gmail.com'}]

for dict  in  range(len(d)):
     dd =d[dict ]
     for keys,values in dd.items():
         if keys == "phone" and values[-1] == "8":
             print(dd)
         if keys == "email" and values =='':
            print(dd)

"""Question#09"""

def teamWIn():
    numberofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(numberofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)






print(teamWIn())