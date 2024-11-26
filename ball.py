from pico2d import *
import game_world
import game_framework
import random
import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1800)
        self.y = y if y else random.randint(100, 1050)

    def draw(self):
        sx, sy = get_canvas_width() // 2, get_canvas_height() // 2

        # 월드 좌표계를 화면좌표로 변환해야 한다.
        sx = self.x - server.background.window_left
        sy = self.y - server.background.window_bottom

        #self.image.clip_draw(int(self.frame) * 100, self.action * 100, 100, 100, sx, sy)

        self.image.draw(sx, sy)
        #draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        match group:
            case 'boy:ball':
                game_world.remove_object(self)

        pass
