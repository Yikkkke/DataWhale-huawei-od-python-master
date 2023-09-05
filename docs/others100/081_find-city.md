# 081 找城市、城市聚集度

## 题目描述

一张地图上有`n`个城市，城市和城市之间有且只有一条道路相连：要么直接相连，要么通过其它城市中转相连（可中转一次或多次）。城市与城市之间的道路都不会成环。

当切断通往某个城市`i`的所有道路后，地图上将分为多个连通的城市群，设该城市`i`的聚集度为DP[i] (Degree of Polymerization)，公式如下：

DP[i]=max(城市群1的城市个数,城市群2的城市个数,...,城市群`m`的城市个数)

请找出地图上DP值最小的城市，即找到城市`j`，使得DP[j]=min(DP[1],DP[2],...,DP[n])。

提示：
- 如果有多个城市都满足条件，这些城市都要找出来（可能存在多个解）。
- DP[i]的计算，可以理解为已知一棵树，删除某个节点后，生成的多个子树，求解多个子树节点数的问题。

## 输入描述

第一行有一个整数`N`，表示有`N`个节点。取值范围是1 <= N <= 1000。

接下来的`N-1`行，每行有两个整数`x`、`y`，表示城市`x`与城市`y`连接。取值范围是1 <= x,y <= N。

## 输出描述

输出城市的编号。如果有多个，按照编号升序输出。

## 示例描述

### 示例一

**输入：**
```text
5
1 2
2 3
3 4
4 5
```

**输出：**
```text
3
```

**说明：**

对于城市3，切断通往3的所有道路后，形成2个城市群`[(1,2), (4,5)]`，其聚集度分别都是2，DP[3]=2。

对于城市4，切断通往4的所有道路后，形成2个城市群`[(1,2,3),(5)]`，DP[4] = max(3,1) = 3。

依次类推，切断其他城市的所有道路后，得到的DP都会大于2，因此城市3就是满足条件的城市，输出是3。

### 示例二

**输入：**
```text
6
1 2
2 3
2 5
3 4
3 6
```

**输出：**
```text
2 3
```

**说明：**  

将通往2或者3的所有路径切断，最大城市群数量是3，其他任意城市切断后，最大城市群数量都比3大，所以输出`2 3`。

## 解题思路

**基本思路：** xxxxx（注：如果存在基本思路，可编写）
1. 初始化dp数组，表示城市的聚集度。
2. 遍历城市`i`：
    - 在道路上，删除该城市（即切断通往该城市的所有道路）。
    - 初始化城市群集合`urban`，每个元素是`set`集合，表示城市群。
    - 初始化城市群标识，如果有交集，表示有道路连接到这个城市群，则为True，如果没有，则为False
      - 如果都没有道路连接该城市，则添加单独城市群。
      - 如果有道路连接该城市，则直接并入已有城市群。
    - 计算聚集度dp。
3. 得到最小的聚集度的城市。   

## 解题代码

```python
from copy import deepcopy


def solve_method(n, city_roads):
    dp = [0] * n
    for i in range(1, n + 1):
        copy_roads = deepcopy(city_roads)
        urban = []

        for x in copy_roads:
            if i in x:
                x.remove(i)

            cities = set(x)
            if len(urban) == 0:
                urban.append(cities)
            else:
                # 如果有交集，表示有道路连接到这个城市群，则为True，如果没有，则为False
                mask_city = [True if len(cities.intersection(x)) > 0 else False for x in urban]

                if not any(mask_city):
                    # 如果都没有，则添加单独城市群
                    urban.append(cities)
                else:
                    # 如果有，则直接并入已有城市群
                    index = mask_city.index(True)
                    urban[index] = urban[index].union(cities)

        # 计算聚集度dp
        dp[i - 1] = max([len(x) for x in urban])

    # 得到最小的聚集度的城市
    min_value = min(dp)
    return [i + 1 for i, x in enumerate(dp) if x == min_value]


if __name__ == '__main__':
    roads = [[1, 2],
             [2, 3],
             [3, 4],
             [4, 5]]
    assert solve_method(5, roads) == [3]

    roads = [[1, 2],
             [2, 3],
             [2, 5],
             [3, 4],
             [3, 6]]
    assert solve_method(6, roads) == [2, 3]
```