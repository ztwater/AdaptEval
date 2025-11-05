breakfast_options = [action.dest for action in breakfast._group_actions]
top_names = {name: value for (name, value) in args._get_kwargs()
             if name not in breakfast_options}
breakfast_names = {name: value for (name, value) in args._get_kwargs()
                   if name in breakfast_options}
top_names['breakfast'] = argparse.Namespace(**breakfast_names)
top_namespace = argparse.Namespace(**top_names)
