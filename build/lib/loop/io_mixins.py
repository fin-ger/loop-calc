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

import shutil

from loop.base_evaluator import BaseEvaluator

class StackMixin (BaseEvaluator):
    """
    This mixin manages the stack of a program.
    """
    def __init__ (self, *args, **kwargs):
        """
        Initialize a stack with a default value.
        """
        super ().__init__ (*args, **kwargs)
        self._stack = [0]

    def _check_stack (self, var):
        """
        Check if stack must be resized and return the correspoding index of the variable on the
        stack.
        """
        idx = int (var[1])
        stack_size = len (self._stack)
        if stack_size <= idx:
            extend = [0] * (idx - stack_size + 1)
            self._stack.extend (extend)
        return idx

    def __getitem__ (self, variable):
        """
        Read the value of the given variable from the stack.
        """
        return self._stack[self._check_stack (variable)]

    def __setitem__ (self, variable, value):
        """
        Set the value of the given variable on the stack.
        """
        self._stack[self._check_stack (variable)] = value
        self._debug ("|".join (
            " x{}: {:03} ".format (i, v) for i, v in enumerate (self._stack)
        ), end = False, right = True)

    def _set_parameters (self, *args):
        """
        Set initial values of the stack with the given parameters where the first parameter
        corresponds x1, the second parameter corresponds x2, etc.
        """
        self._stack.extend (args)

class FileReaderMixin (BaseEvaluator):
    """
    This mixin reads a program string from file.
    """
    def _read_program (self, program):
        """
        Read a program string from file.
        """
        with open (program, 'r') as f:
            data = f.read ()
        return data

class StringReaderMixin (BaseEvaluator):
    """
    This mixin passes through a program string.
    """
    def _read_program (self, program):
        """
        Pass through a program string.
        """
        return program

class ResultPrinterMixin (BaseEvaluator):
    """
    This mixin prints the result of a program (x0) to the console.
    """
    def _handle_result (self):
        """
        Print the result of a program (x0) to the console.
        """
        print (self['x0'])

class DebugMixin (BaseEvaluator):
    """
    This mixin enables debug output of a program if the debug keyword argument is given in the
    constructor.
    """
    def __init__ (self, *args, **kwargs):
        """
        Enable debug output of a program. Set debug keyword argument to True to enable it
        (default False).
        Set indent keyword argument to set the indentation level for loops.
        """
        super ().__init__ (*args, **kwargs)
        self._indentation = kwargs["indent"] if "indent" in kwargs else 4
        self._do_debug = kwargs["debug"] if "debug" in kwargs else False
        self._indent_level = 0
        self._term_size = shutil.get_terminal_size (fallback = (80, 24))
        self._last_end = True
        self._cursor_pos = 0

    def _indent (self):
        """
        Start a new indentation level (eg. beginning of loop).
        """
        self._indent_level += 1

    def _unindent (self):
        """
        End an indentation level (eg. end of loop).
        """
        self._indent_level -= 1

    def _debug (self, msg = "", end = True, right = False):
        """
        If debug flag was set in the constructor this function will print debug information on the
        console.
        Set msg argument to specify information to print.
        Set end argument to indicate the end of an expression that lasted for multiple calls of
        _debug. Useful for intelligent identation.
        Set right argument to print msg aligned to the right of the terminal screen.
        """
        if self._do_debug:
            indent = ' ' * self._indent_level * self._indentation if self._last_end else ""
            s = "{}{}".format (indent, msg)
            if right:
                s = s.rjust (self._term_size.columns - self._cursor_pos)
            if end:
                print (s)
                self._cursor_pos = 0
            else:
                self._cursor_pos += len (s)
                print (s, end = "")
            self._last_end = end
