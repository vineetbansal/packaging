## Hybrid Python/C++ Package

### Non-negotiables
 - We use 64 bit versions of all operating systems
 - We use Anaconda 64 bit
 - We use Python 3.6

All files have been named distinctly (unrealistically) without overlap to keep things clear and avoid ambiguities.
There's enough `name` arguments throughout the process to drive anyone insane, and this hopefully helps tease out the process further.

### To build on Windows 10

Install VS 2017 (or 2015) with Visual C++
Activate x64 Native Tools Command Prompt for VS 2017

Verify we do have a 64 bit toolchain active
```
cl.exe
Microsoft (R) C/C++ Optimizing Compiler Version 19.15.26730 for x64
```

```
cl.exe /c src/examples
lib.exe /out:mylibrary.lib examples.obj
```

Move `mylibrary.lib` to `lib` folder

### setuptools
We're using `setuptools` and ditching `distutils` for good

```
python setup.py install
```

### Try out the library

```
>>> import MyExtension
>>> MyExtension.py_hello(b'world')
hello world
```
