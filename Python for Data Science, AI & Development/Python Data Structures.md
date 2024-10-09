## Tuples
- Tuples are an ordered sequence
- Tuples are written as comma-separeted elements within parentheses
``` python
    tuple = ('disco', 10, 1.2)

    tuple[0] # 'disco'
    tuple[1] # 10
    tuple[2] # 1.2

    tuple2 = tuple + ('hard rock', 10) #('disco', 10, 1.2, 'hard rock', 10)

    len(tuple2) #  5 
```
- Tuples are immutable

```python
    tuple[0] = 10 # TypeError: 'tuple' object does not support item
```

``` python
    ratings(10,9,6,5,10,8,9,2)
    ratings_sorted = sorted(ratings) # (2,5,6,6,8,9,9,10,10)
```

- Nesting: a tuple can contain another tuples
```python
    NT = (1,2,('pop', 'rock'), (3,4), ('disco',(1,2)))
    NT[2]: ('pop', 'rock')
    NT[2][1]:  'rock'
    NT[3][1]: 4
    NT[4][1]: (1,2)

    # It is like a tree
```

## Lists
- Lists are also ordered sequences
- A  list is written as a comma-separated elements within square brackets
- A list can be created from a tuple

```python
    L = ['Michael Jackson', 10.1, 1982]
    L[0] # 'Michael Jackson'
    L[1] # 10.1
    L[2] # 1982
    L[-1]  # 1982

    L1 = L +  ['pop', 10]
    L1 # ['Michael Jackson', 10.1, 1982, 'pop', 10]

    L.extend(['pop', 10])
    L # ['Michael Jackson', 10.1, 1982, 'pop', 10]

    L.append(['pop', 10])
    L # ['Michael Jackson', 10.1, 1982, ['pop', 10]]
```
- Lists are mutable
```python
    A = ['disco', 10, 1.2]
    A[0] = 'hard rock'
    A # ['hard rock', 10, 1.2]

    del(A[0])
    A  # [10, 1.2]
```
- Convert string to list
```python
    'hard rock',split()
    # ['hard', 'rock']
```

## Dictionaries
-  A dictionary is an unordered collection of key-value pairs
- The keys have to be immutable and unique
- The values can be immutable, mutable and duplicates
```python
    dict = {'Thriller':  1982, 'Bad': 1987}
    dict['Thriller']  # 1982
    dict['Bad']  # 1987 
    
    dict['Off the Wall']  # KeyError

    dict['Graduation'] =  2007
    dict  # {'Thriller': 1982, 'Bad': 1987, 'Graduation': 2007}

    del(dict'Thriller')
    dict  # {'Bad': 1987, 'Graduation': 2007}

    'Graduation' in  dict  # True
    'Thriller' in  dict  # False

    dict.keys()  # dict_keys(['Bad', 'Graduation'])
    dict.values()  # dict_values([1987, 2007])
```
