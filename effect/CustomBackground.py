class CustomBackground:
    def __init__(self, **s):
        self.color = s.get("color", 0x000000)
        self.bgImage = s.get("bgImage", "")
        self.imageColor = s.get("imageColor", 0xffffff)
        self.parallax = s.get("parallax", [100, 100])
        self.bgDisplayMode = s.get("bgDisplayMode", 0)
        self.loopBG = s.get("loopBG", False)
        self.unscaledSize = s.get("unscaledSize", 100)
        self.angleOffset = s.get("angleOffset", 0)