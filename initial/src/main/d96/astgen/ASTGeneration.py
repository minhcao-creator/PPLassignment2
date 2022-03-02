# 1813061
from multiprocessing.sharedctypes import Array
from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program(self.visit(ctx.classdecls()))


    # Visit a parse tree produced by D96Parser#classdecls.
    def visitClassdecls(self, ctx:D96Parser.ClassdeclsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.classdecl())]
        return [self.visit(ctx.classdecl())] + self.visit(ctx.classdecls())


    # Visit a parse tree produced by D96Parser#classdecl.
    def visitClassdecl(self, ctx:D96Parser.ClassdeclContext):
        superclass = None
        if ctx.superclass():
            superclass = self.visit(ctx.superclass())
        memberlist = []
        if ctx.memberlist():
            memberlist = self.visit(ctx.memberlist())
            if ctx.ID().getText() == "Program":
                for i in memberlist:
                    if type(i) is MethodDecl:
                        if (i.param == []) and (i.name.name == "main"):
                            i.kind = Static()
        return ClassDecl(Id(ctx.ID().getText()), memberlist, superclass)

    # Visit a parse tree produced by D96Parser#superclass.
    def visitSuperclass(self, ctx:D96Parser.SuperclassContext):
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by D96Parser#memberlist.
    def visitMemberlist(self, ctx:D96Parser.MemberlistContext):
        if ctx.getChildCount() == 1: 
            return self.visit(ctx.member())
        return self.visit(ctx.member()) + self.visit(ctx.memberlist())


    # Visit a parse tree produced by D96Parser#member.
    def visitMember(self, ctx:D96Parser.MemberContext):
        if ctx.attributedecl(): 
            return self.visit(ctx.attributedecl())
        if ctx.methoddecl(): 
            return [self.visit(ctx.methoddecl())]
        if ctx.constructor(): 
            return [self.visit(ctx.constructor())]
        return [self.visit(ctx.destructor())]
        


    # Visit a parse tree produced by D96Parser#attributedecl.
    def visitAttributedecl(self, ctx:D96Parser.AttributedeclContext):
        return self.visit(ctx.vardecl())


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        if ctx.VAR():
            if ctx.idname():
                lsVar = self.visit(ctx.varlist())
                lsVar = [[self.visit(ctx.idname())] + lsVar[0] , lsVar[1] + [self.visit(ctx.value())] , lsVar[2]]
                attrdl = []
                for index in range(0,len(lsVar[0])):
                    idcurr = lsVar[0][index]
                    if idcurr.name[0] == "$":
                        attrdl += [AttributeDecl(Static(), VarDecl(idcurr,lsVar[2],lsVar[1][index]))]
                    else:
                        attrdl += [AttributeDecl(Instance(), VarDecl(idcurr,lsVar[2],lsVar[1][index]))]
                return attrdl
            lsId = self.visit(ctx.idnamelist())
            attrdl = []
            for index in range(0,len(lsId)):
                idcurr = lsId[index]
                if idcurr.name[0] == "$": 
                    if type(self.visit(ctx.typename())) is ClassType: 
                        attrdl += [AttributeDecl(Static(), VarDecl(idcurr,self.visit(ctx.typename()),NullLiteral()))]
                    else: attrdl += [AttributeDecl(Static(), VarDecl(idcurr,self.visit(ctx.typename()),None))]
                else:
                    if type(self.visit(ctx.typename())) is ClassType: 
                        attrdl += [AttributeDecl(Instance(), VarDecl(idcurr,self.visit(ctx.typename()),NullLiteral()))]
                    else: attrdl += [AttributeDecl(Instance(), VarDecl(idcurr,self.visit(ctx.typename()),None))]
            return attrdl
        
        if ctx.idname():
            lsVar = self.visit(ctx.varlist())
            lsVar = [[self.visit(ctx.idname())] + lsVar[0] , lsVar[1] + [self.visit(ctx.value())] , lsVar[2]]
            attrdl = []
            for index in range(0,len(lsVar[0])):
                idcurr = lsVar[0][index]
                if idcurr.name[0] == "$":
                    attrdl += [AttributeDecl(Static(), ConstDecl(idcurr,lsVar[2],lsVar[1][index]))]
                else:
                    attrdl += [AttributeDecl(Instance(),ConstDecl(idcurr,lsVar[2],lsVar[1][index]))]
            return attrdl
        lsId = self.visit(ctx.idnamelist())
        attrdl = []
        for index in range(0,len(lsId)):
            idcurr = lsId[index]
            if idcurr.name[0] == "$": 
                if type(self.visit(ctx.typename())) is ClassType: 
                    attrdl += [AttributeDecl(Static(), ConstDecl(idcurr,self.visit(ctx.typename()),NullLiteral()))]
                else: attrdl += [AttributeDecl(Static(), ConstDecl(idcurr,self.visit(ctx.typename()),None))]
            else:
                if type(self.visit(ctx.typename())) is ClassType: 
                    attrdl += [AttributeDecl(Instance(), ConstDecl(idcurr,self.visit(ctx.typename()),NullLiteral()))]
                else: attrdl += [AttributeDecl(Instance(), ConstDecl(idcurr,self.visit(ctx.typename()),None))]
        return attrdl 
                    

    # Visit a parse tree produced by D96Parser#varlist.
    def visitVarlist(self, ctx:D96Parser.VarlistContext):
        if ctx.getChildCount() == 3: 
            return [[],[],self.visit(ctx.typename())]
        lsVar = self.visit(ctx.varlist())
        return [[self.visit(ctx.idname())] + lsVar[0] , lsVar[1] + [self.visit(ctx.value())] , lsVar[2]]


    # Visit a parse tree produced by D96Parser#idnamelist.
    def visitIdnamelist(self, ctx:D96Parser.IdnamelistContext):
        if ctx.getChildCount() == 1: return [self.visit(ctx.idname())]
        return [self.visit(ctx.idname())] + self.visit(ctx.idnamelist())


    # Visit a parse tree produced by D96Parser#typename.
    def visitTypename(self, ctx:D96Parser.TypenameContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()
        if ctx.ID(): return ClassType(Id(ctx.ID().getText()))
        return self.visit(ctx.arraytypedecl())


    # Visit a parse tree produced by D96Parser#value.
    def visitValue(self, ctx:D96Parser.ValueContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by D96Parser#idname.
    def visitIdname(self, ctx:D96Parser.IdnameContext):
        if ctx.SID(): return Id(ctx.SID().getText())
        return Id(ctx.ID().getText())


    # Visit a parse tree produced by D96Parser#methoddecl.
    def visitMethoddecl(self, ctx:D96Parser.MethoddeclContext):
        idname = self.visit(ctx.idname())
        if ctx.paralist():
            if idname.name[0] == "$":
                return MethodDecl(Static(), idname, self.visit(ctx.paralist()), self.visit(ctx.block_stmt()))
            return MethodDecl(Instance(), idname, self.visit(ctx.paralist()), self.visit(ctx.block_stmt()))
        if idname.name[0] == "$":
            return MethodDecl(Static(), idname, [], self.visit(ctx.block_stmt()))
        return MethodDecl(Instance(), idname, [], self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#paralist.
    def visitParalist(self, ctx:D96Parser.ParalistContext):
        ls = self.visit(ctx.idlist())
        typ = self.visit(ctx.typename())
        if ctx.getChildCount() == 3:
            return list(map(lambda x:VarDecl(x, typ),ls))
        return list(map(lambda x:VarDecl(x, typ),ls)) + self.visit(ctx.paralist())



    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        if ctx.paralist():
            return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paralist()), self.visit(ctx.block_stmt()))
        return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), [], self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], self.visit(ctx.block_stmt()))


    # Visit a parse tree produced by D96Parser#vardeclStatement.
    def visitVardeclStatement(self, ctx:D96Parser.VardeclStatementContext):
        if ctx.VAR():
            if ctx.ID():
                lsVar = self.visit(ctx.varliststmt())
                lsVar = [[Id(ctx.ID().getText())] + lsVar[0] ,lsVar[1] + [self.visit(ctx.value())], lsVar[2]]
                vardl = []
                for index in range(0,len(lsVar[0])):
                    vardl += [VarDecl(lsVar[0][index],lsVar[2],lsVar[1][index])]
                return vardl
            lsId = self.visit(ctx.idlist())
            vardl = []
            for index in range(0,len(lsId)):
                if type(self.visit(ctx.typename())) is ClassType:
                    vardl += [VarDecl(lsId[index],self.visit(ctx.typename()),NullLiteral())]
                else: vardl += [VarDecl(lsId[index],self.visit(ctx.typename()),None)]
            return vardl
        if ctx.ID():
            lsVar = self.visit(ctx.varliststmt())
            lsVar = [[Id(ctx.ID().getText())] + lsVar[0] , lsVar[1] + [self.visit(ctx.value())] , lsVar[2]]
            vardl = []
            for index in range(0,len(lsVar[0])):
                vardl += [ConstDecl(lsVar[0][index],lsVar[2],lsVar[1][index])]
            return vardl
        lsId = self.visit(ctx.idlist())
        vardl = []
        for index in range(0,len(lsId)):
            if type(self.visit(ctx.typename())) is ClassType:
                vardl += [ConstDecl(lsId[index],self.visit(ctx.typename()),NullLiteral())]
            else: vardl += [ConstDecl(lsId[index],self.visit(ctx.typename()),None)]
        return vardl


    # Visit a parse tree produced by D96Parser#varliststmt.
    def visitVarliststmt(self, ctx:D96Parser.VarliststmtContext):
        if ctx.getChildCount() == 3: 
            return [[],[],self.visit(ctx.typename())]
        lsVar = self.visit(ctx.varlist())
        return [[Id(ctx.ID().getText())] + lsVar[0] ,lsVar[1] + [self.visit(ctx.value())], lsVar[2]]


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        if ctx.getChildCount() == 1: return [Id(ctx.ID().getText())]
        return [Id(ctx.ID().getText())] + self.visit(ctx.idlist())


    # Visit a parse tree produced by D96Parser#assignStatement.
    def visitAssignStatement(self, ctx:D96Parser.AssignStatementContext):
        return Assign(self.visit(ctx.assignvar()), self.visit(ctx.expression()))


    # Visit a parse tree produced by D96Parser#assignvar.
    def visitAssignvar(self, ctx:D96Parser.AssignvarContext):
        if ctx.DOT(): 
            return FieldAccess(self.visit(ctx.expression8()), Id(ctx.ID().getText()))
        if ctx.DOUBLECOLON():
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.SID().getText()))
        if ctx.expAssignVar():
            return self.visit(ctx.expAssignVar())
        return Id(ctx.ID().getText())
    
    def visitExpAssignVar(self, ctx:D96Parser.ExpAssignVarContext):
        if ctx.expression7b().getChildCount() == 2: 
            ls = self.visit(ctx.expression7b()) + self.visit(ctx.index_operators())
            star = ls[0]
            ls = ls[1:]
            return ArrayCell(star,ls)
        return ArrayCell(self.visit(ctx.expression7b()), self.visit(ctx.index_operators()))
    

    # Visit a parse tree produced by D96Parser#ifStmtatement.
    def visitIfStmtatement(self, ctx:D96Parser.IfStmtatementContext):
        return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt()), self.visit(ctx.elsePart()))


    # Visit a parse tree produced by D96Parser#elsePart.
    def visitElsePart(self, ctx:D96Parser.ElsePartContext):
        if ctx.ELSEIF(): 
            return If(self.visit(ctx.expression()), self.visit(ctx.block_stmt()), self.visit(ctx.elsePart()))
        if ctx.ELSE():
            return self.visit(ctx.block_stmt())
        return None

    # Visit a parse tree produced by D96Parser#forinStatement.
    def visitForinStatement(self, ctx:D96Parser.ForinStatementContext):
        if ctx.BY():
            return For(Id(ctx.ID().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.block_stmt()), self.visit(ctx.expression(2)))
        return For(Id(ctx.ID().getText()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)), self.visit(ctx.block_stmt()), IntLiteral(1))

    # Visit a parse tree produced by D96Parser#breakStatement.
    def visitBreakStatement(self, ctx:D96Parser.BreakStatementContext):
        return Break()

    # Visit a parse tree produced by D96Parser#continueStatement.
    def visitContinueStatement(self, ctx:D96Parser.ContinueStatementContext):
        return Continue()


    # Visit a parse tree produced by D96Parser#returnStatement.
    def visitReturnStatement(self, ctx:D96Parser.ReturnStatementContext):
        if ctx.expression(): return Return(self.visit(ctx.expression()))
        return Return(None)


    # Visit a parse tree produced by D96Parser#methodInvoStatement.
    def visitMethodInvoStatement(self, ctx:D96Parser.MethodInvoStatementContext):
        if ctx.DOT():
            if ctx.listOfExpressions():
                return CallStmt(self.visit(ctx.expression()), Id(ctx.ID().getText()), self.visit(ctx.listOfExpressions()))
            return CallStmt(self.visit(ctx.expression()), Id(ctx.ID().getText()), [])
        if ctx.DOUBLECOLON():
            if ctx.listOfExpressions():
                return CallStmt(Id(ctx.ID().getText()), Id(ctx.SID().getText()), self.visit(ctx.listOfExpressions()))
            return CallStmt(Id(ctx.ID().getText()), Id(ctx.SID().getText()), [])
                

    # Visit a parse tree produced by D96Parser#block_stmt.
    def visitBlock_stmt(self, ctx:D96Parser.Block_stmtContext):
        return Block(self.visit(ctx.statements()))


    # Visit a parse tree produced by D96Parser#statements.
    def visitStatements(self, ctx:D96Parser.StatementsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.statement()) + self.visit(ctx.statements())


    # Visit a parse tree produced by D96Parser#statement.
    def visitStatement(self, ctx:D96Parser.StatementContext):
        if ctx.vardeclStatement():
            return self.visit(ctx.vardeclStatement())
        if ctx.arraytypedecl():
            return [self.visit(ctx.arraytypedecl())]
        if ctx.assignStatement():
            return [self.visit(ctx.assignStatement())]
        if ctx.ifStmtatement():
            return [self.visit(ctx.ifStmtatement())]
        if ctx.forinStatement():
            return [self.visit(ctx.forinStatement())]
        if ctx.breakStatement():
            return [self.visit(ctx.breakStatement())]
        if ctx.continueStatement():
            return [self.visit(ctx.continueStatement())]
        if ctx.returnStatement():
            return [self.visit(ctx.returnStatement())]
        if ctx.methodInvoStatement():
            return [self.visit(ctx.methodInvoStatement())]
        return [self.visit(ctx.block_stmt())]


    # Visit a parse tree produced by D96Parser#expression.
    def visitExpression(self, ctx:D96Parser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression1(0))
        else:
            if ctx.STREQUAL(): 
                return BinaryOp(ctx.STREQUAL().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))
            return BinaryOp(ctx.STRCAT().getText(), self.visit(ctx.expression1(0)), self.visit(ctx.expression1(1)))

    # Visit a parse tree produced by D96Parser#expression1.
    def visitExpression1(self, ctx:D96Parser.Expression1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression2(0))
        else:
            if ctx.EQUAL(): 
                return BinaryOp(ctx.EQUAL().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
            if ctx.NOTEQUAL(): 
                return BinaryOp(ctx.NOTEQUAL().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
            if ctx.SMALLER(): 
                return BinaryOp(ctx.SMALLER().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
            if ctx.LARGE(): 
                return BinaryOp(ctx.LARGE().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
            if ctx.SMALLOREQUAL(): 
                return BinaryOp(ctx.SMALLOREQUAL().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))
            return BinaryOp(ctx.LARGEOREQUAL().getText(), self.visit(ctx.expression2(0)), self.visit(ctx.expression2(1)))

    # Visit a parse tree produced by D96Parser#expression2.
    def visitExpression2(self, ctx:D96Parser.Expression2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression3())
        else:
            if ctx.AND(): 
                return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))


    # Visit a parse tree produced by D96Parser#expression3.
    def visitExpression3(self, ctx:D96Parser.Expression3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression4())
        else:
            if ctx.ADD(): 
                return BinaryOp(ctx.ADD().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
            return BinaryOp(ctx.SUB().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))


    # Visit a parse tree produced by D96Parser#expression4.
    def visitExpression4(self, ctx:D96Parser.Expression4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expression5())
        else:
            if ctx.MUL(): 
                return BinaryOp(ctx.MUL().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
            if ctx.DIV(): 
                return BinaryOp(ctx.DIV().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))
            return BinaryOp(ctx.MOD().getText(), self.visit(ctx.expression4()), self.visit(ctx.expression5()))


    # Visit a parse tree produced by D96Parser#expression5.
    def visitExpression5(self, ctx:D96Parser.Expression5Context):
        if ctx.getChildCount() == 2: 
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expression5()))
        return self.visit(ctx.expression6())


    # Visit a parse tree produced by D96Parser#expression6.
    def visitExpression6(self, ctx:D96Parser.Expression6Context):
        if ctx.getChildCount() == 2: 
            return UnaryOp(ctx.SUB().getText(), self.visit(ctx.expression6()))
        return self.visit(ctx.expression7a())

    def visitExpression7a(self, ctx:D96Parser.Expression7aContext):
        ls = self.visit(ctx.expression7b())
        if ctx.expression7b().getChildCount() == 2:
            star = ls[0]
            ls = ls[1:]
            return ArrayCell(star,ls)
        return ls

    # Visit a parse tree produced by D96Parser#expression7.
    def visitExpression7b(self, ctx:D96Parser.Expression7bContext):
        if ctx.getChildCount() == 2:
            if ctx.expression7b().getChildCount() == 2:
                return self.visit(ctx.expression7b()) + self.visit(ctx.index_operators())
            return [self.visit(ctx.expression7b())] + self.visit(ctx.index_operators())
        return self.visit(ctx.expression8())


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return [self.visit(ctx.expression())]


    # Visit a parse tree produced by D96Parser#expression8.
    def visitExpression8(self, ctx:D96Parser.Expression8Context):
        if ctx.getChildCount() == 3: 
            return FieldAccess(self.visit(ctx.expression8()), Id(ctx.ID().getText()))
        if ctx.LB():
            if ctx.listOfExpressions():
                return CallExpr(self.visit(ctx.expression8()), Id(ctx.ID().getText()), self.visit(ctx.listOfExpressions()))
            return CallExpr(self.visit(ctx.expression8()), Id(ctx.ID().getText()), [])
        return self.visit(ctx.expression9())


    # Visit a parse tree produced by D96Parser#expression9.
    def visitExpression9(self, ctx:D96Parser.Expression9Context):
        if ctx.getChildCount() == 3: 
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.SID().getText()))
        if ctx.LB():
            if ctx.listOfExpressions():
                return CallExpr(Id(ctx.ID().getText()), Id(ctx.SID().getText()), self.visit(ctx.listOfExpressions()))
            return CallExpr(Id(ctx.ID().getText()), Id(ctx.SID().getText()), [])
        return self.visit(ctx.expression10())
            

    # Visit a parse tree produced by D96Parser#expression10.
    def visitExpression10(self, ctx:D96Parser.Expression10Context):
        if ctx.objectCreate(): 
            return self.visit(ctx.objectCreate())
        return self.visit(ctx.expression11())


    # Visit a parse tree produced by D96Parser#objectCreate.
    def visitObjectCreate(self, ctx:D96Parser.ObjectCreateContext):
        if ctx.listOfExpressions(): 
            return NewExpr(Id(ctx.ID().getText()),self.visit(ctx.listOfExpressions()))
        return NewExpr(Id(ctx.ID().getText()),[])


    # Visit a parse tree produced by D96Parser#listOfExpressions.
    def visitListOfExpressions(self, ctx:D96Parser.ListOfExpressionsContext):
        if ctx.getChildCount() == 1: 
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.listOfExpressions())

    # Visit a parse tree produced by D96Parser#expression11.
    def visitExpression11(self, ctx:D96Parser.Expression11Context):
        if ctx.ID(): 
            return Id(ctx.ID().getText())
        if ctx.INTLIT0(): 
            intnum = ctx.INTLIT0().getText()
            if intnum == '0':
                return IntLiteral(int(intnum))
            elif intnum == '00':
                return IntLiteral(int(intnum, base = 8))
            elif (intnum == '0x0') or (intnum == '0X0'):
                return IntLiteral(int(intnum, base = 16))
            else:
                return IntLiteral(int(intnum, base = 2))
        if ctx.INTLIT1(): 
            intnum = ctx.INTLIT1().getText()
            if intnum[0] == '0':
                s = intnum[1]
                if s == 'x' or s == 'X':
                    return IntLiteral(int(intnum, base = 16))
                if s == 'b' or s == 'B':
                    return IntLiteral(int(intnum, base = 2))
                return IntLiteral(int(intnum, base = 8))
            return IntLiteral(int(intnum))
        if ctx.FLOATLIT(): 
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        if ctx.STRINGLIT(): 
            return StringLiteral(ctx.STRINGLIT().getText())
        if ctx.BOOLLIT(): 
            return BooleanLiteral(ctx.BOOLLIT().getText() == 'True')
        if ctx.arrayofvalue(): 
            return self.visit(ctx.arrayofvalue())
        if ctx.LB(): 
            return self.visit(ctx.expression())
        if ctx.SELF(): 
            return SelfLiteral()
        return NullLiteral()


    # Visit a parse tree produced by D96Parser#arraytypedecl.
    def visitArraytypedecl(self, ctx:D96Parser.ArraytypedeclContext):
        intnum = ctx.INTLIT1().getText()
        if intnum[0] == '0':
            s = intnum[1]
            if s == 'x' or s == 'X':
                return ArrayType(int(intnum, base = 16), self.visit(ctx.typenamearray()))
            if s == 'b' or s == 'B':
                return ArrayType(int(intnum, base = 2), self.visit(ctx.typenamearray()))
            return ArrayType(int(intnum, base = 8), self.visit(ctx.typenamearray()))
        return ArrayType(int(intnum), self.visit(ctx.typenamearray()))


    # Visit a parse tree produced by D96Parser#typenamearray.
    def visitTypenamearray(self, ctx:D96Parser.TypenamearrayContext):
        if ctx.INT(): return IntType()
        if ctx.FLOAT(): return FloatType()
        if ctx.BOOLEAN(): return BoolType()
        if ctx.STRING(): return StringType()
        return self.visit(ctx.arraytypedecl())
        


    # Visit a parse tree produced by D96Parser#arrayofvalue.
    def visitArrayofvalue(self, ctx:D96Parser.ArrayofvalueContext):
        if ctx.listOfExpressions():
            return ArrayLiteral(self.visit(ctx.listOfExpressions()))
        return ArrayLiteral([])


