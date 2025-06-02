# I. Import filename
import kt_03_module
# II. Import particular func/class from the filename
from kt_03_module import myfunction
# III. Import all var/func/class
from kt_03_module import *

# 1. Step-I(import kt_03_module), Call function with filename
x = kt_03_module.myfunction(5, 6)
print(x)

# 2. Call module and get return value
z = myfunction(2, 3)
print("Display returned value:", z)

# 3. Call module and without return value
myfunction(2, 3)

# 4. Check dir of module
print(dir(kt_03_module))
return_val2 = myfunc_2(10, 5)
