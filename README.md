## Get Started: Working with the 'VD_TEST_2_Python' Repository
You will need Python 3.9+ and Git installed.

### Step 1: Cloning the repository (for VSCode)
1. Open the command palette in VSCode by selecting "View" → "Command Palette" from the main menu.
2. Type 'Git clone' and select the corresponding menu option.
3. Clone the repository. To do this, paste the following into the panel:
    `https://github.com/VeraDataLLC/VD_TEST_2_Python.git`
4. In the File Explorer, select the destination directory for the repository.
5. VSCode will suggest opening the cloned directory in a new window.

### Step 2: Creating a virtual environment and installing dependencies
1. In VSCode, open the terminal via 'View' → 'Terminal'.
2. Create a virtual environment using the following command:
   ```bash
   python -m venv venv
   ```
3. Install the dependencies from the `requirements.txt` file using the following command:
   ```bash
   .\venv\Scripts\pip.exe install -r requirements.txt
   ```

### Step 3: Working with tasks and running tests
1. The 'tasks.py' file is where you'll write your functions. Once done, send this file to VeraData.
2. 'test_tasks.py' contains the task descriptions and tests for your functions.
3. To run the tests, use the command:
   ```bash
   .\venv\Scripts\pytest.exe
   ```
  If all tests pass successfully, it means you have correctly implemented the tasks.\
  If the tests fail, review the errors and refine your solutions.

### Step 4: Send us your results (any progress you've made)
1. Run the command below and then take a screenshot of the resulting 'vd_test_2_python_report.html' file.
    ```bash
    .\venv\Scripts\pytest.exe --html=vd_test_2_python_report.html
    ```
2. Send the screenshot and the "tasks.py" file to okachurovska@veradata.com email.
