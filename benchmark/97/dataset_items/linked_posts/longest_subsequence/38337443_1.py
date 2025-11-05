"""
Return the longest increasing subsequence of `seq`.

Parameters
----------
seq : sequence object
  Can be any sequence, like `str`, `list`, `numpy.array`.
mode : {'strict', 'strictly', 'weak', 'weakly'}, optional
  If set to 'strict', the subsequence will contain unique elements.
  Using 'weak' an element can be repeated many times.
  Modes ending in -ly serve as a convenience to use with `order` parameter,
  because `longest_sequence(seq, 'weakly', 'increasing')` reads better.
  The default is 'strict'.
order : {'increasing', 'decreasing'}, optional
  By default return the longest increasing subsequence, but it is possible
  to return the longest decreasing sequence as well.
key : function, optional
  Specifies a function of one argument that is used to extract a comparison
  key from each list element (e.g., `str.lower`, `lambda x: x[0]`).
  The default value is `None` (compare the elements directly).
index : bool, optional
  If set to `True`, return the indices of the subsequence, otherwise return
  the elements. Default is `False`.

Returns
-------
elements : list, optional
  A `list` of elements of the longest subsequence.
  Returned by default and when `index` is set to `False`.
indices : list, optional
  A `list` of indices pointing to elements in the longest subsequence.
  Returned when `index` is set to `True`.
"""
