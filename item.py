class item:
    #I was trying to dynamically set the attributes for the item class based off of the name passed to it
    def __init__(self, name):
        self.name = name

    #define prices
        self.al_price = 2
        self.to_price = 1
        self.sa_price = 1
        self.pe_price = 1
        self.hb_price = 20
        self.sb_price = 15
        self.spb_price = 15
        self.db_price = 20
        self.sf_price = 8
        self.suf_price = 12
        self.pp_price = 15
        self.cc_price = 4
        self.ph_price = 400
        self.ca_price = 600
        self.ta_price = 800
        self.la_price = 1000

    def get_price(self, name):
        if self.name == "aluminum foil":
            return self.al_price
        elif self.name == "toothpaste":
            return self.to_price
        elif self.name == "salt":
            return self.sa_price
        elif self.name == "pepper":
            return self.pe_price
        elif self.name == "Harry Potter Book":
            return self.hb_price
        elif self.name == "SW Design Book":
            return self.sb_price
        elif self.name == "Spiderman Book":
            return self.spb_price
        elif self.name == "Diary of a Wimpy Kid Book":
            return self.db_price
        elif self.name == "Spiderman Figure":
            return self.sf_price
        elif self.name == "Superman Figure":
            return self.suf_price
        elif self.name == "Pikachu Plushy":
            return self.pp_price
        elif self.name == "Charizard Card":
            return self.cc_price
        elif self.name == "Phone":
            return self.ph_price
        elif self.name == "Camera":
            return self.ca_price
        elif self.name == "Tablet":
            return self.ta_price
        elif self.name == "Laptop":
            return self.la_price

    def get_name(self):
        return self.name