class QuestionOne:
    def __init__(self, text):
        self.text = text

    def sorted_letters(self):
        try:
            if self.text == None or len(self.text) < 2:
                raise ValueError
            formatted = self.text.lower().split()
            results = self.sort_formatted_text(formatted)
            return "".join(results)
        except ValueError:
            raise ValueError("Text must be more than two characters")

    def sort_formatted_text(self, formatted):
        """Sort provided list of chars and return it back to caller"""
        formatted = list("".join(formatted))
        for i in range(len(formatted)-1, 0, -1):
            for j in range(i):
                if formatted[j] > formatted[j+1]:
                    temp = formatted[j]
                    formatted[j] = formatted[j + 1]
                    formatted[j + 1] = temp
        return formatted
