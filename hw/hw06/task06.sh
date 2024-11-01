# Vince Andriacco
# vandriac@nd.edu

#!/bin/sh

date_string=$(date +%Y-%m-%d_%H-%M)
filename="${date_string}-UnitTest.log"

cd tests/

python3 -m unittest discover > ../$filename 2>&1

cd ..

if grep -qF "................................" "$filename"; then
    echo "log file: $filename"
else
    cat $filename
fi