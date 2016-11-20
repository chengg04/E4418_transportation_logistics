%2.b
%input the graph with matrix
A=csvread('nyc_roads.csv');
G=biograph(A);
%find out whether it is strongly connected
[num_c, com_nodes]=conncomp(G);
%find the shortest path
lst_bound=double(logical(A));
cvx_begin
    variable x(10,10)
    minimize (sum(sum(A.*x)))
    subject to
        sum(x)-sum(x,2)'== zeros(1,10);
        lst_bound.* x >=lst_bound;
        (ones(10,10)-lst_bound).* x == zeros(10,10);
cvx_end       

%3.c
cvx_begin
    variables x(10,10) y(10,10) z;
    minimize z
    subject to
        lst_bound.*x+lst_bound.*y>=lst_bound;
        sum(sum(A.*x))<=z;
        sum(sum(A.*y))<=z;
        lst_bound.*x>=zeros(10,10);
        lst_bound.*y>=zeros(10,10);
        sum(x)-sum(x,2)'==zeros(1,10);
        sum(y)-sum(y,2)'==zeros(1,10);
        (ones(10,10)-lst_bound).* x == zeros(10,10);
        (ones(10,10)-lst_bound).* y == zeros(10,10);
cvx_end
