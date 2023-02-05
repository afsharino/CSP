from Hall import Hall

class CSP:
    def __init__(self, halls: list['Hall'], assigned_halls: list[bool], edges: list[tuple['Hall', 'Hall']]) -> None:
        self.halls = halls
        self.assigned_halls = assigned_halls
        self.edges = edges
