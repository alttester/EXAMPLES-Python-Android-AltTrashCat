# AltTester Examples Tests for Android Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester to test the Unity endless runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

## Prerequisites

* adb
* python3
* pip3

## Running the tests

> **Note**: The tests are meant to be run on an Android phone.

1. Install the [AltTesterDesktop](https://alttester.com/alttester/#pricing), then open it (you need to accept the Terms and Conditions if the AltTester is opened for the first time).
2. The tests are meant to be run on an Adroid device. Create a folder `app` under project. The app is provided at https://alttester.com/app/uploads/AltTester/TrashCat/TrashCatAndroid2_0_1.zip and needs to be included unzipped under the `app/` folder.
3. To start the tests, depending on your OS run:
    - `./run_tests_mac.sh on MacOS/Linux`
    - `./run_tests_windows.sh` on Windows

This script will:

* try to uninstall the apk and reinstall it
* start the app
* try to create a python virtual env and install the dependencies
* run the tests
* stop the app
