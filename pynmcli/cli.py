import subprocess


def get_stdout(pi):
    result = pi.communicate()
    if len(result[0]) > 0:
        return result[0]
    else:
        return result[1]  #some error has occured


def execute_shell(command):
    return execute(command, wait=True, shellexec=True, errorstring='CLI Error')


def execute(command='', errorstring='', wait=True, shellexec=False, ags=None):
    try:
        if (shellexec):
            p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            p = subprocess.Popen(args=ags)

        if wait:
            p.wait()
            result = get_stdout(p)
            return str(result)
        else:
            return p
    except subprocess.CalledProcessError as e:
        print('error occured:' + errorstring)
        return errorstring
    except Exception as ea:
        print('Exception occured:' + ea.message)
        return errorstring
