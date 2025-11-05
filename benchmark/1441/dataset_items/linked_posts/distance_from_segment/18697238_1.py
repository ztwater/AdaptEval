local P1 = {x = 0, y = 0}
local P2 = {x = 10, y = 10}
local line = { P1, P2 }
local P3 = {x = 7, y = 15}
print(distPointToLine( line, P3 ))  -- prints 5.6568542494924
print(distPointToSegment( line, P3 )) -- prints false
