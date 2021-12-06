import curses


class Window:
    def __init__(self):
        self.stdscr = None
        self.prev_colors = []

    def _convert_color(self, r, g, b):
        return r * 1000 // 255, g * 1000 // 255, b * 1000 // 255

    def _wrapped_show_pixels(self, stdscr, pixels):
        idx = 1
        for pixel in pixels:
            curses.init_color(idx, *(self._convert_color(*pixel)))
            curses.init_pair(idx, idx, curses.COLOR_BLACK)
            stdscr.addstr(0, idx - 1, "●", curses.color_pair(idx))
            idx += 1
        stdscr.refresh()

    def cleanup(self):
        # restore colors
        for i in range(len(self.prev_colors)):
            curses.init_color(i + 1, *(self.prev_colors[i]))

        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def show_pixels(self, pixels):
        if not self.stdscr:
            self.stdscr = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.stdscr.keypad(True)
            curses.start_color()

            # save previous colors
            for i in range(len(pixels)):
                self.prev_colors.append(curses.color_content(i + 1))

        self._wrapped_show_pixels(self.stdscr, pixels)
