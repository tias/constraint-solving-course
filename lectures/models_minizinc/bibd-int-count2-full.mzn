include "globals.mzn";
enum Varieties; enum Blocks;
int: blockSize; int: sampleSize; int: balance;
array[Varieties,Blocks] of var 0..1: BIBD; % BIBD[v,b]=1 iff v is in b
solve satisfy;
constraint forall(b in Blocks)   (blockSize  = count(BIBD[..,b], 1));
constraint forall(v in Varieties)(sampleSize = count(BIBD[v,..], 1));
constraint forall(v, w in Varieties where v < w)              (balance = count([BIBD[v,b]@+@BIBD[w,b] | b in Blocks], @2@));
constraint symmetry_breaking_constraint(            forall(v in Varieties diff {max(Varieties)})( lex_greater(BIBD[v,..],BIBD[enum_next(v),..])));
constraint symmetry_breaking_constraint(            forall(b in Blocks diff {max(Blocks)})( lex_greatereq(BIBD[..,b],BIBD[..,enum_next(b)])));
solve::int_search(BIBD,input_order,indomain_max) satisfy;
output [show2d(BIBD)];