#!/bin/bash

if [[ -f  /etc/zshenv ]]; then
    sudo mv /etc/zshenv /etc/zprofile
fi

exit 0
