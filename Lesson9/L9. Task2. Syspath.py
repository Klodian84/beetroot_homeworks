# Importing sys module to check the current sys.path
import sys

# Checking the current sys.path
initial_sys_path = sys.path.copy()

# Modifying sys.path by appending a new directory
new_path = "/new/test/path"
sys.path.append(new_path)

# Checking sys.path after modification
modified_sys_path = sys.path

(initial_sys_path, modified_sys_path)

# Yes, it is possible to change syspath from within python.
# Now Python will be looking in the new path.