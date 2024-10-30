index_count = 0
for letter in 'rishi':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'
for index, letter in enumerate (word):
    print(index)
    print(letter)
    print('\n') 
    
mylist1 = [1,2,3,4,5,6]
mylist2 = ['a', 'b', 'c']
mylist3 = [100,200,300]

for item in zip (mylist1, mylist2, mylist3):
    print(item)

list (zip (mylist1, mylist2))

#in
k="s" in "rishi"
print(k)