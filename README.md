# Installing on a TI-84 Plus CE Python calculator

# Requirements

- TI-84 Plus CE Python calculator
- USB cable
- TI Connect CE installed on Mac or Windows
- Calculator OS / Python App reasonably up to date

TI Connect CE can send `.py` files to a TI-84 Plus CE Python calculator and convert them to the calculator’s Python AppVar format automatically. ([Texas Instruments Education][1])

# Download the files

1. Go to: `https://github.com/markmick-gh/ti84-python-kit`
2. Click ••Code••.
3. Click ••Download ZIP••.
4. Unzip the downloaded folder.
You should see:
- display/t84disp.py
-  examples/ex01_test.py

# Send the files to the calculator

1. Open ••TI Connect CE••.
2. Connect the TI-84 Plus CE Python calculator by USB.
3. From the Menu, choose "Actions" -> Add Files from Computer
4. Drag these two files into the calculator:
- t84disp.py
- ex01_test.py

Do not send the folders themselves. Send the actual `.py` files.

# Run the example on the calculator

1. On the calculator, open the ••Python App••. "prgm", then select "2: Python App"
2. In the Python File Manager, select:
- ex01_test.py

3. Press "Run"

The example should import `display.py` and demonstrate the screen-formatting functions.

# Troubleshooting

- If `ex01_test.py` cannot import `display`, confirm that `display.py` was also sent to the calculator.
- If a file does not appear in the Python App, check whether it is in Archive; TI notes that Python AppVars execute from RAM. ([Texas Instruments Education][2])
- If transfer fails, update TI Connect CE and the calculator OS/Python App. TI’s Python App guide recommends using the latest CE Bundle. ([Texas Instruments Education][2])

[1]: https://education.ti.com/html/eguides/connectivity/TI-Connect-CE/EN/Content/EG_84_TIConnect/M_UsePython/M_UsePython.HTML?utm_source=chatgpt.com "Python"
[2]: https://education.ti.com/html/eguides/stem/innovator-python/EN/content/eg_pythonappprog/m_pyadpapp/m_pyappuse.HTML?utm_source=chatgpt.com "Using Python App"
