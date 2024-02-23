def feet_to_steps(user_feet):
   return (user_feet / 2.5)

if __name__ == '__main__':
    #take input feet steps here
    #store it into the function
   user_feet = float(input())
   steps = feet_to_steps(user_feet) 
   print(f'{int(steps)}')
    #print your steps here