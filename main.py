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
