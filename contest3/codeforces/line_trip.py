def min_gas_volume(t, test_cases):
    for i in range(t):
        n, x = test_cases[i][0]
        gas_stations = test_cases[i][1]
        max_distance_between_stations = max(gas_stations[j] - gas_stations[j-1] for j in range(1, n))
        
        min_gas = max_distance_between_stations
        min_gas = max(min_gas, gas_stations[0])
        min_gas = max(min_gas, x - gas_stations[-1])
        
        print(min_gas)


t = int(input("Enter the number of test cases: "))
test_cases = []
for _ in range(t):
    n, x = map(int, input().split())
    stations = list(map(int, input().split()))
    test_cases.append((n, x, stations))


min_gas_volume(t, test_cases)
