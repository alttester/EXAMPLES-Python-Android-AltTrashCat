echo "==> Uninstalling the app from the device..."
adb uninstall com.altom.alttrashcat

echo "==> Installing the app on the device..."
adb install app/alttrashcat_latest.apk

echo "==> Setup ADB port forwarding..."
adb forward --remove-all 
adb forward tcp:13000 tcp:13000

echo "==> Start the app..."
adb shell am start -n com.altom.alttrashcat/com.unity3d.player.UnityPlayerActivity
sleep 10

echo "==> Create virtual env if it doesn't exist..."
[ -d alttrashcat-env ] || python -m venv alttrashcat-env

echo "==> Activate Python virtual environment and install dependencies..."
source ./alttrashcat-env/Scripts/activate
./alttrashcat-env/Scripts/python -m pip install -r requirements.txt

echo "==> Run the tests..."
./alttrashcat-env/Scripts/python -m pytest --html=test-report.html --self-contained-html

echo "==> ALL DONE!"