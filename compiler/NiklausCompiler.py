import sys
from antlr4 import *
from NiklausLexer import NiklausLexer
from NiklausParser import NiklausParser
from NiklausVisitor import *


class NiklausCompiler(NiklausVisitor):
    def __init__(self):
        self.file = None
        self.program_name = ""
        self.variables_list = []
        self.library_needed = False
        self.print_id = 0
        self.read_id = 0
        self.condition_id = 0
        self.loop_id = 0

    # Visit a parse tree produced by NiklausParser#program.
    def visitProgram(self, ctx: NiklausParser.ProgramContext):
        self.program_name = str(ctx.ID())
        self.file = open(self.program_name + ".arm", "w")
        self.file.write("mov r6, #stack_initialization\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NiklausParser#declaration.
    def visitDeclaration(self, ctx: NiklausParser.DeclarationContext):
        for variable in ctx.ID():
            if str(variable) in self.variables_list:
                raise ValueError(f"Variable {variable} has been declared more than once")
            else:
                self.variables_list.append(str(variable))

    # Visit a parse tree produced by NiklausParser#assignment.
    def visitAssignment(self, ctx: NiklausParser.AssignmentContext):
        if str(ctx.ID()) not in self.variables_list:
            raise ValueError(f"Variable {ctx.getChild(0)} has not been declared as a variable")
        self.visitChildren(ctx)
        self.file.write("str r0, mem_" + str(ctx.getChild(0)) + "\n")

    # Visit a parse tree produced by NiklausParser#instruction.
    def visitInstruction(self, ctx: NiklausParser.InstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NiklausParser#comparison.
    def visitComparison(self, ctx: NiklausParser.ComparisonContext):
        if str(ctx.SIGNE()) in ['=', '<>', '<', '>=']:
            self.visitExpr(ctx.expr(0))
            self.file.write("push r0\n")
            self.visitExpr(ctx.expr(1))
        elif str(ctx.SIGNE()) in ['<=', '>']:
            self.visitExpr(ctx.expr(1))
            self.file.write("push r0\n")
            self.visitExpr(ctx.expr(0))
        else:
            raise ValueError(f"Comparison operator {ctx.SIGNE()} is not valid")
        self.file.write("pop r1\n")
        self.file.write("cmp r1, r0\n")

    # Visit a parse tree produced by NiklausParser#condition.
    def visitCondition(self, ctx: NiklausParser.ConditionContext):
        self.visitComparison(ctx.comparison())
        if str(ctx.comparison().SIGNE()) == '=':
            self.file.write("beq if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(1))
            self.file.write("b end_test" + str(self.condition_id) + "\n")
            self.file.write("@ if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(0))
        elif str(ctx.comparison().SIGNE()) == '<>':
            self.file.write("beq if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(0))
            self.file.write("b end_test" + str(self.condition_id) + "\n")
            self.file.write("@ if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(1))
        elif str(ctx.comparison().SIGNE()) in ['<', '>']:
            self.file.write("blt if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(1))
            self.file.write("b end_test" + str(self.condition_id) + "\n")
            self.file.write("@ if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(0))
        elif str(ctx.comparison().SIGNE()) in ['<=', '>=']:
            self.file.write("blt if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(0))
            self.file.write("b end_test" + str(self.condition_id) + "\n")
            self.file.write("@ if_true" + str(self.condition_id) + "\n")
            self.visitInstruction(ctx.instruction(1))
        else:
            raise ValueError(f"Comparison operator {ctx.comparison().SIGNE()} is not valid")
        self.file.write("@ end_test" + str(self.condition_id) + "\n")
        self.condition_id += 1

    # Visit a parse tree produced by NiklausParser#loop.
    def visitLoop(self, ctx: NiklausParser.LoopContext):
        self.file.write("@start_loop" + str(self.loop_id) + "\n")
        self.visitComparison(ctx.comparison())
        if str(ctx.comparison().SIGNE()) == '=':
            self.file.write("beq if_true_while" + str(self.loop_id) + "\n")
            self.file.write("b end_loop" + str(self.loop_id) + "\n")
            self.file.write("@ if_true_while" + str(self.loop_id) + "\n")
            self.visitInstruction(ctx.instruction())
            self.file.write("b start_loop" + str(self.loop_id) + "\n")
        elif str(ctx.comparison().SIGNE()) == '<>':
            self.file.write("beq end_loop" + str(self.loop_id) + "\n")
            self.visitInstruction(ctx.instruction())
            self.file.write("b start_loop" + str(self.loop_id) + "\n")
        elif str(ctx.comparison().SIGNE()) in ['<', '>']:
            self.file.write("blt if_true_while" + str(self.loop_id) + "\n")
            self.file.write("b end_loop" + str(self.loop_id) + "\n")
            self.file.write("@ if_true_while" + str(self.loop_id) + "\n")
            self.visitInstruction(ctx.instruction())
            self.file.write("b start_loop" + str(self.loop_id) + "\n")
        elif str(ctx.comparison().SIGNE()) in ['<=', '>=']:
            self.file.write("blt end_loop" + str(self.loop_id) + "\n")
            self.visitInstruction(ctx.instruction())
            self.file.write("b start_loop" + str(self.loop_id) + "\n")
        else:
            raise ValueError(f"Comparison operator {ctx.comparison().SIGNE()} is not valid")
        self.file.write("@end_loop" + str(self.loop_id) + "\n")
        self.loop_id += 1

    # Visit a parse tree produced by NiklausParser#read_var.
    def visitRead_var(self, ctx: NiklausParser.Read_varContext):
        self.library_needed = True
        self.file.write("mov r7, #endread" + str(self.read_id) + "\n")
        self.file.write("b readInt \n")
        self.file.write("@endread" + str(self.read_id) + "\n")
        self.file.write("str r0, mem_" + str(ctx.getChild(1)) + "\n")
        self.read_id += 1

    # Visit a parse tree produced by NiklausParser#write_exp.
    def visitWrite_exp(self, ctx: NiklausParser.Write_expContext):
        self.library_needed = True
        self.file.write("mov r7, #endprint" + str(self.print_id) + "\n")
        self.visitChildren(ctx)
        self.file.write("b printInt\n")
        self.file.write("@endprint" + str(self.print_id) + "\n")
        self.print_id += 1

    # Visit a parse tree produced by NiklausParser#expr.
    def visitExpr(self, ctx: NiklausParser.ExprContext, i=0):
        if i < len(ctx.term()) - 1:
            self.visitTerm(ctx.term(i))
            self.file.write("push r0\n")
            self.visitExpr(ctx, i + 1)
            self.file.write("pop r1\n")
            if str(ctx.ADDOP(i)) == '+':
                self.file.write("add r0, r1, r0\n")
            if str(ctx.ADDOP(i)) == '-':
                self.file.write("sub r0, r1, r0\n")
        else:
            self.visitTerm(ctx.term(i))

    # Visit a parse tree produced by NiklausParser#term.
    def visitTerm(self, ctx: NiklausParser.TermContext, i=0):
        if i < len(ctx.factor()) - 1:
            if type(ctx.factor(i)) == NiklausParser.FactorIntContext:
                self.visitFactorInt(ctx.factor(i))
            if type(ctx.factor(i)) == NiklausParser.FactorIdContext:
                self.visitFactorId(ctx.factor(i))
            if type(ctx.factor(i)) == NiklausParser.FactorBlockContext:
                self.visitFactorBlock(ctx.factor(i))
            self.file.write("push r0\n")
            self.visitTerm(ctx, i + 1)
            self.file.write("pop r1\n")
            self.file.write("str r1, 0xAAAA\n")
            self.file.write("str r0, 0xAAAB\n")
            if str(ctx.MULTOP(i)) == '*':
                self.file.write("ldr r0, 0xAAAC\n")
            if str(ctx.MULTOP(i)) == '/':
                self.file.write("ldr r0, 0xAAAD\n")
        else:
            if type(ctx.factor(i)) == NiklausParser.FactorIntContext:
                self.visitFactorInt(ctx.factor(i))
            if type(ctx.factor(i)) == NiklausParser.FactorIdContext:
                self.visitFactorId(ctx.factor(i))
            if type(ctx.factor(i)) == NiklausParser.FactorBlockContext:
                self.visitFactorBlock(ctx.factor(i))

    # Visit a parse tree produced by NiklausParser#FactorId.
    def visitFactorId(self, ctx: NiklausParser.FactorIdContext):
        if str(ctx.getChild(0)) not in self.variables_list:
            raise ValueError(f"Factor {ctx.getChild(0)}, has not been declared as a variable")
        else:
            self.file.write("ldr r0, mem_" + str(ctx.getChild(0)) + "\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NiklausParser#FactorInt.
    def visitFactorInt(self, ctx: NiklausParser.FactorIntContext):
        self.file.write("mov r0, #" + str(ctx.getChild(0)) + "\n")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by NiklausParser#FactorBlock.
    def visitFactorBlock(self, ctx: NiklausParser.FactorBlockContext):
        return self.visitChildren(ctx)

    def writeEndOfFile(self):
        self.file.write("b end\n@end\nb end\n")
        if self.library_needed:
            with open("lib.arm") as f:
                self.file.writelines(f.readlines())
        for x in self.variables_list:
            self.file.write("@mem_" + x + " rmw 1\n")
        self.file.write("@stack_initialization rmw 1")
        self.file.close()


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = NiklausLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NiklausParser(stream)
    tree = parser.program()
    compiled = NiklausCompiler()
    compiled.visit(tree)
    compiled.writeEndOfFile()


if __name__ == '__main__':
    main(sys.argv)
