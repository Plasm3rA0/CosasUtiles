import os
def shutdown():
    if os.name == "nt":
        os.system("shutdown -s -t 500")
shutdown()