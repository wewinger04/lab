"""
A class representing details for a Television object 
"""
class Television:
    """
    Variables representing the maximum and minimum channel numbers
    """
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    """
    Variables representing the maximum and minimum volume numbers
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self):
        """
        Constructor creating the television's initial channel, volume, and on/off status
        """
        self.__channel = 0
        self.__volume = 0
        self.__is_on = False
        """
        - Private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Private variable to store the TV status. The TV should start when it is off.
        """

    def power(self):
        """
        - Method used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
        """
        if self.__is_on == False:
            self.__is_on = True
        else:
            self.__is_on = False

    def channel_up(self):
        """
        - Method used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        MIN_CHANNEL = 0
        MAX_CHANNEL = 3
        if self.__is_on == False:
            pass
        else:
            if self.__channel == MAX_CHANNEL:
                self.__channel = MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        - Method used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        MIN_CHANNEL = 0     # Minimum TV channel
        MAX_CHANNEL = 3     # Maximum TV channel
        if self.__is_on == False:
            pass
        else:
            if self.__channel == MIN_CHANNEL:
                self.__channel = MAX_CHANNEL
            else:
                self.__channel -= 1
        pass

    def volume_up(self):
        """
        - Method used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        MIN_VOLUME = 0      # Minimum TV volume
        MAX_VOLUME = 2      # Maximum TV volume
        if self.__is_on == False:
            pass
        else:
            if self.__volume == MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self):
        """
        - Method used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        MIN_VOLUME = 0      # Minimum TV volume
        MAX_VOLUME = 2      # Maximum TV volume
        if self.__is_on == False:
            pass
        else:
            if self.__volume == MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self):
        """
        - Method used to return the TV status using the format shown in the comments of main.py
        """
        template = f'TV status: Is on = {self.__is_on}, Channel = {self.__channel}, Volume = {self.__volume}'
        return template
