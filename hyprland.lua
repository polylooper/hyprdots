-- This is an example Hyprland Lua config file.
-- Refer to the wiki for more information.
-- https://wiki.hypr.land/Configuring/Start/

-- Please note not all available settings / options are set here.
-- For a full list, see the wiki

-- You can (and should!!) split this configuration into multiple files
-- Create your files separately and then require them like this:
-- require("myColors")

require("lua.monitors")
require("lua.autostart")
require("lua.env-vars")
require("lua.permissions")
require("lua.decorations")
require("lua.layout")
require("lua.input")
require("lua.binds")
require("lua.windows-and-workspaces")
require("lua.misc")
