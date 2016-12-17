rho=csvread('rou.csv',1,1);
a=0.25;
K=300;
C=length(rho);
%rho_m=ones(C,1)-rho;
cvx_begin
    variable X(C);
    expression z(C);
    for k=1:C,
        z(k)=rho(k)^X(k)/(1-rho(k));
    end
    minimize( sum(z));
    subject to
        X>=1;
        sum(X)==K;
cvx_end
