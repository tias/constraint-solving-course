include "globals.mzn";
int: nbrBlocks; int: nbrVarieties;
set of int: Blocks = 1..nbrBlocks;
set of int: Varieties = 1..nbrVarieties;
int: blockSize; int: sampleSize; int: balance;
constraint assert(nbrBlocks = (balance*nbrVarieties*(nbrVarieties-1)) div (blockSize*(blockSize-1)), "Wrong number of blocks");
constraint assert(sampleSize = (balance*(nbrVarieties-1)) div (blockSize-1), "Wrong sample size");
array[Varieties,Blocks] of var 0..1: BIBD; % BIBD[v,b]=1 iff v is in b
constraint forall(b in Blocks)                      (blockSize =  count(BIBD[..,b], 1));
constraint forall(v in Varieties)                   (sampleSize = count(BIBD[v,..], 1));
constraint forall(v, w in Varieties where v < w)    (balance =    count([BIBD[v,b]+BIBD[w,b] | b in Blocks], 2));
constraint symmetry_breaking_constraint(            forall(v in Varieties diff {max(Varieties)})( lex_greater(BIBD[v,..],BIBD[v+1,..])));
constraint symmetry_breaking_constraint(            forall(b in Blocks diff {max(Blocks)})( lex_greatereq(BIBD[..,b],BIBD[..,b+1])));
solve::int_search(BIBD,input_order,indomain_max) satisfy;
output ["BIBD with nbrBlocks = \(nbrBlocks), nbrVarieties = \(nbrVarieties), blockSize = \(blockSize), sampleSize = \(sampleSize), and balance= \(balance):\n"] ++ [if b > nbrBlocks then "\n" else show(BIBD[v,b]) endif | v in Varieties, b in 1..(nbrBlocks+1)];