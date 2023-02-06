# Making a circuit thing or something

class LogicGate:
    def __init__(self, label):
        self.label = label
        self.output = None
    def get_label(self):
        return self.label
    def get_output(self):
        self.output = self.do_the_thing()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(self, label)
        self.input_0 = None
        self.input_1 = None
    def get_pin_0(self):
        if self.input_0 == None:
            return int(input(f"Enter input for pin 0 gate {self.get_label()}"))
        return self.pin_0.get_from().get_output()
    def get_pin_1(self):
        if self.input_1 == None:
            return int(input(f"Enter input for pin 1 gate {self.get_label()}"))
        return self.pin_1.get_from().get_output()
    def set_next_pin(self, source):
        if self.input_0 == None:
            self.input_0 = source
        else:
            if self.input_1 == None:
                self.input1 = source
            else:
                raise RuntimeError("Error: No empty pins")

class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(self, label)
        self.input_0 = None
    def get_pin_0(self):
        return int(input(f"Enter input for pin 0 gate {self.get_label()}"))
    def set_next_pin(self, source):
        if self.input_0 == None:
            self.input_0 == source
        else:
            raise RuntimeError("Error: No empty pins")

class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(self, label)
    def do_the_thing(self):
        return self.input_0 == 1 and self.input_1 == 1

class OrGate(BinaryGate):
    def __init__(self, label):
        super().__init__(self, label)
    def do_the_thing(self):
        return self.input_0 == 1 or self.input_1 == 1

class NotGate(UnaryGate):
    def __init__(self, label):
        super().__init__(self, label)
    def do_the_thing(self):
        return not self.input_0

class Connector:
    def __init__(self, fgate, tgate):
        self.fgate = fgate
        self.tgate = tgate
        tgate.set_next_pin(self)
    def get_from(self):
        return self.fgate
    def get_to(self):
        return self.tgate

class NorGate(BinaryGate):
    def __init__(self, label):
        super().init(self, label)
    def do_the_thing(self):
        return not (self.input_0 == 1 or self.input_1 == 1)

class NandGate(BinaryGate):
    def __init__(self, label):
        super().init(self, label)
    def do_the_thing(self):
        return not (self.input_0 == 1 and self.input_1 == 1)