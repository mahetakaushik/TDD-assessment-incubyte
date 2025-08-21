class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        num_list = numbers.split(",")
        result = 0
        for num in num_list:
            if num:  # Ignore empty strings
                result += int(num)

        return result
