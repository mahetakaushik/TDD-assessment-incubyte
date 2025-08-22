class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ","
        numbers_to_process = numbers
        delimiters = []

        if numbers.startswith("//"):
            numbers_parts = numbers.split("\n", 1)
            delimiter = numbers_parts[0][2:]
            numbers_to_process = numbers_parts[1] if len(numbers_parts) > 1 else ""

            if delimiter.startswith("[") and "]" in delimiter:
                delimiter_line = delimiter
                delimiter = ","
                while delimiter_line.startswith("[") and "]" in delimiter_line:
                    end_idx = delimiter_line.index("]")
                    delimiters.append(delimiter_line[1:end_idx])
                    delimiter_line = delimiter_line[end_idx + 1:]

        if not numbers.startswith("//"):
            numbers_to_process = numbers_to_process.replace("\n", delimiter)
        for delim in delimiters:
            numbers_to_process = numbers_to_process.replace(delim, delimiter)

        num_list = numbers_to_process.split(delimiter)
        result = 0
        negatives = []
        for num in num_list:
            if num:  # Ignore empty strings
                num_int = int(num)
                if num_int < 0:
                    negatives.append(num)
                elif num_int >= 1000:
                    continue
                else:
                    result += num_int

        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(negatives)}")

        return result
