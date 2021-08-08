# Generated from Niklaus.g by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NiklausParser import NiklausParser
else:
    from NiklausParser import NiklausParser

# This class defines a complete generic visitor for a parse tree produced by NiklausParser.

class NiklausVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NiklausParser#program.
    def visitProgram(self, ctx:NiklausParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#declaration.
    def visitDeclaration(self, ctx:NiklausParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#assignment.
    def visitAssignment(self, ctx:NiklausParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#instruction.
    def visitInstruction(self, ctx:NiklausParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#comparison.
    def visitComparison(self, ctx:NiklausParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#condition.
    def visitCondition(self, ctx:NiklausParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#loop.
    def visitLoop(self, ctx:NiklausParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#read_var.
    def visitRead_var(self, ctx:NiklausParser.Read_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#write_exp.
    def visitWrite_exp(self, ctx:NiklausParser.Write_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#expr.
    def visitExpr(self, ctx:NiklausParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiksslausParser#term.
    def visitTerm(self, ctx:NiklausParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#FactorId.
    def visitFactorId(self, ctx:NiklausParser.FactorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#FactorInt.
    def visitFactorInt(self, ctx:NiklausParser.FactorIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NiklausParser#FactorBlock.
    def visitFactorBlock(self, ctx:NiklausParser.FactorBlockContext):
        return self.visitChildren(ctx)



del NiklausParser