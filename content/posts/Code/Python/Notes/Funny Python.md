---
title: Funny Python
date: 2021-03-02T13:43:21+08:00
toc: true
images:
tags:
  - Python
---

# 有趣/有用的包/模块/用法

记录一些日常用得上的小工具

## `collections` 容器数据类型



### `Counter`计数器

```python
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counters = Counter(words)
```
可以把list传入Counter类来创建一个计数器
```python
>>> word_counters['eyes']
8

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counters2 = Counter(morewords)

sub_counter = word_counter1 - word_counter2
```
可以将两个Counter进行数学运算 + - & |

还有一些自带的方法



#### `elements()`

返回一个迭代器，重复value次的key -- [key]*value，若value < 0,忽略

相当于反向Counter的迭代器
```python
>>> list(Counter({2: 2, 4: 1, 6: 1, 3: 1, 1: 1}).elements())
[2, 2, 4, 6, 3, 1]

```



#### `most_common(n)`

返回最多出现的n个元素



#### `subtract(iterable-or-mapping)`

从迭代对象减去元素，和 操作符 - **貌似不一样，待考究**

```
>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)
>>> c.subtract(d)
>>> c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```



#### `update(iterable-or-mapping)`

从迭代元素加上，和subtract相反, 和操作符 + 一样效果



### `defaultdict`

自动创建要访问的键的映射实体
```python
from collections import defaultdict
d = defaultdict(list)
d['a'] = append(1) # 这种情况不会报错，因为已经有了默认的list映射实体
```



### `namedtuple`命名元组

可以通过名称来访问元素，而不用通过下标来访问（容易让代码不清晰和混乱）
```python
from collections import namedtuple
People = namedtuple('People', ['age', 'name', 'sex'])
p1 = People(24, 'dz', 'male')
p1.age

# Outputs 24
```

> 但是命名元组的元素值不可更改

*若真的要改变值，使用_replace()方法，会创建一个新的命名元组，并取代需要替换的值*

```python
p1 = p1._replace(age = 25)

# Outputs People(age=25, name='dz', sex='male')
```
可以利用这个方法来填充数据（更新数据）

```python
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)

>>> a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
>>> dict_to_stock(a)
# Outputs Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
```



### `ChainMap`

接受多个字典，并逻辑上变为一个字典(映射组合)

ChainMap类会在内部创建一个容纳这些字典的列表

如果出现重复键，第一次出现的映射值会被返回

```
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a, b)
print(c['z'])

# OutPuts 3
```

相比于`update()`方法的合并，`ChainMap`能读取到改变的值变化，update使创建了一个新的存储对象

```
c['z'] = 92
print(a['z'])

# OutPuts 92
```

ChainMap 对于编程语言中的作用范围变量（比如 globals , locals 等）是非常有用的。

```
>>> values = ChainMap()
>>> values['x'] = 1
>>> # Add a new mapping
>>> values = values.new_child()
>>> values['x'] = 2
>>> # Add a new mapping
>>> values = values.new_child()
>>> values['x'] = 3
>>> values
ChainMap({'x': 3}, {'x': 2}, {'x': 1})
>>> values['x']
3
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
2
>>> # Discard last mapping
>>> values = values.parents
>>> values['x']
1
>>> values
ChainMap({'x': 1})
>>>
```


***





## `functools`高阶函数

### `accumulate`

用来做累计的操作（可以加减乘除，其他运算等）

```python
from functools import accumulate
import operator

l = [3, 4, 5]
print(list(accumulate(l, operator.mul)))
# [3, 12, 60]
```









## `operator` 运算符替代函数



### `itemgetter`

可以记录查找值的索引参数，可以是key或者index
```python
from operator import itemgetter
getter = itemgetter(1,3,4)
a = ['a', 'b', 'c', 'd', 'e']

>>> getter(a)
('b', 'd', 'e')
```

> `attrgetter()`类似，但用于获取实例属性


***





## 内置方法 / 自带模块

### `str`



判断字符串是否数字：`str.isdigit()`

判断字符串是否字母：`str.isalpha()`

判断字符串内所有字符是否大写：`str.isupper()`
判断字符串内所有字符是否小写：`str.islower()`




### `print`

`print`*(\***objects**, sep=' ', end='\n', file=sys.stdout, flush=False)*

file：把objects打印到指定文本流

sep：objects之间的分隔符

end：末尾加上end

flush: 是否print的时候立刻刷新，不经过缓存，对于文件流等地方有用。

```python
f = open('test.txt', 'w')
print('123', file=f, flush=True)
```

这时候，不用 `f.close`即可在文件 `test.txt`里看到内容





### `filter`

过滤器，可以通过创建过滤代码传入来过滤列表

会创建生成一个迭代器
```
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)
# Outputs ['1', '2', '-3', '4', '5']
```



### `iter(object[, sentinel])`

返回一个迭代器对象，第二个参数可以定义迭代器结束的条件。

```python
with open('test.txt') as fp:
    for line in iter(fp.readline, ''):
        # 遇到空字符串则停止
        process_line(line)
```





### `heapq` 堆队列算法

堆是一个二叉树，每个父节点的值只会小于或大于所有孩子的节点的值。

使用`heapify()`来把list转换成堆。

#### `heqppush(heap, item)`

把 *item* 值加入到 heap 中



#### `heappop(heap)`

弹出并返回 heap 最小元素，若堆为空，抛出 *IndexError*。



#### `heappushpop(heap, item)`

把item放入堆中，弹出返回 heap 最小元素。比 `heappush` + `heappop`更有效率。



#### `heapify(x)`

把 list 转换成堆，原地，线性时间。



#### `heapreplace(heap, item)`

把最小的元素pop，用新的item替换。如果空，抛出 *IndexError*。



#### `heapq.merge(*iterables, key=None, reverse=False)`

把多个可迭代对象组合排序，返回的是迭代器。

> **输入的迭代对象必须是排过序的**，它只是通过检查序列的开始部分并返回最小，而不会预先读取到堆栈。

和 `sorted(itertools.chain(*iterables))`类似，不过返回的迭代器。

*key* 可以设置输入的迭代对象按照 key方法排序。



#### `nlargest(n, iterable, key=None)`

返回堆的n个最大元素



#### `nsmallest(n, iterable, key=None)`

返回堆的n个最小元素






# TODO--re 待补充

### `re`
强大的正则

- re.split()
```python
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
re.split(r'[;,\s]\s*', line)

# OutPut ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
```
上面的例子把任意个的逗号，分号或空格当作分隔符分割字符串



### `fnmatch`
使用常用的通配符匹配字符串

```
>>> from fnmatch import fnmatch, fnmatchcase
>>> fnmatch('foo.txt', '*.txt')
True
>>> fnmatch('foo.txt', '?oo.txt')
True
>>> fnmatch('Dat45.csv', 'Dat[0-9]*')
True
>>> names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
>>> [name for name in names if fnmatch(name, 'Dat*.csv')]
['Dat1.csv', 'Dat2.csv']
>>>
```

> `fnmatch` 在Windows上对大小写不敏感，Mac上敏感；而`fnmatchcase()` 会完全使用模式里的大小写


|模式|含义|
|---|---|
|`*`|匹配一切|
|`?`|匹配任何单个字符|
|`[seq]`|匹配seq中的任何字符|
| `[!seq]` |匹配不在seq中的任何字符 |



### `format`

- 对齐字符串
    - \>nums 右对齐
    - \<nums 左对齐
    - \^nums 居中
```
text = 'Hello World'
format(text, '>20')
# OutPut '         Hello World'
```

- 填充字符串

在对齐字符串的基础上，填充字符;
eg. `=^20s`
字符串20位居中对齐，其他的用=来补齐

- 数字格式化
    - 0.1f 小数保留一位
    - e 科学计数法
    - 0.2% 两位小数点百分数 `'{:.2%}'.format(0.9333)` 或者 `format(0.9321, '.2%')`



### `format_map`

`str.format_mpa(mapping)` 可以把变量域里能找到的变量放入str中，如
```python
name = 'Dz'
n = 25
s = '{name} has {n} messages'
s.format_map(vars())

# OutPut Dz has 25 messages
```

可以用类包装，处理变量缺失的问题

```
class Safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
s.format_map(vars())

# Output Dz has {n} messages
```



### `enumerate`

`enumerate(iterable, start=0)`

返回一个枚举对象，iterable 必须是一个支持迭代的对象

`start` 是index从多少开始，默认0



### `zip`

创建一个聚合来自每个可迭代对象元素的迭代器

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> list(zip(x, y))
[(1, 4), (2, 5), (3, 6)]
```

一个有趣的用法：

gird是 *n\*m*的数组，`list(zip(*grid))`可以把它变成 *m\*n*的数组。



### `bisect`

数组二分查找算法

- `bisect.bisect_left(a,x,lo=0, hi=len(a))`
  - 找到x合适的插入点，返回对应可以插入的index，如果x已经在a里面，返回对应相同元素的左边
  - `bisect_right` / `bisect`方法类似，不过返回的是a已存在x的右侧
  - 复杂度O(logn)
- `bisect.insort_left(a, x, lo=0, hi=len(a))`
  - x插入到有序序列a里面，维持有序
  - `insort_right` / `insort`插入到右侧
  - 复杂度O(n)

## 迭代器

**迭代器协议**：对象需要提供next方法，迭代器会返回迭代的下一项或者引起StopIteration异常，终止协议。

> 因此，实现迭代器协议，需要实现：__iter__方法&next方法。也可以用iter()来

**可迭代对象**：实现了迭代器协议的对象

> [迭代器协议的实现](https://github.com/yidao620c/python3-cookbook/blob/master/cookbook/c04/p04_iterator_protocol.py)



`itertools`是Python里自带的迭代器函数包

### `compress`

也是过滤工具，可迭代列表，对应的Boolean选择器作为输入参数。输出选择器为True的元素

```
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
```
取对应count大于5的地址：
```python
from itertools import compress
more5 = [n > 5 for n in counts]
list(compress(addresses, more5)

# Outputs ['5800 E 58TH', '1060 W ADDISON', '4801 N BROADWAY']
```



### `islice` 切割迭代器

`itertools.islice(iterable, start, stop[,step])`

若只有一个参数，则为stop。可以切割迭代器

```python
def count(n):
    while True:
        yield n
        n += 1

c = count(0)

import itertools

for n in itertools.islice(c, 3, 5):
    print(n)
    
# 3
# 4
```



### `chain` 串串迭代

可以把多个对象连续迭代，避免重复得循环。同时可以迭代两个不同类型的对象，而不用提前合并。

```python
>>> a = [1, 2, 3]
>>> b = ['x', 'y', 'z']
>>> for x in chain(a, b):
...     print(x)
...
1
2
3
x
y
z
```





## 其他

### 实现一个打乱算法

Fisher-Yates shuffle

in-place方法，x从n-1到1，每次从列表索引为0-(n-x)中任选一个数字，把它和倒数第x位交换。


```python
import random

def shuffle(target):
    for change in range(len(target) - 1, 0, -1):
        lower = random.randint(0, change)
        target[lower], target[change] = target[change], target[lower]
```



### 展开嵌套序列

使用递归生成器来把嵌套的列表展开

```python
from collections import Iterable

def flattern(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flattern(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]
for x in flattern(items):
    print(x)
```

`isinstance(x, Iterable)`用于检查某个元素是否可迭代和检查是否字符串/字节，避免迭代展开字符串输出单个字符。



