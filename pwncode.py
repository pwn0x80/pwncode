#!/usr/bin/env python3
import os
import sys
import subprocess


class s_event:
    def __init__(self, a_er, b_er):
        self.a_ty = a_er
        self.b_ty = b_er

    def __repr__(self):
        return "error %s %s" % (self.a_ty, self.b_ty)


class str_ret:
    def __init__(self, f_nsm=None, v_loc=None, bit=None):
        self.file = "nasm"
        self.a_arg = "-f"
        self.b_arg = "elf"
        self.c_arg = bit
        self.loc = v_loc
        self.slash = "/"
        self.d_arg = f_nsm

    def __str__(self):
        return "%s %s %s%s %s " % (self.file, self.a_arg, self.b_arg,
                                   self.c_arg, self.d_arg)

    def __repr__(self):
        return self.__str__()


def f_compiler(file, bit):
    paste = os.getcwd()

    cstring = str_ret(file, paste, bit)
    c_asm = str(cstring)
    os.system(c_asm)
    c_split = file.split(".")
    r_name = c_split[0]+".o"
    n_name = c_split[0] + ".out"

    subprocess.call(["ld", r_name, "-o", n_name])


class c_compiler:
    def __init__(self, a=None, b=64):
        self.file = a
        self.bit = b

        f_compiler(self.file, self.bit)


c_compiler(sys.argv[1], 64)
