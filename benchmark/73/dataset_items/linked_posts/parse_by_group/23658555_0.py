#!/usr/bin/env python2
import argparse, re

cmdl_skel = {
    'description'       : 'An example of multi-level argparse usage.',
    'opts'              : {
        '--foo' : {
            'type'    : int,
            'default' : 0,
            'help'    : 'foo help main',
        },
        '--bar' : {
            'type'    : str,
            'default' : 'quux',
            'help'    : 'bar help main',
        },
    },
    # Assume your program uses sub-programs with their options. Argparse will
    # first digest *all* defs, so opts with the same name across groups are
    # forbidden. The trick is to use the module name (=> group.title) as
    # pseudo namespace which is stripped off at group parsing
    'groups' : [
        {   'module'        : 'mod1',
            'description'   : 'mod1 description',
            'opts'          : {
                '--mod1-foo, --mod1.foo'  : {
                    'type'    : int,
                    'default' : 0,
                    'help'    : 'foo help for mod1'
                },
            },
        },
        {   'module'        : 'mod2',
            'description'   : 'mod2 description',
            'opts'          : {
                '--mod2-foo, --mod2.foo'  : {
                    'type'    : int,
                    'default' : 1,
                    'help'    : 'foo help for mod2'
                },
            },
        },
    ],
    'args'              : {
        'arg1'  : {
            'type'    : str,
            'help'    : 'arg1 help',
        },
        'arg2'  : {
            'type'    : str,
            'help'    : 'arg2 help',
        },
    }
}


def parse_args ():
    def _parse_group (parser, opt, **optd):
        # digest variants
        optv = re.split('\s*,\s*', opt)
        # this may rise exceptions...
        parser.add_argument(*optv, **optd)

    errors = {}
    parser = argparse.ArgumentParser(description=cmdl_skel['description'],
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # it'd be nice to loop in a single run over zipped lists, but they have
    # different lenghts...
    for opt in cmdl_skel['opts'].keys():
        _parse_group(parser, opt, **cmdl_skel['opts'][opt])

    for arg in cmdl_skel['args'].keys():
        _parse_group(parser, arg, **cmdl_skel['args'][arg])

    for grp in cmdl_skel['groups']:
        group = parser.add_argument_group(grp['module'], grp['description'])
        for mopt in grp['opts'].keys():
            _parse_group(group, mopt, **grp['opts'][mopt])

    args = parser.parse_args()

    all_group_opts = []
    all_group_names = {}
    for group in parser._action_groups[2:]:
        gtitle = group.title
        group_opts = [action.dest for action in group._group_actions]
        all_group_opts += group_opts
        group_names = {
            # remove the leading pseudo-namespace
            re.sub("^%s_" % gtitle, '', name) : value
                for (name, value) in args._get_kwargs()
                    if name in group_opts
        }
        # build group namespace
        all_group_names[gtitle] = argparse.Namespace(**group_names)

    # rebuild top namespace
    top_names = {
        name: value for (name, value) in args._get_kwargs()
            if name not in all_group_opts
    }
    top_names.update(**all_group_names)
    top_namespace = argparse.Namespace(**top_names)

    return top_namespace


def main():
    args = parse_args()

    print(str(args))
    print(args.bar)
    print(args.mod1.foo)


if __name__ == '__main__':
    main()
