grammar FourierGrammar;

program: expression EOF;

expression
    : fourierTransform
    | '(' expression ')'
    | expression '+' expression
    | expression '-' expression
    | expression '*' expression
    | expression '/' expression
    | NUMBER
    | COMPLEX_NUMBER
    ;

fourierTransform: 'Fourier' '(' list ')' ;

list: '[' element (',' element)* ']' ;

element: NUMBER | COMPLEX_NUMBER;

NUMBER: ('0'..'9')+ ('.' ('0'..'9')+)?;
COMPLEX_NUMBER: NUMBER 'i';
WS: [ \t\r\n]+ -> skip;
