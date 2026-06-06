MAJOR_SCALE = [
    60,
    62,
    64,
    65,
    67,
    69,
    71,
    72
]


def measurements_to_notes(measurements):

    notes = []

    for state in measurements:

        value = int(state, 2)

        note = MAJOR_SCALE[
            value % len(MAJOR_SCALE)
        ]

        notes.append(note)

    return notes