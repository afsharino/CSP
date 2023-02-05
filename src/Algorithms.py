from CSP import CSP
from Utils import *
from MRV import MRV
from LCV import LCV
def forward_checking(problem: CSP, hall_index: int, group_index: int) -> None:
    for neighbor_index in problem.halls[hall_index].neighbors: 
        if group_index in problem.halls[neighbor_index].preferences:
            problem.halls[neighbor_index].preferences.remove(group_index)
