procedure permutate(var numbers: array [1..100] of integer; size: integer; 
                    var pos, dir: integer)
begin
  if pos >= size then
  begin
     dir = -1 * dir;
     swap(numbers, 1, 2);
  end
  else if pos < 1 then 
  begin
     dir = -1 * dir;
     swap(numbers, size-1, size);
  end
  else
  begin
     swap(numbers, pos, pos+1);
  end;
  pos = pos + dir;
end;

begin
    var a, b: integer;
    a = 1; b = 1;
    while true do
    begin
       permutate(A, 5, a, b);
       printArray(A, 5);
    end;
end.
