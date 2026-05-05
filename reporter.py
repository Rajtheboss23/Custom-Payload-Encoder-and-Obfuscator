# reporter.py

def generate_report(results: dict, output_file="outputs/report.txt"):
    with open(output_file, "w") as f:
        f.write("=== Payload Obfuscation Report ===\n\n")

        for stage, data in results.items():
            f.write(f"[{stage}]\n")
            f.write(f"{data}\n\n")

        f.write("=== End of Report ===\n")