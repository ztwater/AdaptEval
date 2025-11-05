from contextlib import ExitStack, redirect_stdout
import os

with ExitStack() as stack:
    if should_hide_output():
        null_stream = open(os.devnull, "w")
        stack.enter_context(null_stream)
        stack.enter_context(redirect_stdout(null_stream))
    noisy_function()
