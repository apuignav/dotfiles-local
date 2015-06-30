#!/bin/bash

if hash brew 2>/dev/null
then
    # Install
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    # And caskroom
    brew tap caskroom/versions
    # Get a few taps
    brew tap homebrew/science
    brew tap homebrew/dupes
    brew tap caskroom/versions
    brew tap caskroom/homebrew-fonts
    # Install cask
    brew install caskroom/cask/brew-cask
    # Install X11 requirement
    brew cask install xquartz --appdir=/Applications
fi

# EOF
