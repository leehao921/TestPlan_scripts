# SMT

###  Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Breif Code Introduction: `importOtherTestplan.py`](#introduction-to-importothertestplanpy)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed [Anaconda](https://www.anaconda.com/products/individual).
- You have a terminal or command prompt installed on your computer.

## Installation

Follow these steps to set up your environment and install the necessary dependencies:

### Step 1: Create an Anaconda Environment

1. Open your terminal or command prompt.
2. Create a new Anaconda environment with Python 3.6.8:

    ```bash
    conda create --name {envname} python=3.6.8
    ```

3. Activate the environment:

    ```bash
    conda activate {envname}
    ```

### Step 2: 世界最大男性交友平台 github


1. Navigate to the directory where you want to clone the repository:

    ```bash
    cd path/to/your/directory
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/leehao921/TestPlan_scripts.git
    ```

3. Navigate into the cloned repository:

    ```bash
    cd your-repo
    ```

### Step 3: Install the Requirements

1. Ensure you are in the project directory where the `requirements.txt` file is located.
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

After setting up the environment and installing the dependencies, you can start running your Python scripts:

1. Ensure you are in the Anaconda environment:

    ```bash
    conda activate {envname}
    ```

2. Run your Python script:

    ```bash
    python XXX.py
    ```

## Additional Information

- If you encounter any issues, ensure that you have correctly followed each step.
- You can deactivate the Anaconda environment using:

    ```bash
    conda deactivate
    ```

- For any additional setup or specific instructions related to your project, refer to the project's documentation.

## Introduction to `importOtherTestplan.py`

The `importOtherTestplan.py` script is designed to import various test plan specifications from different file types. It utilizes several helper functions and classes to process these files and integrate them into a cohesive test plan.

### Key Functions and Classes

- **importWafSpec**: Imports wafer specifications from a given file.
- **importDieSpec**: Imports die specifications from a given file.
- **importTstSpec**: Imports test specifications from a given file.
- **importPrbSpec**: Imports probe specifications from a given file.
- **importTpxFile**: Handles the import of multiple file types, including support for multiple files of the same type.
- **exportWafSpec, exportDieSpec, exportTstSpec, exportPrbSpec**: Export the respective specifications to a target directory.
- **exportTpx**: Exports the complete test plan to a target directory.

### Implementation of Multi-file Import

The `importTpxFile` function in `importOtherTestplan.py` has been implemented to handle multi-file imports. It checks if the file paths are provided as a list or a single string. If multiple files are provided, it processes each file individually:

```python
def importTpxFile(self, filesMap: {}, flagsMap: {}):
    # waf
    if 'waf' in filesMap and filesMap['waf']:
        if isinstance(filesMap['waf'], list):
            for file in filesMap['waf']:
                if not self.importWafSpec(file, filesMap["mapping"]):
                    return False, self.err
        else:
            if not self.importWafSpec(filesMap['waf'], filesMap["mapping"]):
                return False, self.err

    # die
    if 'die' in filesMap and filesMap['die']:
        if isinstance(filesMap['die'], list):
            for file in filesMap['die']:
                if not self.importDieSpec(file, False):
                    return False, self.err
        else:
            if not self.importDieSpec(filesMap['die'], False):
                return False, self.err

    # tst
    if 'tst' in filesMap and filesMap['tst']:
        if isinstance(filesMap['tst'], list):
            for file in filesMap['tst']:
                if not self.importTstSpec(file, filesMap['mapping'], filesMap['limit'], filesMap['template'], flagsMap['skipComment']):
                    return False, self.err
        else:
            if not self.importTstSpec(filesMap['tst'], filesMap['mapping'], filesMap['limit'], filesMap['template'], flagsMap['skipComment']):
                return False, self.err

    # prb
    if 'prb' in filesMap and filesMap['prb']:
        if isinstance(filesMap['prb'], list):
            for file in filesMap['prb']:
                if not self.importPrbSpec(file, False):
                    return False, self.err
        else:
            if not self.importPrbSpec(filesMap['prb'], False):
                return False, self.err

    # testplan
    if self.tpx_waf or self.tpx_die or self.tpx_tst or self.tpx_prb:
        self.tpx = tpx.TestPlan(self.tpx_waf, self.tpx_die, self.tpx_tst, self.tpx_prb)
    else:
        return False, 'Please select at least one spec file !'
    return True, ''
# Conclution
exe中的內容無法做任何編輯，只能請原廠那邊重新編輯，但是串接的python script 已經完成，並且完成相關測試。

