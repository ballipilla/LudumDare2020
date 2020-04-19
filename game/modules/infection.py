import random

import pyglet
from pyglet.window import key

from modules.game_object import GameObject
from modules import util


class Infection(GameObject):

    def __init__(self, game_state, game_assets, *args, **kwargs):
        """
        :param game_state:
        :param game_assets:
        :param args:
        :param kwargs:
        """
        images = [game_assets.image_assets["img_infection"]]
        # TODO make this a sprite later
        super(Infection, self).__init__(img=images[0], *args, **kwargs)

        self.game_state = game_state                # game state object
        self.type = "infection"                # type of game object

        self.key_handler = key.KeyStateHandler()    # Key press handler
        self.collider_type = "circle"               # Type of collider attached to this object
        self.collision_radius = self.width/2        # collision radius
        self.previous_position = None
        self.life = 100  # life of the infection
        self.move_step = 0.5     # Distance by which to move in each key press
        self.velocity_x = 0
        self.velocity_y = 0

    def inflict_damage(self, amount):
        """
        Inflicts damage to the object. If the life of the object reaches 0, the object dies.
        :param amount: amount of damage to inflict
        """
        self.life -= amount
        if self.life <= 0:
            self.game_state.score += self.game_state.score_inc_infection_killed   # increase score
            self.dead = True
        else:
            self.dead = False

    def update_object(self, dt):
        self.previous_position = self.position

    def handle_collision_with(self, other_object):
        if other_object.type == "circle":
            self.dead = False
            self.position = self.previous_position
        elif other_object.type == "polygon":
            self.dead = False
            # self.position = self.previous_position
        elif other_object.type == "virus":
            self.dead = False   # no friendly fire
        elif other_object.type == "virus_particle":
            self.dead = False  # no friendly fire
        elif other_object.type == "player":
            self.dead = False    # kill myself
        elif other_object.type == "bullet":
            self.inflict_damage(self.game_state.damage_infection_by_bullet)
        elif other_object.type == "infection":
            self.dead = False
