function [path, cost]=bf_algo(cost,step,node,initial)
k=1;
v=1:node;
for i=v
    d(1,i)=inf;
end;
d(1,initial)=0;
for i=v
    p(1,i)=0;
end
while k<step
    k=k+1;
    for i=v
        for j=v %from nodes
            if d(k-1,j)+c(j,i)<d(k-1,i)
                d(k,i)=d(k-1,j)+c(j,i);
            else
                d(k,i)=d(k,i);
            end
            p(k,i)=j;
        end
    end
                
                
                
                
                
                
                
                
                
                
                
