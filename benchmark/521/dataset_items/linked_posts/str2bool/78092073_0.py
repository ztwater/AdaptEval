import argparse
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bool_flag', type=str)
    args = parser.parse_args()
    args.bool_flag = bool(eval(args.bool_flag))
    print(args.bool_flag, ',', type(args.bool_flag))
