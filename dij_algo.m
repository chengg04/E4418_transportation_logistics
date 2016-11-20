function [ path, min_cost ] = dij_algo(cost, node, initial)
%node is the total number of nodes
v=1:node;
s=initial;
d=1:node;
d(initial)=0;
for i=setdiff(v,s)
    d(i)=inf;
end
u=initial;
k=0;
while setdiff(v,s)~=0
    k=k+1;
    temp=inf;
    for i=setdiff(v,s)
        temp_3=inf;
        for j=s
            temp_4=d(j)+cost(j,i);
            if temp_4<temp_3
                temp_3=temp_4;
                p(k,i)=j;
            end
            d(i)=temp_3;
            
        end
        if d(i)<temp
            temp=d(i);
            u=i;
        end
    end
    s=[s u];   
end
min_cost=d;
path=p;
         
end

