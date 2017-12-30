# Quickstart
## Compatible with Python 3.6+

When placed in the Windows 10 Startup folder, this script will spawn a small dialog box on the desktop with "Begin" and "Quit" options.
"Begin" will open a customisable selection of (minimised) applications.

This allows the user to remove these applications from automatic startup, speeding up the booting process, and only adding the overhead when the user is not in a rush to complete a task.

Before launching any application, it first checks Task Manager to ensure the program is not already running, then calls subprocess.Popen to launch the program.
