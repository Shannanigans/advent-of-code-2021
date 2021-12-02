from day_2_part_1 import process, answer

# PART 2

initial_state = {"depth": 0, "horizontal": 0, "aim": 0}


def forward(state, magnitude):
    state["horizontal"] = state["horizontal"] + magnitude
    state["depth"] = state["depth"] + (magnitude * state["aim"])
    return state


def down(state, magnitude):
    state["aim"] = state["aim"] + magnitude
    return state


def up(state, magnitude):
    state["aim"] = state["aim"] - magnitude
    return state


actions = {
    "forward": forward,
    "down": down,
    "up": up,
}


def main():
    # print(answer(process("day_2_test_data.txt", actions, initial_state)))
    print(answer(process("day_2_data.txt", actions, initial_state)))


if __name__ == "__main__":
    main()
