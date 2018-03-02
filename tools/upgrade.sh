#!/bin/bash
source tools/.pre-process.sh

echo "${BLUE}Updating Ixion Bot${NORMAL}"
if git pull --rebase --stat origin master
then
    echo "${GREEN}Update Success${NORMAL}"
    supervisorctl reload
else
    echo "${RED}There was an error updating. Try again later?${NORMAL}"
fi
