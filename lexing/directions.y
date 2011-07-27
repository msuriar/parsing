%{
#include <stdio.h>
#include <string.h>

void yyerror(const char *str)
{
  fprintf(stderr,"error: %s\n", str);
}

int yywrap()
{
  return 1;
}

main()
{
  yyparse();
}

%}

%token NORTH EAST SOUTH WEST END

%%

move: /* Empty */
    | NORTH move
    | SOUTH move
    | EAST movew
    | END
    ;

movew: /* empty */
    | NORTH move
    | SOUTH move
    | EAST movew
    | WEST move
    | END
    ;

