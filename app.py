from flask import Flask, request, jsonify, send_file
from quantum_music.quantum_engine import generate_quantum_measurements
from quantum_music.music_mapper import measurements_to_notes
from quantum_music.midi_generator import create_midi

import os

app = Flask(__name__)

OUTPUT_DIR = "generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/")
def home():
    return open("static/index.html").read()

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    qubits = int(data.get("qubits", 4))
    depth = int(data.get("depth", 6))

    measurements = generate_quantum_measurements(
        qubits=qubits,
        depth=depth
    )

    notes = measurements_to_notes(measurements)

    output_path = os.path.join(
        OUTPUT_DIR,
        "quantum_music.mid"
    )

    create_midi(notes, output_path)

    return jsonify({
        "measurements": measurements,
        "notes": notes,
        "midi": "/download"
    })


@app.route("/download")
def download():
    return send_file(
        "generated/quantum_music.mid",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
