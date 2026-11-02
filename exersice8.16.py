# 1. import module_name
import my_module
my_module.say_hello("Budi")

# 2. from module_name import function_name
from my_module import say_hello
say_hello("Ani")

# 3. from module_name import function_name as fn
from my_module import say_hello as fn
fn("Joko")

# 4. import module_name as mn
import my_module as mn
mn.say_hello("Siti")

# 5. from module_name import *
from my_module import *
say_hello("Roni")