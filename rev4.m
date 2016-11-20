%(g)
%where rev4 is
function y2=rev4(n)
p_sg=1:n;
p_pg=1:n;
for i=1:n;
    t4=rand*13+7;
    A4=normrnd(1500,500);
    ub=[3+0.9*t4+0.003*A4,1.5+0.7*t4+0.001*A4];
    y3=fmincon(@foo2,[0,0],[-0.8,1],0,[],[],[0,0],ub);
    p_sg(i)=y3(1);
    p_pg(i)=y3(2);
end
    function y=foo2(p_f)
        v_s4=3+0.9*t4+0.003*A4-p_f(1);
        v_p4=1.5+0.7*t4+0.001*A4-p_f(2);
        y=-(p_f(1)*exp(v_s4/2)+p_f(2)*exp(v_p4/2))/(1+exp(v_s4/2)+exp(v_p4/2));
    end
y2=[sum(p_sg)/n,sum(p_pg)/n];
end