%(f)
%n=10000
function y2=rev3(n)
d_f=1:n;
for i=1:n
    t4=rand*13+7;
    A4=normrnd(1500,500);
    d_f(i)=fminbnd(@foo,0,0.8);
end
    function y=foo(d_3)
        p_s4=t4;
        p_p4=d_3*t4;
        v_s4=3+0.9*t4+0.003*A4-p_s4;
        v_p4=1.5+0.7*t4+0.001*A4-p_p4;
        y=-(p_s4*exp(v_s4/2)+p_p4*exp(v_p4/2))/(1+exp(v_s4/2)+exp(v_p4/2));
    end
y2=sum(d_f)/n;
end