import pretty_midi


def create_midi(notes, output_file):

    midi = pretty_midi.PrettyMIDI()

    instrument = pretty_midi.Instrument(
        program=0
    )

    start = 0

    duration = 0.5

    for note in notes:

        midi_note = pretty_midi.Note(
            velocity=100,
            pitch=note,
            start=start,
            end=start + duration
        )

        instrument.notes.append(
            midi_note
        )

        start += duration

    midi.instruments.append(
        instrument
    )

    midi.write(output_file)