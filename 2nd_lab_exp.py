AIM

To write a Python program to compute batting strike rate, bowling economy rate and check the performance of a player using conditional statements.

Algorithm
Start the program.
Input the number of runs scored and balls faced by the batsman.
Calculate the strike rate using the formula runs divided by balls multiplied by 100.
Use conditional statements to decide whether the batting performance is excellent, good, average or poor.

Next read the runs conceded, overs bowled and wickets taken by the bowler.
Calculate the economy rate by dividing runs conceded by overs bowled.
Apply conditions to evaluate the bowling performance.

Then input the number of catches taken in the field.
If the number of catches is at least one, display that the player is an active fielder.
Otherwise display that the player needs improvement.
End the program.

SOURCE CODE

runs = int(input("Enter runs:"))
balls = int(input("Enter the number of balls faced:"))

strike_rate  = (runs/balls) * 100

if runs > 50 and strike_rate > 120:
    print("Excellent Batter")
elif runs > 30 and strike_rate > 100:
    print("Good Batter")
elif runs > 20:
    print("Average Batter")
else:
    print("Poor Batter")

run_conceded = int(input("Enter run conceded:"))
overs = int(input("Enter overs:"))
wickets = int(input("Enter wickets taken :"))

economy = run_conceded/overs

if wickets >= 3 and economy < 6:
    print("Excellent Bowler")
elif wickets >= 2 and economy < 8:
    print("Good Bowler")
else:
    print("Poor Bowler")

catches = int(input("Enter number of catches:"))

if catches > 2:
    print("Outstanding Fielder")
elif catches == 1:
    print("Active Fielder")
else:
    print("Needs Improvement")

OUTPUT :

Enter runs scored:150
Enter balls faced:25
Excellent Batter

Enter runs conceded:28
Enter overs bowled:6
Enter wickets:3
Good Bowler

Enter number of catches:4
Outstanding Fielder


