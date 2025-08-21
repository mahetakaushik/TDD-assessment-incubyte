class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        num_list = numbers.split(",")
        if len(num_list) > 2:
            raise ValueError("Cannot process more than two numbers")

        result = 0
        for num in num_list:
            if num:
                result += int(num)

        return result
