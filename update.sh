#!/bin/bash
hash=`cat hash.md`
echo "HASH = " $hash
last_commit_hash=$hash

get_commit_hash=$(curl -s https://github.com/T3nsh0/Full_Contact | grep -Eom1 '/T3nsh0/Full_Contact/commit/[0-9a-z]+' | cut -d'/' -f5)

if [ "$get_commit_hash" == "$last_commit_hash" ]; then
    echo "No version available."    
    exit 0
else
    echo "New version found!"
    echo "Commit: $get_commit_hash"
    mkdir Full_contact_update 
    wget -q https://github.com/T3nsh0/Full_Contact/archive/master.zip
    mv master.zip Full_contact_update/update.zip
    unzip Full_contact_update/update.zip >/dev/null
    echo "New version downloaded in $PWD/Full_contact_master/"
    rm -r hash.md
    echo $get_commit_hash > hash.md
    rm -r Full_contact_update
    echo "Update script by 0wnes1s, tks"
    exit 0
fi
exit 0
