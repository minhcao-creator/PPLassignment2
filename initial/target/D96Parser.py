# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0213\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3r\n\3\3\4\3")
        buf.write("\4\3\4\5\4w\n\4\3\4\3\4\3\4\5\4|\n\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\5\6\u0087\n\6\3\7\3\7\3\7\3\7\5\7\u008d")
        buf.write("\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u009d\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\5\n\u00a9\n\n\3\13\3\13\3\13\3\13\3\13\5\13\u00b0")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00b8\n\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\17\3\17\5\17\u00c2\n\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00d1\n\20\3\21\3\21\3\21\3\21\5\21\u00d7\n\21\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ed")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00f9\n\24\3\25\3\25\3\25\3\25\5\25\u00ff\n\25\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\5\27\u010f\n\27\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\5\32\u0125\n\32\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u0130\n\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\5\36\u013e\n\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\5\37\u0148\n\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\5\37\u0153\n\37\3\37\3\37\5\37\u0157\n\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\5!\u0161\n!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\5\"\u016d\n\"\3#\3#\3#\3#\3#\5#\u0174")
        buf.write("\n#\3$\3$\3$\3$\3$\5$\u017b\n$\3%\3%\3%\3%\3%\3%\7%\u0183")
        buf.write("\n%\f%\16%\u0186\13%\3&\3&\3&\3&\3&\3&\7&\u018e\n&\f&")
        buf.write("\16&\u0191\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u0199\n\'\f")
        buf.write("\'\16\'\u019c\13\'\3(\3(\3(\5(\u01a1\n(\3)\3)\3)\5)\u01a6")
        buf.write("\n)\3*\3*\3+\3+\3+\3+\3+\7+\u01af\n+\f+\16+\u01b2\13+")
        buf.write("\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01c4")
        buf.write("\n-\3-\7-\u01c7\n-\f-\16-\u01ca\13-\3.\3.\3.\3.\3.\3.")
        buf.write("\3.\3.\3.\5.\u01d5\n.\3.\3.\5.\u01d9\n.\3/\3/\5/\u01dd")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\5\60\u01e4\n\60\3\60\3\60")
        buf.write("\3\61\3\61\3\61\3\61\3\61\5\61\u01ed\n\61\3\62\3\62\3")
        buf.write("\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u01fb\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3")
        buf.write("\64\3\64\3\64\3\64\5\64\u0209\n\64\3\65\3\65\3\65\3\65")
        buf.write("\5\65\u020f\n\65\3\65\3\65\3\65\2\7HJLTX\66\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfh\2\n\3\2\'(\3\2>?\3\2\20\21\3\2")
        buf.write("\22\27\3\2!\"\3\2\33\34\3\2\35\37\3\2\5\6\2\u0225\2j\3")
        buf.write("\2\2\2\4q\3\2\2\2\6s\3\2\2\2\b\177\3\2\2\2\n\u0086\3\2")
        buf.write("\2\2\f\u008c\3\2\2\2\16\u008e\3\2\2\2\20\u009c\3\2\2\2")
        buf.write("\22\u00a8\3\2\2\2\24\u00af\3\2\2\2\26\u00b7\3\2\2\2\30")
        buf.write("\u00b9\3\2\2\2\32\u00bb\3\2\2\2\34\u00bd\3\2\2\2\36\u00d0")
        buf.write("\3\2\2\2 \u00d2\3\2\2\2\"\u00db\3\2\2\2$\u00ec\3\2\2\2")
        buf.write("&\u00f8\3\2\2\2(\u00fe\3\2\2\2*\u0100\3\2\2\2,\u010e\3")
        buf.write("\2\2\2.\u0110\3\2\2\2\60\u0113\3\2\2\2\62\u0124\3\2\2")
        buf.write("\2\64\u0126\3\2\2\2\66\u0134\3\2\2\28\u0137\3\2\2\2:\u013a")
        buf.write("\3\2\2\2<\u0156\3\2\2\2>\u0158\3\2\2\2@\u0160\3\2\2\2")
        buf.write("B\u016c\3\2\2\2D\u0173\3\2\2\2F\u017a\3\2\2\2H\u017c\3")
        buf.write("\2\2\2J\u0187\3\2\2\2L\u0192\3\2\2\2N\u01a0\3\2\2\2P\u01a5")
        buf.write("\3\2\2\2R\u01a7\3\2\2\2T\u01a9\3\2\2\2V\u01b3\3\2\2\2")
        buf.write("X\u01b7\3\2\2\2Z\u01d8\3\2\2\2\\\u01dc\3\2\2\2^\u01de")
        buf.write("\3\2\2\2`\u01ec\3\2\2\2b\u01fa\3\2\2\2d\u01fc\3\2\2\2")
        buf.write("f\u0208\3\2\2\2h\u020a\3\2\2\2jk\5\4\3\2kl\7\2\2\3l\3")
        buf.write("\3\2\2\2mn\5\6\4\2no\5\4\3\2or\3\2\2\2pr\5\6\4\2qm\3\2")
        buf.write("\2\2qp\3\2\2\2r\5\3\2\2\2st\7\n\2\2tv\7?\2\2uw\5\b\5\2")
        buf.write("vu\3\2\2\2vw\3\2\2\2wx\3\2\2\2x{\7\f\2\2y|\5\n\6\2z|\3")
        buf.write("\2\2\2{y\3\2\2\2{z\3\2\2\2|}\3\2\2\2}~\7\r\2\2~\7\3\2")
        buf.write("\2\2\177\u0080\7&\2\2\u0080\u0081\7?\2\2\u0081\t\3\2\2")
        buf.write("\2\u0082\u0083\5\f\7\2\u0083\u0084\5\n\6\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0087\5\f\7\2\u0086\u0082\3\2\2\2\u0086")
        buf.write("\u0085\3\2\2\2\u0087\13\3\2\2\2\u0088\u008d\5\16\b\2\u0089")
        buf.write("\u008d\5\34\17\2\u008a\u008d\5 \21\2\u008b\u008d\5\"\22")
        buf.write("\2\u008c\u0088\3\2\2\2\u008c\u0089\3\2\2\2\u008c\u008a")
        buf.write("\3\2\2\2\u008c\u008b\3\2\2\2\u008d\r\3\2\2\2\u008e\u008f")
        buf.write("\5\20\t\2\u008f\17\3\2\2\2\u0090\u0091\t\2\2\2\u0091\u0092")
        buf.write("\5\32\16\2\u0092\u0093\5\22\n\2\u0093\u0094\5\30\r\2\u0094")
        buf.write("\u0095\7\31\2\2\u0095\u009d\3\2\2\2\u0096\u0097\t\2\2")
        buf.write("\2\u0097\u0098\5\24\13\2\u0098\u0099\7&\2\2\u0099\u009a")
        buf.write("\5\26\f\2\u009a\u009b\7\31\2\2\u009b\u009d\3\2\2\2\u009c")
        buf.write("\u0090\3\2\2\2\u009c\u0096\3\2\2\2\u009d\21\3\2\2\2\u009e")
        buf.write("\u009f\7\30\2\2\u009f\u00a0\5\32\16\2\u00a0\u00a1\5\22")
        buf.write("\n\2\u00a1\u00a2\5\30\r\2\u00a2\u00a3\7\30\2\2\u00a3\u00a9")
        buf.write("\3\2\2\2\u00a4\u00a5\7&\2\2\u00a5\u00a6\5\26\f\2\u00a6")
        buf.write("\u00a7\7\32\2\2\u00a7\u00a9\3\2\2\2\u00a8\u009e\3\2\2")
        buf.write("\2\u00a8\u00a4\3\2\2\2\u00a9\23\3\2\2\2\u00aa\u00ab\5")
        buf.write("\32\16\2\u00ab\u00ac\7\30\2\2\u00ac\u00ad\5\24\13\2\u00ad")
        buf.write("\u00b0\3\2\2\2\u00ae\u00b0\5\32\16\2\u00af\u00aa\3\2\2")
        buf.write("\2\u00af\u00ae\3\2\2\2\u00b0\25\3\2\2\2\u00b1\u00b8\7")
        buf.write("\64\2\2\u00b2\u00b8\7\65\2\2\u00b3\u00b8\7\66\2\2\u00b4")
        buf.write("\u00b8\7\67\2\2\u00b5\u00b8\7?\2\2\u00b6\u00b8\5d\63\2")
        buf.write("\u00b7\u00b1\3\2\2\2\u00b7\u00b2\3\2\2\2\u00b7\u00b3\3")
        buf.write("\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b7\u00b6")
        buf.write("\3\2\2\2\u00b8\27\3\2\2\2\u00b9\u00ba\5D#\2\u00ba\31\3")
        buf.write("\2\2\2\u00bb\u00bc\t\3\2\2\u00bc\33\3\2\2\2\u00bd\u00be")
        buf.write("\5\32\16\2\u00be\u00c1\7\16\2\2\u00bf\u00c2\5\36\20\2")
        buf.write("\u00c0\u00c2\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0\3")
        buf.write("\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4\7\17\2\2\u00c4")
        buf.write("\u00c5\5> \2\u00c5\35\3\2\2\2\u00c6\u00c7\5(\25\2\u00c7")
        buf.write("\u00c8\7&\2\2\u00c8\u00c9\5\26\f\2\u00c9\u00ca\7\31\2")
        buf.write("\2\u00ca\u00cb\5\36\20\2\u00cb\u00d1\3\2\2\2\u00cc\u00cd")
        buf.write("\5(\25\2\u00cd\u00ce\7&\2\2\u00ce\u00cf\5\26\f\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00c6\3\2\2\2\u00d0\u00cc\3\2\2\2")
        buf.write("\u00d1\37\3\2\2\2\u00d2\u00d3\7)\2\2\u00d3\u00d6\7\16")
        buf.write("\2\2\u00d4\u00d7\5\36\20\2\u00d5\u00d7\3\2\2\2\u00d6\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\7\17\2\2\u00d9\u00da\5> \2\u00da!\3\2\2\2\u00db")
        buf.write("\u00dc\7*\2\2\u00dc\u00dd\7\16\2\2\u00dd\u00de\7\17\2")
        buf.write("\2\u00de\u00df\5> \2\u00df#\3\2\2\2\u00e0\u00e1\t\2\2")
        buf.write("\2\u00e1\u00e2\7?\2\2\u00e2\u00e3\5&\24\2\u00e3\u00e4")
        buf.write("\5\30\r\2\u00e4\u00e5\7\31\2\2\u00e5\u00ed\3\2\2\2\u00e6")
        buf.write("\u00e7\t\2\2\2\u00e7\u00e8\5(\25\2\u00e8\u00e9\7&\2\2")
        buf.write("\u00e9\u00ea\5\26\f\2\u00ea\u00eb\7\31\2\2\u00eb\u00ed")
        buf.write("\3\2\2\2\u00ec\u00e0\3\2\2\2\u00ec\u00e6\3\2\2\2\u00ed")
        buf.write("%\3\2\2\2\u00ee\u00ef\7\30\2\2\u00ef\u00f0\7?\2\2\u00f0")
        buf.write("\u00f1\5\22\n\2\u00f1\u00f2\5\30\r\2\u00f2\u00f3\7\30")
        buf.write("\2\2\u00f3\u00f9\3\2\2\2\u00f4\u00f5\7&\2\2\u00f5\u00f6")
        buf.write("\5\26\f\2\u00f6\u00f7\7\32\2\2\u00f7\u00f9\3\2\2\2\u00f8")
        buf.write("\u00ee\3\2\2\2\u00f8\u00f4\3\2\2\2\u00f9\'\3\2\2\2\u00fa")
        buf.write("\u00fb\7?\2\2\u00fb\u00fc\7\30\2\2\u00fc\u00ff\5(\25\2")
        buf.write("\u00fd\u00ff\7?\2\2\u00fe\u00fa\3\2\2\2\u00fe\u00fd\3")
        buf.write("\2\2\2\u00ff)\3\2\2\2\u0100\u0101\5,\27\2\u0101\u0102")
        buf.write("\7\32\2\2\u0102\u0103\5D#\2\u0103\u0104\7\31\2\2\u0104")
        buf.write("+\3\2\2\2\u0105\u010f\7?\2\2\u0106\u0107\5X-\2\u0107\u0108")
        buf.write("\7#\2\2\u0108\u0109\7?\2\2\u0109\u010f\3\2\2\2\u010a\u010b")
        buf.write("\7?\2\2\u010b\u010c\7\3\2\2\u010c\u010f\7>\2\2\u010d\u010f")
        buf.write("\5.\30\2\u010e\u0105\3\2\2\2\u010e\u0106\3\2\2\2\u010e")
        buf.write("\u010a\3\2\2\2\u010e\u010d\3\2\2\2\u010f-\3\2\2\2\u0110")
        buf.write("\u0111\5T+\2\u0111\u0112\5V,\2\u0112/\3\2\2\2\u0113\u0114")
        buf.write("\7-\2\2\u0114\u0115\7\16\2\2\u0115\u0116\5D#\2\u0116\u0117")
        buf.write("\7\17\2\2\u0117\u0118\5> \2\u0118\u0119\5\62\32\2\u0119")
        buf.write("\61\3\2\2\2\u011a\u011b\7.\2\2\u011b\u011c\7\16\2\2\u011c")
        buf.write("\u011d\5D#\2\u011d\u011e\7\17\2\2\u011e\u011f\5> \2\u011f")
        buf.write("\u0120\5\62\32\2\u0120\u0125\3\2\2\2\u0121\u0122\7/\2")
        buf.write("\2\u0122\u0125\5> \2\u0123\u0125\3\2\2\2\u0124\u011a\3")
        buf.write("\2\2\2\u0124\u0121\3\2\2\2\u0124\u0123\3\2\2\2\u0125\63")
        buf.write("\3\2\2\2\u0126\u0127\7\60\2\2\u0127\u0128\7\16\2\2\u0128")
        buf.write("\u0129\7?\2\2\u0129\u012a\7:\2\2\u012a\u012b\5D#\2\u012b")
        buf.write("\u012c\7\4\2\2\u012c\u012f\5D#\2\u012d\u012e\7;\2\2\u012e")
        buf.write("\u0130\5D#\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\u0132\7\17\2\2\u0132\u0133\5> \2")
        buf.write("\u0133\65\3\2\2\2\u0134\u0135\7+\2\2\u0135\u0136\7\31")
        buf.write("\2\2\u0136\67\3\2\2\2\u0137\u0138\7,\2\2\u0138\u0139\7")
        buf.write("\31\2\2\u01399\3\2\2\2\u013a\u013d\7<\2\2\u013b\u013e")
        buf.write("\5D#\2\u013c\u013e\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013c")
        buf.write("\3\2\2\2\u013e\u013f\3\2\2\2\u013f\u0140\7\31\2\2\u0140")
        buf.write(";\3\2\2\2\u0141\u0142\5D#\2\u0142\u0143\7#\2\2\u0143\u0144")
        buf.write("\7?\2\2\u0144\u0147\7\16\2\2\u0145\u0148\5`\61\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2")
        buf.write("\u0148\u0149\3\2\2\2\u0149\u014a\7\17\2\2\u014a\u014b")
        buf.write("\7\31\2\2\u014b\u0157\3\2\2\2\u014c\u014d\7?\2\2\u014d")
        buf.write("\u014e\7\3\2\2\u014e\u014f\7>\2\2\u014f\u0152\7\16\2\2")
        buf.write("\u0150\u0153\5`\61\2\u0151\u0153\3\2\2\2\u0152\u0150\3")
        buf.write("\2\2\2\u0152\u0151\3\2\2\2\u0153\u0154\3\2\2\2\u0154\u0155")
        buf.write("\7\17\2\2\u0155\u0157\7\31\2\2\u0156\u0141\3\2\2\2\u0156")
        buf.write("\u014c\3\2\2\2\u0157=\3\2\2\2\u0158\u0159\7\f\2\2\u0159")
        buf.write("\u015a\5@!\2\u015a\u015b\7\r\2\2\u015b?\3\2\2\2\u015c")
        buf.write("\u015d\5B\"\2\u015d\u015e\5@!\2\u015e\u0161\3\2\2\2\u015f")
        buf.write("\u0161\3\2\2\2\u0160\u015c\3\2\2\2\u0160\u015f\3\2\2\2")
        buf.write("\u0161A\3\2\2\2\u0162\u016d\5$\23\2\u0163\u016d\5d\63")
        buf.write("\2\u0164\u016d\5*\26\2\u0165\u016d\5\60\31\2\u0166\u016d")
        buf.write("\5\64\33\2\u0167\u016d\5\66\34\2\u0168\u016d\58\35\2\u0169")
        buf.write("\u016d\5:\36\2\u016a\u016d\5<\37\2\u016b\u016d\5> \2\u016c")
        buf.write("\u0162\3\2\2\2\u016c\u0163\3\2\2\2\u016c\u0164\3\2\2\2")
        buf.write("\u016c\u0165\3\2\2\2\u016c\u0166\3\2\2\2\u016c\u0167\3")
        buf.write("\2\2\2\u016c\u0168\3\2\2\2\u016c\u0169\3\2\2\2\u016c\u016a")
        buf.write("\3\2\2\2\u016c\u016b\3\2\2\2\u016dC\3\2\2\2\u016e\u016f")
        buf.write("\5F$\2\u016f\u0170\t\4\2\2\u0170\u0171\5F$\2\u0171\u0174")
        buf.write("\3\2\2\2\u0172\u0174\5F$\2\u0173\u016e\3\2\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0174E\3\2\2\2\u0175\u0176\5H%\2\u0176\u0177")
        buf.write("\t\5\2\2\u0177\u0178\5H%\2\u0178\u017b\3\2\2\2\u0179\u017b")
        buf.write("\5H%\2\u017a\u0175\3\2\2\2\u017a\u0179\3\2\2\2\u017bG")
        buf.write("\3\2\2\2\u017c\u017d\b%\1\2\u017d\u017e\5J&\2\u017e\u0184")
        buf.write("\3\2\2\2\u017f\u0180\f\4\2\2\u0180\u0181\t\6\2\2\u0181")
        buf.write("\u0183\5J&\2\u0182\u017f\3\2\2\2\u0183\u0186\3\2\2\2\u0184")
        buf.write("\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185I\3\2\2\2\u0186")
        buf.write("\u0184\3\2\2\2\u0187\u0188\b&\1\2\u0188\u0189\5L\'\2\u0189")
        buf.write("\u018f\3\2\2\2\u018a\u018b\f\4\2\2\u018b\u018c\t\7\2\2")
        buf.write("\u018c\u018e\5L\'\2\u018d\u018a\3\2\2\2\u018e\u0191\3")
        buf.write("\2\2\2\u018f\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190K")
        buf.write("\3\2\2\2\u0191\u018f\3\2\2\2\u0192\u0193\b\'\1\2\u0193")
        buf.write("\u0194\5N(\2\u0194\u019a\3\2\2\2\u0195\u0196\f\4\2\2\u0196")
        buf.write("\u0197\t\b\2\2\u0197\u0199\5N(\2\u0198\u0195\3\2\2\2\u0199")
        buf.write("\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2")
        buf.write("\u019bM\3\2\2\2\u019c\u019a\3\2\2\2\u019d\u019e\7 \2\2")
        buf.write("\u019e\u01a1\5N(\2\u019f\u01a1\5P)\2\u01a0\u019d\3\2\2")
        buf.write("\2\u01a0\u019f\3\2\2\2\u01a1O\3\2\2\2\u01a2\u01a3\7\34")
        buf.write("\2\2\u01a3\u01a6\5P)\2\u01a4\u01a6\5R*\2\u01a5\u01a2\3")
        buf.write("\2\2\2\u01a5\u01a4\3\2\2\2\u01a6Q\3\2\2\2\u01a7\u01a8")
        buf.write("\5T+\2\u01a8S\3\2\2\2\u01a9\u01aa\b+\1\2\u01aa\u01ab\5")
        buf.write("X-\2\u01ab\u01b0\3\2\2\2\u01ac\u01ad\f\4\2\2\u01ad\u01af")
        buf.write("\5V,\2\u01ae\u01ac\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae")
        buf.write("\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1U\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b3\u01b4\7$\2\2\u01b4\u01b5\5D#\2\u01b5\u01b6")
        buf.write("\7%\2\2\u01b6W\3\2\2\2\u01b7\u01b8\b-\1\2\u01b8\u01b9")
        buf.write("\5Z.\2\u01b9\u01c8\3\2\2\2\u01ba\u01bb\f\5\2\2\u01bb\u01bc")
        buf.write("\7#\2\2\u01bc\u01c7\7?\2\2\u01bd\u01be\f\4\2\2\u01be\u01bf")
        buf.write("\7#\2\2\u01bf\u01c0\7?\2\2\u01c0\u01c3\7\16\2\2\u01c1")
        buf.write("\u01c4\5`\61\2\u01c2\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2")
        buf.write("\u01c3\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c7\7")
        buf.write("\17\2\2\u01c6\u01ba\3\2\2\2\u01c6\u01bd\3\2\2\2\u01c7")
        buf.write("\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2")
        buf.write("\u01c9Y\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc\7?\2\2")
        buf.write("\u01cc\u01cd\7\3\2\2\u01cd\u01d9\7>\2\2\u01ce\u01cf\7")
        buf.write("?\2\2\u01cf\u01d0\7\3\2\2\u01d0\u01d1\7>\2\2\u01d1\u01d4")
        buf.write("\7\16\2\2\u01d2\u01d5\5`\61\2\u01d3\u01d5\3\2\2\2\u01d4")
        buf.write("\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2")
        buf.write("\u01d6\u01d9\7\17\2\2\u01d7\u01d9\5\\/\2\u01d8\u01cb\3")
        buf.write("\2\2\2\u01d8\u01ce\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9[")
        buf.write("\3\2\2\2\u01da\u01dd\5^\60\2\u01db\u01dd\5b\62\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd]\3\2\2\2\u01de")
        buf.write("\u01df\79\2\2\u01df\u01e0\7?\2\2\u01e0\u01e3\7\16\2\2")
        buf.write("\u01e1\u01e4\5`\61\2\u01e2\u01e4\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e6")
        buf.write("\7\17\2\2\u01e6_\3\2\2\2\u01e7\u01e8\5D#\2\u01e8\u01e9")
        buf.write("\7\30\2\2\u01e9\u01ea\5`\61\2\u01ea\u01ed\3\2\2\2\u01eb")
        buf.write("\u01ed\5D#\2\u01ec\u01e7\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("a\3\2\2\2\u01ee\u01fb\7?\2\2\u01ef\u01fb\t\t\2\2\u01f0")
        buf.write("\u01fb\7\7\2\2\u01f1\u01fb\7\b\2\2\u01f2\u01fb\7\t\2\2")
        buf.write("\u01f3\u01fb\5h\65\2\u01f4\u01f5\7\16\2\2\u01f5\u01f6")
        buf.write("\5D#\2\u01f6\u01f7\7\17\2\2\u01f7\u01fb\3\2\2\2\u01f8")
        buf.write("\u01fb\7\13\2\2\u01f9\u01fb\78\2\2\u01fa\u01ee\3\2\2\2")
        buf.write("\u01fa\u01ef\3\2\2\2\u01fa\u01f0\3\2\2\2\u01fa\u01f1\3")
        buf.write("\2\2\2\u01fa\u01f2\3\2\2\2\u01fa\u01f3\3\2\2\2\u01fa\u01f4")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01f9\3\2\2\2\u01fb")
        buf.write("c\3\2\2\2\u01fc\u01fd\7\63\2\2\u01fd\u01fe\7$\2\2\u01fe")
        buf.write("\u01ff\5f\64\2\u01ff\u0200\7\30\2\2\u0200\u0201\7\5\2")
        buf.write("\2\u0201\u0202\7%\2\2\u0202e\3\2\2\2\u0203\u0209\7\64")
        buf.write("\2\2\u0204\u0209\7\65\2\2\u0205\u0209\7\66\2\2\u0206\u0209")
        buf.write("\7\67\2\2\u0207\u0209\5d\63\2\u0208\u0203\3\2\2\2\u0208")
        buf.write("\u0204\3\2\2\2\u0208\u0205\3\2\2\2\u0208\u0206\3\2\2\2")
        buf.write("\u0208\u0207\3\2\2\2\u0209g\3\2\2\2\u020a\u020b\7\63\2")
        buf.write("\2\u020b\u020e\7\16\2\2\u020c\u020f\5`\61\2\u020d\u020f")
        buf.write("\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u0210\u0211\7\17\2\2\u0211i\3\2\2\2-qv")
        buf.write("{\u0086\u008c\u009c\u00a8\u00af\u00b7\u00c1\u00d0\u00d6")
        buf.write("\u00ec\u00f8\u00fe\u010e\u0124\u012f\u013d\u0147\u0152")
        buf.write("\u0156\u0160\u016c\u0173\u017a\u0184\u018f\u019a\u01a0")
        buf.write("\u01a5\u01b0\u01c3\u01c6\u01c8\u01d4\u01d8\u01dc\u01e3")
        buf.write("\u01ec\u01fa\u0208\u020e")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'..'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Class'", "'Self'", 
                     "'{'", "'}'", "'('", "')'", "'==.'", "'+.'", "'=='", 
                     "'!='", "'<='", "'>='", "'>'", "'<'", "','", "';'", 
                     "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
                     "'||'", "'.'", "'['", "']'", "':'", "'Val'", "'Var'", 
                     "'Constructor'", "'Destructor'", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Null'", "'New'", "'In'", "'By'", "'Return'" ]

    symbolicNames = [ "<INVALID>", "DOUBLECOLON", "DOUBLEDOT", "INTLIT1", 
                      "INTLIT0", "FLOATLIT", "STRINGLIT", "BOOLLIT", "CLASS", 
                      "SELF", "LC", "RC", "LB", "RB", "STREQUAL", "STRCAT", 
                      "EQUAL", "NOTEQUAL", "SMALLOREQUAL", "LARGEOREQUAL", 
                      "LARGE", "SMALLER", "COMMA", "SEMI", "ASSIGN", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "DOT", 
                      "LSB", "RSB", "COLON", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "INT", 
                      "FLOAT", "BOOLEAN", "STRING", "NULL", "NEW", "IN", 
                      "BY", "RETURN", "COMMENT", "SID", "ID", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_TOKEN" ]

    RULE_program = 0
    RULE_classdecls = 1
    RULE_classdecl = 2
    RULE_superclass = 3
    RULE_memberlist = 4
    RULE_member = 5
    RULE_attributedecl = 6
    RULE_vardecl = 7
    RULE_varlist = 8
    RULE_idnamelist = 9
    RULE_typename = 10
    RULE_value = 11
    RULE_idname = 12
    RULE_methoddecl = 13
    RULE_paralist = 14
    RULE_constructor = 15
    RULE_destructor = 16
    RULE_vardeclStatement = 17
    RULE_varliststmt = 18
    RULE_idlist = 19
    RULE_assignStatement = 20
    RULE_assignvar = 21
    RULE_expAssignVar = 22
    RULE_ifStmtatement = 23
    RULE_elsePart = 24
    RULE_forinStatement = 25
    RULE_breakStatement = 26
    RULE_continueStatement = 27
    RULE_returnStatement = 28
    RULE_methodInvoStatement = 29
    RULE_block_stmt = 30
    RULE_statements = 31
    RULE_statement = 32
    RULE_expression = 33
    RULE_expression1 = 34
    RULE_expression2 = 35
    RULE_expression3 = 36
    RULE_expression4 = 37
    RULE_expression5 = 38
    RULE_expression6 = 39
    RULE_expression7a = 40
    RULE_expression7b = 41
    RULE_index_operators = 42
    RULE_expression8 = 43
    RULE_expression9 = 44
    RULE_expression10 = 45
    RULE_objectCreate = 46
    RULE_listOfExpressions = 47
    RULE_expression11 = 48
    RULE_arraytypedecl = 49
    RULE_typenamearray = 50
    RULE_arrayofvalue = 51

    ruleNames =  [ "program", "classdecls", "classdecl", "superclass", "memberlist", 
                   "member", "attributedecl", "vardecl", "varlist", "idnamelist", 
                   "typename", "value", "idname", "methoddecl", "paralist", 
                   "constructor", "destructor", "vardeclStatement", "varliststmt", 
                   "idlist", "assignStatement", "assignvar", "expAssignVar", 
                   "ifStmtatement", "elsePart", "forinStatement", "breakStatement", 
                   "continueStatement", "returnStatement", "methodInvoStatement", 
                   "block_stmt", "statements", "statement", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7a", "expression7b", 
                   "index_operators", "expression8", "expression9", "expression10", 
                   "objectCreate", "listOfExpressions", "expression11", 
                   "arraytypedecl", "typenamearray", "arrayofvalue" ]

    EOF = Token.EOF
    DOUBLECOLON=1
    DOUBLEDOT=2
    INTLIT1=3
    INTLIT0=4
    FLOATLIT=5
    STRINGLIT=6
    BOOLLIT=7
    CLASS=8
    SELF=9
    LC=10
    RC=11
    LB=12
    RB=13
    STREQUAL=14
    STRCAT=15
    EQUAL=16
    NOTEQUAL=17
    SMALLOREQUAL=18
    LARGEOREQUAL=19
    LARGE=20
    SMALLER=21
    COMMA=22
    SEMI=23
    ASSIGN=24
    ADD=25
    SUB=26
    MUL=27
    DIV=28
    MOD=29
    NOT=30
    AND=31
    OR=32
    DOT=33
    LSB=34
    RSB=35
    COLON=36
    VAL=37
    VAR=38
    CONSTRUCTOR=39
    DESTRUCTOR=40
    BREAK=41
    CONTINUE=42
    IF=43
    ELSEIF=44
    ELSE=45
    FOREACH=46
    TRUE=47
    FALSE=48
    ARRAY=49
    INT=50
    FLOAT=51
    BOOLEAN=52
    STRING=53
    NULL=54
    NEW=55
    IN=56
    BY=57
    RETURN=58
    COMMENT=59
    SID=60
    ID=61
    WS=62
    ILLEGAL_ESCAPE=63
    UNCLOSE_STRING=64
    ERROR_TOKEN=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.classdecls()
            self.state = 105
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classdecl(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclContext,0)


        def classdecls(self):
            return self.getTypedRuleContext(D96Parser.ClassdeclsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecls

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecls" ):
                return visitor.visitClassdecls(self)
            else:
                return visitor.visitChildren(self)




    def classdecls(self):

        localctx = D96Parser.ClassdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_classdecls)
        try:
            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self.classdecl()
                self.state = 108
                self.classdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.classdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LC(self):
            return self.getToken(D96Parser.LC, 0)

        def RC(self):
            return self.getToken(D96Parser.RC, 0)

        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def superclass(self):
            return self.getTypedRuleContext(D96Parser.SuperclassContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_classdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassdecl" ):
                return visitor.visitClassdecl(self)
            else:
                return visitor.visitChildren(self)




    def classdecl(self):

        localctx = D96Parser.ClassdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.CLASS)
            self.state = 114
            self.match(D96Parser.ID)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 115
                self.superclass()


            self.state = 118
            self.match(D96Parser.LC)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR, D96Parser.CONSTRUCTOR, D96Parser.DESTRUCTOR, D96Parser.SID, D96Parser.ID]:
                self.state = 119
                self.memberlist()
                pass
            elif token in [D96Parser.RC]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 123
            self.match(D96Parser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperclassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_superclass

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuperclass" ):
                return visitor.visitSuperclass(self)
            else:
                return visitor.visitChildren(self)




    def superclass(self):

        localctx = D96Parser.SuperclassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_superclass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(D96Parser.COLON)
            self.state = 126
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def member(self):
            return self.getTypedRuleContext(D96Parser.MemberContext,0)


        def memberlist(self):
            return self.getTypedRuleContext(D96Parser.MemberlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_memberlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberlist" ):
                return visitor.visitMemberlist(self)
            else:
                return visitor.visitChildren(self)




    def memberlist(self):

        localctx = D96Parser.MemberlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_memberlist)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 128
                self.member()
                self.state = 129
                self.memberlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 131
                self.member()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributedecl(self):
            return self.getTypedRuleContext(D96Parser.AttributedeclContext,0)


        def methoddecl(self):
            return self.getTypedRuleContext(D96Parser.MethoddeclContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember" ):
                return visitor.visitMember(self)
            else:
                return visitor.visitChildren(self)




    def member(self):

        localctx = D96Parser.MemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_member)
        try:
            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.attributedecl()
                pass
            elif token in [D96Parser.SID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.methoddecl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.constructor()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 137
                self.destructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(D96Parser.VardeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attributedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttributedecl" ):
                return visitor.visitAttributedecl(self)
            else:
                return visitor.visitChildren(self)




    def attributedecl(self):

        localctx = D96Parser.AttributedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attributedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.vardecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def idnamelist(self):
            return self.getTypedRuleContext(D96Parser.IdnamelistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = D96Parser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 143
                self.idname()
                self.state = 144
                self.varlist()
                self.state = 145
                self.value()
                self.state = 146
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                self.idnamelist()
                self.state = 150
                self.match(D96Parser.COLON)
                self.state = 151
                self.typename()
                self.state = 152
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarlist" ):
                return visitor.visitVarlist(self)
            else:
                return visitor.visitChildren(self)




    def varlist(self):

        localctx = D96Parser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varlist)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.match(D96Parser.COMMA)
                self.state = 157
                self.idname()
                self.state = 158
                self.varlist()
                self.state = 159
                self.value()
                self.state = 160
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.match(D96Parser.COLON)
                self.state = 163
                self.typename()
                self.state = 164
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdnamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idnamelist(self):
            return self.getTypedRuleContext(D96Parser.IdnamelistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idnamelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdnamelist" ):
                return visitor.visitIdnamelist(self)
            else:
                return visitor.visitChildren(self)




    def idnamelist(self):

        localctx = D96Parser.IdnamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idnamelist)
        try:
            self.state = 173
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.idname()
                self.state = 169
                self.match(D96Parser.COMMA)
                self.state = 170
                self.idnamelist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.idname()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypenameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def arraytypedecl(self):
            return self.getTypedRuleContext(D96Parser.ArraytypedeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typename

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypename" ):
                return visitor.visitTypename(self)
            else:
                return visitor.visitChildren(self)




    def typename(self):

        localctx = D96Parser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_typename)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 179
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 180
                self.arraytypedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = D96Parser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idname

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdname" ):
                return visitor.visitIdname(self)
            else:
                return visitor.visitChildren(self)




    def idname(self):

        localctx = D96Parser.IdnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_idname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==D96Parser.SID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idname(self):
            return self.getTypedRuleContext(D96Parser.IdnameContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methoddecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




    def methoddecl(self):

        localctx = D96Parser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_methoddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.idname()
            self.state = 188
            self.match(D96Parser.LB)
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 189
                self.paralist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 193
            self.match(D96Parser.RB)
            self.state = 194
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParalistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_paralist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParalist" ):
                return visitor.visitParalist(self)
            else:
                return visitor.visitChildren(self)




    def paralist(self):

        localctx = D96Parser.ParalistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paralist)
        try:
            self.state = 206
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.idlist()
                self.state = 197
                self.match(D96Parser.COLON)
                self.state = 198
                self.typename()
                self.state = 199
                self.match(D96Parser.SEMI)
                self.state = 200
                self.paralist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.idlist()
                self.state = 203
                self.match(D96Parser.COLON)
                self.state = 204
                self.typename()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def paralist(self):
            return self.getTypedRuleContext(D96Parser.ParalistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 209
            self.match(D96Parser.LB)
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.state = 210
                self.paralist()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 214
            self.match(D96Parser.RB)
            self.state = 215
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(D96Parser.DESTRUCTOR)
            self.state = 218
            self.match(D96Parser.LB)
            self.state = 219
            self.match(D96Parser.RB)
            self.state = 220
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def varliststmt(self):
            return self.getTypedRuleContext(D96Parser.VarliststmtContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_vardeclStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardeclStatement" ):
                return visitor.visitVardeclStatement(self)
            else:
                return visitor.visitChildren(self)




    def vardeclStatement(self):

        localctx = D96Parser.VardeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_vardeclStatement)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.match(D96Parser.ID)
                self.state = 224
                self.varliststmt()
                self.state = 225
                self.value()
                self.state = 226
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.idlist()
                self.state = 230
                self.match(D96Parser.COLON)
                self.state = 231
                self.typename()
                self.state = 232
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarliststmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def varlist(self):
            return self.getTypedRuleContext(D96Parser.VarlistContext,0)


        def value(self):
            return self.getTypedRuleContext(D96Parser.ValueContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def typename(self):
            return self.getTypedRuleContext(D96Parser.TypenameContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_varliststmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarliststmt" ):
                return visitor.visitVarliststmt(self)
            else:
                return visitor.visitChildren(self)




    def varliststmt(self):

        localctx = D96Parser.VarliststmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_varliststmt)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(D96Parser.COMMA)
                self.state = 237
                self.match(D96Parser.ID)
                self.state = 238
                self.varlist()
                self.state = 239
                self.value()
                self.state = 240
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.match(D96Parser.COLON)
                self.state = 243
                self.typename()
                self.state = 244
                self.match(D96Parser.ASSIGN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def idlist(self):
            return self.getTypedRuleContext(D96Parser.IdlistContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = D96Parser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_idlist)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.match(D96Parser.ID)
                self.state = 249
                self.match(D96Parser.COMMA)
                self.state = 250
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(D96Parser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignvar(self):
            return self.getTypedRuleContext(D96Parser.AssignvarContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = D96Parser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.assignvar()
            self.state = 255
            self.match(D96Parser.ASSIGN)
            self.state = 256
            self.expression()
            self.state = 257
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def expression8(self):
            return self.getTypedRuleContext(D96Parser.Expression8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def expAssignVar(self):
            return self.getTypedRuleContext(D96Parser.ExpAssignVarContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assignvar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignvar" ):
                return visitor.visitAssignvar(self)
            else:
                return visitor.visitChildren(self)




    def assignvar(self):

        localctx = D96Parser.AssignvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignvar)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.expression8(0)
                self.state = 261
                self.match(D96Parser.DOT)
                self.state = 262
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 264
                self.match(D96Parser.ID)
                self.state = 265
                self.match(D96Parser.DOUBLECOLON)
                self.state = 266
                self.match(D96Parser.SID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.expAssignVar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpAssignVarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7b(self):
            return self.getTypedRuleContext(D96Parser.Expression7bContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expAssignVar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpAssignVar" ):
                return visitor.visitExpAssignVar(self)
            else:
                return visitor.visitChildren(self)




    def expAssignVar(self):

        localctx = D96Parser.ExpAssignVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expAssignVar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.expression7b(0)
            self.state = 271
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elsePart(self):
            return self.getTypedRuleContext(D96Parser.ElsePartContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_ifStmtatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmtatement" ):
                return visitor.visitIfStmtatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStmtatement(self):

        localctx = D96Parser.IfStmtatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ifStmtatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(D96Parser.IF)
            self.state = 274
            self.match(D96Parser.LB)
            self.state = 275
            self.expression()
            self.state = 276
            self.match(D96Parser.RB)
            self.state = 277
            self.block_stmt()
            self.state = 278
            self.elsePart()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsePartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def elsePart(self):
            return self.getTypedRuleContext(D96Parser.ElsePartContext,0)


        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_elsePart

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsePart" ):
                return visitor.visitElsePart(self)
            else:
                return visitor.visitChildren(self)




    def elsePart(self):

        localctx = D96Parser.ElsePartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elsePart)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(D96Parser.ELSEIF)
                self.state = 281
                self.match(D96Parser.LB)
                self.state = 282
                self.expression()
                self.state = 283
                self.match(D96Parser.RB)
                self.state = 284
                self.block_stmt()
                self.state = 285
                self.elsePart()
                pass
            elif token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.match(D96Parser.ELSE)
                self.state = 288
                self.block_stmt()
                pass
            elif token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LC, D96Parser.RC, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.RETURN, D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpressionContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpressionContext,i)


        def DOUBLEDOT(self):
            return self.getToken(D96Parser.DOUBLEDOT, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forinStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinStatement" ):
                return visitor.visitForinStatement(self)
            else:
                return visitor.visitChildren(self)




    def forinStatement(self):

        localctx = D96Parser.ForinStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_forinStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.FOREACH)
            self.state = 293
            self.match(D96Parser.LB)
            self.state = 294
            self.match(D96Parser.ID)
            self.state = 295
            self.match(D96Parser.IN)
            self.state = 296
            self.expression()
            self.state = 297
            self.match(D96Parser.DOUBLEDOT)
            self.state = 298
            self.expression()
            self.state = 301
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 299
                self.match(D96Parser.BY)
                self.state = 300
                self.expression()


            self.state = 303
            self.match(D96Parser.RB)
            self.state = 304
            self.block_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = D96Parser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(D96Parser.BREAK)
            self.state = 307
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = D96Parser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(D96Parser.CONTINUE)
            self.state = 310
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = D96Parser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.RETURN)
            self.state = 315
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                self.state = 313
                self.expression()
                pass
            elif token in [D96Parser.SEMI]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 317
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodInvoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_methodInvoStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodInvoStatement" ):
                return visitor.visitMethodInvoStatement(self)
            else:
                return visitor.visitChildren(self)




    def methodInvoStatement(self):

        localctx = D96Parser.MethodInvoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_methodInvoStatement)
        try:
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.expression()
                self.state = 320
                self.match(D96Parser.DOT)
                self.state = 321
                self.match(D96Parser.ID)
                self.state = 322
                self.match(D96Parser.LB)
                self.state = 325
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                    self.state = 323
                    self.listOfExpressions()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 327
                self.match(D96Parser.RB)
                self.state = 328
                self.match(D96Parser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(D96Parser.ID)
                self.state = 331
                self.match(D96Parser.DOUBLECOLON)
                self.state = 332
                self.match(D96Parser.SID)
                self.state = 333
                self.match(D96Parser.LB)
                self.state = 336
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                    self.state = 334
                    self.listOfExpressions()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 338
                self.match(D96Parser.RB)
                self.state = 339
                self.match(D96Parser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LC(self):
            return self.getToken(D96Parser.LC, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def RC(self):
            return self.getToken(D96Parser.RC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_stmt" ):
                return visitor.visitBlock_stmt(self)
            else:
                return visitor.visitChildren(self)




    def block_stmt(self):

        localctx = D96Parser.Block_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_block_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(D96Parser.LC)
            self.state = 343
            self.statements()
            self.state = 344
            self.match(D96Parser.RC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_statements)
        try:
            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LC, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.VAL, D96Parser.VAR, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.RETURN, D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.statement()
                self.state = 347
                self.statements()
                pass
            elif token in [D96Parser.RC]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardeclStatement(self):
            return self.getTypedRuleContext(D96Parser.VardeclStatementContext,0)


        def arraytypedecl(self):
            return self.getTypedRuleContext(D96Parser.ArraytypedeclContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(D96Parser.AssignStatementContext,0)


        def ifStmtatement(self):
            return self.getTypedRuleContext(D96Parser.IfStmtatementContext,0)


        def forinStatement(self):
            return self.getTypedRuleContext(D96Parser.ForinStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(D96Parser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(D96Parser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(D96Parser.ReturnStatementContext,0)


        def methodInvoStatement(self):
            return self.getTypedRuleContext(D96Parser.MethodInvoStatementContext,0)


        def block_stmt(self):
            return self.getTypedRuleContext(D96Parser.Block_stmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_statement)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.vardeclStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.arraytypedecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 354
                self.assignStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 355
                self.ifStmtatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 356
                self.forinStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 357
                self.breakStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 358
                self.continueStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 359
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 360
                self.methodInvoStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 361
                self.block_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expression1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expression1Context,i)


        def STREQUAL(self):
            return self.getToken(D96Parser.STREQUAL, 0)

        def STRCAT(self):
            return self.getToken(D96Parser.STRCAT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = D96Parser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.expression1()
                self.state = 365
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUAL or _la==D96Parser.STRCAT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expression2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(D96Parser.NOTEQUAL, 0)

        def SMALLER(self):
            return self.getToken(D96Parser.SMALLER, 0)

        def LARGE(self):
            return self.getToken(D96Parser.LARGE, 0)

        def SMALLOREQUAL(self):
            return self.getToken(D96Parser.SMALLOREQUAL, 0)

        def LARGEOREQUAL(self):
            return self.getToken(D96Parser.LARGEOREQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = D96Parser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.expression2(0)
                self.state = 372
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOTEQUAL) | (1 << D96Parser.SMALLOREQUAL) | (1 << D96Parser.LARGEOREQUAL) | (1 << D96Parser.LARGE) | (1 << D96Parser.SMALLER))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 373
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(D96Parser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(D96Parser.Expression2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 386
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 381
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 382
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 383
                    self.expression3(0) 
                self.state = 388
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(D96Parser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(D96Parser.Expression3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 397
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 392
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 393
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 394
                    self.expression4(0) 
                self.state = 399
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(D96Parser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(D96Parser.Expression4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 408
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 403
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 404
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 405
                    self.expression5() 
                self.state = 410
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(D96Parser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(D96Parser.Expression6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = D96Parser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expression5)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.match(D96Parser.NOT)
                self.state = 412
                self.expression5()
                pass
            elif token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expression6(self):
            return self.getTypedRuleContext(D96Parser.Expression6Context,0)


        def expression7a(self):
            return self.getTypedRuleContext(D96Parser.Expression7aContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = D96Parser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expression6)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(D96Parser.SUB)
                self.state = 417
                self.expression6()
                pass
            elif token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
                self.expression7a()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7aContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7b(self):
            return self.getTypedRuleContext(D96Parser.Expression7bContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression7a

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7a" ):
                return visitor.visitExpression7a(self)
            else:
                return visitor.visitChildren(self)




    def expression7a(self):

        localctx = D96Parser.Expression7aContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expression7a)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.expression7b(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7bContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(D96Parser.Expression8Context,0)


        def expression7b(self):
            return self.getTypedRuleContext(D96Parser.Expression7bContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression7b

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7b" ):
                return visitor.visitExpression7b(self)
            else:
                return visitor.visitChildren(self)



    def expression7b(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression7bContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expression7b, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.expression8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expression7bContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression7b)
                    self.state = 426
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 427
                    self.index_operators() 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_index_operators)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(D96Parser.LSB)
            self.state = 434
            self.expression()
            self.state = 435
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression9(self):
            return self.getTypedRuleContext(D96Parser.Expression9Context,0)


        def expression8(self):
            return self.getTypedRuleContext(D96Parser.Expression8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)



    def expression8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expression8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expression8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.expression9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 452
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Expression8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                        self.state = 440
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 441
                        self.match(D96Parser.DOT)
                        self.state = 442
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Expression8Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression8)
                        self.state = 443
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 444
                        self.match(D96Parser.DOT)
                        self.state = 445
                        self.match(D96Parser.ID)
                        self.state = 446
                        self.match(D96Parser.LB)
                        self.state = 449
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                            self.state = 447
                            self.listOfExpressions()
                            pass
                        elif token in [D96Parser.RB]:
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 451
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOUBLECOLON(self):
            return self.getToken(D96Parser.DOUBLECOLON, 0)

        def SID(self):
            return self.getToken(D96Parser.SID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def expression10(self):
            return self.getTypedRuleContext(D96Parser.Expression10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = D96Parser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expression9)
        try:
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(D96Parser.ID)
                self.state = 458
                self.match(D96Parser.DOUBLECOLON)
                self.state = 459
                self.match(D96Parser.SID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.match(D96Parser.ID)
                self.state = 461
                self.match(D96Parser.DOUBLECOLON)
                self.state = 462
                self.match(D96Parser.SID)
                self.state = 463
                self.match(D96Parser.LB)
                self.state = 466
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                    self.state = 464
                    self.listOfExpressions()
                    pass
                elif token in [D96Parser.RB]:
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 468
                self.match(D96Parser.RB)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.expression10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def objectCreate(self):
            return self.getTypedRuleContext(D96Parser.ObjectCreateContext,0)


        def expression11(self):
            return self.getTypedRuleContext(D96Parser.Expression11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)




    def expression10(self):

        localctx = D96Parser.Expression10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expression10)
        try:
            self.state = 474
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.objectCreate()
                pass
            elif token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.ARRAY, D96Parser.NULL, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.expression11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectCreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_objectCreate

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObjectCreate" ):
                return visitor.visitObjectCreate(self)
            else:
                return visitor.visitChildren(self)




    def objectCreate(self):

        localctx = D96Parser.ObjectCreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_objectCreate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(D96Parser.NEW)
            self.state = 477
            self.match(D96Parser.ID)
            self.state = 478
            self.match(D96Parser.LB)
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                self.state = 479
                self.listOfExpressions()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 483
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOfExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_listOfExpressions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListOfExpressions" ):
                return visitor.visitListOfExpressions(self)
            else:
                return visitor.visitChildren(self)




    def listOfExpressions(self):

        localctx = D96Parser.ListOfExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_listOfExpressions)
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.expression()
                self.state = 486
                self.match(D96Parser.COMMA)
                self.state = 487
                self.listOfExpressions()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def INTLIT0(self):
            return self.getToken(D96Parser.INTLIT0, 0)

        def INTLIT1(self):
            return self.getToken(D96Parser.INTLIT1, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def arrayofvalue(self):
            return self.getTypedRuleContext(D96Parser.ArrayofvalueContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expression(self):
            return self.getTypedRuleContext(D96Parser.ExpressionContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expression11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)




    def expression11(self):

        localctx = D96Parser.Expression11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expression11)
        self._la = 0 # Token type
        try:
            self.state = 504
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.INTLIT1, D96Parser.INTLIT0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                _la = self._input.LA(1)
                if not(_la==D96Parser.INTLIT1 or _la==D96Parser.INTLIT0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 496
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 497
                self.arrayofvalue()
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 7)
                self.state = 498
                self.match(D96Parser.LB)
                self.state = 499
                self.expression()
                self.state = 500
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 8)
                self.state = 502
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.NULL]:
                self.enterOuterAlt(localctx, 9)
                self.state = 503
                self.match(D96Parser.NULL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def typenamearray(self):
            return self.getTypedRuleContext(D96Parser.TypenamearrayContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT1(self):
            return self.getToken(D96Parser.INTLIT1, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_arraytypedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytypedecl" ):
                return visitor.visitArraytypedecl(self)
            else:
                return visitor.visitChildren(self)




    def arraytypedecl(self):

        localctx = D96Parser.ArraytypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_arraytypedecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.match(D96Parser.ARRAY)
            self.state = 507
            self.match(D96Parser.LSB)
            self.state = 508
            self.typenamearray()
            self.state = 509
            self.match(D96Parser.COMMA)
            self.state = 510
            self.match(D96Parser.INTLIT1)
            self.state = 511
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypenamearrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def arraytypedecl(self):
            return self.getTypedRuleContext(D96Parser.ArraytypedeclContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_typenamearray

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypenamearray" ):
                return visitor.visitTypenamearray(self)
            else:
                return visitor.visitChildren(self)




    def typenamearray(self):

        localctx = D96Parser.TypenamearrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_typenamearray)
        try:
            self.state = 518
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 515
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 516
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 517
                self.arraytypedecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayofvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def listOfExpressions(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpressionsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_arrayofvalue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayofvalue" ):
                return visitor.visitArrayofvalue(self)
            else:
                return visitor.visitChildren(self)




    def arrayofvalue(self):

        localctx = D96Parser.ArrayofvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_arrayofvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(D96Parser.ARRAY)
            self.state = 521
            self.match(D96Parser.LB)
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT1, D96Parser.INTLIT0, D96Parser.FLOATLIT, D96Parser.STRINGLIT, D96Parser.BOOLLIT, D96Parser.SELF, D96Parser.LB, D96Parser.SUB, D96Parser.NOT, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.ID]:
                self.state = 522
                self.listOfExpressions()
                pass
            elif token in [D96Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 526
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.expression2_sempred
        self._predicates[36] = self.expression3_sempred
        self._predicates[37] = self.expression4_sempred
        self._predicates[41] = self.expression7b_sempred
        self._predicates[43] = self.expression8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expression7b_sempred(self, localctx:Expression7bContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expression8_sempred(self, localctx:Expression8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




