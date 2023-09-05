# 135 有效子字符串

## 题目描述

输入两个字符串`S`和`L`，都只包含小写字母，其中，`S长度 <= 100`，`L长度 <= 500000`，判断`S`是否是`L`的有效子字符串

判断规则：`S`中的每个字符在`L`中都能找到（可以不连续），且`S`在`L`中字符的前后顺序与`S`中顺序要保持一致。

**例如：**

`S`为`ace`，`L`为`abcde`，S是L的一个子序列，且有效字符是`a`、`c`、`e`，而`aec`不是有效子序列，且有效字符只有`a`和`e`。

## 输入描述

输入两个字符串`S`和`L`，都只包含小写字母，其中，`S长度 <= 100`，`L长度 <= 500000`，先输入`S`，再输入`L`，每个字符串占一行。

## 输出描述

`S`串最后一个有效字符在`L`中的位置，首位从0开始计算，无有效字符，则返回-1。

## 示例描述

### 示例一

**输入：**
```text
acce
abcde
```

**输出：**
```text
4
```

### 示例二

**输入：**
```text
fgh
abcde
```

**输出：**
```text
-1
```

## 解题思路

1. 初始化有效位置`last_valid_index`为-1。
2. 遍历S字符串中的每一个字符：
   - 判断有效位置是否还在L长度范围内
   - 如果在，判断S中的字符是否等于L中的字符
        - 如果相等，则跳出while循环，继续遍历S字符串
   - 如果超过L长度范围，表示S字符串还有字符，有效长度`last_valid_index`置为-1，直接跳出遍历 
3. 返回有效长度`last_valid_index`

## 解题代码

```python
def solve_method(s, l):
    last_valid_index = -1
    for ch in s:
        # 判断有效位置是否还在L长度范围内
        while last_valid_index < len(l) - 1:
            last_valid_index += 1
            # 判断S中的字符是否等于L中的字符
            if ch == l[last_valid_index]:
                # 如果相等，则跳出while循环，继续遍历S字符串
                break
        else:
            # 当有效位置已经超过了L长度范围，但S字符串还有字符，直接跳出遍历
            last_valid_index = -1
            break
    return last_valid_index


if __name__ == '__main__':
    assert solve_method("ace", "abcde") == 4
    assert solve_method("fgh", "abcde") == -1
    assert solve_method("acce", "abcdec") == -1
```