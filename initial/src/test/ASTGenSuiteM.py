import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {} """
        input = """Class Program {}"""
        expect = "Program([ClassDecl(Id(Program),[])])"
        self.assertTrue(TestAST.test(input, expect, 'ast1'))

    def test2(self):
        """Simple program: int main() {} """
        input = """Class Program: parent {}"""
        expect = "Program([ClassDecl(Id(Program),Id(parent),[])])"
        self.assertTrue(TestAST.test(input, expect, 'ast2'))

    def test3(self):
        """Simple program: int main() {} """
        input = """Class Program: parent {}
                Class Pro2: par2 {}"""
        expect = "Program([ClassDecl(Id(Program),Id(parent),[]),ClassDecl(Id(Pro2),Id(par2),[])])"
        self.assertTrue(TestAST.test(input, expect, 'ast3'))

    def test4(self):
        """Simple program: int main() {} """
        input = """Class Program: parent {}
                Class Pro2: par2 {
                    Var a : Int;
                }"""
        expect = "Program([ClassDecl(Id(Program),Id(parent),[]),ClassDecl(Id(Pro2),Id(par2),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast4'))

    def test5(self):
        """Simple program: int main() {} """
        input = """Class Program: parent {}
                Class Pro2 {
                    Var a,b : Int = 3,5;
                }"""
        expect = "Program([ClassDecl(Id(Program),Id(parent),[]),ClassDecl(Id(Pro2),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(5)))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast5'))

    def test6(self):
        """Simple program: int main() {} """
        input = """Class Program: parent {}
                Class Pro3 {
                    Var a,b,c,d : Float = 3,5,7,9;
                }"""
        expect = "Program([ClassDecl(Id(Program),Id(parent),[]),ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,IntLit(7))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,IntLit(9)))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast6'))

    def test7(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Var a,b: Float = 0x0 , 0b10101;
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(21)))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast7'))

    def test8(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Var a,b: Float = 0x0 , 0b10101;
                    Val c,d: Float = 0.123e-9878, 1.234;
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(21))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(1.234)))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast8'))

    def test9(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Val c: String = 0.123e-9878;
                    Var d,f: Boolean ;
                    Val e: Boolean = True;
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(d),BoolType)),AttributeDecl(Instance,VarDecl(Id(f),BoolType)),AttributeDecl(Instance,ConstDecl(Id(e),BoolType,BooleanLit(True)))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast9'))

    def test10(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    main() {}              
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast10'))

    def test11(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Val c: String = 0.123e-9878;
                    Constructor(a : Boolean) {}
                    Destructor() {}              
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(0.0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast11'))

    def test12(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    main() {}
                    func() {}
                    Constructor() {}              
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(func),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast12'))

    def test13(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Val c: String = 0.123e-9878;
                    Constructor(a : Boolean) {
                        Val c: String = 0.123e-9878;
                    }
                    Destructor() {}              
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(0.0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType)],Block([ConstDecl(Id(c),StringType,FloatLit(0.0))])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast13'))

    def test14(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Val c: String = 0.123e-9878;
                    Constructor(a : Boolean) {
                        Val c: String = 0.123e-9878;
                        Val d: String = 0.123e-9878;
                    }              
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(0.0))),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType)],Block([ConstDecl(Id(c),StringType,FloatLit(0.0)),ConstDecl(Id(d),StringType,FloatLit(0.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast14'))

    def test15(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Val c: String = 0.123e-9878; 
                    main() {{}}             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(c),StringType,FloatLit(0.0))),MethodDecl(Id(main),Instance,[],Block([Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast15'))

    def test16(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        Val c: String = 0.123e-9878;
                        {}
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c),StringType,FloatLit(0.0)),Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast16'))

    def test17(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        Val c: String = "minhcao";
                        Var c,d: Float = 0x0, 1.23e+9;
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c),StringType,StringLit(minhcao)),VarDecl(Id(c),FloatType,IntLit(0)),VarDecl(Id(d),FloatType,FloatLit(1230000000.0))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast17'))

    def test18(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Var a: Array[Int, 5]; 
                    main() {}             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast18'))

    def test19(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 {
                    Var a: Array[Int, 5] = Array(1,2,3); 
                    main() {}             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])),MethodDecl(Id(main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast19'))

    def test20(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        Var a: Array[Int, 5] = Array(1,2,3);
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast20'))

    def test21(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        Var a: Array[Int, 0b10101] = Array(0x1,1.2,a);
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(21,IntType),[IntLit(1),FloatLit(1.2),Id(a)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast21'))

    def test22(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        Var a: Array[Int, 0b10101] = Array(0x1,1.2,a);
                        Val b,c: Array[String, 012] = Array(b,c,d), "minh";
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(21,IntType),[IntLit(1),FloatLit(1.2),Id(a)]),ConstDecl(Id(b),ArrayType(10,StringType),[Id(b),Id(c),Id(d)]),ConstDecl(Id(c),ArrayType(10,StringType),StringLit(minh))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast22'))

    def test23(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        a = b + c;
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast23'))

    def test24(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    main() {
                        a = b + c;
                        Return;
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast24'))

    def test25(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    Val str: a = Null;
                    Var $b, c: String = Self, Array(Null, Self, a && b);
                    main() {
                        a = b + c;
                        Return;
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,ConstDecl(Id(str),ClassType(Id(a)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($b),StringType,Self())),AttributeDecl(Instance,VarDecl(Id(c),StringType,[NullLiteral(),Self(),BinaryOp(&&,Id(a),Id(b))])),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,Id(b),Id(c))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast25'))

    def test26(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main(a,b: Array[Array[Boolean, 02], 0b101]; c:String) {}             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[param(Id(a),ArrayType(5,ArrayType(2,BoolType))),param(Id(b),ArrayType(5,ArrayType(2,BoolType))),param(Id(c),StringType)],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast26'))

    def test27(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main(a,b: Array[Array[Array[Boolean, 02], 0xA1], 0b101]; c:Float) {
                        Continue;
                        Break;
                        Return;
                    }             
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[param(Id(a),ArrayType(5,ArrayType(161,ArrayType(2,BoolType)))),param(Id(b),ArrayType(5,ArrayType(161,ArrayType(2,BoolType)))),param(Id(c),FloatType)],Block([Continue,Break,Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast27'))

    def test28(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        a = b && c || e;
                    }     
                    Constructor(a,b: Array[Int, 5]; c: Float) {
                        Continue;
                        Break;
                        Return;
                        {}
                    }        
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(a),BinaryOp(||,BinaryOp(&&,Id(b),Id(c)),Id(e)))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(5,IntType)),param(Id(b),ArrayType(5,IntType)),param(Id(c),FloatType)],Block([Continue,Break,Return(),Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast28'))

    def test29(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        Return a;
                        s = Self + (Array(Null, Self, a ==. b)) + Null;
                        Return Self + (Array(Null, Self, a ==. b)) + Null;
                    }     
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([Return(Id(a)),AssignStmt(Id(s),BinaryOp(+,BinaryOp(+,Self(),[NullLiteral(),Self(),BinaryOp(==.,Id(a),Id(b))]),NullLiteral())),Return(BinaryOp(+,BinaryOp(+,Self(),[NullLiteral(),Self(),BinaryOp(==.,Id(a),Id(b))]),NullLiteral()))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast29'))

    def test30(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {}
                    Destructor() {
                        Break;
                        Continue;
                        Return;
                        {}
                    }   
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([Break,Continue,Return(),Block([])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast30'))

    def test31(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        a = New b(Null, Self);
                        b = New c(Array(2,3,4), b&&b, c +. d);
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(b),[NullLiteral(),Self()])),AssignStmt(Id(b),NewExpr(Id(c),[[IntLit(2),IntLit(3),IntLit(4)],BinaryOp(&&,Id(b),Id(b)),BinaryOp(+.,Id(c),Id(d))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast31'))

    def test32(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        a = New b(Null, Self);
                        b = New c(Array(2,3,4), b&&b, c +. d);
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(b),[NullLiteral(),Self()])),AssignStmt(Id(b),NewExpr(Id(c),[[IntLit(2),IntLit(3),IntLit(4)],BinaryOp(&&,Id(b),Id(b)),BinaryOp(+.,Id(c),Id(d))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast32'))

    def test33(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        a = New b();
                        b = a::$foo();
                        c = b::$a;
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(b),[])),AssignStmt(Id(b),CallExpr(Id(a),Id($foo),[])),AssignStmt(Id(c),FieldAccess(Id(b),Id($a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast33'))

    def test34(self):
        """Simple program: int main() {} """
        input = """ Class Pro3 { 
                    $main() {
                        a = New b(Array());
                        b = a::$foo(s,c,d);
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(b),[[]])),AssignStmt(Id(b),CallExpr(Id(a),Id($foo),[Id(s),Id(c),Id(d)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast34'))

    def test35(self):
        """Simple program: int main() {} """
        input = """ Class Pro { 
                    $main() {
                        If (a < b + c * d && e) {
                            Return;
                        }
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id($main),Static,[],Block([If(BinaryOp(<,Id(a),BinaryOp(&&,BinaryOp(+,Id(b),BinaryOp(*,Id(c),Id(d))),Id(e))),Block([Return()]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast35'))

    def test36(self):
        """Simple program: int main() {} """
        input = """ Class Pro { 
                    $main() {
                        Foreach (a In b .. c) {
                            Return;
                        }
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id($main),Static,[],Block([For(Id(a),Id(b),Id(c),IntLit(1),Block([Return()])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast36'))

    def test37(self):
        """Simple program: int main() {} """
        input = """ Class Pro { 
                    $main() {
                        If (a) {
                            Foreach (a In b .. c By 2) {
                                Return;
                            }
                        }
                        Elseif (b) {
                            Foreach (a In b .. c By !a + c) {
                                Return;
                            }
                        } 
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id($main),Static,[],Block([If(Id(a),Block([For(Id(a),Id(b),Id(c),IntLit(2),Block([Return()])])]),If(Id(b),Block([For(Id(a),Id(b),Id(c),BinaryOp(+,UnaryOp(!,Id(a)),Id(c)),Block([Return()])])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast37'))

    def test38(self):
        """Simple program: int main() {} """
        input = """ Class Pro { 
                    $main() {
                        If (a) {
                            Foreach (a In b .. c By -x) {
                                Return;
                            }
                        }
                        Elseif (b) {
                            Foreach (a In b .. c By b && c) {
                                Return;
                            }
                        } 
                        Else {
                            Foreach (a In b .. c) {
                                Return;
                            }
                        }
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id($main),Static,[],Block([If(Id(a),Block([For(Id(a),Id(b),Id(c),UnaryOp(-,Id(x)),Block([Return()])])]),If(Id(b),Block([For(Id(a),Id(b),Id(c),BinaryOp(&&,Id(b),Id(c)),Block([Return()])])]),Block([For(Id(a),Id(b),Id(c),IntLit(1),Block([Return()])])])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast38'))

    def test39(self):
        """Simple program: int main() {} """
        input = """ Class Pro { 
                    $main() {
                        If (a) {
                            Foreach (a In b .. c By -x) {
                                Foreach (a In b .. c By -x) {
                                    Return;
                                }
                            }
                        }
                    }
                }"""
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id($main),Static,[],Block([If(Id(a),Block([For(Id(a),Id(b),Id(c),UnaryOp(-,Id(x)),Block([For(Id(a),Id(b),Id(c),UnaryOp(-,Id(x)),Block([Return()])])])])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast39'))

    def test40(self):
        input = """Class a{
            main(){
                Foreach (i In A..Null By a::$b){
                    Return;
                }
            }
        }"""
        expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
            [For(Id('i'), Id('A'), NullLiteral(), Block([Return()]), FieldAccess(Id('a'), Id('$b')))]))])]))
        self.assertTrue(TestAST.test(input, expect, 'ast40'))

    def test41(self):
        input = """Class Program{
            Var x: Int = ((((a[1])))[2]);
            t(){
                Foreach(i In ((a[1]))[2] + (a)[2] .. 6){}
                Return ((((a[1])))[2]) + 456;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]))),MethodDecl(Id(t),Instance,[],Block([For(Id(i),BinaryOp(+,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),ArrayCell(Id(a),[IntLit(2)])),IntLit(6),IntLit(1),Block([])]),Return(BinaryOp(+,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)]),IntLit(456)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast41'))

    def test42(self):
        input = """Class Program{
            Var x: Int = ((((a[1])))[2]);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType,ArrayCell(ArrayCell(Id(a),[IntLit(1)]),[IntLit(2)])))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast42'))

    def test43(self):
        input = """
        Class Program
        {
            main()
            {
                Var arr: Array[Int, 5] = Array(9, 2, 8, 4, 1);
                Var sorts: Sorting = New Sorting();

                Foreach(i In 0 .. Sys.size_of(arr.to_int())/4)
                {
                    sorts.add(arr[i]);
                }

                sorts.bubbleSort();
            }
        }
                """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(5,IntType),[IntLit(9),IntLit(2),IntLit(8),IntLit(4),IntLit(1)]),VarDecl(Id(sorts),ClassType(Id(Sorting)),NewExpr(Id(Sorting),[])),For(Id(i),IntLit(0),BinaryOp(/,CallExpr(Id(Sys),Id(size_of),[CallExpr(Id(arr),Id(to_int),[])]),IntLit(4)),IntLit(1),Block([Call(Id(sorts),Id(add),[ArrayCell(Id(arr),[Id(i)])])])]),Call(Id(sorts),Id(bubbleSort),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast43'))

    def test44(self):
        input = """
        Class QuickSort
        {
            quicksort(start, end: Array[Int, 100])
            {
                Val size: Int = end - start;
                Var part: Partition;
                If(size >= 1)
                {
                    Var i: Int = part.partition(start, end) - start;
                    Out.Print(i +. " ");
                    QuickSort.quicksort(start, start + i);
                    QuickSort.quicksort(start + i + 1, end);
                }
            }
        }
                """
        expect = "Program([ClassDecl(Id(QuickSort),[MethodDecl(Id(quicksort),Instance,[param(Id(start),ArrayType(100,IntType)),param(Id(end),ArrayType(100,IntType))],Block([ConstDecl(Id(size),IntType,BinaryOp(-,Id(end),Id(start))),VarDecl(Id(part),ClassType(Id(Partition)),NullLiteral()),If(BinaryOp(>=,Id(size),IntLit(1)),Block([VarDecl(Id(i),IntType,BinaryOp(-,CallExpr(Id(part),Id(partition),[Id(start),Id(end)]),Id(start))),Call(Id(Out),Id(Print),[BinaryOp(+.,Id(i),StringLit( ))]),Call(Id(QuickSort),Id(quicksort),[Id(start),BinaryOp(+,Id(start),Id(i))]),Call(Id(QuickSort),Id(quicksort),[BinaryOp(+,BinaryOp(+,Id(start),Id(i)),IntLit(1)),Id(end)])]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast44'))

    def test45(self):
        input = """
        Class P
        {
            print()
            {
                Out.Print("This is not a simple \\b string");
                Out.Print("This is a \\f simple string");
            }
        }
        """
        expect = """Program([ClassDecl(Id(P),[MethodDecl(Id(print),Instance,[],Block([Call(Id(Out),Id(Print),[StringLit(This is not a simple \\b string)]),Call(Id(Out),Id(Print),[StringLit(This is a \\f simple string)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast45'))

    def test46(self):
        input = """
        Class Pro
        {
            Constructor(){}
            Destructor(){}
        }
        """
        expect = "Program([ClassDecl(Id(Pro),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast46'))

    def test47(self):
        input = """
        Class Program
        {
            isSymmetric(arr: Array[Array[Int, 1000], 1000]; row, col: Int)
            {
                Foreach(row In 0 .. 1000 By 1)
                {
                }

                Return True;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(isSymmetric),Instance,[param(Id(arr),ArrayType(1000,ArrayType(1000,IntType))),param(Id(row),IntType),param(Id(col),IntType)],Block([For(Id(row),IntLit(0),IntLit(1000),IntLit(1),Block([])]),Return(BooleanLit(True))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast47'))

    def test48(self):
        input = """
        Class B
        {
            ## this is a simple function ##
            func(a,b: Int; d: String)
            {
                Var r, s: Int;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
            }
        }
        """
        expect = "Program([ClassDecl(Id(B),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(d),StringType)],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI))))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast48'))

    def test49(self):
        input = """
        Class Program
        {
            main(a: Int)
            {
                Var a: Int;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([VarDecl(Id(a),IntType)]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast49'))

    def test50(self):
        input = """
        Class Test
        {
            func(){}
        }
        """
        expect = """Program([ClassDecl(Id(Test),[MethodDecl(Id(func),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast50'))

    def test51(self):
        input = """ 
            Class Ab {
                main(Minh: String){
                    abc = "how to do?";
                }
                Val Minh : Boolean = False;
                main(){
                    abc = cbd.bcd;
                }
                Var b : Boolean = False;
            }
            """
        expect = """Program([ClassDecl(Id(Ab),[MethodDecl(Id(main),Instance,[param(Id(Minh),StringType)],Block([AssignStmt(Id(abc),StringLit(how to do?))])),AttributeDecl(Instance,ConstDecl(Id(Minh),BoolType,BooleanLit(False))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(abc),FieldAccess(Id(cbd),Id(bcd)))])),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BooleanLit(False)))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast51'))

    def test52(self):
        input = """ 
            Class Ab {
                _func(_f:function){
                    Return;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Ab),[MethodDecl(Id(_func),Instance,[param(Id(_f),ClassType(Id(function)))],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast52'))

    def test53(self):
        input = """
                Class Program{
                    Var a,$b,$c : Program; 
                }
                """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Program)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($b),ClassType(Id(Program)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($c),ClassType(Id(Program)),NullLiteral()))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast53'))

    def test54(self):
        input = """
                Class Program{
                    Val a,b,$c : Array[Array[Array[Int, 0123], 123], 0b10101]; 
                }
                """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(21,ArrayType(123,ArrayType(83,IntType))),None)),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(21,ArrayType(123,ArrayType(83,IntType))),None)),AttributeDecl(Static,ConstDecl(Id($c),ArrayType(21,ArrayType(123,ArrayType(83,IntType))),None))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast54'))

    def test55(self):
        input = """
                Class Program{
                    main() {
                        Var a,b,c,d,e,f:Int = 0,00,0x0,0X0,0b0,0B0;
                    } 
                }
                """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0)),VarDecl(Id(e),IntType,IntLit(0)),VarDecl(Id(f),IntType,IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast55'))

    def test56(self):
        input = """
                Class Program{
                    Var i:Array[Int,3];
                    main() {
                        Foreach(i In 0 .. 20) {}
                    } 
                }
                """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(i),ArrayType(3,IntType))),MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(20),IntLit(1),Block([])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast56'))

    def test57(self):
        input = """
                Class Shape {}
                Class Polygon : Shape {}
                Class Program{
                    main() {
                    } 
                }
                """
        expect = """Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Polygon),Id(Shape),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast57'))

    def test58(self):
        input = """Class Polygon : Shape {
            Constructor(a,b:Int;c,d:Float) {}
            Constructor() {}
            Destructor() {}
            Destructor() {}
        }
        """
        expect = "Program([ClassDecl(Id(Polygon),Id(Shape),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType),param(Id(d),FloatType)],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast58'))

    def test59(self):
        input = """
        Class Shape {}
        Class Polygon : Shape {
            Var $a:Int = 1;
            draw() {
                Var c:Float = New Shape() + 1 + 2;
                c = b;
            }
        }
        """
        expect = "Program([ClassDecl(Id(Shape),[]),ClassDecl(Id(Polygon),Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),MethodDecl(Id(draw),Instance,[],Block([VarDecl(Id(c),FloatType,BinaryOp(+,BinaryOp(+,NewExpr(Id(Shape),[]),IntLit(1)),IntLit(2))),AssignStmt(Id(c),Id(b))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast59'))

    def test60(self):
        input = """ 
        Class Polygon {
            draw(b:Polygon;d:Int){
                Foreach(i In "a" .. "b" By 2) {
                    If (i == "b") {
                        Continue;
                    }
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Polygon),[MethodDecl(Id(draw),Instance,[param(Id(b),ClassType(Id(Polygon))),param(Id(d),IntType)],Block([For(Id(i),StringLit(a),StringLit(b),IntLit(2),Block([If(BinaryOp(==,Id(i),StringLit(b)),Block([Continue]))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast60'))

    def test61(self):
        input = """
            Class A{ }
            Class B{ }
            Class C{ }
            Class D{ }
            Class E{ }
            Class F{ }
            """
        expect = "Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[]),ClassDecl(Id(D),[]),ClassDecl(Id(E),[]),ClassDecl(Id(F),[])])"
        self.assertTrue(TestAST.test(input, expect, 'ast61'))

    def test62(self):
        input = """
            Class Program {
                    Val a: Int = 5;
                    getMethod(Minh: Float){
                        a = 3;
                        a[1] = b[1][2][3][4];
                        Self.a = a;
                    }

            }

            """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(5))),MethodDecl(Id(getMethod),Instance,[param(Id(Minh),FloatType)],Block([AssignStmt(Id(a),IntLit(3)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(b),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(FieldAccess(Self(),Id(a)),Id(a))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast62'))

    def test63(self):
        input = """
        Class A{
            $Static(){
                Val a: Array[Int, 1] = 1;
                a.Nonstatic = "Success";
                a::$Static = "Success";

                a::$Static();
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($Static),Static,[],Block([ConstDecl(Id(a),ArrayType(1,IntType),IntLit(1)),AssignStmt(FieldAccess(Id(a),Id(Nonstatic)),StringLit(Success)),AssignStmt(FieldAccess(Id(a),Id($Static)),StringLit(Success)),Call(Id(a),Id($Static),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast63'))

    def test64(self):
        input = """
            Class Shape {
               Contructor(){}
            }
            Class Rectangle : Shape {
               getArea(){
                x.b[2] = x.m()[3];
                }
            }
            Class Triangle : Shape {
                getArea(){
                Return Self.length*Self.width / 2;
                }
            }"""
        expect = "Program([ClassDecl(Id(Shape),[MethodDecl(Id(Contructor),Instance,[],Block([]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Id(x),Id(b)),[IntLit(2)]),ArrayCell(CallExpr(Id(x),Id(m),[]),[IntLit(3)]))]))]),ClassDecl(Id(Triangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(/,BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))),IntLit(2)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast64'))

    def test65(self):

        input = """
            Class main{
                Var $a, $b: Int = shape::$x, class::$y;
                Val c, $d: Float = Self.abc, xyz::$a;
                $ha_ha_ha(){
                    Self.a = a[1][2];
                }
            }
            """
        expect = "Program([ClassDecl(Id(main),[AttributeDecl(Static,VarDecl(Id($a),IntType,FieldAccess(Id(shape),Id($x)))),AttributeDecl(Static,VarDecl(Id($b),IntType,FieldAccess(Id(class),Id($y)))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FieldAccess(Self(),Id(abc)))),AttributeDecl(Static,ConstDecl(Id($d),FloatType,FieldAccess(Id(xyz),Id($a)))),MethodDecl(Id($ha_ha_ha),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),ArrayCell(Id(a),[IntLit(1),IntLit(2)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast65'))

    def test66(self):
        input = '''
        Class A{
            $A(){
                If((a[1][a[1][2]])[3] > 5)
                {
                    If(a < 5){
                        a = a + 1;
                        b = b + 1;
                    }
                    Elseif(Null){
                        a = Null + 1;
                    }
                }
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id($A),Static,[],Block([If(BinaryOp(>,ArrayCell(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[IntLit(1),IntLit(2)])]),[IntLit(3)]),IntLit(5)),Block([If(BinaryOp(<,Id(a),IntLit(5)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))]),If(NullLiteral(),Block([AssignStmt(Id(a),BinaryOp(+,NullLiteral(),IntLit(1)))])))]))]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast66'))

    def test67(self):
        input = """Class Program:sv{
                        Var x:Array[Int,3] = Array(v[1][2][3],y[3/4+5]);
                     }"""
        expect = "Program([ClassDecl(Id(Program),Id(sv),[AttributeDecl(Instance,VarDecl(Id(x),ArrayType(3,IntType),[ArrayCell(Id(v),[IntLit(1),IntLit(2),IntLit(3)]),ArrayCell(Id(y),[BinaryOp(+,BinaryOp(/,IntLit(3),IntLit(4)),IntLit(5))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast67'))

    def test68(self):
        input = """ 
            Class Ab {
                main(){
                    If(aaaaa){
                        Val n:Float = c;
                    }Else{
                        Val n:Float = c;
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Ab),[MethodDecl(Id(main),Instance,[],Block([If(Id(aaaaa),Block([ConstDecl(Id(n),FloatType,Id(c))]),Block([ConstDecl(Id(n),FloatType,Id(c))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast68'))

    def test69(self):
        input = """ 
            Class Pro {
                main(a: Int){
                    If(a==2){
                        Return 2;
                    }
                    Else{
                        Return a * Program.main(a-1);
                    }
                }
            }
            """
        expect = """Program([ClassDecl(Id(Pro),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,Id(a),IntLit(2)),Block([Return(IntLit(2))]),Block([Return(BinaryOp(*,Id(a),CallExpr(Id(Program),Id(main),[BinaryOp(-,Id(a),IntLit(1))])))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast69'))

    def test70(self):
        input = """ 
            Class Pro {
                Var Ha:Int = k.s() - k::$a("a") * k.e[2][4];
                $lala(bcd: Int; _at: Float){
                    Return (bcd * _at) && (bcd/_at);
                }
                $main(n:p){
                    Return n;
                    Break;
                    Continue;
                }
            }
            """
        expect = """Program([ClassDecl(Id(Pro),[AttributeDecl(Instance,VarDecl(Id(Ha),IntType,BinaryOp(-,CallExpr(Id(k),Id(s),[]),BinaryOp(*,CallExpr(Id(k),Id($a),[StringLit(a)]),ArrayCell(FieldAccess(Id(k),Id(e)),[IntLit(2),IntLit(4)]))))),MethodDecl(Id($lala),Static,[param(Id(bcd),IntType),param(Id(_at),FloatType)],Block([Return(BinaryOp(&&,BinaryOp(*,Id(bcd),Id(_at)),BinaryOp(/,Id(bcd),Id(_at))))])),MethodDecl(Id($main),Static,[param(Id(n),ClassType(Id(p)))],Block([Return(Id(n)),Break,Continue]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast70'))

    def test71(self):
        input = """Class Pro {}
        Class Pro1 : Pro {
            Var $num:Int = 0;
            Var arr:Array[Int,5];
            $getNumPol() {
                Return Pro::$num;
            }
            draw() {
            }
        }"""
        expect = "Program([ClassDecl(Id(Pro),[]),ClassDecl(Id(Pro1),Id(Pro),[AttributeDecl(Static,VarDecl(Id($num),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(5,IntType))),MethodDecl(Id($getNumPol),Static,[],Block([Return(FieldAccess(Id(Pro),Id($num)))])),MethodDecl(Id(draw),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast71'))

    def test72(self):
        input = """
            Class Pro {
                Var a:Int = 1;
                Var b:Float = 1.5;
                draw() {
                    Var c:Int;
                    c = Self.a;
                }
            }"""
        expect = "Program([ClassDecl(Id(Pro),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(1.5))),MethodDecl(Id(draw),Instance,[],Block([VarDecl(Id(c),IntType),AssignStmt(Id(c),FieldAccess(Self(),Id(a)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast72'))

    def test73(self):
        input = """
            Class Polygon {
                Var $a:Int = 1;
                Var b:Float = 1.5;
                draw() {
                    r = 2.0;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self.myPI;
                    a[0] = s;
                }
            }"""
        expect = "Program([ClassDecl(Id(Polygon),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(1.5))),MethodDecl(Id(draw),Instance,[],Block([AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast73'))

    def test74(self):
        input = """Class Sort {
                Var a: Array[Int, 100];
                _sort(){
                    Foreach(j In i .. 100){
                        If(a[i] > a[j]){
                            Var temp: Int = a[i];
                            a[i] = a[j];
                            a[j] = temp;
                        }
                    }
                    Foreach(i In 1 .. 100){
                        Out.print(a[i]);
                    }
                }
            }
            """
        expect = "Program([ClassDecl(Id(Sort),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,IntType))),MethodDecl(Id(_sort),Instance,[],Block([For(Id(j),Id(i),IntLit(100),IntLit(1),Block([If(BinaryOp(>,ArrayCell(Id(a),[Id(i)]),ArrayCell(Id(a),[Id(j)])),Block([VarDecl(Id(temp),IntType,ArrayCell(Id(a),[Id(i)])),AssignStmt(ArrayCell(Id(a),[Id(i)]),ArrayCell(Id(a),[Id(j)])),AssignStmt(ArrayCell(Id(a),[Id(j)]),Id(temp))]))])]),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Out),Id(print),[ArrayCell(Id(a),[Id(i)])])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast74'))

    def test75(self):
        input = """Class Student{
            Var name, mssv: String;
            Constructor(_name, _mssv: String){
                Self.name = _name;
                Self.mssv = _mssv;
            }
            print(){
                Out.print("name: " + name + "\\nmssv: " + mssv);
            }
        }
        Class Program{
            main(){
                Var stu: Student = New Student("Minh Cao", "1813061");
            }
        }
        """
        expect = "Program([ClassDecl(Id(Student),[AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(mssv),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(_name),StringType),param(Id(_mssv),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(_name)),AssignStmt(FieldAccess(Self(),Id(mssv)),Id(_mssv))])),MethodDecl(Id(print),Instance,[],Block([Call(Id(Out),Id(print),[BinaryOp(+,BinaryOp(+,BinaryOp(+,StringLit(name: ),Id(name)),StringLit(\\nmssv: )),Id(mssv))])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(stu),ClassType(Id(Student)),NewExpr(Id(Student),[StringLit(Minh Cao),StringLit(1813061)]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast75'))

    def test76(self):
        input = """Class Math{
            factor(n: Int){
                If(n > 1){
                    Return Math.factorial(n - 1) * n;
                }
                Else{
                    Return 1;
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(Math),[MethodDecl(Id(factor),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(>,Id(n),IntLit(1)),Block([Return(BinaryOp(*,CallExpr(Id(Math),Id(factorial),[BinaryOp(-,Id(n),IntLit(1))]),Id(n)))]),Block([Return(IntLit(1))]))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast76'))

    def test77(self):
        input = """Class Main{
            Var main: Main;
            main(){
            }
            Constructor(main: Main){}
            Destructor(){}
        }
        Class Program{
            main(){
                a = New Main(New Main());
                a.main();
            }
        }"""
        expect = "Program([ClassDecl(Id(Main),[AttributeDecl(Instance,VarDecl(Id(main),ClassType(Id(Main)),NullLiteral())),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(main),ClassType(Id(Main)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),NewExpr(Id(Main),[NewExpr(Id(Main),[])])),Call(Id(a),Id(main),[])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast77'))

    def test78(self):
        input = """Class Program{
            Main(){
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(Main),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast78'))

    def test79(self):
        input = """Class Program{
            Var s: String = "Cao" +. "Thi" + "Tuyet" + "Minh";
            main(){
                Out.print(Self.s);
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(s),StringType,BinaryOp(+.,StringLit(Cao),BinaryOp(+,BinaryOp(+,StringLit(Thi),StringLit(Tuyet)),StringLit(Minh))))),MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(s))])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast79'))

    def test80(self):
        input = """Class Program{
            main(){
                i = "" +. "a";
                If(i ==. "abcdefg"){

                }
                Elseif(a * b + c / d != e/f - g *h){

                }
                Else{

                }
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(i),BinaryOp(+.,StringLit(),StringLit(a))),If(BinaryOp(==.,Id(i),StringLit(abcdefg)),Block([]),If(BinaryOp(!=,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),BinaryOp(/,Id(c),Id(d))),BinaryOp(-,BinaryOp(/,Id(e),Id(f)),BinaryOp(*,Id(g),Id(h)))),Block([]),Block([]))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast80'))

    def test81(self):
        input = """Class Program: Parent{
            main(minh: String){
                Return False;
            }
        }
        Class B:Program{
            main(){
                Null.c(Self, 1e4);
                1e1.c(Null, Array(1,False));
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Instance,[param(Id(minh),StringType)],Block([Return(BooleanLit(False))]))]),ClassDecl(Id(B),Id(Program),[MethodDecl(Id(main),Instance,[],Block([Call(NullLiteral(),Id(c),[Self(),FloatLit(10000.0)]),Call(FloatLit(10.0),Id(c),[NullLiteral(),[IntLit(1),BooleanLit(False)]])]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast81'))

    def test82(self):
        input = """Class Progran{
            main(){
                Var a:Int =  False ==. True + "something" || Array(Self, "a thing") * 0765 % !0xFFF;
            }
        }

        """
        expect = 'Program([ClassDecl(Id(Progran),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType,BinaryOp(==.,BooleanLit(False),BinaryOp(||,BinaryOp(+,BooleanLit(True),StringLit(something)),BinaryOp(%,BinaryOp(*,[Self(),StringLit(a thing)],IntLit(501)),UnaryOp(!,IntLit(4095))))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast82'))

    def test83(self):
        input = """Class a{
            Val $instance: a = Self;
            Var count: Int;
            setCount(count:Int){
                Self.count = count;
            }
            getCount(){
                Return Self.count;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Static,ConstDecl(Id($instance),ClassType(Id(a)),Self())),AttributeDecl(Instance,VarDecl(Id(count),IntType)),MethodDecl(Id(setCount),Instance,[param(Id(count),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(count)),Id(count))])),MethodDecl(Id(getCount),Instance,[],Block([Return(FieldAccess(Self(),Id(count)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast83'))

    def test84(self):
        input = """
        Class a{
            Constructor(a,b:Array[Boolean, 3]){
                a = b;
            }

            Constructor(){
                Foreach(i In a::$c..1e5 By (a.c())){
                    Break;
                }
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(3,BoolType)),param(Id(b),ArrayType(3,BoolType))],Block([AssignStmt(Id(a),Id(b))])),MethodDecl(Id(Constructor),Instance,[],Block([For(Id(i),FieldAccess(Id(a),Id($c)),FloatLit(100000.0),CallExpr(Id(a),Id(c),[]),Block([Break])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast84'))

    def test85(self):
        input = """   Class a{
            Constructor(b:a; c:a){
                a::$b = b.a;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Constructor),Instance,[param(Id(b),ClassType(Id(a))),param(Id(c),ClassType(Id(a)))],Block([AssignStmt(FieldAccess(Id(a),Id($b)),FieldAccess(Id(b),Id(a)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast85'))

    def test86(self):
        input = """  Class a: Parent{
            main(){
                Self.a= 2+3;
            }
            Constructor(a:Int){
                Self.print(a);
            }
            Destructor(){
                Self.delete(Self);
            }
        }
        """
        expect = 'Program([ClassDecl(Id(a),Id(Parent),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(+,IntLit(2),IntLit(3)))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([Call(Self(),Id(print),[Id(a)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(delete),[Self()])]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast86'))

    def test87(self):
        input = """
                Class Program{
                    main() {
                        Var i,j,k:Float = 0.,1.,1.12;
                        Val a,b,c:Float = 1.e9,1.e-0,1.e1-2;
                        Val f,g,h:Float = 0.e12,1.e-12,10.e+5;
                        Var d,e:Float = .1e9,.2e-8;
                    } 
                }
                """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(i),FloatType,FloatLit(0.0)),VarDecl(Id(j),FloatType,FloatLit(1.0)),VarDecl(Id(k),FloatType,FloatLit(1.12)),ConstDecl(Id(a),FloatType,FloatLit(1000000000.0)),ConstDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),FloatType,BinaryOp(-,FloatLit(10.0),IntLit(2))),ConstDecl(Id(f),FloatType,FloatLit(0.0)),ConstDecl(Id(g),FloatType,FloatLit(1e-12)),ConstDecl(Id(h),FloatType,FloatLit(1000000.0)),VarDecl(Id(d),FloatType,FloatLit(100000000.0)),VarDecl(Id(e),FloatType,FloatLit(2e-09))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast87'))

    def test88(self):
        input = """ Class Pro3 {
                    main() {}
                    func() {}
                    Constructor() {}     
                    Destructor() {}           
                }"""
        expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(func),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast88'))

    def test89(self):
        input = """Class Progran{
            main(){
                Return False ==. True || Array(Self, "a thing") * 0765 % !0xFFF;
            }
        }

        """
        expect = 'Program([ClassDecl(Id(Progran),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(==.,BooleanLit(False),BinaryOp(||,BooleanLit(True),BinaryOp(%,BinaryOp(*,[Self(),StringLit(a thing)],IntLit(501)),UnaryOp(!,IntLit(4095))))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast89'))

    def test90(self):
        input = """  Class Program{
            main(){
                a = !!!!!!-------Self;
            }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Self()))))))))))))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 'ast90'))

    def test91(self):
        input = """
        Class A{
            A(){
                a = "Hello" +. "World";
                a = c ==. 4 == 4;
                b = a + 1;
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(A),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,StringLit(Hello),StringLit(World))),AssignStmt(Id(a),BinaryOp(==.,Id(c),BinaryOp(==,IntLit(4),IntLit(4)))),AssignStmt(Id(b),BinaryOp(+,Id(a),IntLit(1)))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast91'))

    def test92(self):
        input = """
        Class A{
            $_(){
                Foreach(a In 1.e+2..12.4E-12){
                    Out.printInt(a,b,c);
                }
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[MethodDecl(Id($_),Static,[],Block([For(Id(a),FloatLit(100.0),FloatLit(1.24e-11),IntLit(1),Block([Call(Id(Out),Id(printInt),[Id(a),Id(b),Id(c)])])])]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast92'))

    def test93(self):
        input = """
        Class A{
            Val a: Int = a[1+1][Self.a][1+1];
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1)),FieldAccess(Self(),Id(a)),BinaryOp(+,IntLit(1),IntLit(1))])))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast93'))

    def test94(self):
        input = """
        Class Program{
            $B(){
                Val a:Int = A[1+2][3+4][A[1][2][3]];
            }
            $A(){
            }
            main(){
                Val a:Int = A::$B();
            }
        }

        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($B),Static,[],Block([ConstDecl(Id(a),IntType,ArrayCell(Id(A),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(+,IntLit(3),IntLit(4)),ArrayCell(Id(A),[IntLit(1),IntLit(2),IntLit(3)])]))])),MethodDecl(Id($A),Static,[],Block([])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,CallExpr(Id(A),Id($B),[]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 'ast94'))

    def test95(self):
        input = '''
        Class A{
            Val a,b,c:String;
            main(){
            }

            getShape(a,b,c:String; c,d:Int){
            }
        }

        Class B:Parent{
            Constructor(a,c:String; d:Float){
                Out.printLn("Hello");
            }

        }
        '''
        expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(b),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(c),StringType,None)),MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(getShape),Instance,[param(Id(a),StringType),param(Id(b),StringType),param(Id(c),StringType),param(Id(c),IntType),param(Id(d),IntType)],Block([]))]),ClassDecl(Id(B),Id(Parent),[MethodDecl(Id(Constructor),Instance,[param(Id(a),StringType),param(Id(c),StringType),param(Id(d),FloatType)],Block([Call(Id(Out),Id(printLn),[StringLit(Hello)])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast95'))

    def test96(self):
        input = '''
        Class A{
            $A(){
                If((a[1][a[1][2]])[3] > 5)
                {
                    If(a < 5){
                        a = a + 1;
                        b = b + 1;
                    }
                    Elseif(Null){
                        a = Null + 1;
                    }
                }
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(A),[MethodDecl(Id($A),Static,[],Block([If(BinaryOp(>,ArrayCell(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(a),[IntLit(1),IntLit(2)])]),[IntLit(3)]),IntLit(5)),Block([If(BinaryOp(<,Id(a),IntLit(5)),Block([AssignStmt(Id(a),BinaryOp(+,Id(a),IntLit(1))),AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1)))]),If(NullLiteral(),Block([AssignStmt(Id(a),BinaryOp(+,NullLiteral(),IntLit(1)))])))]))]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast96'))

    def test97(self):
        input = '''
        Class A{
            Val a,b,c:Array[Int, 0x111] = 1+1, "Hello World", Self.a();
            main(){
                Return;
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(273,IntType),BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(273,IntType),StringLit(Hello World))),AttributeDecl(Instance,ConstDecl(Id(c),ArrayType(273,IntType),CallExpr(Self(),Id(a),[]))),MethodDecl(Id(main),Instance,[],Block([Return()]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast97'))

    def test98(self):
        input = ''' 
        Class Parent{
            Destructor(){
                Val a:Int;
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(Parent),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(a),IntType,None)]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast98'))

    def test99(self):
        input = ''' 
        Class Program{
            main(){
                {
                    {
                        c = Array(Null, Null, Null);
                        d = Array();
                    }
                }
                {
                    Return;
                    Continue;
                    Break;
                }
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([Block([AssignStmt(Id(c),[NullLiteral(),NullLiteral(),NullLiteral()]),AssignStmt(Id(d),[])])]),Block([Return(),Continue,Break])]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast99'))

    def test100(self):
        input = ''' 
        Class A{
            Val $a, b:Boolean = True, False;
            Val c,$d: String = 1+1, 2.02*.0e1;
            main(){
            }
        }
        '''
        expect = '''Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($a),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(c),StringType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Static,ConstDecl(Id($d),StringType,BinaryOp(*,FloatLit(2.02),FloatLit(0.0)))),MethodDecl(Id(main),Instance,[],Block([]))])])'''
        self.assertTrue(TestAST.test(input, expect, 'ast100'))
