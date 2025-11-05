def str2bool(var_0):
    if isinstance(var_0, bool):
        return var_0
    if var_0.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif var_0.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
