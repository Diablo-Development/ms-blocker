# ms-blocker
A script that adds a set of entries to the hostsfile for windows that blocks multiple telementry domains called within Windows 11

Windows 11 makes multiple requests a minute to databrokers logging unknown data for "training purposes". To prevent windows 11 from making these requests, this simple script will prevent these domains from being interacted with by redirecting them via hostmod.

## Usage

Download and extract the release.zip file made with pyinstaller from the latest release or [here]("https://github.com/Diablo-Development/ms-blocker/releases/download/release/release.zip)

Either run as administrator or elevate the process via the UAC request to allow for modifications to the host file

Once executed restart your pc to allow for the effects to take place