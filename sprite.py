'''
 ____        _   _                   ____            _
|  _ \ _   _| |_| |__   ___  _ __   | __ )  __ _ ___(_) ___
| |_) | | | | __| '_ \ / _ \| '_ \  |  _ \ / _` / __| |/ __|
|  __/| |_| | |_| | | | (_) | | | | | |_) | (_| \__ \ | (__
|_|    \__, |\__|_| |_|\___/|_| |_| |____/ \__,_|___/_|\___|
       |___/
  ____                        ____  _               _
 / ___| __ _ _ __ ___   ___  |  _ \| |__  _   _ ___(_) ___ ___
| |  _ / _` | '_ ` _ \ / _ \ | |_) | '_ \| | | / __| |/ __/ __|
| |_| | (_| | | | | | |  __/ |  __/| | | | |_| \__ \ | (__\__ \
 \____|\__,_|_| |_| |_|\___| |_|   |_| |_|\__, |___/_|\___|___/
                                          |___/
 _____             _
| ____|_ __   __ _(_)_ __   ___
|  _| | '_ \ / _` | | '_ \ / _ \
| |___| | | | (_| | | | | |  __/
|_____|_| |_|\__, |_|_| |_|\___|
             |___/
A simple physics engine designed for 'axolotl run'.
Plug into any game engine   '''

class sprite:                                           #   Creates class 'sprite'
    class hitbox:                                       #   Creates class 'hitbox'
        def coords(self, operation, x1, y1, x2, y2):    #   Gets operation (write or get), if write, gets x1, y1, x2, y2, if get, retrieves stored coordinates
            if self.operation == "write":                 #   If operation is to write, the parameters x1, y1, x2, y2 are stored in the corrisponding variables
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

            elif self.operation == "get":
                return x1
                return y1
                return x2
                return y2
