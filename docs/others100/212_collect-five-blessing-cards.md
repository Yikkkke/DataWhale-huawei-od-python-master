# 212 集五福

## 题目描述

集五福作为近年来大家喜闻乐见迎新春的或哦那个，收集爱国福、富强福、和谐福、友善福、敬业福，即可分享超大红包。

以0和1组成长度为5的字符串，代表每个人所得到的福卡，每一位代表一种福卡，1表示已经获得该福卡，单类型福卡不超过1张，随机抽取一个小于10人团队，求该团队最多可以集齐多少套五福？

## 输入描述

输入若干个`11010`、`00110`的由0和1组成的长度等于5位的字符串，代表团队中每个人福卡的获得情况。

注意：
- 1人也可以是一个团队。
- 1人可以有0到5张福卡，但福卡不能重复。

## 输出描述

输出该团队能凑齐多少套五福

## 示例描述

### 示例一

**输入：**
```text
11001,11101
```

**输出：**
```text
0
```

### 示例二

**输入：**
```text
11101,10111
```

**输出：**
```text
1
```

## 解题思路

1. 初始化结果列表，表示每种福卡的个数。
2. 遍历团队：
   - 遍历每人的福卡：如果为1，将该种福卡的个数加1
3. 将结果列表排序，返回里面的最小值

## 解题代码

```python
def solve_method(arr):
    result = [0] * 5

    for cards in arr:
        for i in range(5):
            if cards[i] == "1":
                result[i] += 1

    return min(result)


if __name__ == '__main__':
    assert solve_method(["11001", "11101"]) == 0
    assert solve_method(["11101", "10111"]) == 1
```