#question5a:
my_name = input("Enter your name: ")
if my_name == 'Messi':
    print('You must be a natural talent.')
elif my_name == 'Ronaldo':
    print('You must be a driven by your ambition.')
else:
    print('My description of you might be incorrect.')


#question5b
my_score = int(input('Enter you score: '))
if my_score >= 0 and my_score< 40:
    print('That is not a very good score.')
    print('You need to rewrite this.')
elif my_score >= 40 and my_score< 50:
    print('You have a D.')
elif my_score >= 50 and my_score< 60:
    print('You have a C.')
elif my_score >= 60 and my_score< 70:
    print('You have a B.')
elif my_score >= 70 and my_score< 100:
    print('Well done. You have an A.')
else:
    print('That is a wrong input.')
    print('Your entry should be greater than 0 and not more than 100')


#question5c:
weather= input("Enter the weather state: ").lower()
if "sunny" in weather:
    print("I suggest going to the beach")
elif"rainy" in weather:
    print("I ecommend staying indoors and watching movies")
elif "cloudy" in weather:
    print(" I suggest a walk in the park")
else:
    print("It seems the weather state you mentioned i am not familiar with yet")