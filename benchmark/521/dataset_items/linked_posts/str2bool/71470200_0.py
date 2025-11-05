import argparse

parser = argparse.ArgumentParser(description="My parser")

parser.add_argument(
        "--my_bool",
        choices=["False", "True"],
        )

parsed_args = parser.parse_args()

my_bool = parsed_args.my_bool == "True"

print(my_bool)
