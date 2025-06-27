include "globals.mzn";
enum Varieties; enum Blocks;
int: blockSize; int: sampleSize; int: balance;
array[Varieties,Blocks] of var 0..1: BIBD; % BIBD[v,b]=1 iff v is in b
solve satisfy;
constraint forall(b in Blocks)   (blockSize  =   sum(BIBD[..,b]));
constraint forall(v in Varieties)(sampleSize =   sum(BIBD[v,..]));
constraint forall(v, w in Varieties where v < w)              (balance =   sum([BIBD[v,b]*BIBD[w,b] | b in Blocks]));