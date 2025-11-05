Python 3.10.4 on a Debian Google Compute Engine instance:

iterable = ()
 234 ns   234 ns   234 ns  use_first_any
 234 ns   235 ns   235 ns  use_first_next
 264 ns   264 ns   264 ns  next_as_statement
 265 ns   265 ns   265 ns  original

iterable = (1,)
 308 ns   308 ns   308 ns  next_as_statement
 315 ns   315 ns   315 ns  original
 316 ns   316 ns   317 ns  use_first_any
 317 ns   317 ns   317 ns  use_first_next

iterable = (1, 2)
 361 ns   361 ns   361 ns  next_as_statement
 367 ns   367 ns   367 ns  original
 384 ns   385 ns   385 ns  use_first_next
 386 ns   387 ns   387 ns  use_first_any
