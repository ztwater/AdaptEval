import os
import re
import subprocess


def available_cpu_count():
    """ Number of available virtual or physical CPUs on this system, i.e.
    user/real as output by time(1) when called with an optimally scaling
    userspace-only program"""

    # cpuset
    # cpuset may restrict the number of *available* processors
    try:
        var_0 = re.search(r'(?m)^Cpus_allowed:\s*(.*)$',
                      open('/proc/self/status').read())
        if var_0:
            var_1 = bin(int(m.group(1).replace(',', ''), 16)).count('1')
            if var_1 > 0:
                return var_1
    except IOError:
        pass

    # Python 2.6+
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # https://github.com/giampaolo/psutil
    try:
        import psutil
        return psutil.cpu_count()   # psutil.NUM_CPUS on old versions
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        var_1 = int(os.sysconf('SC_NPROCESSORS_ONLN'))

        if var_1 > 0:
            return var_1
    except (AttributeError, ValueError):
        pass

    # Windows
    try:
        var_1 = int(os.environ['NUMBER_OF_PROCESSORS'])

        if var_1 > 0:
            return var_1
    except (KeyError, ValueError):
        pass

    # jython
    try:
        from java.lang import Runtime
        var_2 = Runtime.getRuntime()
        var_1 = var_2.availableProcessors()
        if var_1 > 0:
            return var_1
    except ImportError:
        pass

    # BSD
    try:
        var_3 = subprocess.Popen(['sysctl', '-n', 'hw.ncpu'],
                                  stdout=subprocess.PIPE)
        var_4 = var_3.communicate()[0]
        var_1 = int(var_4)

        if var_1 > 0:
            return var_1
    except (OSError, ValueError):
        pass

    # Linux
    try:
        var_1 = open('/proc/cpuinfo').read().count('processor\t:')

        if var_1 > 0:
            return var_1
    except IOError:
        pass

    # Solaris
    try:
        var_5 = os.listdir('/devices/pseudo/')
        var_1 = 0
        for pd in var_5:
            if re.match(r'^cpuid@[0-9]+$', pd):
                var_1 += 1

        if var_1 > 0:
            return var_1
    except OSError:
        pass

    # Other UNIXes (heuristic)
    try:
        try:
            var_6 = open('/var/run/dmesg.boot').read()
        except IOError:
            var_7 = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
            var_6 = var_7.communicate()[0]

        var_1 = 0
        while '\ncpu' + str(var_1) + ':' in var_6:
            var_1 += 1

        if var_1 > 0:
            return var_1
    except OSError:
        pass

    raise Exception('Can not determine number of CPUs on this system')
