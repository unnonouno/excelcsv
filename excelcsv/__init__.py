import contextlib
import csv
import io
import sys


if sys.version_info[0] > 2:
    reader = csv.reader
    writer = csv.writer

else:
    from excelcsv import py2
    reader = py2.reader
    writer = py2.writer


@contextlib.contextmanager
def read_excel_tsv(path, encoding='utf-16'):
    with io.open(path, 'r', encoding=encoding, newline=None) as f:
        yield reader(f, dialect='excel', delimiter='\t')


@contextlib.contextmanager
def write_excel_tsv(path, encoding='utf-16'):
    with io.open(path, 'w', encoding=encoding) as f:
        yield writer(f, dialect='excel', delimiter='\t')
