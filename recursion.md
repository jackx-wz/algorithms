# 递归

## 概念
包含调用自己的函数

## 效率
由于函数调用是使用调用栈来实现的，如果包含太多次的函数调用，会导致占用大量内存空间。而同样的实现，使用循环来做，只是变量值的变化，，所以使用循环可以更快。
优势是递归的代码比循环更简洁清晰，何时使用递归需要自己判断

## 多种语言比较
看起来 php 的效率居然是最高的

[php版](recursion.php) [python版](recursion.py) [lua版](recursion.lua)
```jshelllanguage
➜  algorithms git:(master) ✗ time lua recursion.lua
lua recursion.lua  1.42s user 0.01s system 99% cpu 1.440 total
➜  algorithms git:(master) ✗ time php recursion.php
php recursion.php  0.90s user 0.03s system 98% cpu 0.941 total
➜  algorithms git:(master) ✗ time python recursion.py
python recursion.py  2.58s user 0.05s system 99% cpu 2.650 total
```