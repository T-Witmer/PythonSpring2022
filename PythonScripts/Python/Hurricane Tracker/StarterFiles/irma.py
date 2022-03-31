import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    data = open("data/irma.csv" , "r")
    data = data.readlines()
    
    t.penup()
    for line in data[1:]:
        t.speed()
        x = line.split(',')
        wind = int(x[-2])
        lat = float(x[-4])
        lon = float(x[-3])

        if wind >= 157:
            t.pensize(12)
            t.color("red")
            t.write("5")

        elif wind < 157 and wind >= 130:
            t.pensize(10)
            t.color("orange")
            t.write("4")

        elif wind < 130 and wind >= 111:
            t.pensize(8)
            t.color("yellow")
            t.write("3")
        
        elif wind < 111 and wind >= 96:
            t.pensize(6)
            t.color("green")
            t.write("2")
        
        elif wind < 96 and wind >= 74:
            t.pensize(4)
            t.color("blue")
            t.write("1")
        
        elif wind < 74:
            t.pensize(2)
            t.color("white") 
           
        t.goto(lon,lat)
        t.pendown()
            
    

    turtle.done()
        
        

    
if __name__ == "__main__":
    irma()


