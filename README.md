# AltTester Examples Tests for Android Build with Python Tests

This repository shows a few Python tests that use the page object model and AltTester to test the Unity endless runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

## Prerequisites

* adb
* python3
* pip3

## Running the tests

> **Note**: The tests are meant to be run on an Android phone.

Create a folder `app` under project

The app is provided at https://altom.com/app/uploads/AltTester/TrashCat/TrashCatAndroid.zip and needs to be included unzipped under the app/ folder.

To start the tests, depending of your OS run:

* `./run-tests-mac.sh` on MacOS/Linux
* `./run-tests-windows.sh` on Windows

This script will:

* try to uninstall the apk and reinstall it
* start the app
* try to create a python virtual env and install the dependencies
* run the tests
* stop the app
