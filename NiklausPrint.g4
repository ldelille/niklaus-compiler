grammar Niklaus;

program : PROGRAM ID ';' declaration? '{' instruction '}';

declaration : VAR ID (',' ID)* ';' ;

assignment : ID EQUAL expr ';' ;

instruction: (write_exp|read_var|condition|assignment|comparison|loop)*;

comparison : expr SIGNE expr;

condition :	IF '(' comparison ')' '{' instruction '}' ELSE '{' instruction '}';

loop : WHILE '(' comparison ')' '{' instruction '}';

read_var 	:	READ ID';' ;

write_exp 	:	WRITE expr';' ;

SIGNE 	:	 '<' | '>' | '<>' | '<='|'>=' |'=';

READ : 'read';
VAR	: 'var';

WRITE 	: 'write';

EQUAL 	:':=';

WHILE 	:'while';

IF	:'if';

ELSE	:'else';

PROGRAM : 'program';

expr : term (ADDOP term)*
    ;

term : factor (MULTOP factor)*
    ;

factor : ID                       # FactorId
       | INT                      # FactorInt
       | '(' expr ')'             # FactorBlock
    ;

INT :  [0-9]+
    ;

COMMENT
    :   '//' ~('\n'|'\r')* '\r'? '\n' -> skip
    ;

WS  :   ( ' '
        | '\t'
        | '\r'
        | '\n'
        ) -> skip
    ;

ADDOP   :   '+' | '-' | 'mod' ;

MULTOP  :   '*' | '/';

ID  :   [a-zA-Z_] [a-zA-Z0-0_]*
    ;
