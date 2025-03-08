""" Prints Hello World """
import logging

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

class HelloWorld:
    """ Prints Hello World """

    def hello(self, name: str):
        """ Prints Hello World """
        logger.debug(f"Hello World! {name}")
        print("Hello!")


# Create an instance of HelloWorld and call the hello method
h = HelloWorld()
h.hello("Yoshi")
h.hello("Chan")
