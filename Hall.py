class Hall:
    neighbors: list[int]
    preferences: list[int]

    def __init__(self, neighbors: list['Hall'], preferences: list[int]) -> None:
        self.neighbors = neighbors
        self.preferences = preferences
        
    def addNeighbor(self, hall: int) -> None:
        self.neighbors.append(hall)

    def addPreference(self, group: int) -> None:
        self.preferences.append(group)