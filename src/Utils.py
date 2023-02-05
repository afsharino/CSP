from CSP import CSP
from Hall import Hall
def has_conflict(problem: CSP, hall_index: int, group_index: int) -> bool:
    for neighbor in problem.halls[hall_index].neighbors:
        if problem.halls[neighbor].preferences == [group_index]:
            return True
    return False

def goal_test(problem: CSP) -> bool:
    for assigned in problem.assigned_halls:
        if not assigned:
            return False
    return True

def zero_preferences(problem: CSP) -> bool:
    for hall in problem.halls:
        if len(hall.preferences) == 0:
            return True
    return False

def set_uncommon_preferences(hall_one : Hall, hall_two : Hall) -> bool:
    had_common = False
    temp=False
    for value in hall_one.preferences:
        temp=False
        for value2 in hall_two.preferences:
            if value == value2:
                temp=True
        if temp :
            hall_one.preferences.remove(value)
            had_common = True       
    
        
    return had_common