from pathlib import Path
import requests
from PyPDF2 import PdfReader
import io
import streamlit as st

# Set Streamlit page configuration at the very beginning
st.set_page_config(page_title="PDF Reader", page_icon="📄")

# Function to download file from Google Drive
def download_file_from_google_drive(file_id, local_path):
    download_url = f'https://drive.google.com/uc?export=download&id={file_id}'
    response = requests.get(download_url)
    
    if response.status_code == 200:
        with open(local_path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(f"Failed to download file. Status code: {response.status_code}")

# Function to validate PDF file
def is_pdf_valid(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)
            return True
    except Exception as e:
        return False

# Extracted Google Drive file ID from the provided link
file_id = '1pyC9WtCBh-fgsE6w1LMQWP_K9WUkqHXv'
local_file_path = 'downloaded_file.pdf'

# Download and validate PDF file
try:
    download_file_from_google_drive(file_id, local_file_path)
except Exception as e:
    st.error(f"Failed to download file: {e}")
    st.stop()

if is_pdf_valid(local_file_path):
    try:
        with open(local_file_path, 'rb') as file:
            reader = PdfReader(file)
            pdf_text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                pdf_text += page.extract_text() + "\n"
            st.text_area("Extracted PDF Text", pdf_text, height=300)
    except FileNotFoundError:
        st.error(f"File {local_file_path} not found.")
    except Exception as e:
        st.error(f"An error occurred while reading the PDF file: {e}")
else:
    st.error("The downloaded file is not a valid PDF.")





# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | NG"
PAGE_ICON = ":wave:"
NAME = "Nithesh Goutham"
DESCRIPTION = """
System Engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "nitheshgoutham2000@gmail.com"
SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/nithesh-goutham-m-0b0514205/",
    "GitHub": "https://github.com/NitheshGoutham",
    "Website": "https://twitter.com"

}
PROJECTS = {
    "🏆 youtube data harvesting and warehousing using sql and streamlit ": "https://github.com/NitheshGoutham",
    "🏆 Face-recogition-attendance-system": "https://github.com/NitheshGoutham/Face-recogition-attendance-system-",
    "🏆 Digital CV using Streamlit": "https://github.com/NitheshGoutham",
    "🏆 Bank-Management-System": "https://github.com/NitheshGoutham/Bank-Management-System",
    "🏆 Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN": "https://github.com/NitheshGoutham/Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open("downloaded_file.pdf") as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open("C:\\Users\\Nisha Preetha M\\DIgital_CV\\assets\\CV.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open("C:\\Users\\Nisha Preetha M\\DIgital_CV\\assets\\profile-img.jpg")


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("C:\\Users\\Nisha Preetha M\\DIgital_CV\\assets\\profile-img.jpg", width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- Summary ---
st.write('\n')

st.write("---") 

st.subheader("Summary")
st.write(
    """
- ✔️ Dedicated and proactive Systems Engineer with over 2 years of experience in designing, implementing, and maintaining complex IT systems
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# ---- Qualification---
st.write('\n')
st.write("---") 

st.subheader("Qualification")
st.write(
    """
- 👩‍💻  
    - ►Rajalakshmi Engineering College, Chennai
    - ►Bachelor of Engineering in ECE 2018 – 2022
    - ►CGPA: 8.2/10

- 👩‍💻  
    - ►Jeeva Velu Residential School, Tiruvannamalai

    - ►HSC, 2017 – 2018
    - ►Score : 83.67 %
- 👩‍💻  
    - ►Jeeva Velu Residential School, Tiruvannamalai

    - ►SSLC, 2015-2016
    - ►Score : 94 %

"""
)

# --- SKILLS ---
st.write('\n')


st.subheader("Hard Skills")
st.write("---")

st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas,Numpy)
- 📊 Data Visulization: Citrix XenDesktop & XenApps
- 📚 Web: HTML, CSS , Stremlit
- 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Atos Global IT Solution , Chennai**")
st.write("🚧", "**System Engineer | Cirtix Support Engineer**")
st.write("12/2023 - Present")
st.write(
    """
- ► Administered and maintained Citrix infrastructure for optimal performance, ensuring seamless access to applications and desktops for end-users
- ► Engaged in regular updates and patch management to ensure the Citrix environment's stability and compliance
- ► Conducted routine monitoring, performance tuning, and capacity planning to optimize Citrix infrastructure
- ► Hands-on experience in configuring and managing Citrix Cloud services, storefront including XenApp and Xen Desktop

"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Associate Engineer | L1 Service Desk**")
st.write("12/2022 - 11/2023")
st.write(
    """
- ► logging diagnosing and managing incoming end-user requests 
- ► Identifying calls as either Service Request or Incident 
- ► Prioritizing calls against agreed upon Service Levels Agreements 
- ► Determining the Priority level of the Incident.
- ► Determining the action required to resolve tickets 
- ► Escalations and referral to other parts of the organization 
- ► Managing issues through to resolution
- ► Monitoring and status tracking of registered tickets

"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Trainee | Active Directory Support**")
st.write("07/2022 - 11/2022")
st.write(
    """
- ► Maintenance and support of Active Directory Federated Services, related hardware, and technologies 
- ► Maintenance and support of DNS
- ► Top Level OU Management 
- ► Migration Issues
- ► Security Scans
- ► Certificate Administration 
- ► DHCP Servers

"""
)

# --- Certificates ---
st.write('\n')


st.subheader("Certificates")
st.write("---")

st.write(
    """

- ► Microsoft Certified: Azure Fundamentals (AZ-900)
- ► Microsoft Certified: Azure Administrator Associate (AZ-104)
- ► Microsoft Certified: Azure Virtual Desktop Specialty (AZ-140)
- ► Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900)
- ► Microsoft 365 Certified: Fundamentals (MS-900)
- ► Microsoft Certified: Azure Data Fundamentals (DP-900)


"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
