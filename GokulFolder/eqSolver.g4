grammar eqSolver;

// Rules:

program
    : statement* EOF
    ;

statement
	: expr '=' expr NEWLINE
    ;

expr
    : Identifier
	| '(' expr ')'
	| Number
	| expr ('+' | '-') expr
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