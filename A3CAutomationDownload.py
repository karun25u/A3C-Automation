import streamlit as st

# Set up the Streamlit application
st.title("A3C Automation in Enovia")

# Description of the application
st.write("""
This Streamlit application is designed to automate processes within Enovia using the A3C framework. 
It streamlines workflows by integrating various automation tasks into a single interface, enhancing productivity and efficiency.
""")
import streamlit as st

st.header("Instructions")
st.write("""
### Step-by-Step Guide for Using A3C Automation in Enovia

1. Download the ZIP File: Begin by downloading the ZIP file using the link provided below. This file contains all necessary components for running the A3C Automation Application.

2. Extract the ZIP File: Once the download is complete, locate the ZIP file on your computer. Right-click on the file and select 'Extract All' to unzip the contents into a designated folder.

3. Locate the Executable: Within the extracted folder, find the executable file named `A3CAutomation Application.exe`. This is the main application file that will initiate the automation process.

4. Run the Application: Double-click on the `A3CAutomation Application.exe` file to launch the application. You may be prompted by your system to confirm that you want to run the file. Proceed by clicking 'Run'.

5. Provide Required Inputs: Upon launching, the application will prompt you to enter necessary input details. Carefully fill out all required fields, ensuring that your entries are accurate.

6. Submit the Information: After entering all required information, click the 'Submit' button within the application. This action will trigger the automation sequence.

7. Chrome Automation: The application will automatically open Chrome and initiate the login process for Enovia. Enter your credentials when prompted to log in.

8. Monitor the Process: Once logged in, the automation process will begin. Monitor the progress through the application's log file, which provides detailed updates on each step. Ensure you read the log entries carefully to understand the current status and any actions taken by the automation.

9. Avoid Multiple Submissions: It is crucial not to submit the request multiple times, as this can lead to errors or unintended consequences. If the application is already running, allow it to complete the process before attempting any new actions.

10. Completion and Verification: Wait patiently until the automation process is fully completed. Verify the results and check for any discrepancies by reviewing the log file. If issues arise, consult the log for troubleshooting information.

By following these instructions, you can efficiently automate processes within Enovia using the A3C framework, ensuring a smooth and effective operation.
""")




# Button to download the file
import streamlit as st

# Specify the path to the file you want to be downloadable
file_path = "C:/Users/gummadi.vr/A3 PASS AUTOMATION/A3cAutomation.zip"

# Create a download button that allows users to download the specified file

with open(file_path, "rb") as file:
        st.download_button(
            label="Download A3C Automation Zip File",
            data=file,
            file_name="A3cAutomation.zip"
        )



