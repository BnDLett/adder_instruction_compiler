from Compiler import Compiler

instruction_set = [
        'subtract 3 4',
        'add 5 6',
        'add 3 1',
    ]

# instruction_set = []

compiler = Compiler(instruction_set)

# while True:
#     instruction = input("> ").lower().strip()
#     if instruction == "":
#         break
#
#     compiler.add_instruction(instruction)

compiler.recursive_compile()
print(compiler.bin_instructions)

with open('out.hex', 'w') as fi:
    fi.write("v2.0 raw\n")
    for instruction in compiler.hex_instructions:
        fi.write(f"{instruction}\n")

    # fi.write(f"{hex(int('0b0000000001', base=2))}")
