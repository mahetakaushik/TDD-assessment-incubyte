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
        negatives = []
        for num in num_list:
            if num:  # Ignore empty strings
                num_int = int(num)
                if num_int < 0:
                    negatives.append(num)
                else:
                    result += num_int

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(negatives)}")

        return result
