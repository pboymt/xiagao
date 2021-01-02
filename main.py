import tkinter.constants as tkc
from tkinter import Tk, Frame, Label
from typing import Optional

from uiautomator2 import Device, ConnectError
import uiautomator2 as u2


def main():
    top = Tk()
    top.wm_minsize(1000, 640)
    top.title("Test")
    f0 = Frame(master=top, width=300)
    f0.pack_propagate(0)

    f0.pack(side=tkc.LEFT, fill=tkc.Y, expand=False)
    l0 = Label(master=f0, text="Hello Tkinter")
    l0.pack(side=tkc.TOP, fill=tkc.X, expand=False)
    f1 = Frame(master=top, bg="#008b8b")
    f1.pack(side=tkc.LEFT, fill=tkc.BOTH, expand=True)
    top.mainloop()


class UIAutomatorManager:
    _device: Optional[Device] = None

    def __init__(self):
        pass

    async def connect(self):
        try:
            self._device = u2.connect()
            return True
        except ConnectError:
            return False

    @property
    def info(self):
        return self._device.info()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
