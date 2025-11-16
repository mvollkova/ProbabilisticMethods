import random

def zad1():
    y = random.random()
    x = 100 * y + 50 #przedz 50 150
    return x

def zad2():
    liczb = random.random()
    
    if liczb < 0.1:
        return 1
    elif liczb < 0.4: 
        return 2
    elif liczb < 0.8:  
        return 3
    else:              
        return 4

if __name__ == '__main__':
    print("zadanie 1:")
    listbucket = []
    for i in range(100000):
        listbucket.append(zad1())
    buckets = [0] * 10
    for num in listbucket:
        buck_index = int((num - 50) / 10) # 50-60,60-70 ...
        buckets[buck_index] += 1
    for count in buckets:
        print(count, end = ' ')

    print("\n")

    print("zadanie 2:")
    
    listbucket = []
    for i in range(100000):
        listbucket.append(zad2())
    buckets = [0] * 4 #przedz 4
    for num in listbucket:
        buck_index = num - 1
        buckets[buck_index] += 1
    for count in buckets:
        print(count, end=' ')



