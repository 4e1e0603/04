## Replace multiple white-space in a string by one.

### Problem

```
text = "My name is David".
```

### Solution

```python
' '.join(text.split())
```

or

```python
re.sub( '\s+', ' ', text).strip()
```
