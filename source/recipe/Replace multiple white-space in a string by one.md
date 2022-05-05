## Replace multiple spaces in a string by a one space.

### Problem

The given string contains multiple spaces which should be replaces by exactly one space.

```
text: str = "My  name  is  David."
```

### Solution

```python
' '.join(text.split())
```

or

```python
re.sub( '\s+', ' ', text).strip()
```
