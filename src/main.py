import fire
import click
import emoji

# for packaging this repo, uncomment the import statements below
from .lib import fetch_value_from_db,random_no, createDB
from .data import fortune_data_values
# from src.lib import fetch_value_from_db, random_no, createDB
# from src.data import fortune_data_values

# try:
#     import lib
# except ModuleNotFoundError:
#     sys.path.insert(1, './src')
#     import lib


@click.command()
def main():
    data = fortune_data_values()
    createDB(data)
    # print("\nFortune db created \n")
    randNum = random_no()
    # print("Random number Generated is: ", randNum)
    fortune_text = fetch_value_from_db(randNum)
    x = emoji.emojize(":sparkles:")
    print(f"\nYour fortune for the day is:\n{x} {fortune_text} {x}")
    print("\n")


if __name__ == "__main__":
    fire.Fire(main)
