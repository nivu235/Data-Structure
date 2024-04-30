def calculate_measurement(n, arr):
    last_occurrence = {}
    measurement = 0

    for i in range(n-1, -1, -1):
        if arr[i] not in last_occurrence:
            last_occurrence[arr[i]] = i

    for i in range(n):
        measurement = (measurement + i + last_occurrence[arr[i]])

    return measurement

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
result = calculate_measurement(n, arr)
print(result)
