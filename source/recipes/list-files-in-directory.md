## Show all files in the given path.

```python
import os
for (root_folder, subfolders, files) in os.walk("."):
    for file in files:
        print(file)
```
