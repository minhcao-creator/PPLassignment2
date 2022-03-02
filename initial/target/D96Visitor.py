# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#superclass.
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#attributedecl.
    def visitAttributedecl(self, ctx:D96Parser.AttributedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varlist.
    def visitVarlist(self, ctx:D96Parser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idnamelist.
    def visitIdnamelist(self, ctx:D96Parser.IdnamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typename.
    def visitTypename(self, ctx:D96Parser.TypenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idname.
    def visitIdname(self, ctx:D96Parser.IdnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methoddecl.
    def visitMethoddecl(self, ctx:D96Parser.MethoddeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paralist.
    def visitParalist(self, ctx:D96Parser.ParalistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardeclStatement.
    def visitVardeclStatement(self, ctx:D96Parser.VardeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varliststmt.
    def visitVarliststmt(self, ctx:D96Parser.VarliststmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignStatement.
    def visitAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#assignvar.
    def visitAssignvar(self, ctx:D96Parser.AssignvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expAssignVar.
    def visitExpAssignVar(self, ctx:D96Parser.ExpAssignVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifStmtatement.
    def visitIfStmtatement(self, ctx:D96Parser.IfStmtatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elsePart.
    def visitElsePart(self, ctx:D96Parser.ElsePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#forinStatement.
    def visitForinStatement(self, ctx:D96Parser.ForinStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#breakStatement.
    def visitBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#continueStatement.
    def visitContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#returnStatement.
    def visitReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#methodInvoStatement.
    def visitMethodInvoStatement(self, ctx:D96Parser.MethodInvoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression1.
    def visitExpression1(self, ctx:D96Parser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression2.
    def visitExpression2(self, ctx:D96Parser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression3.
    def visitExpression3(self, ctx:D96Parser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression4.
    def visitExpression4(self, ctx:D96Parser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression5.
    def visitExpression5(self, ctx:D96Parser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression6.
    def visitExpression6(self, ctx:D96Parser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression7a.
    def visitExpression7a(self, ctx:D96Parser.Expression7aContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression7b.
    def visitExpression7b(self, ctx:D96Parser.Expression7bContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression8.
    def visitExpression8(self, ctx:D96Parser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression9.
    def visitExpression9(self, ctx:D96Parser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression10.
    def visitExpression10(self, ctx:D96Parser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#objectCreate.
    def visitObjectCreate(self, ctx:D96Parser.ObjectCreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#listOfExpressions.
    def visitListOfExpressions(self, ctx:D96Parser.ListOfExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expression11.
    def visitExpression11(self, ctx:D96Parser.Expression11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arraytypedecl.
    def visitArraytypedecl(self, ctx:D96Parser.ArraytypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#typenamearray.
    def visitTypenamearray(self, ctx:D96Parser.TypenamearrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayofvalue.
    def visitArrayofvalue(self, ctx:D96Parser.ArrayofvalueContext):
        return self.visitChildren(ctx)



del D96Parser