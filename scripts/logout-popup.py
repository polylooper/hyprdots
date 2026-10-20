#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk
import subprocess
import os
import getpass

# Expand path so ~/.config works correctly
CSS_PATH = os.path.expanduser("~/.config/hypr/scripts/popup-style.css")
TIMEOUT = 60  # seconds
USER = getpass.getuser()  # current user

class LogoutDialog(Gtk.Window):
    def __init__(self):
        super().__init__(title="Logout Confirmation")
        self.set_border_width(20)
        self.set_default_size(320, 140)
        self.set_position(Gtk.WindowPosition.CENTER)

        # Load CSS for this window only
        self.load_css()

        self.remaining = TIMEOUT

        # Layout
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.add(vbox)

        # Main confirmation text
        label = Gtk.Label(label="Do you really want to log out?")
        label.set_margin_bottom(8)
        label.get_style_context().add_class("title")
        vbox.pack_start(label, False, False, 0)

        # Countdown label
        self.countdown_label = Gtk.Label()
        self.countdown_label.get_style_context().add_class("countdown")
        vbox.pack_start(self.countdown_label, False, False, 0)

        # Buttons
        button_box = Gtk.Box(spacing=10)
        vbox.pack_start(button_box, False, False, 0)

        self.cancel_btn = Gtk.Button(label="Cancel")
        self.cancel_btn.connect("clicked", self.cancel)
        button_box.pack_start(self.cancel_btn, True, True, 0)

        self.logout_btn = Gtk.Button(label="Logout")
        self.logout_btn.connect("clicked", self.logout_now)
        self.logout_btn.get_style_context().add_class("shutdown")  # reuse red style
        button_box.pack_start(self.logout_btn, True, True, 0)

        # Start timer
        self.update_countdown()
        GLib.timeout_add(1000, self.tick)

        # Keyboard shortcuts
        self.connect("key-press-event", self.on_key_press)

    def load_css(self):
        css_provider = Gtk.CssProvider()
        try:
            css_provider.load_from_path(CSS_PATH)
        except Exception as e:
            print(f"Failed to load CSS: {e}")

        screen = Gdk.Screen.get_default()
        Gtk.StyleContext.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

    def update_countdown(self):
        self.countdown_label.set_text(
            f"Logging out automatically in {self.remaining} seconds..."
        )

    def tick(self):
        self.remaining -= 1
        self.update_countdown()
        if self.remaining <= 0:
            self.logout_now(None)
            return False
        return True

    def logout_now(self, widget):
        subprocess.Popen(["loginctl", "terminate-user", USER])
        Gtk.main_quit()

    def cancel(self, widget):
        Gtk.main_quit()

    def on_key_press(self, widget, event):
        if event.keyval == Gdk.KEY_Escape:
            self.cancel(None)
            return True
        elif event.keyval in (Gdk.KEY_Return, Gdk.KEY_KP_Enter):
            self.logout_now(None)
            return True
        return False


win = LogoutDialog()
win.show_all()
Gtk.main()
