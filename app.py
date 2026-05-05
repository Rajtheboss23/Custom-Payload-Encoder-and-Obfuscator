# app.py

from flask import Flask, render_template, request
from encoder import *
from obfuscator import *
from detector import detect
from reporter import generate_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}

    if request.method == "POST":
        payload = request.form.get("payload")

        results["Original Payload"] = payload
        results["Original Detection"] = "Detected" if detect(payload) else "Bypassed"

        # Encoding
        b64 = base64_encode(payload)
        xor = xor_encode(payload, key="key")
        rot = rot13(payload)

        # Obfuscation
        obf1 = random_insertion(payload)
        obf2 = split_and_concat(payload)
        obf3 = escape_sequence(payload)

        # Store results
        results.update({
            "Base64": b64,
            "XOR": xor,
            "ROT13": rot,
            "Random Insertion": obf1,
            "Split & Concat": obf2,
            "Escape Sequence": obf3,

            "Base64 Detection": "Detected" if detect(b64) else "Bypassed",
            "XOR Detection": "Detected" if detect(xor) else "Bypassed",
            "ROT13 Detection": "Detected" if detect(rot) else "Bypassed",
            "Random Detection": "Detected" if detect(obf1) else "Bypassed",
            "Split Detection": "Detected" if detect(obf2) else "Bypassed",
            "Escape Detection": "Detected" if detect(obf3) else "Bypassed"
        })

        # Generate report
        generate_report(results)

    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)