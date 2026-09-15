# Import Behavior Summary

```python
import module_name
```
This imports the whole module. You access functions using `module_name.function_name()`.

```python
from module_name import function_name
```
This imports only one function. You can call it directly without using the module name.

```python
from module_name import *
```
This imports everything from the module. It is convenient but can create name conflicts and make code harder to understand.

It is usually better to use the first two forms in beginner programs.
