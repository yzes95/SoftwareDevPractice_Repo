#question4a
my_name = "Cole"
if my_name == "Helen":
    print('Yes, ', my_name, 'is the exact name')
else:
    print('Nice try')
    print('Not the correct name, try again')

#it will print the 1st print in th enested if if u change the name to Helen

#question4b
my_score = int(input('Enter you score: ')) #problem fixed by casting here intas u compare a score 
if my_score >= 50:
    print('Nice! That is a pass')
else:
    print('That is not a very good score.')
    print('You would have to retake the test')

#there was a problem which is that when ur ecive the input u get it in a str format from input fnc thats why u need casting using int fnc