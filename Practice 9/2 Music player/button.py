import pygame as pg

# abstract button class
class Button:
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pressed = False
        self.just_pressed = False
        self.just_released = False

    def update(self):
        # mouse detection
        if pg.mouse.get_pressed()[0]:
            if self.rect.collidepoint(pg.mouse.get_pos()):
                if not self.pressed:
                    self.just_pressed = True
                self.pressed = True
        else:
            if self.pressed:
                self.just_released = True
            self.pressed = False

    def is_pressed(self):
        if self.pressed:
            return True
        return False

    def is_just_pressed(self):
        # fire only once on press
        if self.just_pressed:
            self.just_pressed = False
            return True
        
        return False
    
    def is_just_released(self):
        # fire only once on release
        if self.just_released:
            self.just_released = False
            return True

        return False


# Button based on Rect with text in center
class RectButton(Button, pg.Rect):

    def __init__(self, x, y, width, height, color="#FFFFFF", text="", text_color="#000000", text_size=14):
        super().__init__(x, y, width, height)

        self.font = pg.font.SysFont("Noto Sans", text_size)
        self.update_text(text, text_color)
        self.color = color
        
        # for compatability with Button class
        self.rect = self

    def update_text(self, text, text_color):
        self.text_surf = self.font.render(text, True, text_color)

        # position for centered text
        self.text_rect = self.text_surf.get_rect(center=self.center)

    def draw(self, sc):
        pg.draw.rect(sc, self.color, self)
        sc.blit(self.text_surf, self.text_rect)

# Button with image
class ImageButton(Button):

    def __init__(self, x, y, width, height, img_path):
        super().__init__()
        self.width = width
        self.height = height
        self.update_image(img_path)
        self.rect = pg.Rect(x, y, width, height)

    def update_image(self, img_path):
        self.original_img = pg.image.load(img_path)
        self.img = pg.transform.smoothscale(self.original_img, (self.width, self.height))
    
    def draw(self, sc):
        sc.blit(self.img, self.rect)

