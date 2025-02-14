#!/bin/sh


DAY=$1
YEAR=$2
SESSION=53616c7465645f5f7c297faef16e669072ffc421cfecceb33b4628e98581e070ad6245976523c0eefb3f843461c8f3eb1cc66fdb426c31880c49b34f216f9614
OUTFILE="$YEAR/day$DAY.input"
SOLVEFILE="$YEAR/day$DAY.py"

curl --cookie "session=$SESSION" https://adventofcode.com/$YEAR/day/$DAY/input > $OUTFILE
cp ./template.py $SOLVEFILE && sed -i "s/day.input/day$DAY.input/g" $SOLVEFILE && chmod +x $SOLVEFILE
