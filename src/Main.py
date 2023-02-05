from Input import *
from Algorithms import *


if __name__ == "__main__":
   problem=generate_problem()


   result = backtracking(problem)


   if result == None:
       print('No Solution')
   else:
       for hall in result.halls:
           print(hall.preferences[0] + 1, end = ' ')
