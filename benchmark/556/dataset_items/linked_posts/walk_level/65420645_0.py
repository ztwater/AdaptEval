def walk_with_depth(root_path, depth):
        if depth < 0:
            for root, dirs, files in os.walk(root_path):
                yield [root, dirs[:], files]

            return

        elif depth == 0:
            return

        base_depth = root_path.rstrip(os.path.sep).count(os.path.sep)
        for root, dirs, files in os.walk(root_path):
            yield [root, dirs[:], files]

            cur_depth = root.count(os.path.sep)
            
            if base_depth + depth <= cur_depth:
                del dirs[:]
