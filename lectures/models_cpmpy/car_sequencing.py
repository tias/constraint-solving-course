import cpmpy as cp


# the CPMpy model and variables
def model_car_sequence(demand, per_slots, at_most, requires):
    n_cars = sum(demand)  # The amount of cars to sequence
    n_options = len(at_most)  # The amount of different options
    n_classes = len(demand)  # The amount of different car types
    requires = cp.cpm_array(requires)  # For element constraint

    model = cp.Model()

    # Sequence of different car types
    sequence = cp.intvar(0, n_classes - 1, shape=n_cars, name="sequence")
    # Auxiliary variables for options
    option = cp.boolvar(shape=(n_cars, n_options), name="option")

    # Each car class occurs the correct number of times
    model.add(cp.GlobalCardinalityCount(sequence, range(n_classes), demand))

    # connect auxiliary variables with decision variables
    for s in range(n_cars):
        model.add([option[s, o] == requires[sequence[s], o] for o in range(n_options)])

    # Option capacities are respected
    for o in range(n_options):
        for s in range(n_cars - per_slots[o] + 1):
            slotrange = range(s, s + per_slots[o])
            model.add(cp.sum(option[slotrange, o]) <= at_most[o])

    return model, (sequence, option)
