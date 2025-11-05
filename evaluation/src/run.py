import argparse
from inference.inference import Inference
from test.test_pipeline import Test

def str2bool(value):
    if isinstance(value, bool):
        return value
    if value.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif value.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start_id",
        type=int,
        default=0,
        help="the start of repo id"
    )
    parser.add_argument(
        "--end_id",
        type=int,
        default=2475,
        help="the end of repo id"
    )
    parser.add_argument(
        "--model_str",
        type=str,
        default="gpt-3.5-turbo-1106",
        help="model name, default is 'gpt-3.5-turbo-1106'"
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="temperature for generation"
    )
    parser.add_argument(
        "--task_mode",
        type=int,
        default=0,
        help="0 for adapt req mode, 1 for task req mode, and 2 for no req mode"
    )
    parser.add_argument(
        "--dep_mode",
        type=str,
        default="None",
        help="the dependency mode, 'None' for no reference and 'Oracle' for the ideal dependencies."
    )
    parser.add_argument(
        "--repeat",
        type=int,
        default=1,
        help="repeat times, or number of samples to generate"
    )
    parser.add_argument("--inference", type=str2bool, default=True, help='include inference phase, default is True')
    parser.add_argument("--test", type=str2bool, default=False, help='include test phase, default is False')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = init_args()
    if args.inference:
        inference = Inference(args)
        inference.pipeline()
    if args.test:
        test = Test(args)
        test_results = test.pipeline()

