approx_sizes = len(input_list)/n_groups 

groups_cont = [input_list[int(i*approx_sizes):int((i+1)*approx_sizes)] 
               for i in range(n_groups)]
