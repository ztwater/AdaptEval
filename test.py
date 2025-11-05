import os
benchmark_path = os.path.abspath('./benchmark')
for idx in os.listdir(benchmark_path):
    proj_path = os.path.join(benchmark_path, idx)
    post_path = os.path.join(proj_path, 'linked_posts')
    item_path = os.path.join(proj_path, 'dataset_items', 'linked_posts')
    os.rename(post_path, item_path)
