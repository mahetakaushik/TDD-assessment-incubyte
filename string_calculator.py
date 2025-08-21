class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            numbers_parts = numbers.split("\n", 1)
            delimiter = numbers_parts[0][2:]
            numbers = numbers_parts[1] if len(numbers_parts) > 1 else ""

        if not numbers.startswith("//"):
            numbers = numbers.replace("\n", delimiter)

        num_list = numbers.split(delimiter)
        result = 0
        for num in num_list:
            if num:  # Ignore empty strings
                result += int(num)

        return result
