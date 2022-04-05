import argparse
import os
import yaml
import sys

# NOTE: Clang-tidy-15 required

def do_check():
    debug = True # debug purposes
    current_dir = os.getcwd()
    llvm_dir = current_dir # When script would be implemented - llvm_dir and current_dir would be different
    sycl_dir = llvm_dir + os.sep + 'sycl' + os.sep
    #include_dir = f'{sycl_dir}{os.sep}include{os.sep}CL{os.sep}sycl{os.sep}'
    src_dir = f'{sycl_dir}source{os.sep}'
    os.chdir(sycl_dir)
    current_dir = os.getcwd()
    extensions = ['.h', '.hpp', '.c', '.cc', '.cpp']
    files_in_src_folder = []
    #print (current_dir)
    tidy_options_dict = {}
    with open (llvm_dir + os.sep + '.clang-tidy', 'r') as f:
        tidy_options_dict = yaml.safe_load(f)
    #print(f'Tidy dict {tidy_options_dict}')
    for root, directory, file in os.walk(src_dir):
        for _file in file:
            for ext in extensions:
                if _file.endswith(ext):
                    files_in_src_folder.append(os.path.join(root, _file))
    #print(files_in_src_folder)
    for file_to_check in files_in_src_folder:
        os.system(f'clang-tidy -header-filter=.* -config="{tidy_options_dict}" -p {llvm_dir}/build {file_to_check}')
        if debug: break

def main() :
    
    do_check()

if __name__ == "__main__":
    main()
    