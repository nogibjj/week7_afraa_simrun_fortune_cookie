
import fire 
import click
import emoji
import sys
sys.path.append('/workspaces/week7_afraa_simrun_fortune_cookie/')
from src.lib import fetch_value_from_db,random_no, createDB


@click.command()

def main():
    createDB()
    # print("\nFortune db created \n")
    randNum = random_no()
    # print("Random number Generated is: ", randNum)
    fortune_text = fetch_value_from_db(randNum)
    x = emoji.emojize(":sparkles:")
    print(f"\nYour fortune for the day is:\n{x} {fortune_text} {x}")
    print("\n")

if __name__ == "__main__":
    fire.Fire(main)