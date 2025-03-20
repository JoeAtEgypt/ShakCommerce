#!/usr/bin/bash

args=${*:2}
docker compose run --rm django sh -c "./scripts/startapp/$1.sh $args"

sudo chown -R $USER $2/

black $2/
