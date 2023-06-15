# How to run external program

```python
import sys
import subprocess

result = subprocess.run([
    sys.executable, "-c", "print('Hello world!')"
])
```
