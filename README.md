[![Build Status](https://travis-ci.org/unnonouno/excelcsv.svg?branch=master)](https://travis-ci.org/unnonouno/excelcsv)
[![Coverage Status](https://coveralls.io/repos/github/unnonouno/excelcsv/badge.svg?branch=master)](https://coveralls.io/github/unnonouno/excelcsv?branch=master)

# excelcsv

## Requirements

- Python 2.7, 3,4, 3.5

## Installation

```
$ pip install excelcsv
```

## Usage

```
with excelcsv.read_excel_tsv(path) as reader:
    for row in reader:
        do_something(row)
```

```
with excelcsv.write_excel_tsv(path) as writer:
    for row in rows:
        writer.writerow(row)
```

## License

MIT License.
