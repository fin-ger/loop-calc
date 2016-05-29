#! /usr/bin/env python3

'''
Copyright (C) 2016  Fin Christensen

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''

import sys
import argparse

from loop.loop_evaluator import LoopEvaluator

def main (argv):
    parser = argparse.ArgumentParser (
        prog = "loop-calc",
        description = "Run a loop program from the command line."
    )

    parser.add_argument ("program", nargs = 1, metavar = "PROGRAM", type = str,
                         help = "the path to the loop program")
    parser.add_argument ("--debug", action = 'store_true',
                         help = "show debugging information for the program")
    parser.add_argument (
        "parameters", nargs = '*', metavar = "PARAM", type = int,
        help = "the parameters given to the loop program beginning with x1"
    )
    args = parser.parse_args (argv[1:])
    loop_eval = LoopEvaluator (debug = args.debug)
    loop_eval.evaluate (args.program[0], *args.parameters)
    return 0

if __name__ == '__main__':
    sys.exit (main (sys.argv))
