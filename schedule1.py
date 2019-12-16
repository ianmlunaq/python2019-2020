name1 = input('What is your first name? ')
name2 = input('What is your last name? ')
id = input('Student ID: ')
className = ''
classNum = ''
blockNum = 0

print('*************************************************')
print('*\t\t\t\t\t\t*')
print('*\t' + name2 + ', ' + name1 + '\t\t' + 'ID: ' + id + '\t*')
print('*\t\t\t\t\t\t*')
print('*************************************************')
print('*\t\t\t\t\t\t*')

while(className != 'STOP'):
    className = input('Enter the next class, STOP to end: ')
    blockNum += 1
    if(className != 'STOP'):
        classNum = input('Enter the room number: ')
        print('*\tBlock ' + str(blockNum) + ': ' + className + '\tRoom: ' + classNum + ' \t*')

print('*\t\t\t\t\t\t*')
print('*************************************************')
print('*\t\t\t\t\t\t*')
print('*************************************************')
