# Generated from Niklaus.g by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NiklausParser import NiklausParser
else:
    from NiklausParser import NiklausParser

# This class defines a complete listener for a parse tree produced by NiklausParser.
class NiklausListener(ParseTreeListener):

    # Enter a parse tree produced by NiklausParser#program.
    def enterProgram(self, ctx:NiklausParser.ProgramContext):
        pass

    # Exit a parse tree produced by NiklausParser#program.
    def exitProgram(self, ctx:NiklausParser.ProgramContext):
        pass


    # Enter a parse tree produced by NiklausParser#declaration.
    def enterDeclaration(self, ctx:NiklausParser.DeclarationContext):
        pass

    # Exit a parse tree produced by NiklausParser#declaration.
    def exitDeclaration(self, ctx:NiklausParser.DeclarationContext):
        pass


    # Enter a parse tree produced by NiklausParser#assignment.
    def enterAssignment(self, ctx:NiklausParser.AssignmentContext):
        pass

    # Exit a parse tree produced by NiklausParser#assignment.
    def exitAssignment(self, ctx:NiklausParser.AssignmentContext):
        pass


    # Enter a parse tree produced by NiklausParser#instruction.
    def enterInstruction(self, ctx:NiklausParser.InstructionContext):
        pass

    # Exit a parse tree produced by NiklausParser#instruction.
    def exitInstruction(self, ctx:NiklausParser.InstructionContext):
        pass


    # Enter a parse tree produced by NiklausParser#comparison.
    def enterComparison(self, ctx:NiklausParser.ComparisonContext):
        pass

    # Exit a parse tree produced by NiklausParser#comparison.
    def exitComparison(self, ctx:NiklausParser.ComparisonContext):
        pass


    # Enter a parse tree produced by NiklausParser#condition.
    def enterCondition(self, ctx:NiklausParser.ConditionContext):
        pass

    # Exit a parse tree produced by NiklausParser#condition.
    def exitCondition(self, ctx:NiklausParser.ConditionContext):
        pass


    # Enter a parse tree produced by NiklausParser#loop.
    def enterLoop(self, ctx:NiklausParser.LoopContext):
        pass

    # Exit a parse tree produced by NiklausParser#loop.
    def exitLoop(self, ctx:NiklausParser.LoopContext):
        pass


    # Enter a parse tree produced by NiklausParser#read_var.
    def enterRead_var(self, ctx:NiklausParser.Read_varContext):
        pass

    # Exit a parse tree produced by NiklausParser#read_var.
    def exitRead_var(self, ctx:NiklausParser.Read_varContext):
        pass


    # Enter a parse tree produced by NiklausParser#write_exp.
    def enterWrite_exp(self, ctx:NiklausParser.Write_expContext):
        pass

    # Exit a parse tree produced by NiklausParser#write_exp.
    def exitWrite_exp(self, ctx:NiklausParser.Write_expContext):
        pass


    # Enter a parse tree produced by NiklausParser#expr.
    def enterExpr(self, ctx:NiklausParser.ExprContext):
        pass

    # Exit a parse tree produced by NiklausParser#expr.
    def exitExpr(self, ctx:NiklausParser.ExprContext):
        pass


    # Enter a parse tree produced by NiklausParser#term.
    def enterTerm(self, ctx:NiklausParser.TermContext):
        pass

    # Exit a parse tree produced by NiklausParser#term.
    def exitTerm(self, ctx:NiklausParser.TermContext):
        pass


    # Enter a parse tree produced by NiklausParser#FactorId.
    def enterFactorId(self, ctx:NiklausParser.FactorIdContext):
        pass

    # Exit a parse tree produced by NiklausParser#FactorId.
    def exitFactorId(self, ctx:NiklausParser.FactorIdContext):
        pass


    # Enter a parse tree produced by NiklausParser#FactorInt.
    def enterFactorInt(self, ctx:NiklausParser.FactorIntContext):
        pass

    # Exit a parse tree produced by NiklausParser#FactorInt.
    def exitFactorInt(self, ctx:NiklausParser.FactorIntContext):
        pass


    # Enter a parse tree produced by NiklausParser#FactorBlock.
    def enterFactorBlock(self, ctx:NiklausParser.FactorBlockContext):
        pass

    # Exit a parse tree produced by NiklausParser#FactorBlock.
    def exitFactorBlock(self, ctx:NiklausParser.FactorBlockContext):
        pass



del NiklausParser