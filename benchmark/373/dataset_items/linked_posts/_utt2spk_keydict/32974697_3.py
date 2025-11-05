parser = ArgumentParser(description= """First paragraph 
                                        |n                              
                                        Second paragraph
                                        |n
                                        Third paragraph""",  
                usage='%(prog)s [OPTIONS]',
                formatter_class=MultilineFormatter)

options = parser.parse_args()
