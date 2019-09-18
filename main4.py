#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.list = arcade.SpriteList()


    def setup(self):
        stuffs = ['food.2','food.3']
        for i in range(2):
            stuff = stuffs[i]
            x = random.randint(0,800)
            y = random.randint(0,600)
            self.stuffs_sprite = arcade.Sprite("assets/{stuff}.png".format(stuff = stuff), 0.1)
            self.stuffs_sprite.center_x = x
            self.stuffs_sprite.center_y = y
            self.list.append(self.stuffs_sprite)
               

    def on_draw(self):
        arcade.start_render()
        self.list.draw()


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()