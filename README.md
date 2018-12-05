# NumGenProbDist

Simple project which shows difference between probability distribution when generating pseudo random numbers in Python

## Usage

### Requirements

This project only supports Python 3.4+.


This project uses `numpy` and `sty` libraries

Use `pip install numpy` and `pip install sty` to obtain it.

### Syntax

`python genprob.py <dist_type> <args> <num_count> <optional_params>`


- `<dist_type>` is integer to choose distribution type

- `<args>` set of arguments for selected distribution type in format `"arg1, arg2, arg3"`

- `<num_count>` parameters is integer which says how many numbers should be generated

- See below for list of distribution types and valid arguments.

#### Optional parameters:
- `-d` or `--debug` - enables debug mode
- `-p` or `--print` - print CDF and PDF of the numbers in CLI stdout
- `-c` or `--csv` - output generated numbers into csv file - can be followed by a string defining output directory path
- `-v` or `--validate` - validates results
- `-b` or `--batch` - enables generating multiple number sequences in separate runs - should be followed by a number defining number of runs

#### Distribution types:

| Distribution type | Value for `<dist_type>` | Arguments for `<args>` |
| --- | :---: | --- |
| Uniform (Pythom impl) | 0 | "low, high" |
| Triangular (Own impl) | 1 | "low, high, mode" |
| Triangular (Python impl) | 2 | "low, high, mode" |
| Triangular (NumPy impl) | 22 | "low, high, mode" |
| Beta (Own impl) | 3 | "alpha, beta" |
| Beta (Python impl) | 4 | "alpha, beta" |
| Beta (NumPy impl) | 20 | "alpha, beta" |
| Exponential (Own impl) | 5 | "lambd" |
| Exponential (Python impl) | 6 | "lambd" |
| Exponential (NumPy impl) | 23 | "lambd" |
| Lognormal (Own impl) | 11 | "mu, sigma" |
| Lognormal (Python impl) | 12 | "mu, sigma" |
| Lognormal (NumPy impls) | 21 | "mu, sigma" |
| Normal (Own impl) | 13 | "mu, sigma" |
| Normal (Python impl) | 14 | "mu, sigma" |
| Normal (NumPy impl) | 24 | "mu, sigma" |
