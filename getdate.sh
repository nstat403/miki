#!/bin/sh

echo $(python ./py/getdate.py) | termux-clipboard-set
