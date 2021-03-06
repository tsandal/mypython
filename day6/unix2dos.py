# import sys
# def unix2dos(fname):
#     dst_fname = fname + '.txt'
#     with open(fname) as src_fobj:
#         with open(dst_fname, 'w') as dst_fobj:
#             for line in src_fobj:
#                 line = line.rstrip('\r\n') + '\r\n'
#                 dst_fobj.write(line)
# if __name__ == '__main__':
#     unix2dos(sys.argv[1])  # python3 unix2dos.py unix2dos.py

import sys
def unix2dos(fname):
    dst_fname = fname + '.txt'
    with open(fname) as src_fobj:
        with open(dst_fname, 'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip('\r\n') + '\r\n'
                dst_fobj.write(line)
if __name__ == '__main__':
    unix2dos(sys.argv[1])  # python3 unix2dos.py unix2dos.py