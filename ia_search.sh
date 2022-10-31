#!/usr/bin/env bash

function addToPATH {
  case ":$PATH:" in
    *":$1:"*) :;; # already there
    *) PATH="$1:$PATH";; # or PATH="$PATH:$1"
  esac
}

# Add poetry to path if its not there already
addToPATH $HOME/.poetry/bin

# run
START_YEAR=$1
END_YEAR=$2
COLLECTION=$3
poetry run chewfiles --collection ${COLLECTION} --start ${START_YEAR} --end ${END_YEAR}
