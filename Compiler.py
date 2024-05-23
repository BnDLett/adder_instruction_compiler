from Exceptions import (
    NotAnOperation,
    InstructionTooShort,
    InstructionTooLong,
)


class Compiler:
    instructions: list[str]
    modes: dict
    bin_instructions: list[str]
    hex_instructions: list[hex]

    def __init__(self, instructions: list[str]):
        self.instructions = instructions
        self.modes = {'add': 0, 'subtract': 1}
        self.bin_instructions = []
        self.hex_instructions = []

        self.recursive_compile()

    def compile(self, instruction: str) -> str:
        split_instruction = instruction.split(" ")

        if len(split_instruction) < 2:
            raise InstructionTooShort
        elif len(split_instruction) > 3:
            raise InstructionTooLong

        num_a = int(split_instruction[1])
        num_b = int(split_instruction[2])
        operation = split_instruction[0]

        if operation not in self.modes:
            raise NotAnOperation

        operation_flag = self.modes[operation]
        bin_a = bin(num_a)
        bin_b = bin(num_b)

        str_operation_flag = str(operation_flag)
        str_bin_a = str(bin_a).removeprefix("0b").rjust(4, '0')
        str_bin_b = str(bin_b).removeprefix("0b").rjust(4, '0')

        return f"0b{str_bin_a}{str_bin_b}{str_operation_flag}"

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

    def recursive_compile(self):
        bin_instructions = []
        hex_instructions = []

        for instruction in self.instructions:
            bin_instruction = self.compile(instruction)
            bin_instructions.append(bin_instruction)
            hex_instructions.append(hex(int(bin_instruction, base=2)))

        self.bin_instructions = bin_instructions
        self.hex_instructions = hex_instructions


if __name__ == "__main__":
    instruction_set = [
        'subtract 3 4',
        'add 5 6',
        'add 3 1',
    ]
    compiler = Compiler(instruction_set)
    for instruct in compiler.bin_instructions:
        print(instruct)

    compiler.add_instruction('add 5 2')
    compiler.recursive_compile()

    print("")
    for instruct in compiler.bin_instructions:
        print(instruct)
