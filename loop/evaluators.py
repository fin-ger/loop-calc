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

import operator

from functools import reduce
from loop.base_evaluator import BaseEvaluator

class EvaluatorMixin (BaseEvaluator):
    """
    This mixin evaluates a given program.
    """
    def evaluate (self, program, *args):
        """
        Evaluate a given program with the given parameters.
        """
        self._set_parameters (*args)
        self._program (self._parse_string (self._read_program (program)))
        self._handle_result ()
        return self['x0']

class ExpressionEvalMixin (BaseEvaluator):
    """
    This mixin evaluates an expression.
    """
    def _expression (self, expression):
        """
        Evaluate an expression.
        """
        if "assignment" in expression:
            self._assignment (expression.assignment)
            self._debug ()
        elif "loop" in expression:
            self._loop (expression.loop)
        else:
            raise Exception ("Unknown expression")

class LoopEvalMixin (BaseEvaluator):
    """
    This mixin evaluates a loop.
    """
    def _loop (self, loop):
        """
        Evaluate a loop expression.
        """
        for i in range (0, self[loop.variable]):
            self._debug ("looping over {} @ {:03}".format (loop.variable, i))
            self._indent ()
            for expression in loop:
                if not isinstance (expression, str):
                    self._expression (expression)
            self._unindent ()

class AssignmentEvalMixin (BaseEvaluator):
    """
    This mixin evaluates an assignment operator.
    """
    def _assignment (self, assignment):
        """
        Evaluate an assignment operator.
        """
        self._debug ("{} :=".format (assignment.variable), end = False)
        self[assignment.variable] = self._calculation (assignment.calculation)

class CalculationEvalMixin (BaseEvaluator):
    """
    This mixin evaluates a calculation.
    """
    def _calculation (self, calculation):
        """
        Evaluate a calculation by reducing the given parameters with the given operator.
        """
        self._debug (" {} {} {} ".format (
            calculation.variable, calculation.operation[0], calculation.number
        ), end = False)
        return reduce (
            self._operation (calculation.operation),
            [self[calculation.variable], calculation.number]
        )

class OperationEvalMixin (BaseEvaluator):
    """
    This mixin evaluates an operation.
    """
    def _operation (self, operation):
        """
        Return the operator for a given operation for use in a reduce function.
        """
        if operation[0] == '+':
            return operator.add
        elif operation[0] == '-':
            return operator.sub
        else:
            raise Exception ("Unknown operator given!")

class ProgramEvalMixin (BaseEvaluator):
    """
    This mixin evaluates expressions of a program.
    """
    def _program (self, program):
        """
        Evaluate expressions of a program.
        """
        for expr in program:
            self._expression (expr)
