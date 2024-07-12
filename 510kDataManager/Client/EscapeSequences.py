# This class contains constants and functions relating to ANSI Escape Sequences that are useful in display

class EscapeSequences:
    def __init__(self):
        self.UNICODE_ESCAPE = "\u001b"
        self.ANSI_ESCAPE = "\033"
        self.ERASE_SCREEN = f"{self.UNICODE_ESCAPE}[H{self.UNICODE_ESCAPE}[2J"
        self.ERASE_LINE = f"{self.UNICODE_ESCAPE}[2K"
        self.SET_TEXT_BOLD = f"{self.UNICODE_ESCAPE}[1m"
        self.SET_TEXT_FAINT = f"{self.UNICODE_ESCAPE}[2m"
        self.RESET_TEXT_BOLD_FAINT = f"{self.UNICODE_ESCAPE}[22m"
        self.SET_TEXT_ITALIC = f"{self.UNICODE_ESCAPE}[3m"
        self.RESET_TEXT_ITALIC = f"{self.UNICODE_ESCAPE}[23m"
        self.SET_TEXT_UNDERLINE = f"{self.UNICODE_ESCAPE}[4m"
        self.RESET_TEXT_UNDERLINE = f"{self.UNICODE_ESCAPE}[24m"
        self.SET_TEXT_BLINKING = f"{self.UNICODE_ESCAPE}[5m"
        self.RESET_TEXT_BLINKING = f"{self.UNICODE_ESCAPE}[25m"
        
        self.SET_TEXT_COLOR = f"{self.UNICODE_ESCAPE}[38;5;"
        self.SET_BG_COLOR = f"{self.UNICODE_ESCAPE}[48;5;"
        
        self.SET_TEXT_COLOR_BLACK = f"{self.SET_TEXT_COLOR}0m"
        self.SET_TEXT_COLOR_LIGHT_GREY = f"{self.SET_TEXT_COLOR}242m"
        self.SET_TEXT_COLOR_DARK_GREY = f"{self.SET_TEXT_COLOR}235m"
        self.SET_TEXT_COLOR_RED = f"{self.SET_TEXT_COLOR}160m"
        self.SET_TEXT_COLOR_GREEN = f"{self.SET_TEXT_COLOR}46m"
        self.SET_TEXT_COLOR_YELLOW = f"{self.SET_TEXT_COLOR}226m"
        self.SET_TEXT_COLOR_BLUE = f"{self.SET_TEXT_COLOR}12m"
        self.SET_TEXT_COLOR_MAGENTA = f"{self.SET_TEXT_COLOR}5m"
        self.SET_TEXT_COLOR_WHITE = f"{self.SET_TEXT_COLOR}15m"
        self.RESET_TEXT_COLOR = f"{self.UNICODE_ESCAPE}[39m"

        self.SET_BG_COLOR_BLACK = f"{self.SET_BG_COLOR}0m"
        self.SET_BG_COLOR_LIGHT_GREY = f"{self.SET_BG_COLOR}242m"
        self.SET_BG_COLOR_DARK_GREY = f"{self.SET_BG_COLOR}235m"
        self.SET_BG_COLOR_RED = f"{self.SET_BG_COLOR}160m"
        self.SET_BG_COLOR_GREEN = f"{self.SET_BG_COLOR}46m"
        self.SET_BG_COLOR_DARK_GREEN = f"{self.SET_BG_COLOR}22m"
        self.SET_BG_COLOR_YELLOW = f"{self.SET_BG_COLOR}226m"
        self.SET_BG_COLOR_BLUE = f"{self.SET_BG_COLOR}12m"
        self.SET_BG_COLOR_MAGENTA = f"{self.SET_BG_COLOR}5m"
        self.SET_BG_COLOR_WHITE = f"{self.SET_BG_COLOR}15m"
        self.RESET_BG_COLOR = f"{self.UNICODE_ESCAPE}[49m"
        
        self.EMPTY = "\u2003"
        
    # EMPTY = "\u2001\u2005\u200A"