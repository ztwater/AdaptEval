from jinja2 import Environment, BaseLoader

a, b, c = 1, 2, "345"
templ = "{a or b}{c[1:]}"

env = Environment(loader=BaseLoader, variable_start_string="{", variable_end_string="}")
env.from_string(templ).render(**locals())
