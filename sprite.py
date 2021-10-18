class sprite:                                                 #   Creates class 'sprite'
    class hitbox:                                             #   Creates class 'hitbox'
        def ManageCoords(self, operation, x1, y1, x2, y2):    #   Gets operation (write or get), if write, gets x1, y1, x2, y2, if get, retrieves stored coordinates
            if self.operation == "write":                 				#   If operation is to write, the parameters x1, y1, x2, y2 are stored in the corrisponding variables
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

            elif self.operation == "get":
                return x1
                return y1
                return x2
                return y2
         
