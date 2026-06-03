q1=input('Enter your name: ')
q2=(input('Enter your birth date (in the format DD/ MM/YYYY): '))
q3=int(input('Enter your age: '))
q4=int(input('Which grade are you in? '))
q5=input('What is your favourite subject? ')
q6=input('What is your favourite hobby? ')
q7=input('What is your favourite cuisine? ')
print('Your name is ',q1)
print('Your birth date is ',q2)
print('Your are ',q3,' years old')
if q4>=10:
    if q3>=18:
        print('You are an adult')
    else:
        print('You are a minor')
    print('You are in high school')
elif q4>=6 and q4<10:
    print('You are a minor')
    print('You are in middle school')
else:
    print('You are a minor')
    print('You are in elementary school')
print('Your favourite subject is ',q5)
print('Your favourite hobby is ',q6)
print('Your favourite cuisine is ',q7)