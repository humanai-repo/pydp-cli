FROM python:3.6
COPY dist/pydp-cli-*.tar.gz ./pydp-cli.tar.gz
WORKDIR ./
RUN pip install pydp-cli.tar.gz
CMD bash