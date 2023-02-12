from gi.repository import GLib
from functions import init, Welcome


def main():
    init()
    Welcome()
    loop = GLib.MainLoop()
    loop.run()


main()
