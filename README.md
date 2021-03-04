# pydp-cli
A technology demonstration cli wrapping
[OpenMined's PYDP](https://github.com/OpenMined/PyDP).

# Example Usage

```bash
pydp-cli -h
usage: pydp-cli [-h] -i INPUT -c COLUMN [--id ID] -a {mean,sum}
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
pydp-cli -i $INPUT -c $COLUMN -a mean -a sum -e 5
```

To run from Docker, launch the docker image in interactive mode with the
directory containing input data mounted in the container.
```bash
docker run -it -v $ABSOLUTE_PATH_INPUT_DIR:$CONTAINER_INPUT --name pydp-cli pydp-cli
```

Then run the commands as above.

# Build
To build a local python package (tested on Mac OS 10.2).

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
# Virtual env bundled with MacOS is faulty.
pip install --upgrade virtualenv
pip install --upgrade build
python3 -m build
# This will output a Tar file in dist/pydp-cli-*.tar.gz
deactivate
```

To wrap the local python package in into a Docker image run
```bash
docker build --tag pydp-cli .
```

# Install
Install from a local tar file.

```bash
# Optionally install in local virtual env.
source venv/bin/activate
pip install dist/pydp-cli-*.tar.gz
# Reload the virtual environment to make the tool available.
deactivate; source venv/bin/activate
```

# Future work

 *  Keep track of privacy budget used.
 *  More sophisticated querying
 *  More sophisticated inputs (protobufs)

# Disclaimer
This tool is an experimental technology demonstration only. It has not been
rigerously tested, code reviewed or audited. Do not use to protect people's
privacy in production applications.
