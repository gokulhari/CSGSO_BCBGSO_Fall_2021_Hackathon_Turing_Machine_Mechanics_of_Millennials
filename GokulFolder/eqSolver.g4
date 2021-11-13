grammar eqSolver;

program
    : statement* EOF
    ;

statement
	: expr '=' expr NEWLINE
    ;

expr
    : expr ('+' | '-') expr # building_exp
    | Identifier # iden_exp
	| Number # num_exp
	| '(' expr ')' # paran_exp
	;

Identifier: Letter (Number) | (Number) Letter;

Number: Integer | Float;

fragment Integer: Sign? NonzeroDigit Digit* | '0';

fragment Float: Sign? Digit+ '.' Digit+;

fragment Sign: [+-];

fragment Digit: [0-9];

fragment NonzeroDigit: [1-9];

fragment Letter: [a-zA-Z_];

Comment: '#' ~[\r\n]* -> skip;
WS: [ \t\r]+ -> skip;
NEWLINE: '\r'? '\n';