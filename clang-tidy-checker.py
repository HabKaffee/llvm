import argparse
import os
import yaml
import sys

# NOTE: Clang-tidy-15 required

def do_check(args):
    debug = True # debug purposes
    current_dir = os.getcwd()
    llvm_dir = current_dir # When script would be implemented - llvm_dir and current_dir would be different
    sycl_dir = llvm_dir + os.sep + 'sycl' + os.sep
    src_dir = f'{sycl_dir}source{os.sep}'
    os.chdir(sycl_dir)
    current_dir = os.getcwd()
    extensions = ['.h', '.hpp', '.c', '.cc', '.cpp']
    files_in_src_folder = []
    tidy_options = {}
    with open (llvm_dir + os.sep + '.clang-tidy', 'r') as f:
        tidy_options = yaml.safe_load(f)
    for root, directory, file in os.walk(src_dir):
        for _file in file:
            for ext in extensions:
                if _file.endswith(ext):
                    files_in_src_folder.append(os.path.join(root, _file))
    #print(files_in_src_folder)
    if args.fix:
        for file_to_check in files_in_src_folder:
            os.system(f'clang-tidy -fix -config="{tidy_options}" -p {llvm_dir}/build {file_to_check}')
            if debug: break
    else:
        for file_to_check in files_in_src_folder:
            os.system(f'clang-tidy -config="{tidy_options}" -p {llvm_dir}/build {file_to_check}')
            if debug: break
def main() :
    parser = argparse.ArgumentParser(prog='clang-tidy-checker.py',
                                    description='script to do clang-tidy for llvm/sycl',
                                    formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--fix', type=bool, default=False, help='Option used to apply suggested fixes where possible')

    args = parser.parse_args()
    print(f"args: {args}")
    do_check(args)

if __name__ == "__main__":
    main()
    