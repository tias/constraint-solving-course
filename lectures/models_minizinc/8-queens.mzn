include "globals.mzn"; % ensures that lines 4 to 6 are understood
int: n = 8; % the given number of queens
array[1..n] of var 1..n: Row; % Row[c] = the unknown row of the queen in column c;      enforces that all queens are in distinct columns
constraint all_different( Row                  ); % distinct rows
constraint all_different([Row[c]+c | c in 1..n]); % distinct   up-dia.
constraint all_different([Row[c]-c | c in 1..n]); % distinct down-dia.
solve satisfy; % solve to satisfaction of all the constraints
output [show(Row)]; % pretty-printing of solutions