from desktop_notifier import DesktopNotifier, Button
import asyncio

# LES FUNCTIONS :

def clicked():
    print("clicked")
    loop.stop()


def dismissed():
    print("dismissed")
    loop.stop()


notifier = DesktopNotifier()


async def makeNotif(title, message, buttons=[], on_clicked=clicked, on_dismissed=dismissed):
    await notifier.send(title=title, message=message, buttons=buttons, on_clicked=on_clicked, on_dismissed=on_dismissed)

loop = asyncio.get_event_loop()

loop.create_task(makeNotif("PokeNotif", "Welcome to PokeNotif"))

loop.run_forever()
