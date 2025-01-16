class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        total_seconds = self.__to_seconds() + other.__to_seconds()
        return Time.__from_seconds(total_seconds)

    def __to_seconds(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    @staticmethod
    def __from_seconds(total_seconds):
        hour = total_seconds // 3600
        total_seconds %= 3600
        minute = total_seconds // 60
        second = total_seconds % 60
        return Time(hour, minute, second)

    def __str__(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"

# Example usage:
time1 = Time(2, 45, 30)
time2 = Time(1, 20, 40)

sum_time = time1 + time2
print("Sum of times:", sum_time)
