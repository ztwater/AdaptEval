import colorama
from colorama import Fore, Back
from pathlib import Path
from os import startfile, system

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = SCRIPT_DIR.joinpath('.')


def main(args):
    ...


if __name__ == '__main__':
    colorama.init(autoreset=True)

    from argparse import ArgumentParser, RawTextHelpFormatter

    format_text = FormatText([(20, '<'), (60, '<')])
    yellow_dc = format_text.new_dc(fore_color=Fore.YELLOW)
    green_dc = format_text.new_dc(fore_color=Fore.GREEN)
    red_dc = format_text.new_dc(fore_color=Fore.RED, back_color=Back.LIGHTYELLOW_EX)

    script_description = \
        '\n'.join([desc for desc in
                   [f'\n{green_dc(f"python {Path(__file__).name} [REFERENCE TEMPLATE] [OUTPUT FILE NAME]")} to create template.',
                    f'{green_dc(f"python {Path(__file__).name} -l *")} to get all available template',
                    f'{green_dc(f"python {Path(__file__).name} -o open")} open template directory so that you can put your template file there.',
                    # <- add your own description
                    ]])
    arg_parser = ArgumentParser(description=yellow_dc('CREATE TEMPLATE TOOL'),
                                # conflict_handler='resolve',
                                usage=script_description, formatter_class=RawTextHelpFormatter)

    arg_parser.add_argument("ref", help="reference template", nargs='?')
    arg_parser.add_argument("outfile", help="output file name", nargs='?')
    arg_parser.add_argument("action_number", help="action number", nargs='?', type=int)
    arg_parser.add_argument('--list', "-l", dest='list',
                            help=f"example: {green_dc('-l *')} \n"
                                 "description: list current available template. (accept regex)")

    arg_parser.add_argument('--option', "-o", dest='option',
                            help='\n'.join([format_text(msg_data_list) for msg_data_list in [
                                ['example', 'description'],
                                [green_dc('-o open'), 'open template directory so that you can put your template file there.'],
                                [green_dc('-o run'), '...'],
                                [green_dc('-o ...'), '...'],
                                # <- add your own description
                            ]]))

    g_args = arg_parser.parse_args()
    task_run_list = [[False, lambda: startfile('.')] if g_args.option == 'open' else None,
                     [False, lambda: [print(template_file_path.stem) for template_file_path in TEMPLATE_DIR.glob(f'{g_args.list}.py')]] if g_args.list else None,
                     # <- add your own function
                     ]
    for leave_flag, func in [task_list for task_list in task_run_list if task_list]:
        func()
        if leave_flag:
            exit(0)

    # CHECK POSITIONAL ARGUMENTS
    for attr_name, value in vars(g_args).items():
        if attr_name.startswith('-') or value is not None:
            continue
        system('cls')
        print(f'error required values of {red_dc(attr_name)} is None')
        print(f"if you need help, please use help command to help you: {red_dc(f'python {__file__} -h')}")
        exit(-1)
    main(g_args)


