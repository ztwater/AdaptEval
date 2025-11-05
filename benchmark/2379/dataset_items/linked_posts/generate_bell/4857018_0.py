permutate(As,[B|Cs]) :- select(B, As, Bs), permutate(Bs, Cs).
select(A, [A|As], As).
select(A, [B|Bs], [B|Cs]) :- select(A, Bs, Cs).

?- permutate([a,b,c], P).
