function chunks=chunkit(array,num)

index = round(linspace(0,size(array,2),num+1));

chunks = cell(1,num);

for x = 1:num
chunks{x} = array(:,index(x)+1:index(x+1));
end
end
