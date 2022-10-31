## Description

Search [ESTC website](http://estc.bl.uk/) for given estc numbers.

### Pre-requisites 
* `Poetry` - run - `curl -sSL https://install.python-poetry.org | python3 -`

### Initialize Poetry

Run the following command in this project directory - 

```shell
poetry update
```

## Usage

```shell
./ia_search.sh <start-year> <end-year> <collection>
```

where collections are mapped as follows - 

```shell
americana - a
europeanlibraries - e
toronto - c
gutenberg - g
princeton - p
```

For e.g. 

```shell
./ia_search.sh 1640 1700 a
```

The output will be a file named `output.csv`.