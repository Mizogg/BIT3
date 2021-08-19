@Echo off
title Mizogg.co.uk
Pushd "%~dp0"
:loop
python bit3.py
goto loop