print('Welcome to my quiz')
next=input('Do u want to play') 
if next !='yes':
   quit()
print('Okay! lets start')
score=0
quiz=input('question1').lower()
if quiz=='answer1':
    print('correct')
    score=+1
else:
    print('incorrect')
quiz=input('question2').lower()
if quiz=='answer2':
    print('correct')
    score=+1
else:
    print('incorrect')
quiz=input('question3').lower()
if quiz=='answer3':
    print('correct')
    score=+1
else:
    print('incorrect')
quiz=input('question4').lower()
if quiz=='answer4':
    print('correct')
    score=+1
else:
    print('incorrect')
quiz=input('question5').lower()
if quiz=='answer5':
    print('correct')
    score=+1
else:
    print('incorrect')
print('you got'+str((score/5)*100)+'%')
    