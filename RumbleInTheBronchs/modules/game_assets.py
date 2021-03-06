import pyglet


class GameAssets(object):

    def __init__(self, *args, **kwargs):
        """
        Initializes the class object.
        :param args: Additional positional arguments
        :param kwargs: Additional keyword arguments
        """
        super(GameAssets, self).__init__(*args, **kwargs)

        self.image_assets = dict()        # dictionary of game assets
        self.audio_assets = dict()        # dictionary of audio assets

        self.load_assets()

    @staticmethod
    def set_anchor_at_centre(image):
        """
        Sets the anchor of an image to its centre
        :param image: Image whose anchor has to be set
        """
        image.anchor_x = image.width // 2
        image.anchor_y = image.height // 2

    def create_image_asset(self, keyword, file, centered=True):
        """
        Creates an image asset from the specified file and adds it to the
        dictionary of image assets using the specified keyword
        :param keyword: Keyword with which to name the asset
        :param file: File from which to create the asset
        :param centered: Boolean indicating if the anchor has to be centered.
                        Default is True. If False, anchor is at bottom left.
        """
        image_asset = pyglet.resource.image(file)
        if centered:
            self.set_anchor_at_centre(image_asset)
        self.image_assets.update({keyword: image_asset})

    def create_audio_asset(self, keyword, file, streaming=False):
        """
        Creates an audio asset from the specified file and adds it to the
        dictionary of sound assets using the specified keyword
        :param keyword: Keyword with which to name the asset
        :param file: Keyword with which to name the asset
        :param streaming: Boolean indicating if the audio has to be streamed live or pre-loaded
        """
        audio_asset = pyglet.resource.media(file, streaming=streaming)
        self.audio_assets.update({keyword: audio_asset})

    def load_assets(self):
        pyglet.resource.path = ['resources']
        pyglet.resource.reindex()

        # load images
        self.create_image_asset("img_player_1", "images/player_1.png", True)
        self.create_image_asset("img_player_2", "images/player_2.png", True)
        self.create_image_asset("img_player_3", "images/player_3.png", True)

        self.create_image_asset("img_bkg_level_1", "images/bkg_red_1000x1000.png", False)
        self.create_image_asset("img_frg_level_1", "images/frg_red_1000x1000.png", False)

        self.create_image_asset("img_bkg_level_2", "images/bkg_green_1000x1000.png", False)
        self.create_image_asset("img_frg_level_2", "images/frg_green_1000x1000.png", False)

        self.create_image_asset("img_bkg_level_3", "images/bkg_blue_1000x1000.png", False)
        self.create_image_asset("img_frg_level_3", "images/frg_blue_1000x1000.png", False)

        self.create_image_asset("img_virus_B", "images/virus_B.png", True)
        self.create_image_asset("img_virus_B_2", "images/virus_B_2.png", True)
        self.create_image_asset("img_virus_C", "images/virus_C.png", True)
        self.create_image_asset("img_virus_C_2", "images/virus_C_2.png", True)
        self.create_image_asset("img_virus_particle", "images/virus_particle.png", True)

        self.create_image_asset("img_bullet_1", "images/bullet_1.png", True)
        self.create_image_asset("img_bullet_2", "images/bullet_2.png", True)

        self.create_image_asset("img_health_bar", "images/dna.png", True)
        self.image_assets["img_health_bar"].anchor_x = self.image_assets["img_health_bar"].width

        self.create_image_asset("img_infection_bar", "images/infectionbar.png", True)
        self.image_assets["img_infection_bar"].anchor_x = self.image_assets["img_infection_bar"].width

        self.create_image_asset("img_infection_A_1", "images/infection_A_1.png", True)
        self.create_image_asset("img_infection_A_2", "images/infection_A_2.png", True)

        self.create_image_asset("img_spawner", "images/spawner.png", True)
        self.create_image_asset("img_dummy", "images/pixel.png", True)

        self.create_image_asset("img_start_screen_C", "images/start_screen_c.png", False)
        self.create_image_asset("img_start_screen_D", "images/start_screen_d.png", False)
        self.create_image_asset("img_game_over", "images/game_over_screen.png", False)
        self.create_image_asset("img_win", "images/win_screen.png", False)

        # load audio
        self.create_audio_asset("ost_music", "music/ost.wav", True)
        self.create_audio_asset("snd_player_death", "sounds/player_death.wav", False)
        self.create_audio_asset("snd_player_fire", "sounds/player_fire.wav", False)
        self.create_audio_asset("snd_virus_birth", "sounds/virus_birth.wav", False)
        self.create_audio_asset("snd_infection_birth", "sounds/infection_birth.wav", False)
        self.create_audio_asset("snd_level_change", "sounds/level_change.wav", False)
