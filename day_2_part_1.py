from utils import get_data, split, compose
from functools import reduce

# PART 1

initial_state = {"depth": 0, "horizontal": 0}


def forward(state, magnitude):
    state["horizontal"] = state["horizontal"] + magnitude
    return state


def down(state, magnitude):
    state["depth"] = state["depth"] + magnitude
    return state


def up(state, magnitude):
    state["depth"] = state["depth"] - magnitude
    return state


actions = {
    "forward": forward,
    "down": down,
    "up": up,
}


def act(instruction, state, actions):
    action = actions[instruction[0]]
    magnitude = int(instruction[1])
    result = action(state, magnitude)
    print("act", instruction[0], magnitude, result)
    return result


def process(file_path, actions, initial_state):
    return reduce(
        lambda result, value: act(value, result, actions),
        compose(split(" "), get_data)(file_path),
        initial_state,
    )


def answer(state):
    return state["depth"] * state["horizontal"]


def main():
    # print(answer(process("day_2_test_data.txt", actions, initial_state)))
    print(answer(process("day_2_data.txt", actions, initial_state)))


if __name__ == "__main__":
    main()
