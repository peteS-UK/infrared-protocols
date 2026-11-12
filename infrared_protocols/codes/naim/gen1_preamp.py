"""Infrared codes for first-generation Naim preamplifiers.

These codes represent the infrared commands for controlling first-generation Naim
preamplifiers.  These include NAC 52, 72, 82, and other first-generation models.
"""

from enum import IntEnum, unique

from infrared_protocols.commands.rc5 import RC5Command

PREAMP_ADDRESS = 0x10


@unique
class NaimGen1PreampCode(IntEnum):
    """Commands for first-generation Naim preamplifiers."""

    VOLUME_UP = 0x10
    VOLUME_DOWN = 0x11
    MUTE = 0x0D
    BALANCE_LEFT = 0x1B
    BALANCE_RIGHT = 0x1A
    INPUT_1 = 0x12
    INPUT_2 = 0x13
    INPUT_3 = 0x14
    INPUT_4 = 0x15
    INPUT_5 = 0x16
    INPUT_6 = 0x17

    def to_command(self, repeat_count: int = 0, *, toggle: int = 0) -> RC5Command:
        """Build the RC5 command for this code.

        Flip ``toggle`` between successive presses of the same key, otherwise
        the device reads the second press as a repeat of the first and ignores it.

        Preamps require repeat_count = 1 (send the frame twice) to register properly.
        """
        return RC5Command(
            address=PREAMP_ADDRESS,
            command=self.value,
            toggle=toggle,
            repeat_count=repeat_count,
        )
