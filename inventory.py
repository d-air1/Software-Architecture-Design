class inventory:
    def __init__(self):
        #define inventory array
        self.stuff = ["aluminum foil", "toothpaste", "salt", "pepper", "Harry Potter Book", "SW Design Book", "Spiderman Book", "Diary of a Wimpy Kid Book", "Spiderman Figure", "Superman Figure", "Pikachu Plushy", "Charizard Card", "Phone", "Camera", "Tablet", "Laptop"]

        #define stock number
        self.al_stock = 10
        self.to_stock = 10
        self.sa_stock = 10
        self.pe_stock = 10
        self.hb_stock = 10
        self.sb_stock = 10
        self.spb_stock = 10
        self.db_stock = 10
        self.sf_stock = 10
        self.suf_stock = 10
        self.pp_stock = 10
        self.cc_stock = 10
        self.ph_stock = 10
        self.ca_stock = 10
        self.ta_stock = 10
        self.la_stock = 10

    def get_stock(self, name):
        if name == "aluminum foil":
            return self.ab_stock
        elif name == "toothpaste":
            return self.to_stock
        elif name == "salt":
            return self.sa_stock
        elif name == "pepper":
            return self.pe_stock
        elif name == "Harry Potter Book":
            return self.hb_stock
        elif name == "SW Design Book":
            return self.sb_stock
        elif name == "Spiderman Book":
            return self.spb_stock
        elif name == "Diary of a Wimpy Kid Book":
            return self.db_stock
        elif name == "Spiderman Figure":
            return self.sf_stock
        elif name == "Superman Figure":
            return self.suf_stock
        elif name == "Pikachu Plushy":
            return self.pp_stock
        elif name == "Charizard Card":
            return self.cc_stock
        elif name == "Phone":
            return self.ph_stock
        elif name == "Camera":
            return self.ca_stock
        elif name == "Tablet":
            return self.ta_stock
        elif name == "Laptop":
            return self.la_stock

    def rm_stock(self, item):
        if item == "aluminum foil":
            self.ab_stock -= 1
        elif item == "toothpaste":
            self.to_stock -= 1
        elif item == "salt":
            self.sa_stock -= 1
        elif item == "pepper":
            self.pe_stock -= 1
        elif item == "Harry Potter Book":
            self.hb_stock -= 1
        elif item == "SW Design Book":
            self.sb_stock -= 1
        elif item == "Spiderman Book":
            self.spb_stock -= 1
        elif item == "Diary of a Wimpy Kid Book":
            self.db_stock -= 1 
        elif item == "Spiderman Figure":
            self.sf_stock -= 1
        elif item == "Superman Figure":
            self.suf_stock -= 1
        elif item == "Pikachu Plushy":
            self.pp_stock -= 1
        elif item == "Charizard Card":
            self.cc_stock -= 1
        elif item == "Phone":
            self.ph_stock -= 1
        elif item == "Camera":
            self.ca_stock -= 1
        elif item == "Tablet":
            self.ta_stock -= 1
        elif item == "Laptop":
            self.la_stock -= 1

    def add_stock(self, item):
        if item == "aluminum foil":
            self.ab_stock += 1
        elif item == "toothpaste":
            self.to_stock += 1
        elif item == "salt":
            self.sa_stock += 1
        elif item == "pepper":
            self.pe_stock += 1
        elif item == "Harry Potter Book":
            self.hb_stock += 1
        elif item == "SW Design Book":
            self.sb_stock += 1
        elif item == "Spiderman Book":
            self.spb_stock += 1
        elif item == "Diary of a Wimpy Kid Book":
            self.db_stock += 1 
        elif item == "Spiderman Figure":
            self.sf_stock += 1
        elif item == "Superman Figure":
            self.suf_stock += 1
        elif item == "Pikachu Plushy":
            self.pp_stock += 1
        elif item == "Charizard Card":
            self.cc_stock += 1
        elif item == "Phone":
            self.ph_stock += 1
        elif item == "Camera":
            self.ca_stock += 1
        elif item == "Tablet":
            self.ta_stock += 1
        elif item == "Laptop":
            self.la_stock += 1

    def getInv(self):
        return self.stuff
