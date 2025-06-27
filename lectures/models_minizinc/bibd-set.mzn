include "globals.mzn";
enum Varieties; enum Blocks;
int: blockSize; int: sampleSize; int: balance;
array[Varieties] of var set of Blocks: BIBD; % BIBD[v] = blocks for v
solve satisfy;
constraint forall(b in Blocks)                                (blockSize  = sum(v in Varieties)(b in BIBD[v]));
constraint forall(v in Varieties)                             (sampleSize = card(BIBD[v]));
constraint forall(v, w in Varieties where v < w)              (balance    = card(BIBD[v] intersect BIBD[w]));