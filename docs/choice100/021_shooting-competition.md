# 021 投篮大赛

## 题目描述

你现在是一场采用特殊赛制投篮大赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。

比赛开始时，记录是空白的，你会得到一个记录操作的字符串列表`ops`，其中`ops[i]`是你需要记录的第`i`项操作，`ops`遵循下述规则：
- 整数`x`表示本回合新获得分数`x`
- `+`表示本回合新获得的得分是前两次得分的总和
- `D`表示本回合新获得的得分是前一次得分的两倍
- `C`表示本回合没有分数，并且前一次得分无效，将其从记录中移除

请你返回记录中所有得分的总和。

## 输入描述

输入为一个字符串数组。

## 输出描述

输出为一个整型数字。

## 备注

- 1 <= ops.length <= 1000
- `ops[i]`为`C`、`D`、`+`，或者一个表示整型的字符串，整数范围是`[-3*104, 3*104]`
- 需要考虑异常的存在，如有异常情况，请返回-1
- 对于`+`操作，题目数据不保证记录此操作时，前面总是存在两个有效的分数
- 对于`C`和`D`操作，题目数据不保证记录此操作时，前面存在一个有效的分数
- 题目输出范围不会超过整型的最大范围，不会超过 263-1

## 示例描述

### 示例一

**输入：**
```text
5 2 C D +
```

**输出：**
```text
30
```

**说明：**  
- `5`：记录加5，记录现在是[5]
- `2`：记录加2，记录现在是[5, 2]
- `C`：使前一次得分的记录无效并将其移除，记录现在是[5]
- `D`：记录加2 * 5 = 10，记录现在是[5, 10]
- `+`：记录加5 + 10 = 15，记录现在是[5, 10, 15]
所有得分的总和：5 + 10 + 15 = 30

### 示例二

**输入：**
```text
5 -2 4 C D 9 + +
```

**输出：**
```text
27
```

**说明：**  
- `5`：记录加5，记录现在是[5]
- `-2`：记录加-2，记录现在是[5, -2]
- `4`：记录加4，记录现在是[5, -2, 4]
- `C`：使前一次得分的记录无效并将其移除，记录现在是[5, -2]
- `D`：记录加2 * -2 = -4，记录现在是[5, -2, -4]
- `9`：记录加9，记录现在是[5, -2, -4, 9]
- `+`：记录加-4 + 9 = 5，记录现在是[5, -2, -4, 9, 5]
- `+`：记录加9 + 5 = 14，记录现在是[5, -2, -4, 9, 5, 14]
所有得分的总和：5 + -2 + -4 + 9 + 5 + 14 = 27

### 示例三

**输入：**
```text
1
```

**输出：**
```text
1
```

### 示例四

**输入：**
```text
+
```

**输出：**
```text
-1
```

## 解题思路

1. 由于本题需要考虑异常情况的存在，可以使用`try-exception`和`raise`解决。
2. 初始化`scores`数组。   
3. 循环遍历`ops`，根据规则，对各个指令进行处理，并对`scores`数组进行操作。
4. 返回`scores`数组的所有元素之和。

## 解题代码

```python
def solve_method(ops):
    scores = []
    try:
        for op in ops:
            if op == "C":
                if len(scores) < 1:
                    raise ValueError
                scores.pop()
            elif op == "D":
                if len(scores) < 1:
                    raise ValueError
                scores.append(2 * scores[-1])
            elif op == "+":
                if len(scores) < 2:
                    raise ValueError
                scores.append(scores[-1] + scores[-2])
            else:
                scores.append(op)

        return sum(scores)
    except ValueError:
        return -1

    
if __name__ == '__main__':
    ops = [5, 2, "C", "D", "+"]
    assert solve_method(ops) == 30

    ops = [5, -2, 4, "C", "D", 9, "+", "+"]
    assert solve_method(ops) == 27

    ops = [1]
    assert solve_method(ops) == 1

    ops = ["+"]
    assert solve_method(ops) == -1
```