bases = [b.__module__ in ('__builtin__', 'builtins') and
         u':class:`%s`' % b.__name__ or
         u':class:`%s.%s`' % (b.__module__, b.__name__)
         for b in self.object.__bases__]
self.add_line(u'   ' + _(u'Bases: %s') % ', '.join(bases), sourcename)
