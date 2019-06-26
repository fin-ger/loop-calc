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

class BaseEvaluator:
    """
    Base class for mixins. Every mixin should inherit from this class to avoid constructor
    collisions.
    """
    def __init__ (self, *args, **kwargs):
        """
        Basic constructor for correct method resolution order (MRO).
        """
        pass

    def evaluate (self, program, *args):
        """
        Evaluate a given program with the given parameters.
        """
        pass

    def _expression (self, expression):
        """
        Evaluate an expression.
        """
        pass

    def _loop (self, loop):
        """
        Evaluate a loop expression.
        """
        pass

    def _assignment (self, assignment):
        """
        Evaluate an assignment operator.
        """
        pass

    def _calculation (self, calculation):
        """
        Evaluate a calculation by reducing the given parameters with the given operator.
        """
        pass

    def _operation (self, operation):
        """
        Return the operator for a given operation for use in a reduce function.
        """
        pass

    def _program (self, program):
        """
        Evaluate expressions of a program.
        """
        pass

    def _read_program (self, program):
        """
        Read a program string from file.
        """
        pass

    def _handle_result (self):
        """
        Print the result of a program (x0) to the console.
        """
        pass

    def _parse_string (self, program):
        """
        Parse a program string to an AST.
        """
        pass

    def __getitem__ (self, variable):
        """
        Read the value of the given variable from the stack.
        """
        pass

    def __setitem__ (self, variable, value):
        """
        Set the value of the given variable on the stack.
        """
        pass

    def _set_parameters (self, *args):
        """
        Set initial values of the stack with the given parameters where the first parameter
        corresponds x1, the second parameter corresponds x2, etc.
        """
        pass

    def _indent (self):
        """
        Start a new indentation level (eg. beginning of loop).
        """
        pass

    def _unindent (self):
        """
        End an indentation level (eg. end of loop).
        """
        pass

    def _debug (self, msg = "", end = True, right = False):
        """
        If debug flag was set in the constructor this function will print debug information on the
        console.
        Set msg argument to specify information to print.
        Set end argument to indicate the end of an expression that lasted for multiple calls of
        _debug. Useful for intelligent identation.
        Set right argument to print msg aligned to the right of the terminal screen.
        """
        pass
