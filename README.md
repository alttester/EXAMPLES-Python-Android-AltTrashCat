# AltUnityTester Examples Tests for AltTrashCat in Python

This repository shows a few Python tests that use the page object model and AltUnityTester to test the Unity endless runner sample:
https://assetstore.unity.com/packages/essentials/tutorial-projects/endless-runner-sample-game-87901

### Running the tests on Android

The tests are meant to be run on an Android phone. The apk is provided in this repository, under the `app/` folder. 

To start the tests, depending of your OS run:

`./start_tests_Mac.sh`
or
`./start_tests_Windows.sh`


This script was tested on MacOS and it will:
- try to uninstall the apk and reinstall it
- try to create a python virtual env and install the dependencies
- run the tests

