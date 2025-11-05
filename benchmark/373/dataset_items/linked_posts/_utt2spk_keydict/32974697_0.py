parser = ArgumentParser(description="""First paragraph 

                                       Second paragraph

                                       Third paragraph""",  
                                       usage='%(prog)s [OPTIONS]', 
                                       formatter_class=RawTextHelpFormatter)

options = parser.parse_args()
