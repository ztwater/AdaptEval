""" Misc utils

Hacked together by / Copyright 2020 Ross Wightman
"""
import argparse

def str2bool(v):
    """
    Thank to stackoverflow user: Maxim
    https://stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse/43357954#43357954
    :param v: A command line argument with values [yes, true, t, y, 1, True, no, false, f, n, 0, False]
    :return: Boolean version of the command line argument
    """

    if v.lower() in ('yes', 'true', 't', 'y', '1', 'True'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0', 'False'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

