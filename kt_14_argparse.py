# 1. Argument Parsing (argparse)
r"""
Step-1: Use -h command
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py -h
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type PROVIDE TEST RUN TYPE

options:
  -h, --help            show this help message and exit
  --os-type {Windows,Linux}
                        Default as Windows, Run only Windows Script if argument as "Windows", Otherwise run the given
                        OS type of Script
  --test-run-type PROVIDE TEST RUN TYPE
                        Like Selenium or REST API test or Normal test case

Step-1.1: Use --help command
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py --help
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type TEST_RUN_TYPE

options:
  -h, --help            show this help message and exit
  --os-type {Windows,Linux}
                        Default as Windows, Run only Windows Script if argument as "Windows", Otherwise run the given
                        OS type of Script
  --test-run-type TEST_RUN_TYPE
                        Like Selenium or REST API test or Normal test case

C:\Users\muthukus\Documents\Python_scripts\Python_KT>

Step-2: Run script without any argument(s)
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py
usage: Argument Parsing Example [-h] [--os-type {Windows,Linux}] --test-run-type TEST_RUN_TYPE
Argument Parsing Example: error: the following arguments are required: --test-run-type

C:\Users\muthukus\Documents\Python_scripts\Python_KT>

Step-3: Run script with argument(s)
C:\Users\muthukus\Documents\Python_scripts\Python_KT>python kt_13_session.py --test-run-type REST
Get Namespace: Namespace(os_type='Windows', test_run_type='REST')
Display (Args Value): Windows, REST

C:\Users\muthukus\Documents\Python_scripts\Python_KT>
"""
import argparse

arg_obj = argparse.ArgumentParser("Argument Parsing Example")
arg_obj.add_argument('--os-type', type=str, choices=['Windows', 'Linux'],
                     dest='os_type', required=False, default='Windows',
                     help='Default as Windows, Run only Windows Script if argument as "Windows", '
                          'Otherwise run the given OS type of Script')
arg_obj.add_argument('--test-run-type', type=str,
                     dest='test_run_type', required=True,
                     help='Like Selenium or REST API test or Normal test case')
get_parse = arg_obj.parse_args()
print(f"Get Namespace: {get_parse}")
final_os_type = get_parse.os_type
final_test_run_type = get_parse.test_run_type
print(f"Display (Args Value): {final_os_type}, {final_test_run_type}")
