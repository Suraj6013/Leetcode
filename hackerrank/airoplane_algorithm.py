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


for i in range(len(fuels)):
    E = E - new_distance[i]    
    E = E + fuels[i]     
    if E >= AtoB:
        print(i)
        break
    else:
        print("-1")
        break

