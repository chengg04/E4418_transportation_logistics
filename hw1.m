c=csvread('C.csv');
%1.a
[path1, cost1]=dij_algo(c,20,1);
[path2, cost2]=dij_algo(c,20,11);
[path3, cost3]=dij_algo(c,20,17);
%1.b
[path7,cost7]=bf_algo(c,5,20,1);
[path8,cost8]=bf_algo(c,5,20,11);
[path9,cost9]=bf_algo(c,5,20,17);






