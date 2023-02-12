import notify2
import gi
gi.require_version('GdkPixbuf', '2.0')
from gi.repository import GdkPixbuf as GP


def callback(n, key=None, data=None):
    print("closing active notification")
    print(data)
    n.close()

def make_notif(title, body, icon="../assets/oak.jpg",
               timeout=8000, func_timeout=callback, buttons=[]):

    n = notify2.Notification(title, body)

    # Set an icon for the notification.
    ico = GP.Pixbuf.new_from_file(icon)
    n.set_icon_from_pixbuf(ico)

    # Set a timeout value
    n.set_timeout(timeout)
    # Warning the func_timeout will also be called when a button is pressed.
    n.connect('closed', func_timeout)

    # Add buttons to the notification.
    for button in buttons:
        key = button[0]
        button_name = button[1]
        func = button[2]
        data = button[3]

        n.add_action(key, button_name, func, data)

    # Show the notification.
    n.show()


def init():
    notify2.init("Notifier", "glib")


def Welcome():
    make_notif(
            "Welcome to PokeNotif",
            "Dummy text",
            buttons=[["Ok_key", "OK", Starter, "function"]],
            )


def Starter(n=None, name=None, data=None):
    make_notif(
            "Choose your starter",
            "Dummy text2",
            buttons=[
                ["Ok_key", "OK", callback, None],
                ["Ok_key", "OK", callback, None],
                ["Ok_key", "OK", callback, None],
                ["Ok_key", "OK", callback, None],
                ],
            )
