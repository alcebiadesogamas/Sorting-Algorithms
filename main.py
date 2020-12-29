alvo = [1,6,3,5,4,7,9,2,8]
flag =  1
print(alvo)

while flag:
    flag = 0
    for i in range(len(alvo)-1):
        if alvo[i] > alvo[i+1]:
            flag = 1
            alvo[i],alvo[i+1] = alvo[i+1], alvo[i]
print(f'{"Bubble Sort":#^30}')
print(alvo)


for i in range(1,len(alvo)):
    indexMenor = i-1
    for j in range(i, len(alvo)):
        if alvo[j] < alvo[indexMenor]:
            indexMenor = j
    alvo[i-1],alvo[indexMenor] = alvo[indexMenor], alvo[i-1]
print(f'{"Insertion Sort":#^30}')    
print(alvo)
