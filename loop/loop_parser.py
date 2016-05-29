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
plus = Literal ('+')
minus = Literal ('-')

number = (Literal ('0') | Literal ('1')).setResultsName ("number").setParseAction (
    lambda token: int (token[0])
)

variable = Combine ('x' + Word ('0123456789')).setResultsName ("variable")
assign = Suppress (':=')
delimiter = Suppress (';')
loop_kw = Suppress ('loop')
begin_kw = Suppress ('begin')
end_kw = Suppress ('end')

# language parser
loop = Forward ()

# expressions
operation = Group (plus | minus).setResultsName ("operation")
calculation = Group (variable + operation + number).setResultsName ("calculation")
assignment = Group (variable + assign + calculation).setResultsName ("assignment")
loop_expr = Group (loop_kw + variable + begin_kw + loop + end_kw).setResultsName ("loop")
expression = Group (assignment | loop_expr).setResultsName ("expression")

loop << expression + ZeroOrMore (delimiter + expression)

class LoopParserMixin (BaseEvaluator):
    """
    This mixin parses a program string to an AST.
    """
    def _parse_string (self, program):
        """
        Parse a program string to an AST.
        """
        return loop.parseString (program, parseAll = True)
