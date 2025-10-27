name = input('type your name : ')
print ('hi ' + name + ' wellocom to the game ')

play_game = input('do you want to play the game ? ')
if (play_game == 'yes' or play_game == 'y') :
     print ('we are playing the game ! ')


     direction = input('Do you want to go left or right :  ')

     if direction == 'right' :
         print ('we are moving to the right ')
         right_choice = input ('do you want to continue move to the right while jumping or crawling (chose jump or crawl) ') 
        
         if right_choice == 'jump' :
            print('you are waking up the lion that will eat you ! ')
         elif right_choice == 'crawl':
            print('a snake will bite your ass!')
         else :
            print('wrong choice')

     elif direction == 'left' :
         print('we are moving to the left ')
         left_choice = input ('do you want to continue moving to the left by running or walking (chose rum or walk) ')

         if left_choice == 'run':
            print('it is better choice if you are running since you donot know what you will encounter on the way' )
         elif left_choice == 'walk':
            print ('you have have not made good choice as by running you would outsmart things better')
         else :
            print ('wrong choice')

     else :
         print('sorry you are going to die !')
else :
    print ('we are not playing the game ')
  
