#!/bin/sh

echo "==> Uninstalling the app from the device..."
adb uninstall com.altom.TrashCat

echo "==> Installing the app on the device..."
adb install app/TrashCat.apk

echo "==> Setup reverse ADB port forwarding..."
adb reverse --remove-all
adb reverse tcp:13000 tcp:13000

echo "==> Start the app..."
adb shell am start -n com.altom.TrashCat/com.unity3d.player.UnityPlayerActivity
sleep 10

echo "==> Create virtual env if it doesn't exist..."
[ -d venv ] || python3 -m venv venv

echo "==> Activate Python virtual environment and install dependencies..."
source ./venv/bin/activate
./venv/bin/python -m pip install -r requirements.txt

echo "==> Run the tests..."
./venv/bin/python -m pytest tests --html=test-report.html --self-contained-html $@

echo "==> Stop the app..."
adb shell am force-stop com.altom.TrashCat

echo "remove all forwarded ports"
adb reverse --remove-all

echo "==> ALL DONE!"
