#!/bin/sh

YEAR=$2
DAY=$1
SESSION=$(cat session_cookie.txt)
OUTFILE="day$DAY.input"
SOLVEFILE="day$DAY.py"

curl --cookie "session=$SESSION" https://adventofcode.com/$YEAR/day/$DAY/input > $OUTFILE
cp ./template.py $SOLVEFILE && sed -i '' "s/day.input/day$1.input/g" $SOLVEFILE && chmod +x $SOLVEFILE
