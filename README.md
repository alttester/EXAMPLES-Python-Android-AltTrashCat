# AltTester® Examples Tests for Android Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester® to test the Unity Endless Runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

## Prerequisites

* adb
* python3
* pip3

## Running the tests

> **Note**: The tests are meant to be run on an Android device.

❗ Starting with version 2.0.0, the AltTester® Desktop must be running on your PC while the tests are running.
1. Download and install the AltTester® Desktop from [here](https://alttester.com/downloads/), then open it.
2. Instrument the TrashCat application using the latest version of AltTester® Unity SDK - for additional information you can follow [this tutorial](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x)
3. Create a folder `app` and include the instrumented app under the folder.
4. To start the tests, depending on your OS run:
    - `./run_tests_mac.sh` on MacOS/Linux
    - `./run_tests_windows.sh` on Windows

This script will:

* try to uninstall the apk and reinstall it
* start the app
* try to create a Python virtual env and install the dependencies
* run the tests
* stop the app
