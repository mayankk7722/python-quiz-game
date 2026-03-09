import time
import random

class Intro:
    def into(self):
        self.title = " Who Will Become a Millionaire \n"
        print(self.title.center(80,"-"))


    def input(self):
        self.name = input("Enter your name: ")
        print(f"Welcome to WWBM {self.name}")
        try:
          self.age = int(input("Enter your age:"))
        except ValueError:
            print("Oops invalid objects ")
            print("Age should be in numbers like 1,2,3,4..etc")
        self.From = input("Enter where are you from:")

    def rule(self):
        self.rule = """

GAME STRUCTURE:
- The game has 3 Levels.
- Each level contains 5 questions.
- Total Questions: 15

----------------------------------------
PRIZE MONEY STRUCTURE
----------------------------------------

============== MONEY LADDER ==============

1  : ₹1,000
2  : ₹2,000
3  : ₹3,000
4  : ₹5,000
5  : ₹10,000   (Level 1)
6  : ₹20,000
7  : ₹40,000
8  : ₹80,000
9  : ₹1,60,000
10 : ₹3,20,000  (Level 2)
11 : ₹6,40,000
12 : ₹12,50,000
13 : ₹25,00,000
14 : ₹50,00,000
15 : ₹1,00,00,000  (Level 3)

----------------------------------------
TIMER RULES:
- Level 1: 45 seconds per question.
- Level 2: 60 seconds per question.
- Level 3: No time limit.
- If time runs out, the answer is considered wrong.

----------------------------------------
LIFELINES (Only 2 Available)

1) 50-50 Lifeline:
- Removes 2 incorrect options.
- Leaves 1 correct and 1 wrong option.
- Can be used only once.

2) Double Tap Lifeline:
- Gives two attempts for the same question.
- If first answer is wrong, player gets one more chance.
- If second answer is wrong, player falls to safe level.
- Can be used only once.

----------------------------------------
WRONG ANSWER RULE:
- If the player gives a wrong answer,
  they fall back to the last safe level amount.
- If no safe level is crossed, they win ₹0.

----------------------------------------
QUIT RULE:
- Player can quit before answering a question.
- Player takes the current prize money.
- Game ends safely.

----------------------------------------
SPECIAL RULE:
- If a player completes an entire level (5 questions),
  their level prize money is squared.

========================================
           BEST OF LUCK!
========================================
"""
        print(self.rule)

class Level_01:
    def question(self):
        self.questions = [
            {"question":"Which is the largest ocean in thw world \n",
            "options":["A. Indian Ocean ","B. Atlantic Ocean ", "C. Arctic Ocea ","D. Pacific Ocean "],
                       "answer":"D"},
            {"question":"Who wrote the national anthem of India\n?",
            "options":["A. Bankim Chandra Chatterjee","B. Rabindranath Tagore","C. Subhash Chandra Bose","D. Mahatma Gandhi"],
                       "answer":"B"},
            {"question":"Which country is known as the Land of the Rising Sun\n?",
            "options":["A. China","B. Thailand","C. Japan","D. South Korea"],
                       "answer":"C"},
            {"question":"What is the currency of the United Kingdom\n",
            "options":["A. Euro","B. Dollar","C. Pound Sterling","D. Yen"],
                       "answer":"C"},
            {"question":"Which planet is the largest in our Solar System\n",
            "options":["A. Earth","B. Mars","C. Saturn","D. Jupiter"],
                       "answer":"D"}                                             
        ]
    
class Level_02:
    def question(self):
        self.questions = [
    {"question":"What is the smallest bone in the human body\n?",
     "options":["A. Stapes","B. Femur","C. Ulna","D. Tibia"],
     "answer":"A"},

    {"question":"Which country has the highest number of time zones\n?",
     "options":["A. USA","B. Russia","C. France","D. China"],
     "answer":"C"},

    {"question":"Which gas is most abundant in the Earth's atmosphere\n?",
     "options":["A. Oxygen","B. Nitrogen","C. Carbon Dioxide","D. Argon"],
     "answer":"B"},

    {"question":"What is the chemical symbol of Gold\n?",
     "options":["A. Gd","B. Go","C. Au","D. Ag"],
     "answer":"C"},

    {"question":"Which is the fastest land animal\n?",
     "options":["A. Lion","B. Cheetah","C. Horse","D. Leopard"],
     "answer":"B"}
]

class Level_03:
    def question(self):
        self.questions = [
    {"question":"Which element has the highest electrical conductivity at room temperature\n?",
     "options":["A. Copper","B. Silver","C. Gold","D. Aluminium"],
     "answer":"B"},

    {"question":"Which planet has the shortest day (fastest rotation) in the Solar System\n?",
     "options":["A. Earth","B. Mars","C. Jupiter","D. Saturn"],
     "answer":"C"},

    {"question":"What is the SI unit of electric capacitance\n?",
     "options":["A. Ohm","B. Henry","C. Tesla","D. Farad"],
     "answer":"D"},

    {"question":"Which blood group is known as the universal donor\n?",
     "options":["A. O+","B. O-","C. AB+","D. A-"],
     "answer":"B"},

    {"question":"Which gas is primarily responsible for the greenhouse effect on Earth\n?",
     "options":["A. Oxygen","B. Nitrogen","C. Carbon Dioxide","D. Helium"],
     "answer":"C"}
]

class Play(Level_01, Level_02, Level_03):

    def ask_questions(self, question_list, money_ladder, start_index, time_limit):

        question_number = start_index

        for q in question_list:

            print(f"\nQuestion {question_number + 1} for ₹{money_ladder[question_number]}")
            print(q["question"])

            options = q["options"].copy()
            correct_answer = q["answer"]

            for option in options:
                print(option)

            start_time = time.time()

            answer = input("\nEnter A/B/C/D, L1(50-50), L2(Double Tap), Q(Quit): ").upper()

            if time_limit is not None:
                end_time = time.time()
                if end_time - start_time > time_limit:
                    print("⏰ Time's up!")
                    print(f"You fall back to ₹{self.safe_amount}")
                    return False

            if answer == "Q":
                print(f"\nYou quit safely with ₹{self.win_amount}")
                return False

            if answer == "L1" and not self.used_5050:
                self.used_5050 = True
                print("\n50-50 Activated!")

                wrong_options = [opt for opt in options if opt[0] != correct_answer]
                removed = random.sample(wrong_options, 2)

                for r in removed:
                    options.remove(r)

                for option in options:
                    print(option)

                answer = input("Now enter your answer: ").upper()

            elif answer == "L1" and self.used_5050:
                print("50-50 already used!")
                answer = input("Enter answer: ").upper()

            if answer == "L2" and not self.used_double:
                self.used_double = True
                print("\nDouble Tap Activated! You have 2 attempts.")

                first_try = input("First attempt: ").upper()

                if first_try == correct_answer:
                    answer = first_try
                else:
                    print("Wrong! Try again.")
                    second_try = input("Second attempt: ").upper()

                    if second_try == correct_answer:
                        answer = second_try
                    else:
                        print("Both attempts wrong!")
                        print(f"You fall back to ₹{self.safe_amount}")
                        return False

            elif answer == "L2" and self.used_double:
                print("Double Tap already used!")
                answer = input("Enter answer: ").upper()

            if answer == correct_answer:
                self.win_amount = money_ladder[question_number]
                print("Correct Answer!")
                question_number += 1

            else:
                print("Wrong Answer!")
                print(f"You fall back to ₹{self.safe_amount}")
                self.win_amount = self.safe_amount
                return False

        self.safe_amount = self.win_amount
        print(f"\nLevel Completed! Safe amount is ₹{self.safe_amount}")

        return True

    def play(self):

        self.win_amount = 0
        self.safe_amount = 0
        self.used_5050 = False
        self.used_double = False

        money_ladder = [
            1000, 2000, 3000, 5000, 10000,
            20000, 40000, 80000, 160000, 320000,
            640000, 1250000, 2500000, 5000000, 10000000
        ]

        Level_01.question(self)
        level1 = self.questions.copy()
        random.shuffle(level1)

        Level_02.question(self)
        level2 = self.questions.copy()
        random.shuffle(level2)

        Level_03.question(self)
        level3 = self.questions.copy()
        random.shuffle(level3)

        print("\nGame Started!\n")

        if not self.ask_questions(level1, money_ladder, 0, 45):
            return

        if not self.ask_questions(level2, money_ladder, 5, 60):
            return

        if not self.ask_questions(level3, money_ladder, 10, None):
            return

        print(f"\n🎉 Congratulations! You won ₹{self.win_amount}")


if __name__ == "__main__":
    intro = Intro()
    intro.into()
    intro.input()
    intro.rule()

    game = Play()
    game.play()


input("\nPress Enter to exit...")




