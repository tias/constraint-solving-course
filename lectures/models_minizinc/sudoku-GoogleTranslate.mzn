array[1..9,1..9] of 0..9: Given;  % the hints, '0' for empty cells
array[1..9,1..9] of var 1..9: Grid;
constraint forall(row in 1..9) (all_different(Grid[row,..]));
constraint forall(col in 1..9) (all_different(Grid[..,col]));
constraint forall(i,j in {1,4,7}) (all_different(Grid[i..i+2,j..j+2]));
constraint forall(i in 1..9, j in 1..9 where Given[i,j] != 0)       (Grid[i,j] = Given[i,j]);  % enforce the hints
solve satisfy;
