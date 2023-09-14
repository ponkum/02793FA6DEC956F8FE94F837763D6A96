class CricketPlayer:
    def __init__(self, name, age, role, batting_average, bowling_average):
        self.name = name
        self.age = age
        self.role = role  # Batsman, Bowler, All-rounder, etc.
        self.batting_average = batting_average
        self.bowling_average = bowling_average

    def bat(self):
        return f"{self.name} is batting."

    def bowl(self):
        return f"{self.name} is bowling."

    def display_player_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Role: {self.role}")
        print(f"Batting Average: {self.batting_average}")
        print(f"Bowling Average: {self.bowling_average}")


# Example usage:
player1 = CricketPlayer("Virat Kohli", 33, "Batsman", 53.00, 0.00)
player2 = CricketPlayer("Jasprit Bumrah", 28, "Bowler", 0.00, 21.64)

print(player1.bat())
print(player2.bowl())

print("\nPlayer 1 Information:")
player1.display_player_info()

print("\nPlayer 2 Information:")
player2.display_player_info()
