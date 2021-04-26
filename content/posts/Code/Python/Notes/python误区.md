---
title: python误区
date: 2020-11-10T17:49:33+08:00
toc: true
images:
tags:
  - Python
  - Notes
---

## 序列递减

```python
for x in range(4):
    print(x)

# 0,1,2,3

for x in range(3,-1,-1):
    print(x)
# 3,2,1,0
```
倒序的range为左边包括，右边未到



## 元素重复

```python
>>> a = [[1,2]] * 3
[[1,2], [1,2], [1,2]]

>>> a[0][1] = 8
[[1,8], [1,8], [1,8]]

# itertools.repeat 生成的也是同理
[[]] 里面的list为同一个指向目标(地址相同)

>> id(a[0]) == id(a[1])
True
```

如果想生成一个list内元素不一样的list，需要如下
```
[[1,2] for _ in range(3)]
```

相当于deep copy 和 copy的区别





## `Bool` 在 `isinstance`的判断

问题：

```python
isinstance(True, (float, int))
True
```

原因：

由于历史原因，`bool`是int的子类，`True + 1`会等于 `2`

```python
int.__subclasses__()
[bool,
 <enum 'IntEnum'>,
 <enum 'IntFlag'>,
 sre_constants._NamedIntConstant,
 subprocess.Handle]
```



如果需要准确判断`bool`或`int`，需要在判断`int`之前，判断`bool`

```python
if isinstance(sth, bool):
    # do sth.
elif isinstance(sth, int):
    # other thing.
```

或者使用`type`准确判断类型

```python
if type(sth) in (float, int):
    # do stuff.
```



## 默认参数的值应该是不可变对象

如果

```python
def spam(a, b=[]):
    print(b)
    return b

x = spam(1)
# x:[]
x.append(99)
# x:[99]
spam(1)
# [99]
```

会被改变

因此要设置成不可变对象，如`None`、`True`、`False`数字或字符串等