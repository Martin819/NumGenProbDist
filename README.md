# NumGenProbDist

Simple project which shows difference between probability distribution when generating pseudo random numbers in Python

## Usage

### Requirements

This project only supports Python 3.4+.


This project uses `numpy` and `sty` libraries
Use `pip install numpy` and `pip install sty` to obtain it.

### Syntax

`python validate.py <dist_type> <args> <num_count> <optional_params>`


- `<dist_type>` is integer to choose distribution type

- `<args>` set of arguments for selected distribution type in format `"arg1, arg2, arg3"`

- `<num_count>` parameters is integer which says how many nubers should be generated

- See below for list of distribution types and valid arguments.

#### Optional parameters:
- `-d` or `--debug` - enables debug mode
- `-p` or `--print` - print distribution in CLI

#### Distribution types:

| Distribution type | Value for `<dist_type>` | Arguments for `<args>` |
| --- | :---: | --- |
| Uniform (Pythom impl) | 0 | "low, high" |
| Triangular (Own impl) | 1 | "low, high, mode" |
| Triangular (Python impl) | 2 | "low, high, mode" |
| Beta (Python impl) | 4 | "alpha, beta" |
| Beta (NumPy impl) | 20 | "alpha, beta" |
| Normal (Own impl) | 13 | "mu, sigma" |
| Normal (Python impl) | 14 | "mu, sigma" |
