---
title: How to run external program
category: Python
---

# Jak spustit externí program

```python
import sys
import subprocess

result = subprocess.run([
    sys.executable, "-c", "print('Hello world!')"
])
```
