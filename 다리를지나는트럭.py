from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * (bridge_length))
    n = len(truck_weights)
    curr = 0

    i = 0
    while i < n or curr != 0:
        answer += 1
        curr -= bridge.popleft()
        if i >= n:
            bridge.append(0)
            continue

        if curr + truck_weights[i] <= weight:
            curr += truck_weights[i]
            bridge.append(truck_weights[i])
            i += 1
        else:
            bridge.append(0)

    return answer
