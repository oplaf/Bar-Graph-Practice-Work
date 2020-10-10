import arcade
import random
#Owen Lafont
def main():
    arcade.open_window(800,800, "Bar Graph")
    arcade.set_background_color(arcade.color.WHITE)

    #asking for input from user
    file_picker = input("What file should I graph?")
    #open and read .txt file
    infile1 = open(file_picker)
    #infile1 = open("input1.txt", 'r')
    readfile1 = infile1.readlines()

    #begin the rendering of the objects in the arcade import
    arcade.start_render()

    #this is the list of colors that are going to be randomly selected for the bars
    colors_list = [arcade.color.BLACK, arcade.color.GREEN, arcade.color.RED, arcade.color.BLUE, arcade.color.YELLOW,
                   arcade.color.ORANGE, arcade.color.PURPLE, arcade.color.TURQUOISE, arcade.color.BROWN,
                   arcade.color.GRAY]

    #a counter for the bar seperation
    bar_sep = 0
    #this is the most important but tricky part of the code. this is the loop that will go through each individual line of the text.
    for item in readfile1:
        # split item will split the list up whenever it come across ":". This seperates the int's from the str's.
        split_item = item.split(':')
        # xpos gathers the ints from the .txt file. the [1] tells it to gather every other starting with the number
        xpos = int(split_item[1])
        # name gathers the names from the .txt file. the [0] tells it to gather every other starting with the name
        name = split_item[0]
        # current_color is how the code selects a random color from the colors_list
        current_color = random.choice(colors_list)
        # bar_sep += is everytime the code runs through the lines, it takes the value then it adds 100 px of seperation to the value everytime the loop is done so the bars are evenly created and spaced
        bar_sep += 100
        # from_bottom is where the graph starts in corrilation with the bottom of the window
        from_bottom = 200
        # rectangle_height takes the int's that are pulled from the code. Higher number pulled from code = higher bar. It is multiplied because it would be too small without the *
        rectangle_height = xpos*10
        # rectangle_width is simply the width of a bar in the bar graph
        rectangle_width = 50
        # foo is the creation of the bars, with the previously created variables to fill in for its design
        foo = arcade.create_rectangle_filled(bar_sep, from_bottom+rectangle_height/2, rectangle_width, rectangle_height, current_color)
        foo.draw()
        # arcade.draw_text is the names gathered using the name variable and formatted to appear below the graph in correspondance with the bars
        arcade.draw_text(name, bar_sep-(rectangle_width/2), from_bottom-30, arcade.color.DARK_GRAY, 15)

#creates the 90 degree angle for the bar graph
    xaxis = arcade.create_line(50, from_bottom, 750,from_bottom, arcade.color.BLACK)
    yaxis = arcade.create_line(50, from_bottom, 50, 700, arcade.color.BLACK)

#draws the graph structure, ends the rendering process of the objects and runs the code
    xaxis.draw()
    yaxis.draw()
    arcade.finish_render()
    arcade.run()



main()

