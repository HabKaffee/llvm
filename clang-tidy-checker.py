import argparse
import os
import shutil
import sys

def do_check():
    #os.system('clear')
    current_dir = os.getcwd()
    llvm_dir = current_dir # for debug purposes. When script would be implemented - llvm_dir and current_dir would be different
    sycl_dir = llvm_dir + os.sep + 'sycl' + os.sep
    os.chdir(sycl_dir)
    shutil.copyfile(llvm_dir+os.sep+'.clang-tidy', llvm_dir+os.sep+'.clang-tidy.txt')
    current_dir = os.getcwd()
    #print (current_dir)
    tidy_options = '{'
    with open(llvm_dir + os.sep + '.clang-tidy.txt', 'r') as f:
        for _ in f:
            tidy_options += f.readline()
    tidy_options += '}'
    print(tidy_options)
    
    os.remove(llvm_dir+os.sep+'.clang-tidy.txt')


def main() :
    
    do_check()

if __name__ == "__main__":
    main()
    