array[Cities,Cities] of float: Distance;  % instance data
array[Cities] of var Cities: Next; % travel from c to Next[c]
solve minimize sum(c in Cities)(Distance[c,@Next[c]@]);
constraint circuit(Next);
constraint ...;            % side constraints, if any
