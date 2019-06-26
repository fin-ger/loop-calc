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

from loop.evaluators import (
    EvaluatorMixin, ProgramEvalMixin, OperationEvalMixin, CalculationEvalMixin,
    AssignmentEvalMixin, LoopEvalMixin, ExpressionEvalMixin
)
from loop.loop_parser import LoopParserMixin
from loop.io_mixins import StackMixin, FileReaderMixin, ResultPrinterMixin, DebugMixin

class LoopEvaluator(EvaluatorMixin,
                    ProgramEvalMixin,
                    OperationEvalMixin,
                    CalculationEvalMixin,
                    AssignmentEvalMixin,
                    LoopEvalMixin,
                    ExpressionEvalMixin,
                    StackMixin,
                    LoopParserMixin,
                    FileReaderMixin,
                    ResultPrinterMixin,
                    DebugMixin):
    """
    The LoopEvaluator is able to parse and evaluate loop programs.
    """
