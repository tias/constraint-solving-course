include "globals.mzn";
int: n; % length of X
enum Alphabet = {s,t};  enum State = {a,b,c,d,e};
array[State,Alphabet] of opt State:            Transition = [| b,c | d,<> | e,<> | <>,b | c,e |];
array[1..n] of var Alphabet: X;
constraint regular(X,Transition,a,{d,e});
constraint regular(X,"s s (t s)* | t s (t | s s)*");
constraint table(X,[| s,s,t,s | t,s,s,s | t,s,t,t |]);
solve satisfy;