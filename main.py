import datetime
import os

YEAR = 2000
PIXEL_ART = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXX XX XX   XXXXX     XX XX XX    XX   XXX    XXXX",
    "XXXX XX XXX XXXXXXXX XXXX XX XX XXXXX XX XX XXXXXXX",
    "XXXX    XXX XXXXXXXX XXXX    XX   XXX   XXX   XXXXX",
    "XXXX XX XXX XXXXXXXX XXXX XX XX XXXXX XX XX XXXXXXX",
    "XXXX XX XX   XXXXXXX XXXX XX XX    XX XX XX    XXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
FILLER = "X"
EMPTYER = " "


def days_before_first_sunday(year):
    return 6 - datetime.date(year, 1, 1).weekday()


def days_in_year(year) -> int:
    return (datetime.date(year + 1, 1, 1) - datetime.date(year, 1, 1)).days


def pixel_art_to_dates() -> list[str]:
    # transpose and join pixel art into a single string

    pixel_art = list(zip(*[list(x) for x in PIXEL_ART]))
    pixel_art_flattened = "".join(["".join(x) for x in pixel_art])

    res_string = (
        FILLER * days_before_first_sunday(YEAR)
        + pixel_art_flattened
        + FILLER
        * (
            days_in_year(YEAR)
            - len(pixel_art_flattened)
            - days_before_first_sunday(YEAR)
        )
    )

    return [
        (
            datetime.datetime(YEAR, 1, 1, 10, 10, 10) + datetime.timedelta(days=day)
        ).strftime("%Y-%m-%d %H:%M:%S")
        for day in range(days_in_year(YEAR))
        if res_string[day] != EMPTYER
    ]

def main():
    dir_name = "./ascii_image"

    os.system("rm -rf .git")
    os.system(f"rm -rf {dir_name}")
    os.system("git init")
    os.system(f"mkdir -p {dir_name}")

    for i, date in enumerate(pixel_art_to_dates()):
        slug = date.replace(" ", "_")
        os.system(f"touch {dir_name}/{slug}")
        os.system("git add .")
        os.system(f"git commit -m '{date}' --date='{date}'")


if __name__ == "__main__":
    main()
