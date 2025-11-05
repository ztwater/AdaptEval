def output_shell(var_0):

    try:
        var_1 = Popen(var_0, stdout=PIPE, stderr=PIPE, shell=True)
    except OSError:
        return None
    except ValueError:
        return None

    (output, err) = var_1.communicate()
    var_1.wait()
    if var_1.returncode != 0:
        print "Shell command failed to execute"
        return None
    return str(output)
