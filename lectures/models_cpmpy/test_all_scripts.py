import os
import pytest
import subprocess

# Path to the folder containing the scripts
SCRIPTS_DIR = '.'

def get_python_scripts(folder):
    """
    Get a list of all Python scripts in the specified folder, excluding this test script.
    """
    test_script_name = os.path.basename(__file__)
    return [f for f in os.listdir(folder) if f.endswith('.py') and f != test_script_name]

@pytest.mark.parametrize("script", get_python_scripts(SCRIPTS_DIR))
def test_script_execution(script):
    """
    Test that the Python script runs without errors.
    """
    script_path = os.path.join(SCRIPTS_DIR, script)
    result = subprocess.run(['python3', script_path], capture_output=True, text=True)
    assert result.returncode == 0, f"Script {script} failed with error:\n{result.stderr}"

if __name__ == "__main__":
    pytest.main()
