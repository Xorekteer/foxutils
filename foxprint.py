verbose = True
def vprint(*args, **kwargs):
    """
    Prints iff foxprint.verbose is True (this is the default case).
    """
    if verbose:
        print(*args, **kwargs)

class cprint():
    """
    A class for color printing in terminal.
    Currently supports the following class-methods:

        __class__.red_print(*args, **kwargs)
        __class__.green_print(*args, **kwargs)
        __class__.blue_print(*args, **kwargs)
        __class__.yellow_print(*args, **kwargs)
    
    You can define others by adding functions (options such as bold, magenta... exist).
    """
    DEFAULT     = '\033[99m'
    WHITE       = '\033[97m'
    CYAN        = '\033[96m'
    MAGETA      = '\033[95m'
    BLUE        = '\033[94m'
    YELLOW      = '\033[93m'
    GREEN       = '\033[92m'
    RED         = '\033[91m'
    GREY        = '\033[90m'
    UNDERLINE   = '\033[4m'
    BOLD        = '\033[1m'
    ENDC        = '\033[0m'

    @classmethod
    def prototype(self, flag, *args, **kwargs):
        print(flag, end="")
        print(*args, **kwargs, end="")
        print(self.ENDC)
        return ""   # necessary so that wrapping inside another 
                    # print won't print the returned None

    @classmethod
    def red_print(self, *args, **kwargs):
        self.prototype(self.RED, *args, **kwargs)

    @classmethod
    def green_print(self, *args, **kwargs):
        self.prototype(self.GREEN, *args, **kwargs)
        
    @classmethod
    def blue_print(self, *args, **kwargs):
        self.prototype(self.BLUE, *args, **kwargs)

    @classmethod
    def yellow_print(self, *args, **kwargs):
        self.prototype(self.YELLOW, *args, **kwargs)