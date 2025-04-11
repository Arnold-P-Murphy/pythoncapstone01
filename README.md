# pythoncapstone01
capstone for python course
✅ Step-by-Step Execution in VS Code

🧱 1. Prerequisites
Make sure:

You have Python 3.x installed.

You’ve installed VS Code and the Python extension.

You’ve saved the image (capstone_coins.png) into the images/ folder.


📁 2. Folder Structure Should Look Like:


coin_identifier/
├── images/
|   └── capstone_coins.png
├── output/
│   └── (will contain: detected_coins.png, detection_log.txt)
├── utils/
│   └── coin_utils.py
├── coin_detector.py
├── requirements.txt

🐍 3. Create Virtual Environment
✅ For Windows:
python -m venv venv

venv\Scripts\activate

✅ For macOS/Linux:

python3 -m venv venv

source venv/bin/activate


You should now see (venv) in your terminal prompt.

📦 4. Install Dependencies

pip install -r requirements.txt

🧠 
🧪 6. Run the Script
In your terminal (with venv activated):

python coin_detector.py

✅ 7. Results
After running:

💾 output/detected_coins.png: Image with labeled coins and total value.

📄 output/detection_log.txt: Text log with coin values and info.

🖼 A pop-up window will show the image with labels.

✅ Console will print save confirmation.

❌ To Exit the Virtual Environment

deactivate
