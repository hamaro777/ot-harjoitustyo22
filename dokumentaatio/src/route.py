class Route():

    def __init__(self, grade, location) -> None:
        self.grade = grade
        self.location = location
        #self.climber = climber

    
    def __str__(self) -> str:
        return f"{self.grade}, {self.location}"