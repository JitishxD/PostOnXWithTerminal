from pathlib import Path

def pick_latest_image():
    folder = Path(r"C:\Users\jitis\Pictures\Screenshots")
    valid_ext = (".png", ".jpg", ".jpeg")

    files = sorted(
        [f for f in folder.iterdir() if f.suffix.lower() in valid_ext],
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    top = files[:5]

    print("\nRecent screenshots:\n")
    for idx, f in enumerate(top, start=1):
        print(f"{idx}. {f.name}")

    choice = int(input("\nPick an image (1–5): "))
    return str(top[choice - 1])  # return full path
