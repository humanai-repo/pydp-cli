# pydp-cli
A cli wrapping [OpenMined's PYDP](https://github.com/OpenMined/PyDP).

Takes as input:
 *  A set of CSV files (presumes the same columns for all files)
 *  Columns to operate over
 *  Aggregations to run
 *  Epsilon (Differential Privacy parameter)
 *  Output file

# Dependencies

 *  Python3
 *  python-dp
 *  Pandas

# Example Usage

```bash
python3 src/pydp-cli.py -h
usage: pydp-cli.py [-h] -i INPUT -c COLUMN [--id ID] -a {mean,sum}
                   [-e EPSILON] [-o OUTPUT]

Perform a differentially private aggregation across specified data.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file (or files) to process. CSV format.
  -c COLUMN, --column COLUMN
                        The column to aggregate.
  --id ID               Column containing a unique identifier to be
                        differentially private with respect to.
  -a {mean,sum}, --aggregation {mean,sum}
                        Select the required aggregation algorithm.
  -e EPSILON, --epsilon EPSILON
                        Epsilon value for the differential privacy algo.
                        Suggested value is 0.1 - 1.0.
  -o OUTPUT, --output OUTPUT
                        Output file (otherwise writes to STD out).
```

```bash
> python3 src/pydp-cli.py -i $INPUT -c words -a mean -a sum -e 5
```

# Future work

 *  Keep track of privacy budget used.
 *  More sophisticated querying
 *  More sophisticated inputs (protobufs)