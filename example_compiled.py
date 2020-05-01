import os, sys

 
class ClassWithBraces:
    print('There should be normal indentation')
    
    for i in range(10):
        print(i)
         
     
print('And here, should\'t be any indentation')


for file in os.listdir():
    print(file, 'lays here. Don\'t touch it!')
     

a = {a: b for a, b in enumerate(['one', 'two', 'three', 'four'])}

b = {
    'ufo': 'exists',
    'yetti': 'exists',
    'human': 'not exists',
    'author has a schizophrenia': True,
    'another-dict': {'test': True}
}

print('end')
