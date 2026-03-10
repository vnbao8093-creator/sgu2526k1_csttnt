def read_input():
    n = int(input())
    A = []
    
    for _ in range(n):
        A.append(input().strip())
        
    return n, A


def Try(k, n, A, perm, used, result):

    for i in range(n):

        if not used[i]:

            perm[k] = A[i]
            used[i] = True

            if k == n-1:
                result.append(perm.copy())
            else:
                Try(k+1, n, A, perm, used, result)

            used[i] = False


def permutations(A):

    n = len(A)
    perm = [None]*n
    used = [False]*n
    result = []

    Try(0, n, A, perm, used, result)

    return result


def main():

    n, A = read_input()

    result = permutations(A)

    print(len(result))

    for p in result:
        print(*p)


if __name__ == "__main__":
    main()