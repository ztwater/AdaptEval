# env.py
def process_revision_directives(var_0, var_1, var_2):
    # extract Migration
    var_3 = var_2[0]
    # extract current head revision
    var_4 = ScriptDirectory.from_config(context.config).get_current_head()
    
    if var_4 is None:
        # edge case with first migration
        var_5 = 1
    else:
        # default branch with incrementation
        var_6 = int(var_4.lstrip('0'))
        var_5 = var_6 + 1
    # fill zeros up to 4 digits: 1 -> 0001
    var_3.rev_id = '{0:04}'.format(var_5) 