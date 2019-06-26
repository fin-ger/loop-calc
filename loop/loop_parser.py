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

from pyparsing import Literal, Combine, Word, Forward, Group, Suppress, ZeroOrMore
from loop.base_evaluator import BaseEvaluator

# atoms
PLUS = Literal('+')
MINUS = Literal('-')

NUMBER = (Literal('0') | Literal('1')).setResultsName("number").setParseAction(
    lambda token: int(token[0])
)

VARIABLE = Combine('x' + Word('0123456789')).setResultsName("variable")
ASSIGN = Suppress(':=')
DELIMITER = Suppress(';')
LOOP_KW = Suppress('loop')
BEGIN_KW = Suppress('begin')
END_KW = Suppress('end')

# language parser
LOOP = Forward()

# expressions
OPERATION = Group(PLUS | MINUS).setResultsName("operation")
CALCULATION = Group(VARIABLE + OPERATION + NUMBER).setResultsName("calculation")
ASSIGNMENT = Group(VARIABLE + ASSIGN + CALCULATION).setResultsName("assignment")
LOOP_EXPR = Group(LOOP_KW + VARIABLE + BEGIN_KW + LOOP + END_KW).setResultsName("loop")
EXPRESSION = Group(ASSIGNMENT | LOOP_EXPR).setResultsName("expression")

#pylint: disable=expression-not-assigned
LOOP << EXPRESSION + ZeroOrMore(DELIMITER + EXPRESSION)

class LoopParserMixin(BaseEvaluator):
    """
    This mixin parses a program string to an AST.
    """
    def _parse_string(self, program):
        """
        Parse a program string to an AST.
        """
        return LOOP.parseString(program, parseAll=True)
