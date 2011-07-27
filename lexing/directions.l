%{
#include <stdio.h>
#include "y.tab.h"
%}

%%
n return NORTH;
e return EAST;
s return SOUTH;
w return WEST;
\n return END;
%%
