import logging

"""
logging.basicConfig(filename="my_log.txt", level=logging.INFO)
logging.info("Hello World")
"""

"""
logging.basicConfig(filename="my_log.txt", level=logging.INFO, format= '%(asctime)s, %(message)s')
logging.info("Hello World")
"""

# Debug, INFO, Warning, Error, Critical
"""
logging.basicConfig(filename="my_log.txt", level=logging.DEBUG, format= '%(asctime)s, %(message)s')
logging.debug("debuging")



logging.basicConfig(filename="my_log.txt", level=logging.WARNING, format= '%(asctime)s, %(message)s')
logging.warning("warning..")
logging.basicConfig(filename="my_log.txt", level=logging.CRITICAL, format= '%(asctime)s, %(message)s',
                    datefmt='%d-%b-%y %H%M%S', filemode= 'w')
logging.critical("critical..")


#a = "morning"
#print("Good %s" %a)
"""

def divide(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)
        logging.error("%s occured by dividing %d and %d" %(e, a, b))

print(divide(4,0))