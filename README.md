# Clocked
A simple tool for updating Windows time, if your CMOS is faulty

### This is for whom?

This is for people like me, who have an "ancient" windows desktop (or laptop), who have some issues with BIOS hardware time...

Its symptoms are:
* Booting and finding out System time is the same as yesterday
* Internet Time update sometimes doesn't work.
* Hardware Time doesn't update when system is not active (i.e, sleep, shutdown, etc)

This issue is caused primarily by CMOS's failure and its "end-of-life"...

### What's CMOS?

CMOS, or "Complementary Metal Oxide Semiconductor" is a "tiny" "cheap-to-replace" part in all MotherBoards... Its main function is to store BIOS, which in turn looks after "System" time, hardware and other stuffs...

### What does it do?

This program just, once in every 10 minutes, try to connect to NTP server @ `time.windows.com` and update Windows time using `win32api` found in `pywin32`.
