%where rev2 is
function y=rev2(p)
y=-(p(1)*exp(9-p(1)/2)+p(2)*exp(4.75-p(2)/2))/(1+exp(9-p(1)/2)+exp(4.75-p(2)/2));
end