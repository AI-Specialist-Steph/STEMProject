def activity():

    options = []

    correct_options = 0

    first_quiz = 1

    for q in sub_dict:
        print(q)
        for j in choose[first_quiz-1]:
            print(j)
        option = input("Choose (A, B, or C): ")
        option = option.upper()
        options.append(option)

        correct_options += is_correct(sub_dict.get(q), option)
        first_quiz += 1
    points(correct_options, options)

def is_correct(correctA, option):

    if correctA == option:
        print("Teacher Remark: Great Job!")
        return 5
    else:
        print("Wrong answer")
        return 0




def points(correct_options, options):
    print("\n")
    print("TOTAL POINTS")
    print("\n")
    print("Correct Answer:  ", end="")
    for j in sub_dict:
        print(sub_dict.get(j), end="")
    print()

    print("Options Chosen:  ", end="")
    for j in options:
        print(j, end="")
    print()

    points = int((correct_options + 2)*10)
    print("Point achieved: "+str(points))


def next():
    question = input ("Play again?  "
                      "yes or no    ")
    question = question.upper()

    if question == "YES":
        return True
    else:
        return False



sub_dict = {
    "65 is what percent of 500?: ": "A", "\n"
    "2+2 is what?: ": "B", "\n"
    "If two-thirds of Sam’s weekly income is $480, what is one-fourth of his weekly income?: ": "A", "\n"
    "If 43 of the 148 reams of paper purchased by a department are used, what is the percentage that remains? Round your answer to the nearest whole percent.: ": "C", "\n"
    "Juanita’s salary is $2,650.00 per month. If she receives a salary increase of 5%, what is her new monthly salary?: ": "B", "\n"
    "A 9' x 15' tool room was enlarged to 11' x 20'. How many square feet of floor space were added?: ": "C" "\n"



}

choose = [["A.  13 ", "B.  6", "C.  8"],
         ["A.  22", "B.  4", "C.  0"],
         ["A.  $80", "B.  $180", "C.  $200"],
         ["A.  91%", "B.  50%", "C.  71%"],
         ["A.  $2,782.50", "B.  $3000", "C.  $3500"],
         ["A.  85 square feet", "B.  45 square feet", "C.  95 square feet"]]


activity()

while next():
    activity()

print("move on to next activity")