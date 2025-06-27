include "globals.mzn";
enum Varieties; enum Blocks;
int: blockSize; int: sampleSize; int: balance;
array[Varieties,Blocks] of var 0..1: BIBD; % BIBD[v,b]=1 iff v is in b
solve satisfy;
constraint forall(b in Blocks)   (blockSize  = count(BIBD[..,b], 1));
constraint forall(v in Varieties)(sampleSize = count(BIBD[v,..], 1));
constraint forall(v, w in Varieties where v < w)              (balance = count([BIBD[v,b]@+@BIBD[w,b] | b in Blocks], @2@));