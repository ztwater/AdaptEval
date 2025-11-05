>>> foo.__code__.co_consts[1].co_consts[2]
<code object y at 0x10a5df5d0, file "<stdin>", line 4>
>>> foo.__code__.co_consts[1].co_consts[2].co_cellvars
('x',)
