# 029 最大报酬

## 题目描述

小明每周上班都会拿到自己的工作清单，工作清单内包含`n`项工作，每项工作都有对应的耗时时间（单位：h）和报酬，工作的总报酬为所有已完成工作的报酬之和，那么请你帮小明安排一下工作，保证小明在指定的工作时间内工作收入最大化。

## 输入描述

输入的第一行为两个正整数`T`和`n`。其中，`T`代表工作时长（单位：h，0 <T < 1000000），`n`代表工作数量（1 < n <= 3000）。

接下来是`n`行，每行包含两个整数`t`和`w`，其中，`t`代表该工作消耗的时长（单位：h，t > 0），`w`代表该项工作的报酬。

## 输出描述

输出小明在指定工作时长内工作可获得的最大报酬。

## 示例描述

### 示例一

**输入：**
```text
40 3
20 10
20 20
20 5
```

**输出：**
```text
30
```

**说明：**  

## 解题思路

**基本思路：** 使用动态规划解题。
1. 获得最短工作时长`min_time`。
2. 使用动态规划：
    - 确定dp数组以及下标的含义：dp[i][j]表示在前i个任务中，花费时间不超过j的最大报酬。
    - 确定递推公式：
         - 如果不做第i个任务，则dp[i][j] = dp[i - 1][j]。
         - 如果做第i个任务，则dp[i][j] = dp[i - 1][j - job[0]] + job[0]。
         - 取dp[i][j]里面最大的那个报酬。
    - dp数组初始化：初始化dp[i][j]都为0。
    - 确定遍历顺序：i从1到`N+1`，j从`mit_time`到`T+1`。
3. 返回在`N`个任务中，花费时间不超过`N`的最大报酬为dp[N][T]。   

## 解题代码

```python
def solve_method(T, jobs):
    N = len(jobs)
    # 最短工作时长
    min_time = min(jobs, key=lambda x: x[0])[0]
    # dp[i][j]表示在前i个任务中，花费时间不超过j的最大报酬
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(min_time, T + 1):
            job = jobs[i - 1]
            w1 = dp[i - 1][j]
            w2 = job[1] + dp[i - 1][j - job[0]] if job[0] <= j else 0
            dp[i][j] = max(w1, w2)
    return dp[N][T]


if __name__ == '__main__':
    jobs = [[20, 10],
            [20, 20],
            [20, 5]]
    assert solve_method(40, jobs) == 30
```