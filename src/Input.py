from CSP import CSP
from Hall import Hall


def generate_problem() -> CSP:
   halls = []
   assigned_halls = []
   edges = []


   halls_count,groups_count=input().split()
   halls_count=int(halls_count)
   groups_count=int(groups_count)


   for hall in range(halls_count):
       halls.append(Hall([], []))
       assigned_halls.append(False)
  
   for preference in range(groups_count):
       for hall_number in input().split():
           halls[int(hall_number)-1].addPreference(preference) 
  
   constraints_count=int(input())


   for constrain in range(constraints_count):
       first_index, second_index =input().split()
       halls[int(first_index)-1].addNeighbor(int(second_index)-1)
       halls[int(second_index)-1].addNeighbor(int(first_index)-1)
       edges.append((halls[int(first_index)-1],halls[int(second_index)-1]))


 
   problem=CSP(halls,assigned_halls,edges)
  
   return problem