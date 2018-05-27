try:
    # Try uPython utime 1st
    import utime as time
except ImportError:
    # Fallback to normal python
    import time


class YX5300:
    """
    Wraps up control of a YX5300 via serial port
    """

    def __init__(self, serial_port):
        """
        Setup serial port
        """
        self._current_volume = 15
        self._serial_port = serial_port

        self.reset_module()
        self._set_tf_card_as_device()
        self.set_volume(self._current_volume)

    def _send_cmd(self, cmd):
        self._serial_port.write(bytearray(cmd))
        time.sleep(0.5)

    def play_next(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x01, 0x00, 0x00, 0x02, 0xEF])

    def play_previous(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x02, 0x00, 0x00, 0x00, 0xEF])

    def play_track(self, track_num):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x03, 0x00, 0x00, track_num, 0xEF])

    def volume_up(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x04, 0x00, 0x00, 0x00, 0xEF])

    def volume_down(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x05, 0x00, 0x00, 0x00, 0xEF])

    def set_volume(self, volume_level):
        """
        Set volume level
        """
        self._send_cmd([0x7e, 0xFF, 0x06, 0x06, 0x00, 0x00, volume_level, 0xEF])

    def play_track_loop(self, track_num):
        """
        Set volume level
        """
        self._send_cmd([0x7e, 0xFF, 0x06, 0x08, 0x00, 0x00, track_num, 0xEF])

    def _set_tf_card_as_device(self):
        """
        Set storage device as TF card
        """
        self._send_cmd([0x7e, 0xFF, 0x06, 0x09, 0x00, 0x00, 0x02, 0xEF])

    def sleep_module(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x0A, 0x00, 0x00, 0x00, 0xEF])

    def wake_module(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x0B, 0x00, 0x00, 0x00, 0xEF])

    def reset_module(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x0C, 0x00, 0x00, 0x00, 0xEF])

    def resume_track(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x0D, 0x00, 0x00, 0x00, 0xEF])

    def pause_track(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x0E, 0x00, 0x00, 0x00, 0xEF])

    def stop_track(self):
        self._send_cmd([0x7e, 0xFF, 0x06, 0x10, 0x00, 0x00, 0x00, 0xEF])



