#!/usr/bin/bash
dpkg -l | grep clang-tidy
if [ $? != 0 ]
then
    echo "You don't have clang-tidy installed"
    exit -1
fi

#start of checks
echo "Provide a full path to llvm"
read llvm_path
echo "Provide dir for clang-tidy check"
read $to_check_path
clang-tidy -header-filter=.* -config="{Checks: '-*,readability-identifier-naming', CheckOptions: [ {key: readability-identifier-naming.VariablePrefix, value: 'pref_1_'} ]}" --enable-check-profile --format-style=$llvm_path/.clang-tidy -p $llvm_path/build $to_check_path