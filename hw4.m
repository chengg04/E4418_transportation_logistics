%c
ps_op=fminbnd(@rev1,0,18);
%p_s can't be more than 18 or the utility would be negative

%d
A=[-0.8,1];
b=0;
Aeq=[];
beq=[];
psp_op=fmincon(@rev2,[0,0],A,b,Aeq,beq,[0,0],[18,9.5]);

%e
n=10000;
rev=1:n;
for i=1:n
    t=rand*13+7;
    A=normrnd(1500,500);
    p_s3=t;
    p_p3=0.8*t;
    v_s=3+0.003*A-0.1*t;
    v_p=1.5+0.001*A;
    rev(i)=(p_s3*exp(v_s/2)+p_p3*exp(v_p/2))/(1+exp(v_s/2)+exp(v_p/2));
end
rev_e=sum(rev)/n;

%g
%This function runs very slowly, so we only do 100 simulations
revg_op=rev2(rev4(100));

%h
revf_op=rev2(rev5(100));













