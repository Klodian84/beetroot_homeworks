CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_idx = 0

    def first_channel(self):

        self.current_channel_idx = 0
        return self.channels[self.current_channel_idx]

    def last_channel(self):


        self.current_channel_idx = len(self.channels) - 1
        return self.channels[self.current_channel_idx]

    def turn_channel(self, N):

        if 1 <= N <= len(self.channels):
            self.current_channel_idx = N - 1
            return self.channels[self.current_channel_idx]
        else:
            return "Channel does not exist"

    def next_channel(self):

        self.current_channel_idx = (self.current_channel_idx + 1) % len(self.channels)
        return self.channels[self.current_channel_idx]

    def previous_channel(self):

        self.current_channel_idx = (self.current_channel_idx - 1) % len(self.channels)
        return self.channels[self.current_channel_idx]

    def current_channel(self):

        return self.channels[self.current_channel_idx]

    def is_exist(self, channel):

        if isinstance(channel, int):
            return "Yes" if 1 <= channel <= len(self.channels) else "No"
        elif isinstance(channel, str):
            return "Yes" if channel in self.channels else "No"
        return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())  # "BBC"
print(controller.last_channel())  # "TV1000"
print(controller.turn_channel(1))  # "BBC"
print(controller.next_channel())  # "Discovery"
print(controller.previous_channel())  # "BBC"
print(controller.current_channel())  # "BBC"
print(controller.is_exist(4))  # "No"
print(controller.is_exist("BBC"))  # "Yes"
