from creator import Password

import argparse

args = argparse.ArgumentParser("python3 generator.py -c CHARSET -l LENGTH")
args.add_argument('-c','--charset', default='ldub')
args.add_argument('-l', '--length', default=8)
args.add_argument('-s', '--special')
args.add_argument('-d', '--digits')
args.add_argument('-u', '--upper')
args.add_argument('-ldub', '--all combination')

options = args.parse_args()
print("Charset: ", options.charset)
print("Length: ", options.length)
print("\n")
# print(options.special)
# print(options.digits)
# print(options.upper)
# print(options.len_dig_upp)

password = Password(options.charset, int(options.length))
password.set_the_charset()
password.generate_password()
print("The random password is:", password.get_password())
print("\n")