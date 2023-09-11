from itertools import combinations

def solve_method(array, num):
    result = []

    chain_1 = [i for i in array if i>=0 and i<=3]
    chain_2 = [i for i in array if i>=4 and i<=7]
    n_1 = len(chain_1)
    n_2 = len(chain_2)
    priority = []

    if num==1:
        priority = [1, 3, 2, 4]
    elif num==2:
        priority = [2, 4, 3]
    elif num==4:
        priority = [4]
    elif num==8 and len(array)==8:
        return array

    # 判断哪个链路优先
    if priority.count(n_1) and priority.count(n_2):
        i_1 = priority.index(n_1)
        i_2 = priority.index(n_2)
        if i_1 < i_2:
            return cpuN(chain_1, num)
        elif i_1 > i_2:
            return cpuN(chain_2, num)
        else:
            return cpuN(chain_1, num) + cpuN(chain_2, num)
    elif priority.count(n_1):
        return cpuN(chain_1, num)
    elif priority.count(n_2):
        return cpuN(chain_2, num)

    return result

def cpuN(array, num):
    combine = list(combinations(array, num))
    combine = [list(i) for i in combine]
    return combine


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7]
    num = 4
    print(solve_method(array, num))