#!/bin/bash
if which tput >/dev/null 2>&1; then
    ncolors=$(tput colors)
fi
if [ -t 1 ] && [ -n "$ncolors" ] && [ "$ncolors" -ge 8 ]; then
  RED="$(tput setaf 1)"
  GREEN="$(tput setaf 2)"
  YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"
  BOLD="$(tput bold)"
  NORMAL="$(tput sgr0)"
else
  RED=""
  GREEN=""
  YELLOW=""
  BLUE=""
  BOLD=""
  NORMAL=""
fi

PROGRAM=$1
if [[ !  -z  $PROGRAM  ]]; then
    echo "${GREEN}Install Ixion Bot with name${NORMAL} ${YELLOW}${PROGRAM}${NORMAL}"
    CONFIG="config-${PROGRAM}.yml"
    PROGRAM="ixion_bot_${PROGRAM}"
else
    echo "${GREEN}Install Ixion Bot${NORMAL}"
    CONFIG="config.yml"
    PROGRAM="ixion_bot"
fi

FILENAME="/etc/supervisor/conf.d/${PROGRAM}.conf"
if [ -e $FILENAME ]; then
    echo "${GREEN}You have installed Ixion Bot.${NORMAL}"
    echo "${GREEN}To re-install, delete ${BLUE}${FILENAME}${GREEN} and re-run this script.${NORMAL}"
else
    if [ ! -e ${PWD}/${CONFIG} ]; then
        echo "${RED}NOTE: You should create config file ${BLUE}${PWD}/${CONFIG} ${NORMAL}"
    fi
    touch $FILENAME
    echo "[program:${PROGRAM}]" >> $FILENAME
    echo "directory=${PWD}" >> $FILENAME
    echo "command=${PWD}/venv/bin/python3 ${PWD}/main.py --config ${PWD}/${CONFIG}" >> $FILENAME
    echo "autorestart=true" >> $FILENAME
    supervisorctl reload
    #supervisorctl start $PROGRAM
    echo "${GREEN}Success${NORMAL}"
fi
