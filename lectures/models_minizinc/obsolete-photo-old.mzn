include "globals.mzn";
enum Persons;
int: q; % number of preferences
% Pref[k,1] wants to pay Weight[k] in order to be next to person Pref[k,2]:
array[1..q,1..2] of Persons: Pref;
%% array[1..q] of int: Weight;
% Pos[p] is the position, in left-to-right order, of person p on the photo:
array[Persons] of var 1..card(Persons): Pos;
constraint all_different(Pos); % every person is at a different position on the photo:
%var int: obj = sum(k in 1..q)(
%%  Weight[k]*
%             bool2int(abs(Pos[Pref[k,1]]-Pos[Pref[k,2]])=1));
var int: obj = count([abs(Pos[Pref[k,1]]-Pos[Pref[k,2]]) | k in 1..q],true);
solve maximize obj;
output [show(obj)] ++ [": "] ++ [show(Pos[p]) ++ " " | p in Persons];
% Toy data:
Persons = {A,B,C};
q = 3;
Pref = [|A,B|A,C|B,C|];
%% Weight = [3,  2,  1];