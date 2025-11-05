@writer.rewrites(ops.MigrationScript)
def revid_increment(ctx: migration.MigrationContext, revisions: tuple, op: ops.MigrationScript):
    op.rev_id = '{0:04}'.format(len(tuple(ctx.script.walk_revisions())) + 1)
    return op
