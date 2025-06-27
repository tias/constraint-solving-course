array[Apps] of 0..1000: Salary;  % Salary[a] = cost per job to appl. a
array[Jobs] of var Apps: Worker; % Worker[j] = appl. allocated job j
solve minimize sum(j in Jobs)(Salary[@Worker[j]@]);
constraint ...;       % qualifications, workload, etc