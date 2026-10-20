-------------------
---- AUTOSTART ----
-------------------

-- See https://wiki.hypr.land/Configuring/Basics/Autostart/

-- Autostart necessary processes (like notifications daemons, status bars, etc.)
-- Or execute your favorite apps at launch like this:

-- autostart programs and daemons

local waybar        = "waybar"
local awww          = "awww-daemon"

hl.on("hyprland.start", function () 
  hl.exec_cmd(waybar)
  hl.exec_cmd(awww)
  --hl.exec_cmd("waybar & hyprpaper & firefox")
end)
