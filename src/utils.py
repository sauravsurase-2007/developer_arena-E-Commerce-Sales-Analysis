import os


def create_folders():

    folders = [
        "visualizations",
        "report"
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def heading(title):

    print("=" * 50)

    print(title.center(50))

    print("=" * 50)