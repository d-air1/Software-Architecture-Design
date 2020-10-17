class item:
    #I was trying to dynamically set the attributes for the item class based off of the name passed to it
    def __init__(self, name):
        self.name = name

    #define price
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
        if name == "aluminum foil":
            return self.ab_price
        elif name == "toothpaste":
            return self.to_price
        elif name == "salt":
            return self.sa_price
        elif name == "pepper":
            return self.pe_price
        elif name == "Harry Potter Book":
            return self.hb_price
        elif name == "SW Design Book":
            return self.sb_price
        elif name == "Spiderman Book":
            return self.spb_price
        elif name == "Diary of a Wimpy Kid Book":
            return self.db_price
        elif name == "Spiderman Figure":
            return self.sf_price
        elif name == "Superman Figure":
            return self.suf_price
        elif name == "Pikachu Plushy":
            return self.pp_price
        elif name == "Charizard Card":
            return self.cc_price
        elif name == "Phone":
            return self.ph_price
        elif name == "Camera":
            return self.ca_price
        elif name == "Tablet":
            return self.ta_price
        elif name == "Laptop":
            return self.la_price

        def getName():
            return self.name