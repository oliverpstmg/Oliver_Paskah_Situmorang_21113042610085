
import exercise8_15
exercise8_15.say_hello("Budi")

# 2. from module_name import function_name
from exercise8_15 import say_hello
say_hello("Ani")

# 3. from module_name import function_name as fn
from exercise8_15 import say_hello as fn
fn("Joko")

# 4. import module_name as mn
import exercise8_15 as mn
mn.say_hello("Siti")

# 5. from module_name import *
from exercise8_15 import *
say_hello("Roni")