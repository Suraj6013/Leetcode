N = int(input())
user_input = input()
distance = list(map(int, user_input.split()))
F = int(input())
user_input = input()
fuels = list(map(int, user_input.split()))
AtoB = int(input())
E = int(input())
new_distance = [distance[0]]
for i in range(len(distance)-1):
    x = distance[i+1]-distance[i]
    new_distance.append(x)
print(new_distance)