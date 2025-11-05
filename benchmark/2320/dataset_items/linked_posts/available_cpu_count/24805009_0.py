#!/usr/bin/env python
import hwloc
topology = hwloc.Topology()
topology.load()
print topology.get_nbobjs_by_type(hwloc.OBJ_CORE)
