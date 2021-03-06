import pyglet
from pyglet.window import key

from modules.game_object import GameObject


class Bullet(GameObject):

    def __init__(self, game_state, game_assets, *args, **kwargs):
        images = [game_assets.image_assets["img_bullet_1"], game_assets.image_assets["img_bullet_2"]]
        anim = pyglet.image.Animation.from_image_sequence(images, duration=0.2, loop=True)
        super(Bullet, self).__init__(img=anim, *args, **kwargs)

        self.game_state = game_state        # game state object
        self.type = "bullet"                # type of game object

        self.key_handler = key.KeyStateHandler()  # Key press handler
        self.collider_type = "circle"  # Type of collider attached to this object
        self.collision_radius = self.image.get_max_width() / 2  # collision radius
        self.previous_position = None

        self.move_step = 0.5  # Distance by which to move in each key press
        self.velocity_x = 0
        self.velocity_y = 0

    def check_bounds(self):
        if self.x > 1000:
            self.dead = True
        if self.y > 1000:
            self.dead = True
        if self.x < 0:
            self.dead = True
        if self.y < 0:
            self.dead = True

    def update_object(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()

    def handle_collision_with(self, other_object):
        if other_object.type == "circle":
            self.dead = False
        elif other_object.type == "polygon":
            self.dead = True        # kill myself
        elif other_object.type == "virus":
            self.dead = True        # kill myself, damage to virus is handled by the virus
        elif other_object.type == "virus_particle":
            self.dead = True        # kill myself
        elif other_object.type == "player":
            self.dead = False       # no friendly fire
        elif other_object.type == "bullet":
            self.dead = False       # no friendly fire
        elif other_object.type == "infection":
            self.dead = True        # kill myself, damage to infection in handled by the infection
