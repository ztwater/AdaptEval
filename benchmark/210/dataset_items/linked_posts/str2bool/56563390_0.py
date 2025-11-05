parser = argparse.ArgumentParser()
parser.add_argument('--my-flag',choices=('True','False'))

args = parser.parse_args()
flag = args.my_flag == 'True'
print(flag)
