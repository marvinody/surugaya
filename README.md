# Suruguya Wrapper

A simple api wrapper around the Surugu-ya site.

Simple usage can be something like

```python
import suruguya

for item in suruguya.search("fumofumo plush"):
  print("{}, {}".format(item.productName, item.productURL))
```
