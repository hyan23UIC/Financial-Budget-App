# Final Project
# CS 111, Hayes & Reckinger
# Htet Oo Wai Yan & Hung Nguyen
# Date created: 11/20/2023

# Import necessary modules
import turtle
import math

# Disable turtle animation to speed up drawing
turtle.tracer(False)

# Set up turtle screen
s = turtle.getscreen()

# Set default window size
s.setup()

# Set up main turtle object
start = turtle.Turtle()

# Add custom shapes for different elements in the program
turtle.addshape("start.gif")
turtle.addshape("text_box.gif")
turtle.addshape("next.gif")
turtle.addshape("background.gif")
turtle.addshape("turtwig.gif")
turtle.addshape("grotle.gif")
turtle.addshape("torterra.gif")
turtle.addshape("plusun.gif")
turtle.addshape("emboar.gif")
turtle.addshape("empoleon.gif")

# Set the shape of the "start" turtle
start.shape("start.gif")

# Create turtles for various elements in the program
text_box = turtle.Turtle()
avatar = turtle.Turtle()
avatar1 = turtle.Turtle()
avatar2 = turtle.Turtle()
avatar3 = turtle.Turtle()
avatar4 = turtle.Turtle()
avatar5 = turtle.Turtle()
avatar6 = turtle.Turtle()
avatar7 = turtle.Turtle()
avatar8 = turtle.Turtle()
bunny = turtle.Turtle()
enemy = turtle.Turtle()
enemy1 = turtle.Turtle()
enemy2 = turtle.Turtle()
enemy3 = turtle.Turtle()
enemy4 = turtle.Turtle()

# Customize screen settings
s.bgcolor("white")
s.title("Financial Adventure")

# Create a title turtle for displaying a welcome message
title = turtle.Turtle()
title.penup()
title.hideturtle()
title.goto(0, 100)
title.color("black")
title.write("Welcome to your financial plan",
            False,
            align="center",
            font=("Arial", 20, "bold"))

# Create turtles and set initial positions for different "next" elements
next0 = turtle.Turtle()
next0.penup()
next0.hideturtle()
next0.goto(200, -150)

next3 = turtle.Turtle()
next3.penup()
next3.hideturtle()
next3.goto(150, -150)

next4 = turtle.Turtle()
next4.penup()
next4.hideturtle()
next4.goto(150, -150)

next5 = turtle.Turtle()
next5.penup()
next5.hideturtle()
next5.goto(150, -150)

next6 = turtle.Turtle()
next6.penup()
next6.hideturtle()
next6.goto(150, -150)

next7 = turtle.Turtle()
next7.penup()
next7.hideturtle()
next7.goto(150, -150)

next8 = turtle.Turtle()
next8.penup()
next8.hideturtle()
next8.goto(200, -150)

next9 = turtle.Turtle()
next9.penup()
next9.hideturtle()
next9.goto(200, -150)

next10 = turtle.Turtle()
next10.penup()
next10.hideturtle()
next10.goto(200, -150)

next11 = turtle.Turtle()
next11.penup()
next11.hideturtle()
next11.goto(200, -150)

next12 = turtle.Turtle()
next12.penup()
next12.hideturtle()
next12.goto(200, -150)

next13 = turtle.Turtle()
next13.penup()
next13.hideturtle()
next13.goto(200, -150)

next14 = turtle.Turtle()
next14.penup()
next14.hideturtle()
next14.goto(200, -150)

next15 = turtle.Turtle()
next15.penup()
next15.hideturtle()
next15.goto(200, -150)

next16 = turtle.Turtle()
next16.penup()
next16.hideturtle()
next16.goto(200, -150)

next17 = turtle.Turtle()
next17.penup()
next17.hideturtle()
next17.goto(200, -150)

next18 = turtle.Turtle()
next18.penup()
next18.hideturtle()
next18.goto(200, -150)

# Create a text turtle for displaying text
text = turtle.Turtle()
text.penup()
text.hideturtle()


# Define a function to set up the character details
def get_character(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("This is you!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next0.showturtle()
         next0.shape("next.gif")

         avatar.penup()
         avatar.goto(-50, -150)
         avatar.shape("turtwig.gif")

         next0.onclick(get_goal)


# Define a function to get the financial goal from the user
def get_goal(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next1 = turtle.Turtle()
         next1.penup()
         next1.hideturtle()
         next1.goto(150, -150)
         next1.showturtle()
         next1.shape("next.gif")

         text_box.shape("text_box.gif")
         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-120, 0)
         text.color("orange")
         text.write("Enter your \nfinancial goal:",
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         global goal
         goal = turtle.textinput("Financial Goal",
                                 "Enter your financial goal:")
         text.goto(100, 10)
         text.write("$" + str(goal),
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         # Check if the entered goal is valid
         if goal:
                  if int(goal) <= 0:
                           text.goto(120, -100)
                           text.color("red")
                           text.write("Please enter a valid financial goal!",
                                      False,
                                      align='center',
                                      font=('Arial', 20, 'bold'))
                           next1.onclick(get_goal)
                  else:
                           next1.onclick(race)
         else:
                  text.goto(120, -100)
                  text.color("red")
                  text.write("Please enter a valid financial goal!",
                             False,
                             align='center',
                             font=('Arial', 20, 'bold'))
                  next1.onclick(get_goal)


# Define a function to make a turtle walk from start1 to end1
def turtles_walk(turtle1, start1, end1):
         steps = 35
         deltax1 = (end1[0] - start1[0]) / steps
         deltay1 = (end1[1] - start1[1]) / steps

         # Setting up starting coordinates
         x1 = start1[0]
         y1 = start1[1]

         # Move the turtle to the starting position
         turtle1.goto(x1, y1)
         turtle1.showturtle()
         turtle1.speed(5)

         # Move the turtle step by step to the destination
         for iter in range(1, steps):
                  x1 = x1 + deltax1
                  y1 = y1 + deltay1
                  turtle1.goto(x1, y1)


# Define a function to initiate a race
def race(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("This is your goal!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))
         turtle.tracer(True)

         bunny.penup()
         bunny.goto(-50, -150)
         bunny.shape("plusun.gif")

         next8.showturtle()
         next8.shape("next.gif")
         next8.onclick(begin)


# Define a function to start the race
def begin(x, y):
         next8.hideturtle()

         title.goto(0, 90)
         title.color("red")
         title.write("It's getting away, let's chase after it!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         bunny.penup()
         bunny.goto(-50, -150)
         bunny.shape("plusun.gif")

         turtles_walk(bunny, [-150, -50], [1000, -50])

         next9.showturtle()
         next9.shape("next.gif")
         next9.onclick(chase)


# Define a function for the chase phase
def chase(x, y):
         next9.hideturtle()

         avatar1.penup()
         avatar1.goto(-500, -50)
         avatar1.shape("turtwig.gif")

         turtles_walk(avatar1, [-500, -50], [1000, -50])

         next10.showturtle()
         next10.shape("next.gif")
         next10.onclick(meet_income)


# Define a function for encountering the first enemy
def meet_income(x, y):
         s.clear()
         avatar2.penup()
         avatar2.goto(-500, -50)
         avatar2.shape("turtwig.gif")

         title.goto(0, 200)
         title.color("red")
         title.write("Enemy ahead! \nIt's your Income",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         enemy.penup()
         enemy.goto(150, -50)
         enemy.shape("empoleon.gif")

         turtles_walk(avatar2, [-500, -50], [-220, -50])

         next11.showturtle()
         next11.shape("next.gif")
         next11.onclick(get_income)


# Define a function to get the user's monthly income
def get_income(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next2 = turtle.Turtle()
         next2.penup()
         next2.hideturtle()
         next2.goto(150, -150)
         next2.showturtle()
         next2.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your \nmonthly income:",
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         global income
         income = turtle.textinput("Monthly income",
                                   "Enter your monthly income:")
         text.goto(100, 10)
         text.write("$" + str(income),
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         # Check if the entered income is valid
         if income:
                  if int(income) <= 0:
                           text.goto(120, -100)
                           text.color("red")
                           text.write("Please enter a valid income!",
                                      False,
                                      align='center',
                                      font=('Arial', 20, 'bold'))
                           next2.onclick(get_income)
                  else:
                           next2.onclick(evolving_1)
         else:
                  text.goto(120, -100)
                  text.color("red")
                  text.write("Please enter a valid income!",
                             False,
                             align='center',
                             font=('Arial', 20, 'bold'))
                  next2.onclick(get_income)


# Define a function for the first evolution
def evolving_1(x, y):
         s.clear()
         avatar3.penup()
         avatar3.goto(-50, -50)
         avatar3.shape("turtwig.gif")

         for i in range(3):
                  r = 50
                  avatar3.circle(r)

         avatar3.shape("grotle.gif")

         title.goto(0, 200)
         title.color("blue")
         title.write("Congratulations! \nYou've evolved!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next12.showturtle()
         next12.shape("next.gif")
         next12.onclick(fight_1)


# Define a function for the first fight
def fight_1(x, y):
         s.clear()
         avatar4.penup()
         avatar4.goto(-220, -50)
         avatar4.shape("grotle.gif")

         title.goto(0, 200)
         title.color("red")
         title.write("Take him down!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         enemy1.penup()
         enemy1.goto(150, -50)
         enemy1.shape("empoleon.gif")

         turtles_walk(avatar4, [-220, -50], [150, -50])
         if (avatar4.distance(enemy1.xcor(), enemy1.ycor()) < 30):
                  enemy1.hideturtle()

         next13.showturtle()
         next13.shape("next.gif")
         next13.onclick(meet_expenses)


# Define a function for encountering the second enemy
def meet_expenses(x, y):
         s.clear()
         avatar5.penup()
         avatar5.goto(-500, -50)
         avatar5.shape("grotle.gif")

         title.goto(0, 200)
         title.color("red")
         title.write("Enemy ahead! \nIt's your Expenses!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         enemy2.penup()
         enemy2.goto(180, -50)
         enemy2.shape("emboar.gif")

         turtles_walk(avatar5, [-500, -50], [-250, -50])

         next14.showturtle()
         next14.shape("next.gif")
         next14.onclick(get_housings)


# Define a function to get monthly housing expenses
def get_housings(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next3.showturtle()
         next3.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your monthly \nhousing expenses:",
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         global housing
         housing = turtle.textinput("Housing",
                                    "Enter your monthly housing expenses:")
         text.goto(100, 10)
         text.write("$" + str(housing),
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         next3.onclick(get_food)


# Define a function to get monthly food expenses
def get_food(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next4.showturtle()
         next4.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your monthly \ngroceries expenses:",
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         global grocery
         grocery = turtle.textinput("Grocery",
                                    "Enter your monthly food expenses:")
         text.goto(100, 10)
         text.write("$" + str(grocery),
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         next4.onclick(get_transport)


# Define a function to get monthly transportation expenses
def get_transport(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next5.showturtle()
         next5.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your monthly \ntransportation expenses:",
                    False,
                    align="center",
                    font=("Arial", 16, "bold"))

         global transportation
         transportation = turtle.textinput(
             "Transportation", "Enter your monthly transportation expenses:")
         text.goto(100, 10)
         text.write("$" + str(transportation),
                    False,
                    align="center",
                    font=("Arial", 16, "bold"))

         next5.onclick(get_loan)


# Define a function to get monthly debt payments
def get_loan(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next6.showturtle()
         next6.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your monthly \ndebt payments:",
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         global debt
         debt = turtle.textinput("Debt", "Enter your monthly debt payments:")
         text.goto(100, 10)
         text.write("$" + str(debt),
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         next6.onclick(get_additional)


# Define a function to get additional monthly expenses
def get_additional(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Enter the following information to continue",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next18.showturtle()
         next18.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Enter your additional \nmonthly expenses:",
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         global additional
         additional = turtle.textinput(
             "Others", "Enter your additional monthly expenses:")
         text.goto(100, 10)
         text.write("$" + str(additional),
                    False,
                    align="center",
                    font=("Arial", 18, "bold"))

         next18.onclick(get_total)


# Define a function to get total expenses
def get_total(x, y):
         s.clear()
         title.goto(0, 120)
         title.color("red")
         title.write("Here is tour total monthly expenses!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next7.showturtle()
         next7.shape("next.gif")

         text_box.goto(100, 30)
         text_box.stamp()
         text_box.hideturtle()

         text.goto(-150, 0)
         text.color("orange")
         text.write("Your total \nmonthly expenses:",
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         global total_expenses, housing, grocery, transportation, additional, debt
         total_expenses = int(housing or 0) + int(grocery or 0) + int(
             transportation or 0) + int(debt or 0) + int(additional or 0)
         text.goto(100, 10)
         text.write("$" + str(total_expenses),
                    False,
                    align="center",
                    font=("Arial", 20, "bold"))

         next7.onclick(evolving_2)


# Define a function for the second evolution
def evolving_2(x, y):
         s.clear()
         avatar6.penup()
         avatar6.goto(-50, -50)
         avatar6.shape("grotle.gif")

         for i in range(3):
                  r = 50
                  avatar6.circle(r)

         avatar6.shape("torterra.gif")

         title.goto(0, 200)
         title.color("blue")
         title.write("Congratulations! \nYou've evolved!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next15.showturtle()
         next15.shape("next.gif")
         next15.onclick(fight_2)


# Define a function for the second fight
def fight_2(x, y):
         s.clear()
         avatar7.penup()
         avatar7.goto(-220, -50)
         avatar7.shape("torterra.gif")

         title.goto(0, 200)
         title.color("red")
         title.write("Take him down!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         enemy3.penup()
         enemy3.goto(150, -50)
         enemy3.shape("emboar.gif")

         turtles_walk(avatar7, [-220, -50], [150, -50])
         if (avatar7.distance(enemy3.xcor(), enemy3.ycor()) < 30):
                  enemy3.hideturtle()

         next16.showturtle()
         next16.shape("next.gif")
         next16.onclick(end_chase)


# Define a function for the end of the chase
def end_chase(x, y):
         s.clear()
         avatar8.penup()
         avatar8.goto(-550, -50)
         avatar8.shape("torterra.gif")

         enemy4.penup()
         enemy4.goto(150, -50)
         enemy4.shape("plusun.gif")

         turtles_walk(avatar8, [-220, -50], [150, -50])
         if (avatar8.distance(enemy4.xcor(), enemy4.ycor()) < 200):
                  enemy4.hideturtle()

         title.goto(0, 200)
         title.color("red")
         title.write("You've made it to the end!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         next17.showturtle()
         next17.shape("next.gif")
         next17.onclick(get_recommendation)


# Define a function to dispkay financial recommendations
def get_recommendation(x, y):
         s.clear()
         s.bgpic("background.gif")
         title.goto(0, 200)
         title.color("purple")
         title.write("Here are your results!",
                     False,
                     align="center",
                     font=("Arial", 20, "bold"))

         # Check if total expenses are within budget
         if int(total_expenses) <= int(income or 0):
                  # Calculate the money left after expenses
                  global money_left, recommendation
                  money_left = int(income or 0) - int(total_expenses)

                  # Check if there is money left
                  if money_left > 0:
                           # Calculate the recommendation based on the financial goal
                           recommendation = float(
                               (int(goal or 0) / int(money_left)))
                  else:
                           # Display a message if there is no money left
                           text.goto(0, 120)
                           text.color("orange")
                           text.write(
                               "Oh no! You have no money left! Please try again.",
                               False,
                               align="center",
                               font=("Arial", 18, "bold"))
                           text.goto(0, -100)
                           text.color("red")
                           text.write(
                               "Some advices that might be useful: \n\n- Try the 50/30/20 rule as a simple budgeting framework. \n- Allow up to 50% of your income for needs. \n- Leave 30% of your income for wants. \n- Commit 20% of your income to savings and debt repayment. \n- Track and manage your budget through regular check-ins.",
                               False,
                               align="center",
                               font=("Arial", 18, "bold"))
                  # Display information about money left
                  text.goto(0, 150)
                  text.color("orange")
                  text.write(
                      "After calculating your total monthly expenses, you've left $"
                      + str(money_left) + ".",
                      False,
                      align="center",
                      font=("Arial", 18, "bold"))

                  # Check if the financial goal is achieved
                  if int(goal or 0) <= int(money_left):
                           text.goto(0, 120)
                           text.color("orange")
                           text.write(
                               "You have already achieve your financial goal with the money you've left!",
                               False,
                               align="center",
                               font=("Arial", 18, "bold"))
                  elif int(goal or 0) > int(money_left):
                           # Display how many months are needed to reach the financial goal
                           text.goto(0, 120)
                           text.color("orange")
                           text.write(
                               "To reach your financial goal, you need to save for  "
                               + str(math.ceil(recommendation)) + " months.",
                               False,
                               align="center",
                               font=("Arial", 18, "bold"))
         else:
                  # Display a message if the expenses exceed income
                  text.goto(0, 150)
                  text.color("orange")
                  text.write("Oh no! you have spent more than your income!",
                             False,
                             align="center",
                             font=("Arial", 18, "bold"))
                  text.goto(0, -100)
                  text.color("red")
                  text.write(
                      "Some advices that might be useful: \n\n- Try the 50/30/20 rule as a simple budgeting framework. \n- Allow up to 50% of your income for needs. \n- Leave 30% of your income for wants. \n- Commit 20% of your income to savings and debt repayment. \n- Track and manage your budget through regular check-ins.",
                      False,
                      align="center",
                      font=("Arial", 18, "bold"))


# Set up the initial click event to start the program
start.onclick(get_character)

# Enable turtle graphics updates
turtle.tracer(True)
turtle.mainloop()
