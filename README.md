# Loop calculator

This program evaluates loop programs as described in the lecture
`Grundlagen der theoretischen Informatik 2`.

This software is written in python using pyparsing for language parsing.

## How to build

In order to build this project just type `make` in the projects root directory.
The build will then install all requirements for your local user via pip.

This project was tested with python 3.4 and pip 8.1.1 on gentoo linux.

## How to run

To run a loop program do `./loop-calc examples/fib.loop`. Have a look on the help page
`./loop-calc --help` for more details.

## Troubleshooting

#### `python3 is not installed on this system`

Make sure that python 3 is available over a `python3` executable in your `PATH`.

#### `pip3 is not installed on this system`

Make sure that the `pip3` executable is available in your `PATH`.
