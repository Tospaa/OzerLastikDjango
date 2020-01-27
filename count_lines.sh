#!/bin/sh

git ls-files -- ':!:*.js' ':!:*.css' ':!:*.eot' ':!:*.svg' ':!:*.ttf' ':!:*.woff'  ':!:*.woff2' | xargs wc -l
