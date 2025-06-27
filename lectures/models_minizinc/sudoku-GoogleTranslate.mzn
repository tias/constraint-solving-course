...  % load the hints
array[1..9,1..9] of var 1..9: Sudoku;
constraint forall(row in 1..9)(all_different(Sudoku[row,..]));
constraint forall(col in 1..9)(all_different(Sudoku[..,col]));
constraint forall(i,j in {0,3,6}) (all_different(Sudoku[i+1..i+3,j+1..j+3]));
solve satisfy;
