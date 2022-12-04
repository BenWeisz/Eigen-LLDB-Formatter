# Eigen-LLDB-Formatter
Formatter for basic matrix and vector types in lldb

Eigen::Vector3f Example:
```sh
(1.02, 2.33, 6.54).T
```

Eigen::MatrixXf Example:

```sh
Size: 3 x 4
| -0.02  1.22  3.33  4.80 |
|  2.02 -1.32 -3.63 -4.12 |
|  0.02  4.22  6.33  9.37 |
```

I've haven't tested the formatter throughly so its bound to be a bit wonky with different number of signigicant digits.

## Supported Types
The types supported so far are:
- Eigen::Vector3f
- Eigen::VectorXf
- Eigen::Matrix2f
- Eigen::Matrix3f
- Eigen::MatrixXf

To add more [Eigen](https://eigen.tuxfamily.org/dox/GettingStarted.html) types, adapt the formatter code in `eigen_format.py` by adding another formatter function:

The basic function signature is:

```python
def type_formatter(valobj, internal_dict, options):
  return "The string format for the specific type"
```

Once you've added the function for your type to the `eigen_format.py` file, you want to add an additional command to the `.lldbinit` file.

```sh
type summary add -F eigen_format.matxf Eigen::MatrixXf
...
...
type summary add -F eigen_format.<python function name> <Eigen Structure Prefixed With Eigen Namespace>
```

## Set up
To set up the Eigen formatter, place the `eigen_format.py` files in a folder where you keep your dev configuration files. For me its `~/dev/config`

Next place the `.lldbinit` file in your home directory (ie. `~/` on linux / macos) This will ensure that when you start lldb it will load the format summary strings into lldb. Note that if you dont want these formats to always run, you can always just run the command to load the formatters on a case by case. All the commands in the `.lldbinit` file are lldb commands themselves.

The final thing to do is update the `.lldbinit` file with the path to your `eigen_format.py` file. Edit the path in the first line of the `.lldbinit` file.

## VSCode and the CodeLLDB Extension
Currently the formatter doesn't work in vscode but if I have some time I'm going to try to get that set up to. 

Enjoy!
