team_A_1, team_B_1 = map(int, input().split(":"))
team_A_2, team_B_2 = map(int, input().split(":"))
place = int(input())

sum_A = team_A_1 + team_A_2
sum_B = team_B_1 + team_B_2

goal = sum_B - sum_A
if goal < 0:
    goal = 0
else:
    team_A_2 += goal
    if place == 1 and team_A_2 <= team_B_1 or place == 2 and team_A_1 <= team_B_2:
        goal += 1

print(goal)







