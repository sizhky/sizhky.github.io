## Ideas
#personal #10/Blog/ideas/tinydb Tinydb is not a columnar db. Can I modify it to be adaptive? i.e., make modifications that can make the following
	- db['column'] (gets all column items)
	- db.column gets all column items
	- db[0].column (convenience)


## Patches
```python
from tinydb import TinyDB, Query
from tinydb.table import Table

@patch_to(Table)
def __getitem__(self, input):
    if isinstance(input, int):
        return self.all()[input]
    elif isinstance(input, str):
        return [item[input] for item in self.all()]

@patch_to(Table)
def sample(self, n=1):
    o = [self[randint(len(self))] for _ in range(n)]
    if n == 1: return o[0]
    return o
```