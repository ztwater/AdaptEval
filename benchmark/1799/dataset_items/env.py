from alembic.migration import MigrationContext
from alembic.operations.ops import MigrationScript
from alembic.script import ScriptDirectory 


def process_revision_directives(context: MigrationContext, _, directives: list[MigrationScript]):
    """
    Custom revision directive to automatically generate revision id's sequentially.
    Reference: https://stackoverflow.com/a/67398484/19517403
    """
    # extract Migration
    migration_script = directives[0]
    # extract current head revision
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()  # type: ignore

    if head_revision is None:
        # edge case with first migration
        new_rev_id = 1
    else:
        # default branch with incrementation
        last_rev_id = int(head_revision.lstrip("0"))
        new_rev_id = last_rev_id + 1
    # fill zeros up to 4 digits: 1 -> 0001
    migration_script.rev_id = f"{new_rev_id:04}"
 
