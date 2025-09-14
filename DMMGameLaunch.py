import sys
import subprocess
import os

# Hardcoded DMM launcher URL format
DMM_URL_TEMPLATE = "dmmgameplayer://play/GCL/{game_id}/cl/win"

def main():
    # Expecting: -game <game_id>
    if len(sys.argv) < 3 or sys.argv[1].lower() != "-game":
        exe_name = os.path.basename(sys.argv[0])
        print(f"Usage: {exe_name} -game <game_id>")
        return

    game_id = sys.argv[2]
    url = DMM_URL_TEMPLATE.format(game_id=game_id)

    print(f"Launching: {url}")
    subprocess.run(["start", "", url], shell=True)

if __name__ == "__main__":
    main()
