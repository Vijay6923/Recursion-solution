def determine_winner(n, goals):
    goal_count = {}
    
    for team in goals:
        if team in goal_count:
            goal_count[team] += 1
        else:
            goal_count[team] = 1
    winner = max(goal_count, key=goal_count.get)
    return winner
n = int(input())
goals = [input().strip() for _ in range(n)]
winner = determine_winner(n, goals)
print(winner)