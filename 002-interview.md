# An Interview Questions for Python Junior/Senior Developer

### Q1. How would you modify the definition of `extendList` to produce the presumably desired behavior?

```python
def extendList(val, list=[]):
	list.append(val)
	return list

l1 = extendList(10)
l2 = extendList(123, [])
l3 = extendList('a')

print("l1 = %s" % l1)
print("l2 = %s" % l2)
print("l3 = %s" % l3)
```

The output of the above code will be:

```python
l1 = [10, 'a']
l2 = [123]
l3 = [10, 'a']
```

Many will mistakenly expect `l1` to be equal to [10] and `l3` to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

`l1` and `l3` are therefore operating on the same default list, whereas `l2` is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

**The definition of the extendList function could be modified as follows**, though, to always begin a new list when no `list`  argument is specified, which is more likely to have been the desired behavior:

```python
def extendList(val, list=None):
	if list is None:
		list = []
	list.append(val)
	return list
```
With this revised implementation, the output would be:
```python
list1 = [10]
list2 = [123]
list3 = ['a']
```