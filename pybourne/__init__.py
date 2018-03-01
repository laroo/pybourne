from sys import stdout, stderr

def write_line(msg, io):
    if isinstance(msg, bytes):
        print(msg.rstrip().decode("utf-8"), file=io, flush=True)
    else:
        print(msg, file=io, flush=True)

def error(msg):
    write_line(msg, stderr)


def info(msg):
    write_line(msg, stdout)
