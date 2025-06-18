import streamlit as st

# Set up the Streamlit application
st.title("A3C Automation in Enovia")

# Description of the application
st.write("""

This Streamlit application is designed to automate the A3C Automation Process in Enovia. It streamlines workflows by integrating various automation tasks into a single interface, enhancing productivity and efficiency.

""")
import streamlit as st

st.header("Instructions")
st.write("""
### Step-by-Step Guide for Using A3C Automation in Enovia

1. Download the ZIP File: Click on the provided link to download the ZIP file containing the A3C Automation Application components.

""")
url="https://pgone.sharepoint.com/:u:/s/ProjectX305-A3CPassAutomation/EdR5Fm4UU8tAkdICK2VyXhoBfcIfPJKeUHVDnWhmEKqwxg?e=3Nh7rP"

st.markdown(
    f'<a href="{url}" target="_blank">'
    '<button style="padding: 10px 20px; font-size: 16px;">Open A3C Automation Zip File</button>'
    '</a>',
    unsafe_allow_html=True
)
st.write("""
         
2. Extract the ZIP File:
Locate the downloaded ZIP file on your computer.
Right-click on the file and select 'Extract All' to unzip it into a designated folder.
         
3. Locate the Executable:
Navigate to the extracted folder.
Find the executable file named `A3CAutomation Application.exe`

4. Run the Application:
Double-click the `A3CAutomation Application.exe` file to launch the application.
If prompted by your system, confirm by clicking 'Run'.
         
5. Provide Required Inputs:
Enter the necessary input details as prompted by the application.
Ensure all entries are accurate.
         
6. Submit the Information:
Click the 'Submit' button to trigger the automation sequence.
         
7. Chrome Automation:
The application will automatically open Chrome and start the login process for Enovia.
Enter your credentials when prompted.
         
8. Monitor the Process:
Observe the automation progress through the application flow.
Read log entries carefully to understand the current status and actions taken.
         
9. Avoid Multiple Submissions:
Do not submit the request multiple times. Wait for the current process to complete before initiating new actions.
         
10. Completion and Verification:
Wait for the automation process to finish.
Review the log file for results and check for any discrepancies.
If issues arise, consult the log for troubleshooting information.
         
By following these instructions, you can efficiently automate processes within Enovia using the A3C framework, ensuring a smooth and effective operation.
""")




# Button to download the file
import streamlit as st

# Specify the path to the file you want to be downloadable
import streamlit as st
import requests
from io import BytesIO

# URL of the file you want to download



url="https://pgone.sharepoint.com/:p:/s/ProjectX305-A3CPassAutomation/EYD2TUVlFQlBpN9ycQ9uY0gB2vSbfAth-7gD5cynoF3cxQ?e=gfVY5N"

st.markdown(
    f'<a href="{url}" target="_blank">'
    '<button style="padding: 10px 20px; font-size: 16px;">Open A3C Automation Flow Overview</button>'
    '</a>',
    unsafe_allow_html=True
)


