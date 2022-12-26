import turtle
pen = turtle.Turtle()
turtle.Screen().setup(width=750, height=500)
def txt():
    pen.up()
    pen.setpos(-360,0)
    pen.down()
    pen.color('black') # change color here <------------------------------------------------------
    pen.write("Made by 12y brainpower!", font=( # change text here <-------------------------------------------
      "Ariel", 40, "bold")) #change font here <----------------------------------------------------
txt()
turtle.done()