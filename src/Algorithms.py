from CSP import CSP
from Utils import *
from MRV import MRV
from LCV import LCV
def forward_checking(problem: CSP, hall_index: int, group_index: int) -> None:
    for neighbor_index in problem.halls[hall_index].neighbors: 
        if group_index in problem.halls[neighbor_index].preferences:
            problem.halls[neighbor_index].preferences.remove(group_index)


def AC3(problem: CSP , conflicts:list=None) -> bool:
    if conflicts == None:
        conflicts = problem.edges

    while conflicts:
        (hall_one,hall_two)= conflicts.pop(0)
        if set_uncommon_preferences(hall_one, hall_two):
            if len(hall_one.preferences) == 0: 
                return False
            for neighbor_index in hall_one.neighbors:
                neighbor_hall = problem.halls[neighbor_index]
                if (neighbor_hall, hall_one) not in conflicts:
                    conflicts.append((neighbor_hall, hall_one))
                    
    return True

 
def backtracking(problem: CSP) -> CSP | None:
    stack = [(problem, None, None)]

    while stack:
        state, hall, group = stack.pop()

        if zero_preferences(state):
            continue

        if goal_test(state):
            return state

        if hall != None:
            forward_checking(state, hall, group)
            
        else:
            if not AC3(state):
                return None
        hall = MRV(state)
        for group in LCV(state, hall)[-1::-1]:
            if not has_conflict(state, hall, group):
                newProblem=CSP(state.halls,state.assigned_halls,state.edges)
                newProblem.halls[hall].preferences = [group]
                newProblem.assigned_halls[hall] = True
                stack.append((newProblem, hall, group))
        
    return None