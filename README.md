## Hybrid Python/C++ Package

### Non-negotiables
 - We use 64 bit versions of all operating systems
 - We use Anaconda 64 bit
 - We use Python 3.6

All files have been named distinctly (unrealistically) without overlap to keep things clear and avoid ambiguities.
There's enough `name` arguments throughout the process to drive anyone insane, and this hopefully helps tease out the process further.

### Windows 10

CPython (most commonly used version of Python and one that ships with Anaconda), is built using Visual Studio. On activating the `python` interpreter:

```
Python 3.6.7 |Anaconda, Inc.| (default, Oct 28 2018, 19:44:12) [MSC v.1915 64 bit (AMD64)] on win32
```

 - `win32` indicates Windows (whether 32 or 64 bit).
 - `64 bit (AMD64)` indicates that we're using 64-bit Python
 - `MSC v.1915` is the version no. of the Visual C++ compiler used to build Python. In general Visual C++ 14 (which ships with Visual Studio 2015 and later) is used for Python 3.5 and above. Looks at [Wikipedia](https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B#Internal_version_numbering) to decipher version numbers.
 
 `1915` in our case corresponds to:
 ```
 MSVC++ 14.15 _MSC_VER == 1915 (Visual Studio 2017 version 15.8)
 ```
 
To keep things sane, we'll install VS 2015 (or 2017) with Visual C++
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
