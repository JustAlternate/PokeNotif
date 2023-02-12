from desktop_notifier import DesktopNotifier, Button
import asyncio

notify = DesktopNotifier(
        app_name="PokeNotif",
        )


async def main():
    n = await notify.send(
        title="title",
        message="message",
        buttons=[
            Button(
                title="button_name",
                on_pressed=lambda: print("pressed"),
                )
            ],
        on_clicked=lambda: print("Notif clicked"),
        on_dismissed=lambda: print("dismissed"),
        )

    await asyncio.sleep(10)
    await notify.clear(n)
    print("timed out")

asyncio.run(main())
