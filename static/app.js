async function generateMusic() {

    const qubits =
        parseInt(
            document.getElementById("qubits").value
        );

    const depth =
        parseInt(
            document.getElementById("depth").value
        );

    const response = await fetch(
        "/generate",
        {
            method: "POST",
            headers: {
                "Content-Type":
                "application/json"
            },
            body: JSON.stringify({
                qubits,
                depth
            })
        }
    );

    const data = await response.json();

    document.getElementById(
        "measurements"
    ).textContent =
        JSON.stringify(
            data.measurements,
            null,
            2
        );

    document.getElementById(
        "notes"
    ).textContent =
        JSON.stringify(
            data.notes,
            null,
            2
        );

    const download =
        document.getElementById(
            "download"
        );

    download.href = data.midi;
    download.style.display =
        "inline-block";
}