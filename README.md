<!-- Logo -->
<p align="center">
  <a href="https://www.freepik.com/icon/pill_5419351"><img width="256" height="256" src="https://raw.githubusercontent.com/maekind/imagepills/main/logo.png"></a>
</p>
<!-- Shields -->
<p align="center">
<a href="https://github.com/maekind/imagepills"><img src="https://img.shields.io/github/actions/workflow/status/maekind/imagepills/.github%2Fworkflows%2Ftesting.yaml?label=tests&color=green" hspace="5"></a>
<a href="https://codecov.io/gh/maekind/imagepills"><img src="https://codecov.io/gh/maekind/imagepills/branch/main/graph/badge.svg?token=L8IS93O0XV" hspace="5"></a>
<a href="https://github.com/maekind/imagepills/releases"><img src="https://img.shields.io/github/actions/workflow/status/maekind/imagepills/.github%2Fworkflows%2Frelease.yaml?label=package&color=green" hspace="5"></a>
<a href="https://pypi.org/project/imagepills"><img src="https://img.shields.io/github/v/release/maekind/imagepills?color=blue&label=pypi latest" hspace="5"></a>
<br>
<a href="https://github.com/maekind/imagepills/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-orange.svg" hspace="5"></a>
<a href="https://github.com/maekind/imagepills"><img src="https://img.shields.io/github/repo-size/maekind/imagepills?color=red" hspace="5"></a>
<a href="https://github.com/maekind/imagepills"><img src="https://img.shields.io/github/last-commit/maekind/imagepills?color=black" hspace="5"></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/github/languages/top/maekind/imagepills?color=darkgreen" hspace="5"></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python%20version-%3E3.9-lightblue" hspace="5"></a>
</p>

<h1 align="center">IMAGEPILLS</h1>

## Description

This package provides a high level abstraction for some image utilities. Check out the [Usage](#usage) section for commands details.
## Installation

This package can be installed using `pip`:

```bash
$> pip install imagepills
```

or

```bash
$> python -m pip install imagepills
```

## Usage

### Size

Use the command `pills_size` as follows:

```bash
$> pills_size [-h] [-v] [-d STRING] [-f STRING]
```

Those are the options to pass to the command:

```bash
  -h, --help                      Show the help message and exit
  -v, --verbose                   Set verbose option
  -d STRING, --directory STRING,  Path to directory containing images
  -f STRING, --file STRING,       Image file path
```

We can use the pill to calculate the size of one file or a group of files inside a folder.
### Resize

Use the command `pills_resize` as follows:

```bash
$> pills_resize [-h] [-v] -o STRING -f STRING -w STRING -e STRING
```

Those are the options to pass to the command:

```bash
  -h, --help                      Show the help message and exit
  -v, --verbose                   Set verbose option
  -o STRING, --output STRING,     Path to output folder
  -f STRING, --file STRING,       Image file to convert
  -w STRING, --width STRING,      New width
  -e STRING, --height STRING,     New height
```

For project purpouses, minimum height and width under 256 pixels are not allowed, and an `argparse.ArgumentTypeError` exception will be raised in such case.

If new sizes are not proportional to the original ones, the tool will resize to the biggest size (weight or height) and calculate the other one proportionally.

### Convert to png format

Use the command `pills_image2png` as follows:

```bash
$> pills_image2png [-h] [-v] [-d STRING] -o STRING [-f STRING]
```

Those are the options to pass to the command:

```bash
  -h, --help                      Show the help message and exit
  -v, --verbose                   Set verbose option
  -d STRING, --directory STRING,  Path to directory containing images
  -o STRING, --output STRING,     Path to ouput folder
  -f STRING, --file STRING,       Image file to convert
```

We can use the pill to convert one or a group of files inside a folder. The ouput folder is mandatory to store converted images.

## Contributors

<a href="https://github.com/maekind/imagepills/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=maekind/imagepills" />
</a>
<br/>
<br/>
<a href="mailto:marco@marcoespinosa.es"> Say hello!</a>
