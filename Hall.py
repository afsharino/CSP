class Hall:
    neighbors: list[int]
    preferences: list[int]

    def __init__(self, neighbors: list['Hall'], preferences: list[int]) -> None:
        self.neighbors = neighbors
        self.preferences = preferences
