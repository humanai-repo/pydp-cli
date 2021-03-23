import argparse
import pandas as pd
from pydp.algorithms.laplacian import BoundedSum, BoundedMean, Count, Max


def build_parser():
    parser = argparse.ArgumentParser(
        description='Perform a differentially private aggregation across ' +
        'specified data.')
    parser.add_argument('-i', '--input', action='append', required=True,
                        help='input file (or files) to process. CSV format.')
    parser.add_argument('-c', '--column', required=True,
                        help='The column to aggregate.')
    parser.add_argument('--id',
                        help='Column containing a unique identifier to be ' +
                        'differentially private with respect to.')
    parser.add_argument('-a', '--aggregation', required=True, action='append',
                        choices=['mean', 'sum'],
                        help='Select the required aggregation algorithm.')
    parser.add_argument('-e', '--epsilon', default=1.0, type=float,
                        help='Epsilon value for the differential privacy ' +
                        'algo. Suggested value is 0.1 - 1.0.')
    parser.add_argument('-o', '--output',
                        help='Output file (otherwise writes to STD out).')
    return parser


def read_inputs(inputs):
    """Read a list of CSVs with headers into a dataframe."""
    frames = [pd.read_csv(i) for i in inputs]
    df = pd.concat(frames)
    return df


def validate_unique_ids(df, id):
    """Validate every ID appears exactly once."""
    if not id is None:
        if df[id].size() != df[id].unique().size():
            raise Exception("Multiple rows for the same primary key")


def run_aggregations(df, column, aggregations, epsilon):
    series = df[column]
    d = dict([(a, aggregate(series, a, epsilon)) for a in aggregations])
    out = pd.DataFrame.from_dict(d, orient='index', columns=[column])
    return out


def aggregate(series, aggregate, epsilon):
    if aggregate == 'mean':
        x = BoundedMean(epsilon)
        return x.quick_result(list(series))
    elif aggregate == 'sum':
        x = BoundedSum(epsilon)
        return x.quick_result(list(series))
    else:
        raise Exception("Unrecognised aggregation: %s" % aggregate)


def write_output(df, output_f):
    """Pretty-print the output-dataframe or write to file."""
    if not output_f is None:
        print("Writing output to: %s" % output_f)
        df.to_csv(output_f)
    else:
        print(df)


def main():
    parser = build_parser()
    parsed = parser.parse_args()
    df_i = read_inputs(parsed.input)
    validate_unique_ids(df_i, parsed.id)
    df_o = run_aggregations(df_i, parsed.column,
                            parsed.aggregation, parsed.epsilon)
    write_output(df_o, parsed.output)


if __name__ == "__main__":
    main()
