Clear["Global`*"];
 distance[{start_, end_}, pt_] := 
   Module[{param},
   param = ((pt - start).(end - start))/Norm[end - start]^2; (*parameter. the "."
                                                       here means vector product*)

   Which[
    param < 0, EuclideanDistance[start, pt],                 (*If outside bounds*)
    param > 1, EuclideanDistance[end, pt],
    True, EuclideanDistance[pt, start + param (end - start)] (*Normal distance*)
    ]
   ];  
