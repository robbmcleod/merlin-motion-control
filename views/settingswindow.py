"""Class for adding functionality to Settings modal window."""
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.clock import Clock
from models.galil import MotionLink
import copy


class SettingsWindow(ModalView):
    """Add functionality to Settings modal window."""

    software_version = StringProperty('Def')
    software_title = StringProperty('Def')
    ip_address = StringProperty('Def')
    speed = StringProperty('Def')
    speed_out = StringProperty('Def')

    def __init__(self, ml_object, **kwargs):
        """Initialize Settings modal window of main interface.

        Pull software version, title, ip address, speed, and speed out from
          MotionLink object.
        Deepcopy of MotionLink object to pass onto set_values().
        """
        super(SettingsWindow, self).__init__(**kwargs)
        self.software_version = str(ml_object.software_version)
        self.software_title = str(ml_object.software_title)
        self.ip_address = str(ml_object.mer_ip_address)
        self.speed = str(ml_object.speed)
        self.speed_out = str(ml_object.speed_out)
        self.ml = copy.deepcopy(ml_object)

    def set_values(self):
        """Update values of MotionLink object when called.

        After MotionLink object has been updated, update own values based on
          the current ones of the MotionLink object.
        """
        self.ml.ip_address = self.ip_address
        self.ml.speed = self.speed
        self.ml.speed_out = self.speed_out
        self.ml.set_values()
        self.ip_address = self.ml.mer_ip_address
        self.speed = str(self.ml.speed)
        self.speed_out = str(self.ml.speed_out)
