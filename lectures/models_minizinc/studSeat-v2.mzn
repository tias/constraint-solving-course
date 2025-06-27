include "globals.mzn"; % include "gecode.mzn";

int: nStudents = 15; % value of slide T04:05
int: nPgms =      3; % value of slide T04:05
int: nChairs =   20; % value of slide T04:05
constraint assert(nChairs >= nStudents, "There are not enough chairs for the students!");
array[int] of set of int: Tables = [1..4, 5..8, 9..12, 13..16, 17..20]; % value of slide T04:05
% Pgm[s] = the given study programme of student s:
array[1..nStudents] of 1..nPgms: Pgm = [1 + s mod nPgms | s in 1..nStudents]; % made-up values for experiments

set of int: DummyS = {0};  % Advice: also experiment with {nStudents+1} and (nStudents+1)..nChairs
set of int: StudentsAndDummy = 1..nStudents union DummyS;
% Student[c] = the student, possibly dummy, on chair c:
array[1..nChairs] of var StudentsAndDummy: Student;
%constraint value_precede_chain(DummyS,StudentsAndDummy); % partial value symmetry if >1 dummy students
%constraint alldifferent(Student);              % only if  DummyS  = (nStudents+1)..nChairs
constraint alldifferent_except(Student,DummyS); % only if |DummyS| = 1
constraint global_cardinality(Student,set2array(DummyS),[nChairs-nStudents]); % only if |DummyS| = 1
%constraint global_cardinality_low_up_closed(Student, set2array(1..nStudents)++set2array(DummyS), [0 | i in 1..nStudents]++[nChairs-nStudents], [1 | i in 1..nStudents]++[nChairs-nStudents]); % bundled 2 previous constraints for |DummyS|=1

int: dummyP = 0;      % Advice: also experiment with nPgms+1
set of int: PgmsAndDummy = 1..nPgms union {dummyP};
% Programme[c] = the programme of the student on chair c (non-mutually redundant with Student):
array[1..nChairs] of var PgmsAndDummy: Programme;
% 1-way channelling from Student to Programme:
%% option 1, which generates more variables and constraints than the other options:
%constraint forall(c in 1..nChairs)(Programme[c] = if Student[c] in DummyS then dummyP else Pgm[Student[c]] endif);
%% option 2, building a help array independently of the value of DummyS:
%array[StudentsAndDummy] of PgmsAndDummy: PgmDummy = array1d(StudentsAndDummy,[if s in DummyS then dummyP else Pgm[s] endif | s in StudentsAndDummy]);
%constraint forall(c in 1..nChairs)(Programme[c] = PgmDummy[Student[c]]);
%% option 3, based on the choice of DummyS:
constraint forall(c in 1..nChairs)(Programme[c] = array1d(StudentsAndDummy,[dummyP]++Pgm)[Student[c]]);  % for DummyS = {0}
%constraint forall(c in 1..nChairs)(Programme[c] = array1d(StudentsAndDummy,Pgm++[dummyP])[Student[c]]); % for DummyS = {nStudents+1}

% Constraint (1) Each table has students of distinct study programmes:
constraint forall(T in Tables)(alldifferent_except([Programme[c] | c in T],{dummyP}));
% ... % Constraint (2) of slide T04:05
solve
  :: int_search(Student,first_fail,indomain_max) % for DummyS = {0}
% :: int_search(Student,first_fail,indomain_min) % for DummyS = {nStudents+1} or DummyS = (nStudents+1)..nChairs
% maximize ...; % Objective (3) of slide T04:05
  satisfy;