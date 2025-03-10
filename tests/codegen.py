import subprocess


def run_playwright_codegen(url="http://192.168.0.1", output_file="recorded_script.py"):
    try:
        # Run playwright codegen
        process = subprocess.run(["playwright", "codegen", url], check=True)

        print(f"Recording completed. Check {output_file} for the script.")
    except subprocess.CalledProcessError as e:
        print(f"Error running playwright codegen: {e}")


if __name__ == "__main__":
    website_url = (
        input(
            "Enter the website URL to record interactions (default: http://192.168.0.1): "
        )
        or "http://192.168.0.1"
    )
    run_playwright_codegen(website_url)
