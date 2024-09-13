class BettingGame:
    def __init__(self):
        self.Teams = ["RCB", "CSK", "DC", "GT", "KKR", "LSG", "MI", "PK", "RR", "SRH"]
        self.Stages = ["League Stage", "Semi-Finals", "Final"]
        self.Nandit = []
        self.Rishab = []
        self.Nandit_Money = 0
        self.Rishab_Money = 0

    def input_team(self, player_name):
        while True:
            team = input(f"Enter the team for {player_name}: ")
            if team in self.Teams:
                return team
            print("Invalid team name. Please enter a valid team name.")

    def input_stage(self):
        while True:
            stage = input("Enter the stage of the tournament: ")
            if stage in self.Stages:
                return stage
            print("Invalid stage. Please enter a valid stage.")

    def determine_winner(self, nandit_team, rishab_team):
        winner = input("Who is the winner: ")
        if winner == nandit_team:
            return "Nandit"
        elif winner == rishab_team:
            return "Rishab"
        else:
            print("Invalid winner. Please enter a valid winner.")
            return self.determine_winner(nandit_team, rishab_team)

    def update_wallets(self, stage, winner):
        prize_money = {"League Stage": 100, "Semi-Finals": 500, "Final": 1000}
        if winner == "Nandit":
            self.Nandit_Money += prize_money[stage]
            print(f"Rishab owes Nandit: {self.Nandit_Money}")
        else:
            self.Rishab_Money += prize_money[stage]
            print(f"Nandit owes Rishab: {self.Rishab_Money}")

    def print_status(self):
        print("\nCurrent Status:")
        print(f"Nandit's Money: {self.Nandit_Money}")
        print(f"Rishab's Money: {self.Rishab_Money}\n")

    def play(self):
        while True:
            nandit_team = self.input_team("Nandit")
            self.Nandit.append(nandit_team)
            
            rishab_team = self.input_team("Rishab")
            self.Rishab.append(rishab_team)

            stage = self.input_stage()
            winner = self.determine_winner(nandit_team, rishab_team)

            self.update_wallets(stage, winner)
            self.print_status()

            # Break the loop if the Final stage is played
            if stage == "Final":
                print("The Final stage has been played. Ending the game.")
                break

            restart = input("Do you want to start a new iteration? (Y/N): ").lower()
            if restart == 'n':
                break


if __name__ == "__main__":
    game = BettingGame()
    game.play()
