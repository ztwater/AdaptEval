def main():
    #Your application code

if __name__ == "__main__":
    try:
        main()
    except BaseException:
        lines = traceback.format_exc().splitlines()
        for line in lines:
            print re.sub(r'File ".*[\\/]([^\\/]+.py)"', r'File "\1"', line)
