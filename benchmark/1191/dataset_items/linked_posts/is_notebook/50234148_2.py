import sys,os
def jupyterNotebookOrQtConsole():
    env = 'Unknow'
    cmd = 'ps -ef'
    try:
        with os.popen(cmd) as stream:
            if not py2:
                stream = stream._stream
            s = stream.read()
        pid = os.getpid()
        ls = list(filter(lambda l:'jupyter' in l and str(pid) in l.split(' '), s.split('\n')))
        if len(ls) == 1:
            l = ls[0]
            import re
            pa = re.compile(r'kernel-([-a-z0-9]*)\.json')
            rs = pa.findall(l)
            if len(rs):
                r = rs[0]
                if len(r)<12:
                    env = 'qtipython'
                else :
                    env = 'jn'
        return env
    except:
        return env
    
pyv = sys.version_info.major
py3 = (pyv == 3)
py2 = (pyv == 2)
class pyi():
    '''
    python info
    
    plt : Bool
        mean plt avaliable
    env :
        belong [cmd, cmdipython, qtipython, spyder, jn]
    '''
    pid = os.getpid()
    gui = 'ipykernel' in sys.modules
    cmdipython = 'IPython' in sys.modules and not gui
    ipython = cmdipython or gui
    spyder = 'spyder' in sys.modules
    if gui:
        env = 'spyder' if spyder else jupyterNotebookOrQtConsole()
    else:
        env = 'cmdipython' if ipython else 'cmd'
    
    cmd = not ipython
    qtipython = env == 'qtipython'
    jn = env == 'jn'
    
    plt = gui or 'DISPLAY' in os.environ 

print('Python Envronment is %s'%pyi.env)
