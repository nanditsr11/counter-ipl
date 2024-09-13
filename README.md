## Match Outcome Betting Tracker
This Python script allows two users, Nandit and Rishab, to track the outcomes of cricket matches based on their chosen teams. The script allows them to bet on different stages of the tournament, with winnings increasing at each stage.

## Features
•	Users can input their chosen teams from a predefined list.
•	Tracks results and calculates winnings at different tournament stages: League Stage, Semi-Finals, and Final.
•	Displays current status after each round.
•	Users can choose to continue or stop after each match iteration.

## Prerequisites
•	Python 3 must be installed on your system.

## How to Run the Script
1.	Clone or download the repository containing the script.
2.	Open a terminal and navigate to the folder containing the script.
3.	Run the script using:
            python betting_tracker.py

## Instructions
1.	Select Teams:
o	The script will ask both Nandit and Rishab to enter their chosen team from the list below:
            	RCB, CSK, DC, GT, KKR, LSG, MI, PK, RR, SRH
o	If an invalid team name is entered, the user will be prompted to input a valid team name.

2.	Enter Winner:
o	After each round, input the team that won the match.

3.	Enter Tournament Stage:
o	Input the current stage of the tournament:
            	League Stage: Winner gets 100 units.
            	Semi-Finals: Winner gets 500 units.
            	Final: Winner gets 1000 units.

4.	Winnings Calculation:
o	The script will track how much money Nandit and Rishab owe each other based on who wins.

5.	Current Status:
o	The script will display the current status of the money owed after each round.

6.	Restart Option:
o	After each round, you can decide whether to continue to the next iteration or stop by entering Y (yes) or N (no).

## Example Usage
Enter the team for Nandit : MI
Enter the team for Rishab: CSK

Who is the winner : MI
Nandit's Team :  MI
Rishab's Team :  CSK

Enter the stage of the tournament : League Stage
Rishab Ows Nandit :  100

Current Status:
Nandit's Money:  100
Rishab's Money:  0

Do you want to start a new iteration? (Y/N): Y

## List of Teams
•	RCB – Royal Challengers Bangalore
•	CSK – Chennai Super Kings
•	DC – Delhi Capitals
•	GT – Gujarat Titans
•	KKR – Kolkata Knight Riders
•	LSG – Lucknow Super Giants
•	MI – Mumbai Indians
•	PK – Punjab Kings
•	RR – Rajasthan Royals
•	SRH – Sunrisers Hyderabad

## Stages of the Tournament
•	League Stage – Betting amount: 100 units
•	Semi-Finals – Betting amount: 500 units
•	Final – Betting amount: 1000 units

## License
This project is licensed under the MIT License. See the LICENSE file for details.
