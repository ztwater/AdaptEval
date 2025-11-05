def matToTex(a, roundn=2, matrixType = "b",rowVector = False):
    if type(a) != np.ndarray:
        raise ValueError("Input must be np array")
    if len(a.shape) > 2:
        raise ValueError("matrix can at most display two dimensions")
    if matrixType not in ["b","p"]:
        raise ValueError("matrix can be either type \"b\" or type \"p\"")
    if rowVector:
        if not (len(a.shape) != 1 or a.shape[0] != 1):
            raise ValueError("Cannot rowVector this bad boi, it is not a vector!")
    lines = str(a).splitlines()
    ret = "\n\\begin{"+matrixType+"matrix}\n"
    for line in lines:
        line = re.sub("\s+",",",re.sub("\[|\]","",line).strip())
        nums = line.split(",");
        if roundn != -1:
            nums = [str(round(float(num),roundn)) for num in nums]
        if rowVector:
            ret += " \\\\\n".join(nums)
        else:
            ret += " & ".join(nums)+" \\\\ \n"
    ret += "\n\\end{"+matrixType+"matrix}\n"
    ret = re.sub("(\-){0,1}0.[0]* ","0 ",ret)
    print(ret)
