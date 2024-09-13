import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle object
pig = turtle.Turtle()
pig.speed(3)

# Draw the face
pig.penup()
pig.goto(0, -100)
pig.pendown()
pig.begin_fill()
pig.fillcolor("pink")
pig.circle(100)  # Big face circle
pig.end_fill()

# Draw the left eye (white part)
pig.penup()
pig.goto(-40, 40)
pig.pendown()
pig.begin_fill()
pig.fillcolor("white")
pig.circle(20)
pig.end_fill()

# Draw the right eye (white part)
pig.penup()
pig.goto(40, 40)
pig.pendown()
pig.begin_fill()
pig.fillcolor("white")
pig.circle(20)
pig.end_fill()

# Draw the left pupil (black)
pig.penup()
pig.goto(-40, 50)
pig.pendown()
pig.begin_fill()
pig.fillcolor("black")
pig.circle(10)
pig.end_fill()

# Draw the right pupil (black)
pig.penup()
pig.goto(40, 50)
pig.pendown()
pig.begin_fill()
pig.fillcolor("black")
pig.circle(10)
pig.end_fill()

# Draw the nose
pig.penup()
pig.goto(0, 0)
pig.pendown()
pig.begin_fill()
pig.fillcolor("lightpink")
pig.circle(30)
pig.end_fill()

# Draw the left nostril (black)
pig.penup()
pig.goto(-10, 10)
pig.pendown()
pig.begin_fill()
pig.fillcolor("black")
pig.circle(5)
pig.end_fill()

# Draw the right nostril (black)
pig.penup()
pig.goto(10, 10)
pig.pendown()
pig.begin_fill()
pig.fillcolor("black")
pig.circle(5)
pig.end_fill()

# Draw the smile (mouth)
pig.penup()
pig.goto(-40, -30)
pig.setheading(-60)
pig.pendown()
pig.circle(40, 120)

# Hide the turtle
pig.hideturtle()

# Keep the window open until clicked
screen.exitonclick()
