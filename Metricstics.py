import math

# Metricstics class handles various statistical calculations without using built-in functions.
class Metricstics:
    def calculate_min(self, data):
        # Calculates the minimum value in the given data.
        if not data:
            return 0
        min_value = data[0]
        for num in data:
            if num < min_value:
                min_value = num
        return min_value

    def calculate_max(self, data):
        # Calculates the maximum value in the given data.
        if not data:
            return 0
        max_value = data[0]
        for num in data:
            if num > max_value:
                max_value = num
        return max_value

    def calculate_mean(self, data):
        # Calculates the mean (average) of the given data.
        if not data:
            return 0
        total = 0
        for num in data:
            total += num
        return total / len(data)

    def calculate_median(self, data):
        # Calculates the median of the given data.
        if not data:
            return 0
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid] + sorted_data[mid - 1]) / 2
        else:
            return sorted_data[mid]

    def calculate_mode(self, data):
        # Calculates the mode(s) of the given data.
        if not data:
            return 0
        count_dict = {}
        for num in data:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        max_count = max(count_dict.values())
        mode_values = [num for num, count in count_dict.items() if count == max_count]

        if len(mode_values) == 1:
            return mode_values[0]
        else:
            return mode_values

    def calculate_mad(self, data):
        # Calculates the Mean Absolute Deviation (MAD) of the given data.
        if not data:
            return 0
        mean = self.calculate_mean(data)
        total = 0
        for num in data:
            total += self.absolute(num - mean)
        return total / len(data)

    def calculate_standard_deviation(self, data):
        # Calculates the standard deviation of the given data.
        if not data:
            return 0
        mean = self.calculate_mean(data)
        variance = 0
        for num in data:
            variance += (num - mean) ** 2
        return math.sqrt(variance / (len(data) - 1))

    def absolute(self, num):
        # Returns the absolute value of a number.
        if num < 0:
            return -num
        return num