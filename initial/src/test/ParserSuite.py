import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test1(self):
        """Simple program: int main() {}"""
        input = """Class test{
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser01'))

    def test2(self):
        """Simple program: int main() {}"""
        input = """Class $test{
}"""
        expect = "Error on line 1 col 6: $test"
        self.assertTrue(TestParser.test(input, expect, 'parser02'))

    def test3(self):
        """Simple program: int main() {}"""
        input = """Class test: $par{
}"""
        expect = "Error on line 1 col 12: $par"
        self.assertTrue(TestParser.test(input, expect, 'parser03'))

    def test4(self):
        """Simple program: int main() {}"""
        input = """Class test:s ,b{
}"""
        expect = "Error on line 1 col 13: ,"
        self.assertTrue(TestParser.test(input, expect, 'parser04'))

    def test5(self):
        """Simple program: int main() {}"""
        input = """Class 1test{
}"""
        expect = "Error on line 1 col 6: 1"
        self.assertTrue(TestParser.test(input, expect, 'parser05'))

    def test6(self):
        """Simple program: int main() {}"""
        input = """Class {
}"""
        expect = "Error on line 1 col 6: {"
        self.assertTrue(TestParser.test(input, expect, 'parser06'))

    def test7(self):
        """Simple program: int main() {}"""
        input = """ """
        expect = "Error on line 1 col 1: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 'parser07'))

    def test8(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val a: Int;
        Var $12, as: Boolean = 0;
}"""
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 'parser08'))

    def test9(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Var a: Float = 2,4,5;
}"""
        expect = "Error on line 2 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 'parser09'))

    def test10(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Var a: Float = ;
}"""
        expect = "Error on line 2 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 'parser10'))

    def test11(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Var _, $2: $a = d;
}"""
        expect = "Error on line 2 col 19: $a"
        self.assertTrue(TestParser.test(input, expect, 'parser11'))

    def test12(self):
        """Simple program: int main() {}"""
        input = """Class test{
        s(){}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser12'))

    def test13(self):
        """Simple program: int main() {}"""
        input = """Class test: par{
        s(3){}
}"""
        expect = "Error on line 2 col 10: 3"
        self.assertTrue(TestParser.test(input, expect, 'parser13'))

    def test14(self):
        """Simple program: int main() {}"""
        input = """Class test:s{
        s(a;b:Int){};
        s(a;b:Float){};
}"""
        expect = "Error on line 2 col 11: ;"
        self.assertTrue(TestParser.test(input, expect, 'parser14'))

    def test15(self):
        """Simple program: int main() {}"""
        input = """Class test{
            s(b,c,v:f){}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser15'))

    def test16(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s:String= "asdasddfg \\b fdg";
            $1(s:Int,b:String){};
}"""
        expect = "Error on line 3 col 20: ,"
        self.assertTrue(TestParser.test(input, expect, 'parser16'))

    def test17(self):
        """Simple program: int main() {}"""
        input = """Class test{
            1(2){};
} """
        expect = "Error on line 2 col 12: 1"
        self.assertTrue(TestParser.test(input, expect, 'parser17'))

    def test18(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Int s(){};
}"""
        expect = "Error on line 2 col 8: Int"
        self.assertTrue(TestParser.test(input, expect, 'parser18'))

    def test19(self):
        """Simple program: int main() {}"""
        input = """Class test{
            s();
}"""
        expect = "Error on line 2 col 15: ;"
        self.assertTrue(TestParser.test(input, expect, 'parser19'))

    def test20(self):
        """Simple program: int main() {}"""
        input = """Class test{
}
Class b{
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser20'))

    def test21(self):
        """Simple program: int main() {}"""
        input = """Class Shape {
                Val $numOfShape: Array[Int , 2] = 0;
                $getNumOfShape() {
                    Return 2;
                }
            }
            Class Program{
                main(){
                    Out.print(arr[3]);
                    Out.print(Shape::$getNumOfShape());
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser21'))

    def test22(self):
        """Simple program: int main() {}"""
        input = """Class Shape {
                Val $numOfShape: Array[Int , 2] = 0;
                $getNumOfShape() {
                    Return 2;
                }
            }
            Class Program{
                main(){
                    Out.print(arr[3]);
                    Out.print(Shape::$getNumOfShape());
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser22'))

    def test23(self):
        """Simple program: int main() {}"""
        input = """Class test: par{
        ##s(3){}
        ##
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser23'))

    def test24(self):
        """Simple program: int main() {}"""
        input = """Class test:s{
        a(){
            a = Array(Array(1,3),fd, "fgdg");
            b = Array(Array(1,3),, "as);
        }
}"""
        expect = "as);"
        self.assertTrue(TestParser.test(input, expect, 'parser24'))

    def test25(self):
        """Simple program: int main() {}"""
        input = """Class A{
            $(){
                a = 1;
                a = a + 1;
            }
        }"""
        expect = "$"
        self.assertTrue(TestParser.test(input, expect, 'parser25'))

    def test26(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Destructor(a:Int){}
}"""
        expect = "Error on line 2 col 23: a"
        self.assertTrue(TestParser.test(input, expect, 'parser26'))

    def test27(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Array[Array[Float, 0], 5];
} """
        expect = "Error on line 2 col 38: 0"
        self.assertTrue(TestParser.test(input, expect, 'parser27'))

    def test28(self):
        """Simple program: int main() {}"""
        input = """Class test{
        s(){
            d = New New New a();
        }
}"""
        expect = "Error on line 3 col 20: New"
        self.assertTrue(TestParser.test(input, expect, 'parser28'))

    def test29(self):
        """Simple program: int main() {}"""
        input = """Class test{
            s(){
            d = New New New Self;
        }
}"""
        expect = "Error on line 3 col 20: New"
        self.assertTrue(TestParser.test(input, expect, 'parser29'))

    def test30(self):
        """Simple program: int main() {}"""
        input = """Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Break::$numOfShape();
            }
        }
        """
        expect = "Error on line 6 col 21: ::"

        self.assertTrue(TestParser.test(input, expect, 'parser30'))

    def test31(self):
        """Simple program: int main() {}"""
        input = """Class test{
    Val s: Int = 2.0 % 3;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser31'))

    def test32(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = "as" ==. d +. f;
}"""
        expect = "Error on line 2 col 36: +."
        self.assertTrue(TestParser.test(input, expect, 'parser32'))

    def test33(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = "as" == Self > v;
}"""
        expect = "Error on line 2 col 38: >"
        self.assertTrue(TestParser.test(input, expect, 'parser33'))

    def test34(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 213 && "xv\\tc" || Array();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser34'))

    def test35(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 213 && "xv\\tc" || Array(1) != d;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser35'))

    def test36(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = f * d() + 3 -4 *4 /6 +2 /3 +6 *5;
}"""
        expect = "Error on line 2 col 30: ("
        self.assertTrue(TestParser.test(input, expect, 'parser36'))

    def test37(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 3 + !!!!!2 * 43 --5;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser37'))

    def test38(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = Array(2,3)[3+2] ==. 5 +.4;
}"""
        expect = "Error on line 2 col 47: +."
        self.assertTrue(TestParser.test(input, expect, 'parser38'))

    def test39(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = Array(2,3)[Array(2,3)]+ Self[2];
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser39'))

    def test40(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = Array(2,3)[]+ Self();
}"""
        expect = "Error on line 2 col 36: ]"
        self.assertTrue(TestParser.test(input, expect, 'parser40'))

    def test41(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = 5::2.3.4;
}"""
        expect = "Error on line 2 col 22: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser41'))

    def test42(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 1+3.7.4.3.2;
}"""
        expect = "Error on line 2 col 31: 4.3"
        self.assertTrue(TestParser.test(input, expect, 'parser42'))

    def test43(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 2 + ().7;
}"""
        expect = "Error on line 2 col 30: )"
        self.assertTrue(TestParser.test(input, expect, 'parser43'))

    def test44(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = d::3::fg();
}"""
        expect = "Error on line 2 col 28: 3"
        self.assertTrue(TestParser.test(input, expect, 'parser44'))

    def test45(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = 2.f::5.h::g();
}"""
        expect = "Error on line 2 col 27: f"
        self.assertTrue(TestParser.test(input, expect, 'parser45'))

    def test46(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = Self.d() --- Self.Self * 2e0.Self;
}"""
        expect = "Error on line 2 col 43: Self"
        self.assertTrue(TestParser.test(input, expect, 'parser46'))

    def test47(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = Self :: Self.Self::Self;
}"""
        expect = "Error on line 2 col 30: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser47'))

    def test48(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = a::$b;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser48'))

    def test49(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = New New New S();
}"""
        expect = "Error on line 2 col 29: New"
        self.assertTrue(TestParser.test(input, expect, 'parser49'))

    def test50(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = s ::$c;
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser50'))

    def test51(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Destructor(){}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser51'))

    def test52(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Constructor(){}
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser52'))

    def test53(self):
        """Simple program: int main() {}"""
        input = """Class test{
            Val s: Int = s.d+ d::$a();
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser53'))

    def test54(self):
        """Simple program: int main() {}"""
        input = """Class test{
        a(){
            a = 1+2;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser54'))

    def test55(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            a[0] = 1+2;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser55'))

    def test56(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            a::S = 1+2;
            a.S = 1+2;
        }
        e(){
            a::S = a.d(1);
            a.S = a.d(1) ==.2+3* (3+.-2);
        }
}"""
        expect = "Error on line 3 col 15: S"
        self.assertTrue(TestParser.test(input, expect, 'parser56'))

    def test57(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = 2;
        a(){
            Val s: Int ;
            Val $s: Int;
        }
}"""
        expect = "Error on line 5 col 16: $s"
        self.assertTrue(TestParser.test(input, expect, 'parser57'))

    def test58(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = a::$b;
        a(){
            Val s: Int = Self :: Self.Self::Self;
            Val $s: Int;
        }
}
Class test1{
        Val s: Int = a::$b;
        b(){
            Val s: Bool = Self ;
            Val $s: Int;
        }
}"""
        expect = "Error on line 4 col 30: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser58'))

    def test59(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: a = a.b;
        a(){
            Val s: $f ;
            Val $s: Int;
        }
}"""
        expect = "Error on line 4 col 19: $f"
        self.assertTrue(TestParser.test(input, expect, 'parser59'))

    def test60(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s,f: Float = s :: $c;
}"""
        expect = "Error on line 2 col 32: ;"
        self.assertTrue(TestParser.test(input, expect, 'parser60'))

    def test61(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Destructor(){
            a = Self;
            a = Array(1,2,3);
            a = Array[Bool, 5];
        }
}"""
        expect = "Error on line 5 col 21: ["
        self.assertTrue(TestParser.test(input, expect, 'parser61'))

    def test62(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Constructor(){
            a[-1] = "\\n";
            a[0] = a();
            a[1_3] = S::$sda;
            a[] = Array(1,2);
        }
}"""
        expect = "Error on line 4 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 'parser62'))

    def test63(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = s.d+ d::$Sel();
        a(){
            a::s = 0 ==. 3;
        }
}"""
        expect = "Error on line 4 col 15: s"
        self.assertTrue(TestParser.test(input, expect, 'parser63'))

    def test64(self):
        """Simple program: int main() {}"""
        input = """Class test{
        a(){
            $d::s = 2+ 3 ==5;
        }
}"""
        expect = "Error on line 3 col 12: $d"
        self.assertTrue(TestParser.test(input, expect, 'parser64'))
# -----------------

    def test65(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            a.$sda = a();
        }
}"""
        expect = "Error on line 3 col 14: $sda"
        self.assertTrue(TestParser.test(input, expect, 'parser65'))

    def test66(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            $s.$a = a();
        }
        e(){
            a::S = a.d(1);
        }
}"""
        expect = "Error on line 3 col 12: $s"
        self.assertTrue(TestParser.test(input, expect, 'parser66'))

    def test67(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = S:: $S;
        a(){
            If (3+3){
                s = b.c.e::d;
            }
        }
}"""
        expect = "Error on line 5 col 25: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser67'))

    def test68(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = a::$b;
        a(){
            If((((a-1)))) {
                If (1){}
                Else{}
            }
        }
}
Class test1{
        Val s: Int = a::$b;
        $b(){
            If(1+-3){}
            Elseif {
                Var id = a1::2.4::3;
            }
        }
}"""
        expect = "Error on line 14 col 19: {"
        self.assertTrue(TestParser.test(input, expect, 'parser68'))

    def test69(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: a = New a::b;
        a(){
            If(a){}
            Elseif(2){}
            Elseif(a==.2){}
            Else{}
            Else{}
        }
}"""
        expect = "Error on line 2 col 24: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser69'))

    def test70(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Float = s ::$c;
        aw(){
            If(a){
                Break;
            }
            Elseif(2){
                Continue;
            }
            Else{
                Return;
            }
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser70'))

    def test71(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Destructor(){
            a.as() = Self;
        }
}"""
        expect = "Error on line 3 col 19: ="
        self.assertTrue(TestParser.test(input, expect, 'parser71'))

    def test72(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Constructor(){
            $a = ls1;
        }
}"""
        expect = "Error on line 3 col 12: $a"
        self.assertTrue(TestParser.test(input, expect, 'parser72'))

    def test73(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = s.d+ d::$a();
        a(){
            Foreach(a In 1 .. 20){
                a=b;
            }
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser73'))

    def test74(self):
        """Simple program: int main() {}"""
        input = """Class test{
        a(){
            Foreach(a In 2+4 .. "20"){
                a = b;
            }
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser74'))

    def test75(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Foreach($a In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 3 col 20: $a"
        self.assertTrue(TestParser.test(input, expect, 'parser75'))

    def test76(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Foreach(a::$b In c .. Self){
                a = b;
            }
        }
        e(){
            Foreach(a() In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 8 col 21: ("
        self.assertTrue(TestParser.test(input, expect, 'parser76'))

    def test77(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = S :: $S;
        a(){
            Foreach(a[2][4] In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 4 col 28: In"
        self.assertTrue(TestParser.test(input, expect, 'parser77'))

    def test78(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = a::$b;
        a(){
            Foreach(a.e In 2 .. "20" By 3==.4){
                a = b;
            }
        }
}
Class test1{
        Val s: Int = a::$b;
        $b(){
            Foreach(a.$s In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 12 col 22: $s"
        self.assertTrue(TestParser.test(input, expect, 'parser78'))

    def test79(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: a = a::$b;
        a(){
            Foreach(Self In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 4 col 25: In"
        self.assertTrue(TestParser.test(input, expect, 'parser79'))

    def test80(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Float = s :: $c;
        aw(){
            Foreach(a[2][4] In 2 .. "20" By Self){
                a = b;
            }
        }
}"""
        expect = "Error on line 4 col 28: In"
        self.assertTrue(TestParser.test(input, expect, 'parser80'))

    def test81(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Destructor(){
            a::$as() = Self;
        }
}"""
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 'parser81'))

    def test82(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Constructor(){
            a.b.c = 1;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser82'))

    def test83(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = s.d+ d::$a();
        a(){
            Foreach(a.b.f.d In 1 .. 20 By a.3){
                a=b;
            }
        }
}"""
        expect = "Error on line 4 col 44: 3"
        self.assertTrue(TestParser.test(input, expect, 'parser83'))

    def test84(self):
        """Simple program: int main() {}"""
        input = """Class test{
        a(){
            Foreach(a.$1 In 2+4 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 3 col 22: $1"
        self.assertTrue(TestParser.test(input, expect, 'parser84'))

    def test85(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Foreach(a.a[5] In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 3 col 27: In"
        self.assertTrue(TestParser.test(input, expect, 'parser85'))

    def test86(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Foreach(a::$b[0] In c .. Self By 1.){
                a = b;
            }
        }
        e(){
            Foreach(a In 2 .. "20" By True){
                a = b;
            }
        }
}"""
        expect = "Error on line 3 col 29: In"
        self.assertTrue(TestParser.test(input, expect, 'parser86'))

    def test87(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = S :: $S;
        a(){
            Foreach( In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 4 col 21: In"
        self.assertTrue(TestParser.test(input, expect, 'parser87'))

    def test88(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = a::$b;
        a(){
            Foreach(a.a() In 2 .. "20" By 3==.4){
                a = b;
            }
        }
}
Class test1{
        Val s: Int = a::$b;
        $b(){
            Return a.a[1];
        }
}"""
        expect = "Error on line 4 col 26: In"
        self.assertTrue(TestParser.test(input, expect, 'parser88'))

    def test89(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: a = a::$b;
        a(){
            Return a::$a[1];
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser89'))

    def test90(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Float = s :: $c;
        aw(){
            Return a[1].d;
        }
}"""
        expect = "Error on line 4 col 23: ."
        self.assertTrue(TestParser.test(input, expect, 'parser90'))

    def test91(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Destructor(){
            a::$as() = Self;
        }
}"""
        expect = "Error on line 3 col 21: ="
        self.assertTrue(TestParser.test(input, expect, 'parser91'))

    def test92(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Constructor(){
            Return a[1][a[2]];
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser92'))

    def test93(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = s.d+ d::$a();
        a(){
            Return a[1][a[2].a];
        }
}"""
        expect = "Error on line 4 col 28: ."
        self.assertTrue(TestParser.test(input, expect, 'parser93'))

    def test94(self):
        """Simple program: int main() {}"""
        input = """Class test{
        a(){
            Return a[1][a[2]::$f];
        }
}"""
        expect = "Error on line 3 col 28: ::"
        self.assertTrue(TestParser.test(input, expect, 'parser94'))

    def test95(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Return a[1][a[2]+a[3][5].a()];
        }
}"""
        expect = "Error on line 3 col 36: ."
        self.assertTrue(TestParser.test(input, expect, 'parser95'))

    def test96(self):
        """Simple program: int main() {}"""
        input = """Class test{
        e(){
            Return a[1]::$;
        }
}"""
        expect = "$"
        self.assertTrue(TestParser.test(input, expect, 'parser96'))

    def test97(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = S :: $S;
        a(){
            Foreach(a::$a.d[6] In 2 .. "20"){
                a = b;
            }
        }
}"""
        expect = "Error on line 4 col 31: In"
        self.assertTrue(TestParser.test(input, expect, 'parser97'))

    def test98(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Int = a::$b;
        a(){
            Return a::$a.a.a.a;
        }
}
Class test1{
        Val s: Int = a::$b;
        $b(){
            Return a.a[1] +. a ==. _;
        }
}"""
        expect = "Error on line 10 col 31: ==."
        self.assertTrue(TestParser.test(input, expect, 'parser98'))

    def test99(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: a = a::$b;
        a(){
            Return a::$a[1].New a;
        }
}"""
        expect = "Error on line 4 col 27: ."
        self.assertTrue(TestParser.test(input, expect, 'parser99'))

    def test100(self):
        """Simple program: int main() {}"""
        input = """Class test{
        Val s: Float = s :: $c;
        aw(){
            Return New a().b;
        }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 'parser100'))

    def test101(self):
        input = """ 
        Class main{
            Val a, b: Array[Int, 123_456_789] = Array(1,2,3), Array(0x123, 0x456, 0x789);
            Var c: Int = a[0] + b[0] + C[1];
             
            $GETsHAPE(){
                Foreach(i In 1..10){
                Val a: Int = Array(
                    Array(1,2,3),
                    ,
                    Array(4,5,6)
                )
                }
            }
        }
        """
        expect = """Error on line 7 col 32: 10"""
        self.assertTrue(TestParser.test(input, expect, 'parser101'))
