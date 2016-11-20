%a
fun3=@(t) ((6*t).^3.*exp(-6*t)/6).*(3 - 3*exp(-3*t));
a3=integral(fun3, 0,inf);

fun2=@(t) (1-(6*t).^2.*exp(-6*t)/2-(6*t).*exp(-6*t)-exp(-6*t)).*(3 - 3*exp(-3*t));
a2=integral(fun2,0,inf);

%b
sum=0;
for i=1:10
    a=3^(i-1)/factorial(i-1)*6^(10-i)/factorial(10-i);
    sum=sum+a;
end
p=sum*exp(-3)*exp(-6);

%4.3
fun4=@(n) 8*(1/(0.5*sqrt(n)-1)*40)+10*n*8;
y4=fminbnd(fun4,0,50);

%4.7
m=10;
sum=1;
for i=1:m
    sum=sum+(3125)^i/factorial(i);
end;
fd=(3125)^m/factorial(m);
f=fd/sum;







    