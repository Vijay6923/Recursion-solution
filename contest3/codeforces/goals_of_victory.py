def efficiency_of_missing_team(n, efficiencies):
    total_efficiency = sum(range(1, n + 1))
    known_efficiency = sum(efficiencies)
    missing_efficiency = total_efficiency - known_efficiency
    return missing_efficiency

def main():
    t = int(input()) # number of test cases
    for _ in range(t):
        n = int(input()) # number of teams
        efficiencies = list(map(int, input().split())) # efficiencies of n-1 teams
        missing_efficiency = efficiency_of_missing_team(n, efficiencies)
        print(missing_efficiency)

if __name__ == "__main__":
    main()
