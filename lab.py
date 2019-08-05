# Students should not edit this file, since changes here will _only_
# affect how your code runs locally.  It will not change how your code
# executes in the cloud.
 
lab_name = "Dot Product"
output_files = ['submission/code.out', 'submission/code-stats.csv', 'foo']
input_files = ['submission/code.c']
run_cmd = ['make', '-C', 'submission']
clean_cmd = ['make', 'clean']
env = ['CC','CXX','CFLAGS','CXXFLAGS']
repo = "https://d21e33605495c4eb7ef7d4fc27d78f422324e710@github.com/NVSL/CSE141pp-lab-dot-product"
reference_tag = "314bfbd09ab3a28b446742234851eeef2c29dcba"
time_limit = 40

valid_options={
    "compiler":
        {
        'gcc' : 
        {'CC': 'gcc',
         'CXX': 'g++'},
        'gcc-8' : 
        {'CC': 'gcc-8',
         'CXX': 'g++-8'},
        'gcc-9' : 
        {'CC': 'gcc-9',
         'CXX': 'g++-9'
         },
        'clang' : 
        {'CC': 'clang',
         'CXX': 'clang++'
         }
        },
    "optimize" :
        {
        '-O0' : 
        {'OPT_FLAGS': '-O0 -mno-mmx'},
        '-O1' : 
        {'OPT_FLAGS': '-O1 -mno-mmx'},
        '-O2' : 
        {'OPT_FLAGS': '-O2 -mno-mmx'},
        '-O3' : 
        {'OPT_FLAGS': '-O3 -mno-mmx'}
        },
    "MHz" : lambda x: {"MHZ": str(int(x))}
    }

default_options={
    'compiler' : 'gcc',
    'optimize' : '-O0'
}

figures_of_merit=[
    {
        "file": 'submission/code-stats.csv',
        "field": 'WallTime',
        "name": 'execution_time'
        },
    {
        "file": 'submission/code-stats.csv',
        "field": 'rapl:::PACKAGE_ENERGY:PACKAGE0',
        "name": 'energy'
    }
]
