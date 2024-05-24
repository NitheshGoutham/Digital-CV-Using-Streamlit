from pathlib import Path
import io
import requests
from PyPDF2 import PdfReader
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Digital CV | NG", page_icon=":wave:")

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-img.jpg"



# Define the columns
col1, col2, col3 = st.columns(3)

# Use the columns and place the content within them
with col1:
    st.title("Nithesh Goutham M")
    st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    st.write("""
    System Engineer, assisting enterprises by supporting data-driven decision-making.
    """)
EMAIL = "nitheshgoutham2000@gmail.com"

SOCIAL_MEDIA = {
    
    "LinkedIn": "https://www.linkedin.com/in/nithesh-goutham-m-0b0514205/",
    "GitHub": "https://github.com/NitheshGoutham",
    "Resume": "https://drive.google.com/file/d/1-Xo35GVdhVGGiJpaFWnTuxFT9nk809Gy/view?usp=sharing",
    "Website": "https://digital-cv-using-streamlit.onrender.com"

}
PROJECTS = {
    "🏆 youtube data harvesting and warehousing using sql and streamlit ": "https://github.com/NitheshGoutham",
    "🏆 Face-recogition-attendance-system": "https://github.com/NitheshGoutham/Face-recogition-attendance-system-",
    "🏆 Digital CV using Streamlit": "https://github.com/NitheshGoutham/Digital-CV-Using-Streamlit",
    "🏆 Bank-Management-System": "https://github.com/NitheshGoutham/Bank-Management-System",
    "🏆 Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN": "https://github.com/NitheshGoutham/Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN",
}



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
