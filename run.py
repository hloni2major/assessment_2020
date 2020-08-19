from src.question_one import QuestionOne


if __name__ == '__main__':
    placeholder = 'Please enter some text, to terminate the program, click the letter \'x\' on your keyboard: \n'
    text = input(placeholder)
    while text != 'x':
        instance = QuestionOne(text)
        print("\n"*2+instance.sorted_letters() + "\n"*2)

        text = input(placeholder)
