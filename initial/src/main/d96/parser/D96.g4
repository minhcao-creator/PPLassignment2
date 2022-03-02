// 1813061
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// phần PARSER phần khai báo class
program: classdecls EOF;

classdecls: classdecl classdecls | classdecl;

classdecl: CLASS ID superclass? LC (memberlist |) RC;

superclass: COLON ID;

memberlist: member memberlist | member; // boby of class

member: attributedecl | methoddecl | constructor | destructor;
//hết phần khai báo class

//khai báo attribute
attributedecl: vardecl; // có 2 loại khai báo biến là var và val

vardecl: (VAR | VAL) idname varlist value SEMI // có dấu ; SEMI, thiếu khai báo array
	| (VAR | VAL) idnamelist COLON typename SEMI;

varlist:
	COMMA idname varlist value COMMA
	| COLON typename ASSIGN;

idnamelist: idname COMMA idnamelist | idname; // có biến tĩnh

typename:
	INT
	| FLOAT
	| BOOLEAN
	| STRING
	| ID
	| arraytypedecl; // ID là tên của class

value: expression; // exp chưa làm, thiếu array

idname: SID | ID; // có biến tĩnh 
//hết phần attribute declaration -> VAL pair_list SEMI

// pair_list -> ID pair expression

// pair -> COMMA ID pair expression COMMA | COLON TYPE ASSIGN

//khai báo method
methoddecl: idname LB (paralist |) RB block_stmt;

paralist: idlist COLON typename SEMI paralist | idlist COLON typename;

constructor: CONSTRUCTOR LB (paralist |) RB block_stmt;

destructor: DESTRUCTOR LB RB block_stmt;
//hết phần khai báo method

//phần statements
vardeclStatement: (VAR | VAL) ID varliststmt value SEMI // có dấu ; SEMI, thiếu khai báo array
	| (VAR | VAL) idlist COLON typename SEMI;

varliststmt:
	COMMA ID varlist value COMMA
	| COLON typename ASSIGN;

idlist: ID COMMA idlist | ID;

assignStatement: assignvar ASSIGN expression SEMI;
assignvar:
	ID
	| expression8 DOT ID //instance attribute access a+b.c
	| ID DOUBLECOLON SID
	| expAssignVar;

expAssignVar: expression7b index_operators;
//a::$b[5]
// a.b[5] if statement
ifStmtatement: IF LB expression RB block_stmt elsePart;

elsePart:
	ELSEIF LB expression RB block_stmt elsePart
	| ELSE block_stmt
	|;

// For In statement
forinStatement:
	FOREACH LB ID IN expression DOUBLEDOT expression (
		BY expression
	)? RB block_stmt;
//a[5].foo;

breakStatement: BREAK SEMI;
continueStatement: CONTINUE SEMI;
returnStatement: RETURN (expression |) SEMI;

// Method Invocation statement
methodInvoStatement:
	expression DOT ID LB (listOfExpressions |) RB SEMI //instance method invocation 
	| ID DOUBLECOLON SID LB (listOfExpressions |) RB SEMI; //static method invocation
// Class A { Val $a: Int = 5; foo() { return $a;}} b(){} c(){return self.b();}
block_stmt: LC statements RC;

statements: statement statements |;

statement:
	vardeclStatement
	| arraytypedecl
	| assignStatement
	| ifStmtatement
	| forinStatement
	| breakStatement
	| continueStatement
	| returnStatement
	| methodInvoStatement
	| block_stmt;

//hết phần statements

//a = A.foo(); phần Expressions
expression:
	expression1 (STREQUAL | STRCAT) expression1
	| expression1;

expression1:
	expression2 (
		EQUAL
		| NOTEQUAL
		| SMALLER
		| LARGE
		| SMALLOREQUAL
		| LARGEOREQUAL
	) expression2
	| expression2;

expression2: expression2 (AND | OR) expression3 | expression3;

expression3: expression3 (ADD | SUB) expression4 | expression4;

expression4:
	expression4 (MUL | DIV | MOD) expression5
	| expression5;

expression5: NOT expression5 | expression6;

expression6: SUB expression6 | expression7a;

expression7a: expression7b;

expression7b: expression7b index_operators | expression8;

index_operators: LSB expression RSB;

expression8:
	expression8 DOT ID //instance attribute access
	| expression8 DOT ID LB (listOfExpressions |) RB //instance method invocation 
	| expression9;

expression9:
	ID DOUBLECOLON SID //static attribute access
	| ID DOUBLECOLON SID LB (listOfExpressions |) RB //static method invocation
	| expression10;

expression10: objectCreate | expression11;

objectCreate:
	NEW ID LB (listOfExpressions |) RB; //Object creation

listOfExpressions:
	expression COMMA listOfExpressions
	| expression;

expression11:
	ID
	| (INTLIT0 | INTLIT1)
	| FLOATLIT
	| STRINGLIT
	| BOOLLIT
	| arrayofvalue
	| LB expression RB
	| SELF
	| NULL;

//hết phần Expressions

//phần ARRAY
arraytypedecl:
	ARRAY LSB typenamearray COMMA INTLIT1 RSB; //khai báo array, intlit trừ số 0: chưa làm
typenamearray: INT | FLOAT | BOOLEAN | STRING | arraytypedecl ;
//Array[Int,5] = Array(1,2,3,4,5);
//VAR a:Array[Int,5] = Array(1,2,3,4,5);

arrayofvalue: ARRAY LB (listOfExpressions |) RB; // chưa có ; SEMI
//Array(4,5,6)

DOUBLECOLON: '::';

DOUBLEDOT: '..';

//phần LEXER phần integer literals
fragment DECIMAL: [1-9]+ [0-9]* ('_' [0-9]+)*;

fragment DECIMALZERO: '0';

fragment HEXA: '0' [xX][1-9A-F]+ [0-9A-F]* ('_' [0-9A-F]+)*;

fragment HEXAZERO: '0' [xX]'0';

fragment OCTAL: '0' [1-7]+ [0-7]* ('_' [0-7]+)*;

fragment OCTALZERO: '00';

fragment BINARY: '0' [bB][1]+ [01]* ('_' [01]+)*;

fragment BINARYZERO: '0' [bB]'0';

INTLIT1: (DECIMAL | HEXA | OCTAL | BINARY) {self.text = self.text.replace("_","")};

INTLIT0: DECIMALZERO | HEXAZERO | OCTALZERO | BINARYZERO;

//hết phần integer literals

//phần float literals
fragment EXPON: [Ee] [+-]? [0-9]+;

fragment DECIMALPART: DOT [0-9]*;

FLOATLIT: (
		(DECIMAL | DECIMALZERO) DECIMALPART
		| (DECIMAL | DECIMALZERO) EXPON
		| DECIMALPART EXPON
		| (DECIMAL | DECIMALZERO) DECIMALPART EXPON
	) {self.text = self.text.replace("_","")};
//hết phần float literals

//phần string
fragment CHARACTER: ~( [\r\n\f\b\t"\\]) | ESCAPE | '\'"';

fragment ESCAPE:
	'\\' ('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\');

fragment ILLEGELESCAPE:
	'\\' ~('b' | 'f' | 'r' | 'n' | 't' | '\'' | '\\')?;

fragment DOUBLEQUOTES: '"';

STRINGLIT:
	DOUBLEQUOTES CHARACTER* DOUBLEQUOTES {
    self.text = self.text[1:-1]
};

BOOLLIT: TRUE | FALSE;

CLASS: 'Class';

SELF: 'Self';

LC: '{';

RC: '}';

LB: '(';

RB: ')';

STREQUAL: '==.';

STRCAT: '+.';

EQUAL: '==';

NOTEQUAL: '!=';

SMALLOREQUAL: '<=';

LARGEOREQUAL: '>='; // 

LARGE: '>'; //

SMALLER: '<';

COMMA: ',';

SEMI: ';';

ASSIGN: '=';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

MOD: '%';

NOT: '!';

AND: '&&';

OR: '||';

DOT: '.';

LSB: '['; // Left Square Bracket

RSB: ']'; // Right Square Bracket

COLON: ':';

VAL: 'Val';

VAR: 'Var';

CONSTRUCTOR: 'Constructor';

DESTRUCTOR: 'Destructor';

BREAK: 'Break';

CONTINUE: 'Continue';

IF: 'If';

ELSEIF: 'Elseif';

ELSE: 'Else';

FOREACH: 'Foreach';

TRUE: 'True';

FALSE: 'False';

ARRAY: 'Array';

INT: 'Int';

FLOAT: 'Float';

BOOLEAN: 'Boolean';

STRING: 'String';

NULL: 'Null';

NEW: 'New';

IN: 'In';

BY: 'By';

RETURN: 'Return';

COMMENT: '##' (.)*? '##' -> skip;

SID: '$' [a-zA-Z0-9_]+;

ID: [a-zA-Z_]+ [0-9a-zA-Z_]*; // section 3.3

WS: [ \t\r\n\b\f]+ -> skip; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE:
	'"' CHARACTER* ILLEGELESCAPE {
					y = str(self.text)
					raise IllegalEscape(y[1:])
				};

UNCLOSE_STRING:
	DOUBLEQUOTES CHARACTER* ([\r\n\b\t\f] | EOF) {
				esc = ['\n', '\r', '\b', '\t', '\f']
				content = str(self.text)
				if (content[-1] in esc):
					raise UncloseString(content[1:-1])
				else:
					raise UncloseString(content[1:])
			};

ERROR_TOKEN: . {raise ErrorToken(self.text)};
