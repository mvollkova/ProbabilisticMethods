def gen_liniowy(xn, a, c, m, n, list):
    for i in range(n):
        xn = (a * xn + c) % m
        list.append(xn)
    return list


def gen_rej(n, p, q, arr, list):
    for i in range(n):
        iter = 7
        while iter != 31:
            arr[iter] = arr[iter - p] ^ arr[iter - q]
            iter += 1

        number = 0
        for j in range(31):
            number = (number << 1) | arr[j]

        list.append(number)

        tmp = arr[24:31]
        arr = [0] * 31
        arr[:7] = tmp
    return list


def print_arr(list, m):
    buckets = [0] * 10
    for num in list:
        bucket_index = min(num // (m // 10), 9)
        buckets[bucket_index] += 1
    suma = 0
    for count in buckets:
        suma += count
        print(count, end=' ')
    print(' ')


def main():
    a = 69069
    c = 1
    m = 2 ** 31
    xn = 15
    n = 100000
    list = [xn]
    list = gen_liniowy(xn, a, c, m, n, list)
    print("Generator liniowy: ")
    print_arr(list, m)

    p = 7
    q = 3
    arr = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    list2 = []

    list2 = gen_rej(n, p, q, arr, list2)
    print("Generator rejestrowy: ")
    print_arr(list2, m)


if __name__ == "__main__":
    main()





