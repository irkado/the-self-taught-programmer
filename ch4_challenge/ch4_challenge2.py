"""
This func replace 'a cat' in 'a dog'.

:parameter #1: None.
:return: Nothing.
"""

func = lambda: print(
    "%s" % input("Type a str sent with word a cat: ").replace("a cat", "a dog :)")
)
func()
