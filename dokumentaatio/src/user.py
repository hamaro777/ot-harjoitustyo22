

class User():

    def __init__(self, name: str, password: str) -> None:
        self.name = name
        self.password = password
    
    def __str__(self) -> str:
        return (f"{self.name}, {self.password}")