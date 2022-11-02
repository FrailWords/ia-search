import click
import csv
import internetarchive as ia
from enum import Enum


class CollectionsEnum(str, Enum):
    americana = "a"
    europeanlibraries = "e"
    toronto = "c"
    gutenberg = "g"
    princeton = "p"


@click.command()
@click.option('--collection', is_flag=False, required=False, default=CollectionsEnum.americana,
              metavar='collection', type=click.Choice(CollectionsEnum), help='Collection Name')
@click.option('--start', is_flag=False, required=True,
              metavar='start', type=click.STRING, help='Start Year')
@click.option('--end', is_flag=False, required=True,
              metavar='end', type=click.STRING, help='End Year')
def main(collection: CollectionsEnum, start, end):
    search_query = f"collection:{collection.name} date:[{start} TO {end}] (language:eng OR language:english)"
    results = ia.search_items(query=search_query, params={"page": 1, "rows": 20}).iter_as_items()
    columns = ["IA URL", "Title", "Author", "Publication Date", "Publisher",
               "Digitizing Sponsor", "Contributor", "Language", "Identifier"]
    output = [columns]
    for item in results.iterator:
        print("Fetching data for item: ", item.identifier)
        item_details = ia.get_item(item.identifier)
        if item_details is not None:
            metadata = item_details.metadata
            url = map_to_value(metadata.get('identifier-access', ''))
            title = map_to_value(metadata.get('title', ''))
            author = map_to_value(metadata.get('creator', ''))
            publication_date = map_to_value(metadata.get('date', ''))
            publisher = map_to_value(metadata.get('publisher', ''))
            digitizing_sponsor = map_to_value(metadata.get('sponsor', ''))
            contributor = map_to_value(metadata.get('contributor', ''))
            language = map_to_value(metadata.get('language', ''))
            identifier = map_to_value(metadata.get('identifier', ''))
            output.append([url, title, author, publication_date, publisher,
                           digitizing_sponsor, contributor, language, identifier])
    with open("output.csv", "w+") as output_csv:
        csv_writer = csv.writer(output_csv, delimiter=',')
        csv_writer.writerows(output)


def map_to_value(arg):
    if isinstance(arg, list):
        return '\t---\t'.join(arg)
    else:
        return str(arg)


if __name__ == "__main__":
    main()
