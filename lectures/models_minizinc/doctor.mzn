include "globals.mzn";
set of int: Days;  % d mod 7 = 1 iff d is a Monday
enum Doctors;
enum ShiftTypes = {appt, call, oper, none};
% Roster[i,j] = shift type of Dr i on day j:
array[Doctors,Days] of var ShiftTypes: Roster;
solve minimize ...;  % plug in an objective function
constraint forall(d in Days)(count(Roster[..,d],call) = 1);
constraint forall(d in Days where d mod 7 in 1..5)       (count(Roster[..,d],oper) <= 2);
constraint count(Roster,oper) >= 7;
constraint count(Roster,appt) >= 4;
constraint forall(d in Doctors)                          (regular(Roster[d,..],"((oper none) | appt | call | none)*"));
...  % other constraints