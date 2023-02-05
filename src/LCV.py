from CSP import CSP


def LCV(problem: CSP, hall: int):
   constraint = {}
   count = 0
   for preference in problem.halls[hall].preferences:
       for neighbor_index in problem.halls[hall].neighbors:
           if not problem.assigned_halls[neighbor_index]:
               if preference in problem.halls[neighbor_index].preferences:
                   count+=1
       constraint[preference] = count
       count = 0


   return sorted(constraint, key=constraint.get)


