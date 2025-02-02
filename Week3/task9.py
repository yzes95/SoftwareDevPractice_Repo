#question9A
from random import randint
for count in range(9):
    add_count = randint(0,100) + count
    print ('The addition = ', add_count)
    if add_count-10 > 3:
        break
    print('Not found the right number.')
    print('Iteration #',count+1)
    print()

#question9b:
random_number = int(input('Enter some random number: '))
check = 0
while check <= 14:
    add_count = random_number + check
    print ('The addition = ', add_count)
    check+=1
    if add_count-10 == 2:
        continue
    print(random_number, ' does not give the result as 5')
    print('Iteration #',check)
    print('The current loop continues')
    print()

#c
count = 0
while(count<10):
    city = input('Enter the name of a popular city: ')
    if city != 'Dundee':
        pass #should be changed with count+=1
    else:
        print('My city is Dundee!')