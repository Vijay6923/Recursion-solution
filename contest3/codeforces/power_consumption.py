def calculate_power_consumption(period_duration, current_mode, P1, P2, P3, T1, T2):
    if current_mode == 0:
        return period_duration * P1
    elif current_mode == 1:
        t1_duration = min(period_duration, T1)
        return t1_duration * P1 + max(0, period_duration - T1) * P2
    else:  # current_mode == 2
        t2_duration = min(period_duration, T2)
        t1_duration = min(t2_duration, T1)
        return t1_duration * P1 + max(0, t1_duration - T1) * P2 + max(0, t2_duration - T1) * P2 + max(0, period_duration - T2) * P3

n, P1, P2, P3, T1, T2 = map(int, input().split())

total_power_consumption = 0
current_mode = 0
last_interaction_time = 0

for _ in range(n):
    l, r = map(int, input().split())
    
    # Calculate the time period for this work session
    period_duration = r - l
    
    # Calculate power consumption during this period
    total_power_consumption += calculate_power_consumption(period_duration, current_mode, P1, P2, P3, T1, T2)
    
    # Check if there's a transition to screensaver mode within this work session
    if last_interaction_time + T1 <= l:
        current_mode = 1
    # Check if there's a transition to sleep mode within this work session
    if last_interaction_time + T2 <= l:
        current_mode = 2
    
    # Update current mode and last interaction time
    last_interaction_time = r
    # If the next work session starts immediately after this one, no change in mode is needed
    if _ < n - 1 and last_interaction_time == l:
        continue
    # Check if there's a transition to screensaver mode after this work session
    if last_interaction_time + T1 <= r:
        current_mode = 1
    # Check if there's a transition to sleep mode after this work session
    if last_interaction_time + T2 <= r:
        current_mode = 2

print(total_power_consumption)
