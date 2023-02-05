from CSP import CSP
import math


def find_Least_preference(problem:CSP)->int:
   least_preference=math.inf
   for hall_index in range(len(problem.halls)):
       hall_pref_size=len(problem.halls[hall_index].preferences)
       if not problem.assigned_halls[hall_index]:
           if hall_pref_size < least_preference:
               least_preference = hall_pref_size
   return least_preference




def find_highest_neighbor(problem:CSP, least_pref:int):
   highest_neighbor=-1*math.inf
   hall=0
   for hall_index in range(len(problem.halls)):
       hall_pref_size=len(problem.halls[hall_index].preferences)
       hall_neighbor_size=len(problem.halls[hall_index].neighbors)
       if hall_pref_size == least_pref and not problem.assigned_halls[hall_index]:
           if hall_neighbor_size > highest_neighbor:
               highest_neighbor = hall_neighbor_size
               hall = hall_index
   return hall  


def MRV(problem: CSP) -> int:
  return find_highest_neighbor(problem,find_Least_preference(problem))