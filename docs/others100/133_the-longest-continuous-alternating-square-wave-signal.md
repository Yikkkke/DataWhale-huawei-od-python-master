# 133 最长连续交替方波信号

## 题目描述

输入一串方波信号，求取最长的完全连续交替方波信号，并将其输出，如果有相同长度的交替方波信号，输出任一即可，方波信号高位用1标识，低位用0标识。

说明：
1. 一个完整的信号一定是以0开始，然后以0结尾，即010是一个完整的信号，但101、1010、0101不是。
2. 输入的一串方波信号是由一个或多个完整信号组成。
3. 两个相邻信号之间可能有0个或多个低位，如0110010，011000010。
4. 同一个信号中可能有连续的高位，如01110101011110001010，其中有4个1，是一个具有连续高位的信号。
5. 完全连续交替方波是具有10交替，如01010是完全交替方波，0110不是。

## 输入描述

输入信号字符串，字符串长度`3 <= length <= 1024`。

注：输入总是合法的，不考虑异常情况。

## 输出描述

输出最长的完全连续交替方波信号串，若不存在，则输出-1。

## 示例描述

### 示例一

**输入：**
```text
0010101010110000101000010
```

**输出：**
```text
010101010
```

## 解题思路

1. 设置正则表达式`0(10)+`
2. 遍历字符串
   - 使用正则表达式查找符合的完全连续交替方波信号串
   - 记录字符串位置`pos`
   - 将找到的子串存入结果列表中
3. 将结果列表按照子串长度从大到小排序
4. 如果存在，返回最大长度，如果不存在，返回-1

## 解题代码

```python
import re


def solve_method(line):
    result = []
    # 设置正则表达式
    p = re.compile("0(10)+")
    pos = 0
    while pos < len(line):
        # 使用正则表达式查找
        m = p.search(line, pos)
        # 记录字符串位置
        pos = m.span()[1]
        # 保存子串
        result.append(m.group())
    # 按照子串长度从大到小排序
    result.sort(key=lambda x: len(x), reverse=True)
    # 如果存在，返回最大长度，如果不存在，返回-1
    return result[0] if len(result) != 0 else -1


if __name__ == '__main__':
    assert solve_method("0010101010110000101000010") == "010101010"
```