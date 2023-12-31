# 032 分苹果

## 题目描述

`AB`两个人把苹果分为两堆，`A`希望按照他的计算规则等分苹果，他的计算规则是按照二进制加法计算，并且不计算仅为`12+5=9(1100+0101=9)`，`B`的计算规则是十进制加法，包括正常进位，`B`希望在满足`A`的情况下获取苹果重量最多。

他的计算规则是按照二级制加法计算，并且不计算进位 `12+5-9(1100+0101=9)`，`B` 的计算规则是十进制加法，包括正常进位, `B` 希望在满足 `A` 的情况下获取苹果重量最多

输入苹果的数量和每个苹果重量，输出满足`A`的情况下`B`获取的苹果总重量，如果无法满足`A`的要求，输出-1。

## 输入描述

输入第一行是苹果数量：3。

输入第二行是每个苹果重量: 3 5 6。

## 输出描述

输出第一行是`B`获取的苹果总重量：11。

## 示例描述

### 示例一

**输入：**

```text
3
3 5 6
```

**输出：**

```text
11
```

### 示例二

**输入：**

```text
8
7258 6579 2602 6716 3050 3564 5396 1773
```

**输出：**

```text
35165
```

## 解题思路

**基本思路：** 二进制的异或运算等同于不进位的加法运算。

1. 遍历每一个积木的重量：
    - 进行重复的异或运算。
2. 判断运算结果是否为0：
    - 如果为0，表示可以分为两堆苹果，减去其中最小的值，返回最大的苹果重量。
    - 如果不为0，表示无法分为两堆，返回-1。

## 解题代码

```Python
def solve_method(apples):
    count = 0
    for i in apples:
        # 进行异或运算，等同于不进位的加法
        count = count ^ i
    if count == 0:
        return sum(apples) - min(apples)
    else:
        return -1


if __name__ == '__main__':
    assert solve_method([3, 5, 6]) == 11
    assert solve_method([7258, 6579, 2602, 6716, 3050, 3564, 5396, 1773]) == 35165
```

