class Oven:
    valid_size = ("4 pan","6 pan", "10 pan")
    
    def __init__(self, oven_size = '', **kwargs):
        super().__init__(**kwargs)
        self.oven_size = oven_size

    def display(self):
        print("Oven size: {}".format(self.oven_size))
        print()

    def get_valid_input(input_string, valid_option):
        input_string += " ({}) ".format(", ".join(valid_option))
        response = input(input_string)
        while response not in valid_option:
            response = input(input_string)
        return response
    
    def prompt_init():
        return dict(oven_size = Oven.get_valid_input("What size oven do you want", (Oven.valid_size)))
        
    prompt_init = staticmethod(prompt_init)

class Electrical(Oven):
    valid_element = ("5kw", "10kw", "15kw")
    valid_plug = ("USA", "Europe", "RSA")

    def __init__(self, element = '', plug = '', **kwargs):
        super().__init__(**kwargs)
        self.element = element
        self.plug = plug
        
    def display(self):
        super().display()
        print("Detail of Electrical Oven")
        print("You have chosen {} element".format(self.element))
        print("You have chosen {} plug".format(self.plug))
        print()

    def prompt_init():
        parent_init = Oven.prompt_init()
        element = Oven.get_valid_input("Choose element: ", (Electrical.valid_element))
        plug = Oven.get_valid_input("Choose plug: ", (Electrical.valid_plug))

        parent_init.update({"element":element,
                            "plug":plug
                            })
        return parent_init

    prompt_init = staticmethod(prompt_init)

class Gas(Oven):
    valid_btu = ("500 btu", "1000btu")
    
    def __init__(self, btu = '', **kwargs):
        super().__init__(**kwargs)
        self.btu = btu

    def display(self):
        super().display()
        print("Gas btu detail")
        print("You have chosen {} ".format(self.btu))
        print()

    def prompt_init():
        parent_init = Oven.prompt_init()
        btu = Oven.get_valid_input("Choos btu: ", (Gas.valid_btu))
        parent_init.update({"btu":btu})
        return parent_init
    
    prompt_init = staticmethod(prompt_init)
        
class Fan:
    valid_phase = ("Single phase", "Three phase")

    def __init__(self, phase = '', **kwargs):
        super().__init__(**kwargs)
        self.phase = phase

    def display(self):
        super().display()
        print("Fan phase detail")
        print("Fan phase is {} ".format(self.phase))
        print()

    def prompt_init():
        return dict(phase = Oven.get_valid_input("Choose phase: ", (Fan.valid_phase)))
    
    prompt_init = staticmethod(prompt_init)

class ElectricOven(Fan, Electrical):
    
    def prompt_init():
        init = Electrical.prompt_init()
        init.update(Fan.prompt_init())
        return init
    
    prompt_init = staticmethod(prompt_init)

class GasOven(Fan, Gas):
    
    def prompt_init():
        init = Fan.prompt_init()
        init.update(Gas.prompt_init())
        return init
    
    prompt_init = staticmethod(prompt_init)

class BuyOven:

    def __init__(self):
        self.oven_list = []
        
    type_map = {
                ("electrical"): ElectricOven,
                ("gas"):GasOven
                }

    def buy_oven(self):
        global oven_type
        oven_type = Oven.get_valid_input("What type of oven do you want to buy",
                                         ("electrical", "gas"))
        OvenClass = self.type_map[oven_type]
        init_args = OvenClass.prompt_init()
        self.oven_list.append(OvenClass(**init_args))

    def display_oven(self):
        print("Details of Oven")
        print("oven type is: {} ".format(oven_type))
        for oven in self.oven_list:
            oven.display()
        


    
    
    
    
    
                
    


