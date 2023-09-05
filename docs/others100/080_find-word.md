# 080 找单词

## 题目描述

给一个字符串和一个二维字符数组，如果该字符串存在于该数组中，则按字符串的字符顺序输出字符串每个字符所在单元格的位置下标字符串，如果找不到返回字符串`N`。规则如下：

1. 需要按照字符串的字符组成顺序搜索，且搜索到的位置必须是相邻单元格，其中“相邻单元格”是指那些水平相邻或垂直相邻的单元格。
2. 同一个单元格内的字母不允许被重复使用。
3. 假定在数组中最多只存在一个可能的匹配。

## 输入描述

第1行是一个数字`N`，表示二维数组在后续输入所占的行数。

第2行到第`N+1`行输入为一个二维大写字符数组，每行字符用`,`分隔。二维数组的大小为`N*N`，其中0 < N <= 100。

第N+2行是待查找的字符串，由大写字符组成。单词长度为`K`，其中0 < K < 1000。

## 输出描述

输出一个位置下标字符串，拼接格式为：
```text
第1个字符行下标,第1个字符列下标,第2个字符行下标,第2个字符列下标,...,第N个字符行下标,第N个字符列下标
```

## 示例描述

### 示例一

**输入：**
```text
4
A,C,C,F
C,D,E,D
B,E,S,S
F,E,C,A
ACCESS
```

**输出：**
```text
0,0,0,1,0,2,1,2,2,2,2,3
```

**说明：**

`ACCESS`分别对应二维数组的`[0,0]`、`[0,1]`、`[0,2]`、`[1,2]`、`[2,2]`、`[2,3]`下标位置。

## 解题思路

**基本思路：** 使用深度优先搜索DFS求解。

1. 遍历矩阵中每一个字母，使用深度优先搜索：
    - 确定参数：当前字母的坐标`row`和`col`、目标字母的位置`k`、已访问字母的坐标列表`visited`。
    - 终止条件：如果遍历到最后一个单词，则表示找到了单词，则返回单词的所有坐标。
    - 递归处理：
        - 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历。
        - 添加该字母的坐标存入已访问列表中。
        - 如果遍历到最后一个单词，则表示找到了单词，返回该字母的坐标。
        - 上下左右进行寻找目标单词的下一个字母。
2. 如果没有找到，则返回`N`。

## 解题代码

```python
def solve_method(matrix, word):
    def dfs(row, col, k, visited, word):
        # 如果出界、字母已访问过、该位置的字母不是目标字母，则没有找到，继续遍历
        if row < 0 or row > m - 1 or col < 0 or col > n - 1 or matrix[row][col] != word[k] or [row, col] in visited:
            return []
        # 添加该字母的坐标存入已访问列表中
        visited.append([row, col])
        # 如果遍历到最后一个单词，则表示找到了单词，返回该字母的坐标
        if k == len(word) - 1:
            return [[row, col]]
        # 上下左右进行寻找目标单词的下一个字母
        for d1, d2 in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            res = dfs(row + d1, col + d2, k + 1, visited, word)
            if res:
                return [[row, col]] + res
        return []

    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == word[0]:
                visited = []
                res = dfs(i, j, 0, visited, word)
                if res:
                    # 如果找到了，则返回单词的所有坐标
                    return [i for x in res for i in x]
    return "N"


if __name__ == '__main__':
    matrix = [["A", "C", "C", "F"],
              ["C", "D", "E", "D"],
              ["B", "E", "S", "S"],
              ["F", "E", "C", "A"]]
    assert solve_method(matrix, "ACCESS") == [0, 0, 0, 1, 0, 2, 1, 2, 2, 2, 2, 3]
```
