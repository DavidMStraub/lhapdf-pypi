# LHAPDF

This repository uses Travis CI to build binary Python wheels for the [LHAPDF](https://lhapdf.hepforge.org/) tool and uploads them to PyPI to allow convenient installation without compilation on Linux or Mac OS, using `pip`.

**Not that this is an unofficial effort and not supported by the LHAPDF authors.**

For documentation of the original program, official installation methods, and
citation info, please see the [LHAPDF web site](https://lhapdf.hepforge.org/).

## Installation

To install the package without root privileges, run
```
python3 -m pip install lhapdf --user
```

## Usage

The only caveat compared to an installation from source is the configuration of the paths and the location of `lhapdf.conf`. By default, on Linux the path will be `.local/share/lhapdf` under the user's home directory. If `lhapdf.conf` does not exist there, it will be generated on running the shell command `lhapdf`. Other paths can be selected for the shell command by setting the environment variable `LHAPDF_DATA_PATH`. Once the Python package is loaded, the path to the PDF files can be changed as usual with `lhapdf.pathsAppend` or `lhapdf.setPaths`.

## License

The file `bin/lhapdf` is modified from the LHAPDF source and is thus licensed under the GPLv3. Everything else in this repository is released under [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
