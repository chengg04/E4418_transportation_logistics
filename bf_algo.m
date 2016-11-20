function [path, total_cost]=bf_algo(cost,step,node,initial)
k=1;
v=1:node;
for i=v
    d(1,i)=inf;
end;
d(1,initial)=0;
for i=v
    p(1,i)=0;
end
while k<=step
    k=k+1;
    for i=v
        temp=d(k-1,i);
        for j=v %from nodes
            if d(k-1,j)+cost(j,i)<=temp
                temp=d(k-1,j)+cost(j,i);
                d(k,i)=temp;
                p(k,i)=j;
            end
        end
    end
end
path=p;
total_cost=d;
end
                
                
                
                
                
                
                
                
                
                
                
