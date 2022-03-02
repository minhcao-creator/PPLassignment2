import unittest
from TestUtils import TestAST
from AST import *
from main.d96.utils.AST import BooleanLiteral, IntLiteral, SelfLiteral, StringLiteral, VarDecl


class ASTGenSuite(unittest.TestCase):
    # def test1(self):
    #     """Simple program: int main() {} """
    #     input = """Class Program {}"""
    #     expect = str(Program([ClassDecl(Id('Program'), [])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast1'))

    # def test2(self):
    #     """More complex program"""
    #     input = """Class A{
    #         Val a:Int;
    #     }"""
    #     expect = str(Program([ClassDecl(
    #         Id('A'), [AttributeDecl(Instance(), ConstDecl(Id('a'), IntType(), None))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast2'))

    # def test3(self):
    #     """More complex program"""
    #     input = """
    #     Class a:parent{
    #     }
    #     """
    #     expect = str(Program([ClassDecl(Id('a'), [], Id('parent'))]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast3'))

    # def test4(self):
    #     """More complex program"""
    #     input = """
    #     Class a{
    #         Var a,b:Int;
    #     }
    #     """
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(
    #         Id('a'), IntType())), AttributeDecl(Instance(), VarDecl(Id('b'), IntType()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast4'))

    # def test5(self):
    #     """More complex program"""
    #     input = """
    #     Class a{
    #         Var a,b:Int;
    #         Val c, $d ,e: Boolean;
    #     }
    #     """
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), IntType())), AttributeDecl(Instance(), VarDecl(Id('b'), IntType())), AttributeDecl(
    #         Instance(), ConstDecl(Id('c'), BoolType(), None)), AttributeDecl(Static(), ConstDecl(Id('$d'), BoolType(), None)), AttributeDecl(Instance(), ConstDecl(Id('e'), BoolType(), None))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast5'))

    # def test6(self):
    #     """More complex program"""
    #     input = """Class a{
    #             Var a:Int = 0x12;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(
    #         Instance(), VarDecl(Id('a'), IntType(), IntLiteral(18)))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast6'))

    # def test7(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{
    #             Var a,b,$c:Int = 0x12, 02, 0;
    #             Val d: Int = 0B1101;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), IntType(), IntLiteral(18))), AttributeDecl(Instance(), VarDecl(Id('b'), IntType(
    #     ), IntLiteral(2))), AttributeDecl(Static(), VarDecl(Id('$c'), IntType(), IntLiteral(0))), AttributeDecl(Instance(), ConstDecl(Id('d'), IntType(), IntLiteral(13)))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast7'))

    # def test8(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{
    #             Var a,b: Boolean;
    #             Val c,d,e, $_: Float = 2.01, .0e3, .0e2, 1e3;
    #             Val f, $G: Float = 1.e4, 1.5e15;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), BoolType())), AttributeDecl(Instance(), VarDecl(Id('b'), BoolType())), AttributeDecl(Instance(), ConstDecl(Id('c'), FloatType(), FloatLiteral(2.01))), AttributeDecl(Instance(), ConstDecl(Id('d'), FloatType(), FloatLiteral(0.0))), AttributeDecl(
    #         Instance(), ConstDecl(Id('e'), FloatType(), FloatLiteral(0.0))), AttributeDecl(Static(), ConstDecl(Id('$_'), FloatType(), FloatLiteral(1000.0))), AttributeDecl(Instance(), ConstDecl(Id('f'), FloatType(), FloatLiteral(10000.0))), AttributeDecl(Static(), ConstDecl(Id('$G'), FloatType(), FloatLiteral(1500000000000000.0)))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast8'))

    # def test9(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{
    #             Var a,b: Boolean = True, False;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), BoolType(), BooleanLiteral(
    #         True))), AttributeDecl(Instance(), VarDecl(Id('b'), BoolType(), BooleanLiteral(False)))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast9'))

    # def test10(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{
    #             Var a,b: String;
    #             Val c, d, $e, $f: String = "asd", Null, "a \\n  \\b b", "";
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), StringType())), AttributeDecl(Instance(), VarDecl(Id('b'), StringType())), AttributeDecl(Instance(), ConstDecl(Id('c'), StringType(), StringLiteral('asd'))), AttributeDecl(
    #         Instance(), ConstDecl(Id('d'), StringType(), NullLiteral())), AttributeDecl(Static(), ConstDecl(Id('$e'), StringType(), StringLiteral('a \\n  \\b b'))), AttributeDecl(Static(), ConstDecl(Id('$f'), StringType(), StringLiteral('')))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast10'))

    # def test11(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{
    #         Var a: Array[Boolean, 1];
    #         Val c, d: Array[Array[String, 2], 3] = Array(1,2, Array(True), Array("bv", 2.0e1)), Array();
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), ArrayType(1, BoolType()))), AttributeDecl(Instance(), ConstDecl(Id('c'), ArrayType(3, ArrayType(2, StringType())), ArrayLiteral([
    #         IntLiteral(1), IntLiteral(2), ArrayLiteral([BooleanLiteral(True)]), ArrayLiteral([StringLiteral('bv'), FloatLiteral(20.0)])]))), AttributeDecl(Instance(), ConstDecl(Id('d'), ArrayType(3, ArrayType(2, StringType())), ArrayLiteral([])))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast11'))

    # def test12(self):
    #     """Simple program: int main() {} """
    #     input = """Class a{}
    #     Class b: C{}"""
    #     expect = str(
    #         Program([ClassDecl(Id('a'), []), ClassDecl(Id('b'), [], Id('C'))]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast12'))

    # def test13(self):
    #     input = """Class a{
    #         Var a: Boolean;
    #         main(){
    #         }
    #         $sub(){
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), BoolType())), MethodDecl(
    #         Instance(), Id('main'), [], Block([])), MethodDecl(Static(), Id('$sub'), [], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast13'))

    # def test14(self):
    #     input = """Class a{
    #         Var $a: Boolean = True;
    #         main(){
    #             Var a: Boolean;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Static(), VarDecl(Id('$a'), BoolType(), BooleanLiteral(
    #         True))), MethodDecl(Instance(), Id('main'), [], Block([VarDecl(Id('a'), BoolType())]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast14'))

    # def test15(self):
    #     input = """Class a{
    #         main(){
    #             Var a: Boolean;
    #             Var b,c: String = Array(0x1), "hien";
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([VarDecl(Id('a'), BoolType(
    #     )), VarDecl(Id('b'), StringType(), ArrayLiteral([IntLiteral(1)])), VarDecl(Id('c'), StringType(), StringLiteral('hien'))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast15'))

    # def test16(self):
    #     input = """Class a{
    #         main(){
    #             Val a: Boolean;
    #             Val b,c: Float = 1==2, Null + 1;
    #             Var d: Boolean = Self ==. Array();
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([ConstDecl(Id('a'), BoolType(), None), ConstDecl(Id('b'), FloatType(), BinaryOp('==', IntLiteral(
    #         1), IntLiteral(2))), ConstDecl(Id('c'), FloatType(), BinaryOp('+', NullLiteral(), IntLiteral(1))), VarDecl(Id('d'), BoolType(), BinaryOp('==.', SelfLiteral(), ArrayLiteral([])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast16'))

    # def test17(self):
    #     input = """Class a{
    #         main(){
    #             Val a: Boolean = 0b10 +. .0e3;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [ConstDecl(Id('a'), BoolType(), BinaryOp('+.', IntLiteral(2), FloatLiteral(0.0)))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast17'))

    # def test18(self):
    #     input = """Class a{
    #         main(){
    #             a = b;
    #             c = d;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [
    #     ], Block([Assign(Id('a'), Id('b')), Assign(Id('c'), Id('d'))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast18'))

    # def test19(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 == 2;
    #             b = 011 != 0XAB;
    #             c = 0b111> .0e5;
    #             d = True < Null;
    #             e = False <= Self;
    #             f = "hien :D" >= Array(2, "VinhHien");
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('==', IntLiteral(1), IntLiteral(2))), Assign(Id('b'), BinaryOp('!=', IntLiteral(9), IntLiteral(171))), Assign(Id('c'), BinaryOp('>', IntLiteral(7), FloatLiteral(
    #         0.0))), Assign(Id('d'), BinaryOp('<', BooleanLiteral(True), NullLiteral())), Assign(Id('e'), BinaryOp('<=', BooleanLiteral(False), SelfLiteral())), Assign(Id('f'), BinaryOp('>=', StringLiteral('hien :D'), ArrayLiteral([IntLiteral(2), StringLiteral('VinhHien')])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast19'))

    # def test20(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 && 2;
    #             b = 3 || 4;
    #             c = d ||e && a || b || c;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('&&', IntLiteral(1), IntLiteral(2))), Assign(Id('b'), BinaryOp(
    #         '||', IntLiteral(3), IntLiteral(4))), Assign(Id('c'), BinaryOp('||', BinaryOp('||', BinaryOp('&&', BinaryOp('||', Id('d'), Id('e')), Id('a')), Id('b')), Id('c')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast20'))

    # def test21(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 == 2 ==. 2e2 && b || e && True;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('==.', BinaryOp('==', IntLiteral(
    #         1), IntLiteral(2)), BinaryOp('&&', BinaryOp('||', BinaryOp('&&', FloatLiteral(200.0), Id('b')), Id('e')), BooleanLiteral(True))))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast21'))

    # def test22(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 + 2.5;
    #             b = 3 - 4.2;
    #             c = a + b - 2 -3 +4;

    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('+', IntLiteral(1), FloatLiteral(2.5))), Assign(Id('b'), BinaryOp(
    #         '-', IntLiteral(3), FloatLiteral(4.2))), Assign(Id('c'), BinaryOp('+', BinaryOp('-', BinaryOp('-', BinaryOp('+', Id('a'), Id('b')), IntLiteral(2)), IntLiteral(3)), IntLiteral(4)))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast22'))

    # def test23(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 + 2.5 || 3 == 4 && 3 - 1 - 3;
    #             b = False && True +. "Hien" + "VinhHien" > Null || Self - 0;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('==', BinaryOp('||', BinaryOp('+', IntLiteral(1), FloatLiteral(2.5)), IntLiteral(3)), BinaryOp('&&', IntLiteral(4), BinaryOp('-', BinaryOp('-', IntLiteral(3), IntLiteral(
    #         1)), IntLiteral(3))))), Assign(Id('b'), BinaryOp('+.', BinaryOp('&&', BooleanLiteral(False), BooleanLiteral(True)), BinaryOp('>', BinaryOp('+', StringLiteral('Hien'), StringLiteral('VinhHien')), BinaryOp('||', NullLiteral(), BinaryOp('-', SelfLiteral(), IntLiteral(0))))))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast23'))

    # def test24(self):
    #     input = """Class a{
    #         main(){
    #             a = 1 * 2 ;
    #             b = 1 / 2 ;
    #             c = 1 % 2 ;
    #             d = 1 * 3 / 3 % 5 * 1 / 5 % 7;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('*', IntLiteral(1), IntLiteral(2))), Assign(Id('b'), BinaryOp('/', IntLiteral(1), IntLiteral(2))), Assign(Id('c'), BinaryOp(
    #         '%', IntLiteral(1), IntLiteral(2))), Assign(Id('d'), BinaryOp('%', BinaryOp('/', BinaryOp('*', BinaryOp('%', BinaryOp('/', BinaryOp('*', IntLiteral(1), IntLiteral(3)), IntLiteral(3)), IntLiteral(5)), IntLiteral(1)), IntLiteral(5)), IntLiteral(7)))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast24'))

    # def test25(self):
    #     input = """Class a{
    #         main(){
    #             a = a[1] ;
    #             b = 1[2][3];
    #             c = Self[b[2][4]][5][7];
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), ArrayCell(Id('a'), [IntLiteral(1)])), Assign(Id('b'), ArrayCell(IntLiteral(
    #         1), [IntLiteral(2), IntLiteral(3)])), Assign(Id('c'), ArrayCell(SelfLiteral(), [ArrayCell(Id('b'), [IntLiteral(2), IntLiteral(4)]), IntLiteral(5), IntLiteral(7)]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast25'))

    # def test26(self):
    #     input = """Class a{
    #         main(){
    #             a[1] = 1 + a[2];
    #             b[1][2] = Self + c[a][b];
    #             c[2][3][4] = "a" || c[2][3][4];
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(ArrayCell(Id('a'), [IntLiteral(1)]), BinaryOp('+', IntLiteral(1), ArrayCell(Id('a'), [IntLiteral(2)]))), Assign(ArrayCell(Id('b'), [IntLiteral(1), IntLiteral(2)]),
    #                                                                                                                                                                                                                    BinaryOp('+', SelfLiteral(), ArrayCell(Id('c'), [Id('a'), Id('b')]))), Assign(ArrayCell(Id('c'), [IntLiteral(2), IntLiteral(3), IntLiteral(4)]), BinaryOp('||', StringLiteral('a'), ArrayCell(Id('c'), [IntLiteral(2), IntLiteral(3), IntLiteral(4)])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast26'))

    # def test27(self):
    #     input = """Class a{
    #         Var a: b;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(
    #         Instance(), VarDecl(Id('a'), ClassType(Id('b')), NullLiteral()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast27'))

    # def test28(self):
    #     input = """Class a{
    #         Var a: b;
    #         Val c, d: cl = Null, Null;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), ClassType(Id('b')), NullLiteral())), AttributeDecl(Instance(), ConstDecl(
    #         Id('c'), ClassType(Id('cl')), NullLiteral())), AttributeDecl(Instance(), ConstDecl(Id('d'), ClassType(Id('cl')), NullLiteral()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast28'))

    # def test29(self):
    #     input = """Class a{
    #         Var a: b;
    #         Val c, d: cl = Null, Null;
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [AttributeDecl(Instance(), VarDecl(Id('a'), ClassType(Id('b')), NullLiteral())), AttributeDecl(Instance(), ConstDecl(
    #         Id('c'), ClassType(Id('cl')), NullLiteral())), AttributeDecl(Instance(), ConstDecl(Id('d'), ClassType(Id('cl')), NullLiteral()))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast29'))

    # def test30(self):
    #     input = """Class a{
    #         main(a:int){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id(
    #         'main'), [VarDecl(Id('a'), ClassType(Id('int')))], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast30'))

    # def test31(self):
    #     input = """Class a{
    #         main(a,b:Float){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [
    #         VarDecl(Id('a'), FloatType()), VarDecl(Id('b'), FloatType())], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast31'))

    # def test32(self):
    #     input = """Class a{
    #         main(a,b:String; c,d: Array[Int , 2]){}
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [VarDecl(Id('a'), StringType()), VarDecl(
    #         Id('b'), StringType()), VarDecl(Id('c'), ArrayType(2, IntType())), VarDecl(Id('d'), ArrayType(2, IntType()))], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast32'))

    # def test32(self):
    #     input = """Class a{
    #         main(){
    #             Var a: b;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id(
    #         'main'), [], Block([VarDecl(Id('a'), ClassType(Id('b')), NullLiteral())]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast32'))

    # def test33(self):
    #     input = """Class a{
    #         main(){
    #             Val a,b:c = Null, Self;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([ConstDecl(
    #         Id('a'), ClassType(Id('c')), NullLiteral()), ConstDecl(Id('b'), ClassType(Id('c')), SelfLiteral())]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast33'))

    # def test34(self):
    #     input = """Class a{
    #         main(){
    #             a = -b;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id(
    #         'main'), [], Block([Assign(Id('a'), UnaryOp('-', Id('b')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast34'))

    # def test35(self):
    #     input = """Class a{
    #         main(){
    #             a = -b ---1 + -c;
    #             b = - a[2] % "hien :)";
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), BinaryOp('+', BinaryOp('-', UnaryOp('-', Id('b')), UnaryOp(
    #         '-', UnaryOp('-', IntLiteral(1)))), UnaryOp('-', Id('c')))), Assign(Id('b'), BinaryOp('%', UnaryOp('-', ArrayCell(Id('a'), [IntLiteral(2)])), StringLiteral('hien :)')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast35'))

    # def test36(self):
    #     input = """Class a{
    #         main(){
    #             a = !1;
    #             b = !!1;
    #             c = !True == False || Null;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), UnaryOp('!', IntLiteral(1))), Assign(Id('b'), UnaryOp(
    #         '!', UnaryOp('!', IntLiteral(1)))), Assign(Id('c'), BinaryOp('==', UnaryOp('!', BooleanLiteral(True)), BinaryOp('||', BooleanLiteral(False), NullLiteral())))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast36'))

    # def test37(self):
    #     input = """Class a{
    #         main(){
    #             a = True.b;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [
    #     ], Block([Assign(Id('a'), FieldAccess(BooleanLiteral(True), Id('b')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast37'))

    # def test38(self):
    #     input = """Class a{
    #         main(){
    #             a = Self.b;
    #             b = Null.a.b.c;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(Id('a'), FieldAccess(
    #         SelfLiteral(), Id('b'))), Assign(Id('b'), FieldAccess(FieldAccess(FieldAccess(NullLiteral(), Id('a')), Id('b')), Id('c')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast38'))

    # def test39(self):
    #     input = """Class a{
    #         main(){
    #             a = b[1][2][3];
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [Assign(Id('a'), ArrayCell(Id('b'), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast39'))

    # def test40(self):
    #     input = """Class a{
    #         main(){
    #             2[1][2][3] =1  ;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Assign(
    #         ArrayCell(IntLiteral(2), [IntLiteral(1), IntLiteral(2), IntLiteral(3)]), IntLiteral(1))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast40'))

    # def test41(self):
    #     input = """Class a{
    #         main(){
    #             Break     ;
    #         }
    #     }"""
    #     expect = str(Program(
    #         [ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Break()]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast41'))

    # def test42(self):
    #     input = """Class a{
    #         main(){
    #             Continue     ;
    #         }
    #     }"""
    #     expect = str(Program(
    #         [ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Continue()]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast42'))

    # def test43(self):
    #     input = """Class a{
    #         main(){
    #             Return ;
    #         }
    #     }"""
    #     expect = str(Program(
    #         [ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return()]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast43'))

    # def test44(self):
    #     input = """Class a{
    #         main(){
    #             Return Null;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(
    #         Instance(), Id('main'), [], Block([Return(NullLiteral())]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast44'))

    # def test45(self):
    #     input = """Class a{
    #         main(){
    #             Return a.b();
    #             Return a.b(1,2e3);
    #             Return a.b.c(1,2e3);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(CallExpr(Id('a'), Id('b'), [])), Return(CallExpr(Id('a'), Id(
    #         'b'), [IntLiteral(1), FloatLiteral(2000.0)])), Return(CallExpr(FieldAccess(Id('a'), Id('b')), Id('c'), [IntLiteral(1), FloatLiteral(2000.0)]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast45'))

    # def test46(self):
    #     input = """Class a{
    #         main(){
    #             Return a::$b;
    #             Return a :: $b ();
    #             Return a :: $b (Null, Self);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(FieldAccess(Id('a'), Id(
    #         '$b'))), Return(CallExpr(Id('a'), Id('$b'), [])), Return(CallExpr(Id('a'), Id('$b'), [NullLiteral(), SelfLiteral()]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast46'))

    # def test47(self):
    #     input = """Class a{
    #         main(){
    #             Return New a();
    #             Return New a("hien", True);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(
    #         NewExpr(Id('a'), [])), Return(NewExpr(Id('a'), [StringLiteral('hien'), BooleanLiteral(True)]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast47'))

    # def test48(self):
    #     input = """Class a{
    #         main(){
    #             Return New a().b;
    #             Return New a("hien", True).c(False);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(FieldAccess(NewExpr(Id('a'), []), Id(
    #         'b'))), Return(CallExpr(NewExpr(Id('a'), [StringLiteral('hien'), BooleanLiteral(True)]), Id('c'), [BooleanLiteral(False)]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast48'))

    # def test49(self):
    #     input = """Class a{
    #         main(){
    #             Return New a().b + Null || True && New b(2);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(BinaryOp('&&', BinaryOp('||', BinaryOp(
    #         '+', FieldAccess(NewExpr(Id('a'), []), Id('b')), NullLiteral()), BooleanLiteral(True)), NewExpr(Id('b'), [IntLiteral(2)])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast49'))

    # def test50(self):
    #     input = """Class a{
    #         main(){
    #             Return New a().b + Null || True && New b(2);
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([Return(BinaryOp('&&', BinaryOp('||', BinaryOp(
    #         '+', FieldAccess(NewExpr(Id('a'), []), Id('b')), NullLiteral()), BooleanLiteral(True)), NewExpr(Id('b'), [IntLiteral(2)])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast50'))

    # def test51(self):
    #     input = """Class a{
    #         main(){
    #             Return (a::$b).a;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [
    #     ], Block([Return(FieldAccess(FieldAccess(Id('a'), Id('$b')), Id('a')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast51'))

    # def test51(self):
    #     input = """Class a{
    #         main(){
    #             Return (a::$b).a;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [
    #     ], Block([Return(FieldAccess(FieldAccess(Id('a'), Id('$b')), Id('a')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast51'))

    # def test52(self):
    #     input = """Class a{
    #         main(){
    #             If (1 +2) { a[1][2] = Null;}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([If(BinaryOp(
    #         '+', IntLiteral(1), IntLiteral(2)), Block([Assign(ArrayCell(Id('a'), [IntLiteral(1), IntLiteral(2)]), NullLiteral())]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast52'))

    # def test53(self):
    #     input = """Class a{
    #         main(){
    #             If (1 +2) {Return 0xF;}
    #             Else {a = Self || b[c.d];}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([If(BinaryOp('+', IntLiteral(1), IntLiteral(2)), Block(
    #         [Return(IntLiteral(15))]), Block([Assign(Id('a'), BinaryOp('||', SelfLiteral(), ArrayCell(Id('b'), [FieldAccess(Id('c'), Id('d'))])))]))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast53'))

    # def test54(self):
    #     input = """Class a{
    #         main(){
    #             If (1 +2) {Return 0;}
    #             Elseif (5 == True) {Return;}
    #             Else {{a = 2;}}
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([If(BinaryOp('+', IntLiteral(1), IntLiteral(2)), Block([Return(
    #         IntLiteral(0))]), If(BinaryOp('==', IntLiteral(5), BooleanLiteral(True)), Block([Return()]), Block([Block([Assign(Id('a'), IntLiteral(2))])])))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast54'))

    # def test55(self):
    #     input = """Class a{
    #         main(){
    #             If (True) {Return 0;}
    #             Elseif (5  == True) {Return;}
    #             Elseif ("") {Return Null;}
    #             Elseif ("hien") {Return Self;}
    #             Else {{a = 2;}}
    #         }
    #     }"""
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(main),Instance,[],Block([If(BooleanLit(True),Block([Return(IntLit(0))]),If(BinaryOp(==,IntLit(5),BooleanLit(True)),Block([Return()]),If(StringLit(),Block([Return(NullLiteral())]),If(StringLit(hien),Block([Return(Self())]),Block([Block([AssignStmt(Id(a),IntLit(2))])])))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast55'))

    # def test56(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In 1 .. 3){
    #                 Val a:Array[Int, 2];
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [For(Id('i'), IntLiteral(1), IntLiteral(3), Block([ConstDecl(Id('a'), ArrayType(2, IntType()))]), IntLiteral(1))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast56'))

    # def test57(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In 1*2 .. b){
    #                 Return;
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [For(Id('i'), BinaryOp('*', IntLiteral(1), IntLiteral(2)), Id('b'), Block([Return()]), IntLiteral(1))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast57'))

    # def test58(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In 1*2 .. b){
    #                 Return;
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [For(Id('i'), BinaryOp('*', IntLiteral(1), IntLiteral(2)), Id('b'), Block([Return()]), IntLiteral(1))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast58'))

    # def test58(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In a..1+2){
    #                 Return;
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [For(Id('i'), Id('a'), BinaryOp('+', IntLiteral(1), IntLiteral(2)), Block([Return()]), IntLiteral(1))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast58'))

    # def test59(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In A..Null By a::$b){
    #                 Return;
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [For(Id('i'), Id('A'), NullLiteral(), Block([Return()]), FieldAccess(Id('a'), Id('$b')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast59'))

    # def test60(self):
    #     input = """Class a{
    #         main(){
    #             Foreach (i In A..Null By a::$b){
    #                 Foreach (i In A..Null By a::$b){
    #                     {
    #                         Return Null;
    #                     }
    #                 }
    #             }
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block([For(Id('i'), Id('A'), NullLiteral(), Block(
    #         [For(Id('i'), Id('A'), NullLiteral(), Block([Block([Return(NullLiteral())])]), FieldAccess(Id('a'), Id('$b')))]), FieldAccess(Id('a'), Id('$b')))]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast60'))

    # def test61(self):
    #     input = """Class a{
    #         main(){
    #             A::$B();
    #             C.D();
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('a'), [MethodDecl(Instance(), Id('main'), [], Block(
    #         [CallStmt(Id('A'), Id('$B'), []), CallStmt(Id('C'), Id('D'), [])]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast61'))

    # def test62(self):
    #     input = """Class a{
    #         main(){
    #             A::$B("Bui","Luong");
    #             New a("Vinh").b.D("Hien", "handSome :D");
    #         }
    #     }"""
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(main),Instance,[],Block([Call(Id(A),Id($B),[StringLit(Bui),StringLit(Luong)]),Call(FieldAccess(NewExpr(Id(a),[StringLit(Vinh)]),Id(b)),Id(D),[StringLit(Hien),StringLit(handSome :D)])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast62'))

    # def test63(self): 
    #     input = """Class Program{
    #         main(){
    #         }
    #     }"""
    #     expect = str(Program(
    #         [ClassDecl(Id('Program'), [MethodDecl(Static(), Id('main'), [], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast63'))

    # def test64(self):
    #     input = """Class Program{
    #         Main(){

    #         }
    #         main(){
    #         }
    #         temp(){

    #         }
    #         main(){

    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Program'), [MethodDecl(Instance(), Id('Main'), [], Block([])), MethodDecl(Static(), Id(
    #         'main'), [], Block([])), MethodDecl(Instance(), Id('temp'), [], Block([])), MethodDecl(Static(), Id('main'), [], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast64'))

    # def test65(self):
    #     input = """Class Program{
    #         Var a:Int = 1;
    #         Val $b: String = "Hien dep trai";
    #         main(){
    #         }
    #         temp(){

    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Program'), [AttributeDecl(Instance(), VarDecl(Id('a'), IntType(), IntLiteral(1))), AttributeDecl(Static(), ConstDecl(
    #         Id('$b'), StringType(), StringLiteral('Hien dep trai'))), MethodDecl(Static(), Id('main'), [], Block([])), MethodDecl(Instance(), Id('temp'), [], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast65'))

    # def test66(self):
    #     input = """Class Program{
    #         Var a:Int = 1;
    #         Val $b: String = "Hien dep trai";
    #         main(){
    #         }
    #         temp(){

    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Program'), [AttributeDecl(Instance(), VarDecl(Id('a'), IntType(), IntLiteral(1))), AttributeDecl(Static(), ConstDecl(
    #         Id('$b'), StringType(), StringLiteral('Hien dep trai'))), MethodDecl(Static(), Id('main'), [], Block([])), MethodDecl(Instance(), Id('temp'), [], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast66'))

    # def test67(self):
    #     input = """Class Program{
    #         Var a:Array[Float, 1] = Array(True, False);
    #         main(a,b:Boolean){
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Program'), [AttributeDecl(Instance(), VarDecl(Id('a'), ArrayType(1, FloatType()), ArrayLiteral([BooleanLiteral(
    #         True), BooleanLiteral(False)]))), MethodDecl(Instance(), Id('main'), [VarDecl(Id('a'), BoolType()), VarDecl(Id('b'), BoolType())], Block([]))])]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast67'))

    # def test68(self):
    #     input = """Class Program: ProParent{
    #         main(a,b:Boolean){
    #             a = b;
    #         }
    #         main(){
    #             Return 0b1101;
    #         }
    #     }"""
    #     expect = str(Program([ClassDecl(Id('Program'), [MethodDecl(Instance(), Id('main'), [VarDecl(Id('a'), BoolType()), VarDecl(Id('b'), BoolType(
    #     ))], Block([Assign(Id('a'), Id('b'))])), MethodDecl(Static(), Id('main'), [], Block([Return(IntLiteral(13))]))], Id('ProParent'))]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast68'))

    # def test69(self):
    #     input = """Class Program{
    #         main(){
    #             Return 0b1101;
    #         }
    #     }
    #     Class A{
    #         main(){
    #             a.b(Self);
    #         }
    #     }
    #     Class Program{
    #         main(){
    #             If (a) {
    #                 Continue;
    #             }
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(IntLit(13))]))]),ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([Call(Id(a),Id(b),[Self()])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(Id(a),Block([Continue]))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast69'))

    # def test70(self):
    #     input = """Class Program: Parent{
    #         main(hien: String){
    #             hien = "handsome";
    #         }
    #         main(){
    #             Self.main();
    #             Self.main("Sure");
    #         }
    #     }
    #     """
    #     expect = str(Program([ClassDecl(Id('Program'), [MethodDecl(Instance(), Id('main'), [VarDecl(Id('hien'), StringType())], Block([Assign(Id('hien'), StringLiteral('handsome'))])), MethodDecl(
    #         Static(), Id('main'), [], Block([CallStmt(SelfLiteral(), Id('main'), []), CallStmt(SelfLiteral(), Id('main'), [StringLiteral('Sure')])]))], Id('Parent'))]))
    #     self.assertTrue(TestAST.test(input, expect, 'ast70'))

    # def test71(self):
    #     input = """Class Program: Parent{
    #         main(hien: String){
    #             Val a: b;
    #             Var c: d = Self.a.b.c;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Instance,[param(Id(hien),StringType)],Block([ConstDecl(Id(a),ClassType(Id(b)),NullLiteral()),VarDecl(Id(c),ClassType(Id(d)),FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),Id(c)))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast71'))

    # def test72(self):
    #     input = """Class Program: Parent{
    #         main(hien: String){
    #             Return False;
    #         }
    #     }
    #     Class Program{
    #         Val a: Boolean;
    #         main(){
    #             Self.a.B();
    #         }
    #     }
    #     Class B:Program{
    #         main(){
    #             Null.c(Self, 1e4);
    #             1e1.c(Null, Array(1,False));
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Instance,[param(Id(hien),StringType)],Block([Return(BooleanLit(False))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,None)),MethodDecl(Id(main),Static,[],Block([Call(FieldAccess(Self(),Id(a)),Id(B),[])]))]),ClassDecl(Id(B),Id(Program),[MethodDecl(Id(main),Instance,[],Block([Call(NullLiteral(),Id(c),[Self(),FloatLit(10000.0)]),Call(FloatLit(10.0),Id(c),[NullLiteral(),[IntLit(1),BooleanLit(False)]])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast72'))

    # def test73(self):
    #     input = """Class Progran{
    #         main(){
    #             Return False ==. True + "something" || Array(Self, "a thing") * 0765 % !0xFFF;
    #         }
    #     }

    #     """
    #     expect = 'Program([ClassDecl(Id(Progran),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(==.,BooleanLit(False),BinaryOp(||,BinaryOp(+,BooleanLit(True),StringLit(something)),BinaryOp(%,BinaryOp(*,[Self(),StringLit(a thing)],IntLit(501)),UnaryOp(!,IntLit(4095))))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast73'))

    # def test74(self):
    #     input = """Class a{
    #         Val $instance: a = Self;
    #         Var count: Int;
    #         setCount(count:Int){
    #             Self.count = count;
    #         }
    #         getCount(){
    #             Return Self.count;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Static,ConstDecl(Id($instance),ClassType(Id(a)),Self())),AttributeDecl(Instance,VarDecl(Id(count),IntType)),MethodDecl(Id(setCount),Instance,[param(Id(count),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(count)),Id(count))])),MethodDecl(Id(getCount),Instance,[],Block([Return(FieldAccess(Self(),Id(count)))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast74'))

    # def test75(self):
    #     input = """Class Program{
    #         main(){
    #             If (((Null == Self))){
    #                 Foreach (i In True..False){
    #                     i = i*Self.main();
    #                 }
    #             }
    #             Elseif (Array(Array(a)) ==. a){
    #                 Program::$main();
    #             }
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,NullLiteral(),Self()),Block([For(Id(i),BooleanLit(True),BooleanLit(False),IntLit(1),Block([AssignStmt(Id(i),BinaryOp(*,Id(i),CallExpr(Self(),Id(main),[])))])])]),If(BinaryOp(==.,[[Id(a)]],Id(a)),Block([Call(Id(Program),Id($main),[])])))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast75'))

    # def test76(self):
    #     input = """Class Progran{
    #         main(){
    #             Return False ==. True + "something" || Array(Self, "a thing") * 0765 % !0xFFF;
    #         }
    #     }

    #     """
    #     expect = 'Program([ClassDecl(Id(Progran),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(==.,BooleanLit(False),BinaryOp(||,BinaryOp(+,BooleanLit(True),StringLit(something)),BinaryOp(%,BinaryOp(*,[Self(),StringLit(a thing)],IntLit(501)),UnaryOp(!,IntLit(4095))))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast76'))

    # def test77(self):
    #     input = """Class Program: Parent{
    #         main(){
    #             Break;
    #         }
    #     }
    #     Class a:A{}
    #     Class b:B{
    #         Val c: a;
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),Id(Parent),[MethodDecl(Id(main),Static,[],Block([Break]))]),ClassDecl(Id(a),Id(A),[]),ClassDecl(Id(b),Id(B),[AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(a)),NullLiteral()))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast77'))

    # def test78(self):
    #     input = """Class Program{
    #         Constructor(){
    #             Self.a = 1;
    #             Self.a = Self.constructor();
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(a)),CallExpr(Self(),Id(constructor),[]))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast78'))

    # def test79(self):
    #     input = """
    #     Class a{
    #         Constructor(a,b:Array[Boolean, 3]){
    #             a = b;
    #         }

    #         Constructor(){
    #             Foreach(i In a::$c..1e5 By a.c()){
    #                 Break;
    #             }
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(3,BoolType)),param(Id(b),ArrayType(3,BoolType))],Block([AssignStmt(Id(a),Id(b))])),MethodDecl(Id(Constructor),Instance,[],Block([For(Id(i),FieldAccess(Id(a),Id($c)),FloatLit(100000.0),CallExpr(Id(a),Id(c),[]),Block([Break])])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast79'))

    # def test80(self):
    #     input = """
    #     Class a{
    #         Destructor(){
    #             Return;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Destructor),Instance,[],Block([Return()]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast80'))

    # def test81(self):
    #     input = """ Class a{
    #         Destructor(){
    #             Val a,b: Int = 1_23_567, 0x2_3;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Destructor),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(123567)),ConstDecl(Id(b),IntType,IntLit(35))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast81'))

    # def test82(self):
    #     input = """   Class a{
    #         Constructor(b:a; c:a){
    #             a::$b = b.a;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Constructor),Instance,[param(Id(b),ClassType(Id(a))),param(Id(c),ClassType(Id(a)))],Block([AssignStmt(FieldAccess(Id(a),Id($b)),FieldAccess(Id(b),Id(a)))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast82'))

    # def test83(self):
    #     input = """    Class a{
    #         Main(){
    #             Foreach(i In 1...10){
    #                 If (i == 5){
    #                     Break;
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(Main),Instance,[],Block([For(Id(i),FloatLit(1.0),IntLit(10),IntLit(1),Block([If(BinaryOp(==,Id(i),IntLit(5)),Block([Break]))])])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast83'))

    # def test84(self):
    #     input = """    Class a{
    #         Val a,b:Array[Int, 2] = Array(0X1A, 0B100), Array(076, Null);
    #         Main(){
    #             Foreach(i In a::$_ .. 1==. "hien" == True){
    #                 Foreach(j In a::$_(Array(Null)) .. !1e0){
    #                     If (i == j) {
    #                         Program::$print(i + j);
    #                     }
    #                 }
    #             }
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(2,IntType),[IntLit(26),IntLit(4)])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(2,IntType),[IntLit(62),NullLiteral()])),MethodDecl(Id(Main),Instance,[],Block([For(Id(i),FieldAccess(Id(a),Id($_)),BinaryOp(==.,IntLit(1),BinaryOp(==,StringLit(hien),BooleanLit(True))),IntLit(1),Block([For(Id(j),CallExpr(Id(a),Id($_),[[NullLiteral()]]),UnaryOp(!,FloatLit(1.0)),IntLit(1),Block([If(BinaryOp(==,Id(i),Id(j)),Block([Call(Id(Program),Id($print),[BinaryOp(+,Id(i),Id(j))])]))])])])])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast84'))

    # def test85(self):
    #     input = """Class a{
    #         Var a: Array[Array[Float, 012], 0x111];
    #         main(){
    #             Var a: Array[Boolean, 0X111];
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(273,ArrayType(10,FloatType)))),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(273,BoolType))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast85'))

    # def test86(self):
    #     input = """
    #             Class Program{
    #                 Var $a : Array[Int, 0b1101] = Array(1,2,3); 
    #                 main(){
    #                     Var a : Array[Int, 0B1101] = (((((Array(012))))));
    #                 }
    #             }
    #             """
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(13,IntType),[IntLit(1),IntLit(2),IntLit(3)])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(13,IntType),[IntLit(10)])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast86'))

    # def test87(self):
    #     input = """  Class a: Parent{
    #         main(){
    #             Self.a= 2+3;
    #         }
    #         Constructor(a:Int){
    #             Self.print(a);
    #         }
    #         Destructor(){
    #             Self.delete(Self);
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),Id(Parent),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),BinaryOp(+,IntLit(2),IntLit(3)))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([Call(Self(),Id(print),[Id(a)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(delete),[Self()])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast87'))

    # def test88(self):
    #     input = """  Class a{
    #         main(){
    #             Val a,b: Program = New Program(1,2), Null;
    #             b = New Program(Array(1., .0e2));
    #             c[b[a][0xA]] = a || b;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(Program)),NewExpr(Id(Program),[IntLit(1),IntLit(2)])),ConstDecl(Id(b),ClassType(Id(Program)),NullLiteral()),AssignStmt(Id(b),NewExpr(Id(Program),[[FloatLit(1.0),FloatLit(0.0)]])),AssignStmt(ArrayCell(Id(c),[ArrayCell(Id(b),[Id(a),IntLit(10)])]),BinaryOp(||,Id(a),Id(b)))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast88'))

    # def test89(self):
    #     input = """  Class a{
    #         Val a: String = "hien";
    #     }
    #     Class A: a{
    #         getA(){
    #             Return Self.a;
    #         }
    #     }
    #     Class AA: A{
    #         getA(){
    #             Self.getA();
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit(hien)))]),ClassDecl(Id(A),Id(a),[MethodDecl(Id(getA),Instance,[],Block([Return(FieldAccess(Self(),Id(a)))]))]),ClassDecl(Id(AA),Id(A),[MethodDecl(Id(getA),Instance,[],Block([Call(Self(),Id(getA),[])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast89'))

    # def test90(self):
    #     input = """ Class a{
    #         Val $instance: a = Self;
    #         $doSomething(){
    #             Program::$print(a::$instance);
    #             Program::$print("done");
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[AttributeDecl(Static,ConstDecl(Id($instance),ClassType(Id(a)),Self())),MethodDecl(Id($doSomething),Static,[],Block([Call(Id(Program),Id($print),[FieldAccess(Id(a),Id($instance))]),Call(Id(Program),Id($print),[StringLit(done)])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast90'))

    # def test91(self):
    #     input = """   Class a{
    #         main(){
    #             Return 1+ 2. * 0x20 % "Hien" || Null == Self +. True - -False >= !021 / a::$instance.count(1) --- Array(1,0b1101);
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(main),Instance,[],Block([Return(BinaryOp(+.,BinaryOp(==,BinaryOp(||,BinaryOp(+,IntLit(1),BinaryOp(%,BinaryOp(*,FloatLit(2.0),IntLit(32)),StringLit(Hien))),NullLiteral()),Self()),BinaryOp(>=,BinaryOp(-,BooleanLit(True),UnaryOp(-,BooleanLit(False))),BinaryOp(-,BinaryOp(/,UnaryOp(!,IntLit(17)),CallExpr(FieldAccess(Id(a),Id($instance)),Id(count),[IntLit(1)])),UnaryOp(-,UnaryOp(-,[IntLit(1),IntLit(13)]))))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast91'))

    # def test92(self):
    #     input = """  Class Program{
    #         main(){
    #             a = !!!!!!-------Self;
    #         }
    #     }
    #     """
    #     expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,UnaryOp(-,Self()))))))))))))))]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast92'))

    # def test93(self):
    #     input = """
    #             Class Program{
    #                 main() {
    #                     Val a,b,c:Float = 1.e9,1.e-0,1.e1-2;
    #                     Var d,e:Float = .1e9,.2e-8;
    #                     Val f,g,h:Float = 0.e12,1.e-12,10.e+5;
    #                     Var i,j,k:Float = 0.,1.,1.12;
    #                 } 
    #             }
    #             """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),FloatType,FloatLit(1000000000.0)),ConstDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),FloatType,BinaryOp(-,FloatLit(10.0),IntLit(2))),VarDecl(Id(d),FloatType,FloatLit(100000000.0)),VarDecl(Id(e),FloatType,FloatLit(2e-09)),ConstDecl(Id(f),FloatType,FloatLit(0.0)),ConstDecl(Id(g),FloatType,FloatLit(1e-12)),ConstDecl(Id(h),FloatType,FloatLit(1000000.0)),VarDecl(Id(i),FloatType,FloatLit(0.0)),VarDecl(Id(j),FloatType,FloatLit(1.0)),VarDecl(Id(k),FloatType,FloatLit(1.12))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 'ast93'))

    # def test94(self):
    #     input = """ Class Pro3 {
    #                 main() {}
    #                 func() {}
    #                 Constructor() {}              
    #             }"""
    #     expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(func),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast94'))

    # def test95(self):
    #     input = """  Class a{
    #         main(){{{}}}
    #         }
    #     """
    #     expect = 'Program([ClassDecl(Id(a),[MethodDecl(Id(main),Instance,[],Block([Block([Block([])])]))])])'
    #     self.assertTrue(TestAST.test(input, expect, 'ast95'))

    # def test96(self):
    #     input = """ Class Pro3 {
    #                 Var a: Array[Int, 5]; 
    #                 main() {}             
    #             }"""
    #     expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),MethodDecl(Id(main),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast96'))

    # def test97(self):
    #     input = """ Class Pro3 {
    #                 Var a: Array[Int, 5] = Array(1,2,3); 
    #                 main() {}             
    #             }"""
    #     expect = "Program([ClassDecl(Id(Pro3),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])),MethodDecl(Id(main),Instance,[],Block([]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast97'))

    # def test98(self):
    #     input = """ Class Pro3 { 
    #                 main() {
    #                     Var a: Array[Int, 5] = Array(1,2,3);
    #                 }             
    #             }"""
    #     expect = "Program([ClassDecl(Id(Pro3),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3)])]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast98'))

    def test99(self):
        input = """ 
        Class A{
            Val a,b:String = (1+1)[1][2][3], (a[1][2]);
            main(){
                Out.printLn("Hello");
                Val _,__:Float = 1,2;
            }
        }
        """
        expect = "Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(BinaryOp(+,IntLit(1),IntLit(1)),[IntLit(1),IntLit(2),IntLit(3)]))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,ArrayCell(Id(a),[IntLit(1),IntLit(2)]))),MethodDecl(Id(main),Instance,[],Block([Call(Id(Out),Id(printLn),[StringLit(Hello)]),ConstDecl(Id(),FloatType,IntLit(1)),ConstDecl(Id(_),FloatType,IntLit(2))]))])])"
        self.assertTrue(TestAST.test(input, expect, 'ast99'))
    
    # def test101(self):
    #     input = """
    #     Class A{
    #         main(){
    #             a = (a[0][1])[2][3];
    #             a = (Self.a)[0][1][2];
    #             a = a[0][1][2];
    #             (a[3])[1][2] = 1;
    #             a[1][2][3] = 123;
    #             (Self.a)[1][2] = 0x123;
    #         }
    #     }"""
    #     expect = "Program([ClassDecl(Id(A),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(a),ArrayCell(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),[IntLit(2),IntLit(3)])),AssignStmt(Id(a),ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(0),IntLit(1),IntLit(2)])),AssignStmt(Id(a),ArrayCell(Id(a),[IntLit(0),IntLit(1),IntLit(2)])),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(3)]),[IntLit(1),IntLit(2)]),IntLit(1)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),IntLit(123)),AssignStmt(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2)]),IntLit(291))]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 'ast101'))
    
    
    
    
    
