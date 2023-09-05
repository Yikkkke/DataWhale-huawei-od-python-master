# 012 寻找关键钥匙

## 题目描述

小强正在参加《密室逃生》游戏，当前关卡要求找到符合给定密码`K`（升序的不重复小写字母组成）的箱子，并给出箱子编号，箱子编号为1\~N。

每个箱子中都有一个字符串`s`，字符串由大写字母、小写字母、数字、标点符号和空格组成，需要在这些字符串中找到所有的字母，忽略大小写后排列出对应的密码串，并返回匹配密码的箱子序号。

提示：满足条件的箱子不超过1个。

## 输入描述

第一行为`key`的字符串，第二行为箱子`boxes`（数组格式），以空格分隔。

箱子`N`数量满足`1 <= N <= 10000`，`s`长度满足`0 <= s.length <= 50`，密码仅为包含小写字母的升序字符串，且不存在重复字母，密码`K`长度为`K.length`，其中`1 <= K.length <= 26`。

## 输出描述

返回对应箱子编号，如果不存在符合要求的密码箱，则返回-1。

**补充说明：**  
箱子中字符拼出的字符串与密码的匹配忽略大小写，且要求与密码完全匹配，如密码`abc`匹配`aBc`，但是密码`abc`不匹配`abcd`。

## 示例描述

### 示例一

**输入：**
```text
abc
s,sdf123 A2c4b
```

**输出：**
```text
2
```

**说明：**  
第2个箱子中的`Abc`，符合密码`abc`。

### 示例二

**输入：**
```text
abc
s,sdf123 A2c4bd 523[]
```

**输出：**
```text
-1
```

**说明：**  
第2个箱子中的`Abcd`，与密码不完全匹配，不符合要求。

## 解题思路

1. 对箱子的字符串进行字母过滤（找出所有的字母，并转换为小写），得到箱子的有效密码串。
2. 对字符串进行排序，存入已处理好的箱子密码串序列中。
3. 匹配密码，得到箱子序号，直接使用`index`方法，如果找不到，则会报错`ValueError`，捕获错误之后，返回-1。

## 解题代码
```python
def solve_method(key, line):
    boxes = line.split()
    processed_boxes = []
    for box in boxes:
        # 得到箱子的有效密码串
        box_keys = [char.lower() for char in box if char.isalpha()]
        if len(box_keys) > 0:
            # 对字符串排序
            box_keys.sort()
            processed_boxes.append("".join(box_keys))
    try:
        # 返回对应箱子编号
        return processed_boxes.index(key) + 1
    except ValueError:
        # 如果不存在，则返回-1
        return -1


if __name__ == '__main__':
    assert solve_method("abc", "s,sdf123  A2c4b") == 2
    assert solve_method("abc", "s,sdf123 A2c4bd 523[]") == -1
```