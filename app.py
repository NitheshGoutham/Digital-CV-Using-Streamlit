
from pathlib import Path
import io
import requests
from PyPDF2 import PdfReader
import streamlit as st
from streamlit_option_menu import option_menu

# Set the page configuration
st.set_page_config(page_title="Digital CV | NG", page_icon=":wave:")
#set up the sidebar with optionmenu
with st.sidebar:
    selected = option_menu("MainMenu",
                            options=["Summary","Professional Experience","Skills","Projects","Certificates","Education","Connect"],
                            default_index=1,
                            orientation="vertical",)
    
if selected=="Professional Experience":

    st.subheader(":red[Professional Experience]")
    st.write('\n')
    c1,c2,c3=st.columns(3)     
    with c1:
        st.image('https://lh3.googleusercontent.com/p/AF1QipM6kkYG5l9XSAS5EOFjgi3VzCks59mh9uv_2Hen=s1360-w1360-h1020',use_column_width=True)
    with c2:
        st.image('https://lh3.googleusercontent.com/p/AF1QipMMIjJL7X2MuXq69LYj7g1ynusSTygUHzJ91O6r=s1360-w1360-h1020',use_column_width=True)
    with c3:
        st.image('https://lh3.googleusercontent.com/p/AF1QipOi4v5fefzn_sdvr7smbo8f6H57LPu3MvMW7vj0=s1360-w1360-h1020',use_column_width=True)


    st.link_button(label='Official Website',url='https://atos.net/en/india',use_container_width=True)
    st.subheader("**Atos Global IT Solution , :red[Chennai]**")
    st.subheader(" June'22 - September'24 ")
    st.subheader("**:red[System Engineer]**")
    st.write("🚧", "**:red[ Cirtix Support Engineer]**")
    st.write(
        """
    -  Administered and maintained Citrix infrastructure for optimal performance, ensuring seamless access to applications and desktops for end-users
    -  Engaged in regular updates and patch management to ensure the Citrix environment's stability and compliance
    -  Conducted routine monitoring, performance tuning, and capacity planning to optimize Citrix infrastructure
    -  Hands-on experience in configuring and managing Citrix Cloud services, storefront including XenApp and Xen Desktop
    -  Monitored system operations and generated daily and weekly performance reports.
    -  Maintained related Windows networking and established remote accessibility.
    -  Identified and resolved LAN and WAN network issues affecting Citrix network.
    -  Daily maintenance and troubleshooting of the servers in Citrix
    -  Developed and maintained disaster recovery plans and procedures to ensure business continuity in case of system failures.


    """
    )

    st.write('\n')
    st.write("🚧", "**:red[L1 Service Desk]**")
    st.write(
        """
    
    -  Acted as the first point of contact for end-users via phone, email, or ticketing system.
    -  Achieved a 75% first-call resolution rate, improving user satisfaction and reducing escalations.
    -  Diagnosed and troubleshot IT issues related to hardware, software, network, and peripherals.
    -  Escalated complex issues to L2/L3 teams with thorough documentation.
    -  Serve as the first point of contact for end-users seeking technical assistance via phone, email, or ticketing system.
    -  Log, categorize, and prioritize incidents and service requests in the ticketing system, ensuring accurate documentation and timely resolution
    -  Assist with user account tasks such as password resets, account unlocks, and basic Active Directory maintenance.
    -  Participated in on-call rotation to provide 24/7 support for critical Citrix infrastructure issues.

    """
    )

    
   
    
if selected=="Summary":
    
    st.title(":red[Nithesh] Goutham M ")
    st.subheader( "System :red[Enginner]")
    st.subheader(':red[Summary]')
    st.markdown(''' Dedicated and proactive professional with over 2 years of experience in system engineering, focusing on Citrix administration, Active Directory, and service desk support. 
                    I have a strong foundation in designing, implementing, and maintaining IT infrastructures, with expertise in server configuration, network management, and virtualization technologies like VMware and Hyper-V. 
                    Throughout my career, I’ve developed excellent problem-solving skills, often using automation tools like PowerShell and Python to streamline tasks and improve operational efficiency..''')
    st.markdown('''Recently, I’ve shifted my focus towards data science, earning a certification from GUVI’s Master Data Science Program. I’ve gained hands-on experience with machine learning, statistical modeling, and predictive analytics, and I’m proficient in Python and SQL. 
                    My goal is to apply these skills to drive insights and improve business outcomes through data-driven decision-making.''')

    st.markdown('''Additionally, I’ve completed an MBA in HRM, further fueling my interest in the management side of technology and operations. 
                    I am eager to explore roles that combine my technical expertise with leadership and strategic decision-making in management.''')
   
    st.markdown('''With a keen interest in cloud technologies, I’m also exploring certifications like AZ-104 and AZ-140 to deepen my understanding of Azure and cloud-based solutions. 
                    I am actively seeking roles in data science and management, where I can leverage my technical background, data science skills, and leadership potential to contribute effectively to organizational growth.''')
    st.markdown('''Let’s connect and discuss how my diverse skills, certifications, and management insights align with your organization’s needs.''')
    



if selected =="Education":

    st.subheader(':red[Rajalakshmi Engineering College, Chennai]')
    st.markdown('Bachelor of Engineering in ECE 2018 – 2022')
    st.markdown('CGPA: 8.2/10')

    c1,c2,c3=st.columns(3)     
    with c1:
        st.image('https://www.rajalakshmi.org/image/banner-1.jpg',use_column_width=True)
    with c2:
        st.image('https://i.ytimg.com/vi/ek6h-WNRR1Y/maxresdefault.jpg',use_column_width=True)
    with c3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTzGqaQ9cskQMFXWvsVAXUSJxTxpIpoCT-qEg&s',use_column_width=True)


    st.link_button(label='Official Website',url='https://www.rajalakshmi.org/',use_container_width=True)

    st.subheader(':red[Jeeva Velu Residential School, Tiruvannamalai]')
    st.markdown('HSC, 2017 – 2018')
    st.markdown('Score : 83.67 %')

    st.write("---") 

    st.markdown('SSLC, 2015 – 2016')
    st.markdown('Score : 94 %')
    c1,c2,c3=st.columns(3)     
    with c1:
        st.image('https://content.jdmagicbox.com/comp/tiruvannamalai/v6/9999p4175.4175.121017112458.v9v6/catalogue/jeeva-velu-international-school-mathur-tiruvannamalai-cbse-schools-3evijsp.jpg',use_column_width=True)
    with c2:
        st.image('https://lh3.googleusercontent.com/p/AF1QipPKer1AIQouiDnhd1BwdgAWpCYvAwlXOZfIa4ax=s1360-w1360-h1020',use_column_width=True)
    with c3:
        st.image('https://lh3.googleusercontent.com/p/AF1QipNPHby3FyJeKbU64VUH1zNUP0gZ7-rY83cfkM8l=s1360-w1360-h1020',use_column_width=True)


    st.link_button(label='Official Website',url='https://jeevavelu.org/',use_container_width=True)

    st.subheader(':red[Pondicheery University - PUDDE , Puducherry]')
    st.markdown('Master of Business Administration in Human Resource Management 2022 – 2024')
    st.markdown('CGPA: 8/10')

    c1,c2,c3=st.columns(3)     
    with c1:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwwMfsijW45v84aLYFEu2OjWJnl7j68WkPSQ&s',use_column_width=True)
    with c2:
        st.image('https://www.pv-magazine-india.com/wp-content/uploads/sites/8/2021/09/PHOTO-2021-09-14-15-28-11-1200x675.jpg',use_column_width=True)
    with c3:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReXZfqaF2v_kwNu0Ss0DJ5pKHRgUvxQ2ayrw&s',use_column_width=True)


    st.link_button(label='Official Website',url='https://dde.pondiuni.edu.in/',use_container_width=True)


if selected == "Projects":
    st.subheader('Projects & Accomplishments')

    with st.container():
        with st.expander(':red[***Digital CV using Streamlit***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>Upon completion of the project, the user will have a fully interactive and visually appealing digital CV hosted via Streamlit.
                         The digital CV will enhance the user's professional presence by offering a more engaging and modern alternative to traditional resumes. Viewers will be able to interact with the CV, explore the user's skills, experience, and achievements in a dynamic way, and download a PDF version if needed. 
                        This project will also serve as a demonstration of the user's ability to integrate programming skills and data visualization into real-world applications, showcasing technical capabilities for future career opportunities.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Digital CV',url='https://digital-cv-using-streamlit.onrender.com/',use_container_width=True)

        with st.expander(':red[***K-Means Clustering: Airline-Customer-Value-Analysis***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project aims to analyze airline customer value using K-Means clustering to segment customers based on factors such as travel frequency, spending habits, ticket preferences, and loyalty status. By identifying distinct customer segments, the model will help airlines optimize marketing strategies, tailor loyalty programs, and enhance customer experience.
                            The model will also be designed to adapt to evolving customer behaviors and trends, allowing airlines to continuously refine their customer segmentation over time.''',unsafe_allow_html=True)
            
            st.link_button(label='Airline Customer Segmentation',url='https://github.com/NitheshGoutham/Airline-Customer-Segmentation',use_container_width=True)

        with st.expander(':red[***Singapore Reslae Flat Price Predicting***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project will deliver a machine learning model capable of predicting the resale prices of flats in Singapore based on features such as location, size, flat type, age, and nearby amenities. 
                        The model will assist buyers, sellers, and real estate professionals in making informed pricing decisions.The model will be designed to integrate additional data (e.g., future real estate trends, government policies) to improve its accuracy over time, making it adaptable to Singapore’s evolving housing market.
                        This project will serve as a showcase of the user's expertise in data science, machine learning, and real-world problem-solving, enhancing their portfolio and demonstrating practical skills in predictive modeling and real estate analytics.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Flat Price Predicting',url='https://singapore-resale-flat-prices-predicting-600l.onrender.com/',use_container_width=True)

        with st.expander(':red[***Industrial Copper Modeling***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project will deliver a machine learning model capable of accurately predicting copper prices based on historical data, market trends, macroeconomic indicators, and industry-specific variables. 
                        This model can be used by businesses in the industrial sector to forecast copper price fluctuations and make more informed purchasing and investment decisions.
                        Through data analysis, the project will reveal the most influential factors driving copper price changes, such as supply-demand dynamics, global trade policies, currency exchange rates, and production levels. 
                        Understanding these factors will provide strategic insights for stakeholders. The model will provide actionable predictions that can help companies plan inventory, manage risk, and optimize their operations by anticipating copper price changes. 
                        This will support cost-saving strategies and improve budgeting accuracy.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Copper Modeling',url='https://github.com/NitheshGoutham/Industrial-Copper-Modeling',use_container_width=True)
            
        with st.expander(':red[***Airbnb Analysis***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project will deliver an interactive and visually rich Power BI dashboard that provides insights into Airbnb listings, performance metrics, and key market trends. Users will be able to explore data through dynamic charts, graphs, and heat maps, enabling deeper analysis and decision-making.
                        The use of Power BI’s geospatial mapping features will provide visual insights into the distribution of Airbnb listings by region and proximity to key attractions. This will help investors understand location-based performance and identify potential opportunities in untapped areas.
                        The final report and dashboard will be a practical example of the user’s ability to apply business intelligence and data visualization techniques to real-world scenarios, showcasing their expertise in turning raw data into actionable business insights. This can be used to enhance their portfolio and demonstrate their analytical skills to potential employers or clients.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Airbnb Analysis',url='https://github.com/NitheshGoutham/Airbnb-Analysis-Using-PowerBi',use_container_width=True)

        with st.expander(':red[***PhonePe Pulse Data***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The analysis will yield detailed insights into digital transactions across various categories such as payments, merchant transactions, and peer-to-peer transfers.
                        The project will break down transaction volumes by sectors such as e-commerce, travel, utilities, and retail, helping businesses understand how PhonePe is used across industries. This can guide businesses in tailoring their digital payment strategies according to sector trends.
                         This will help in understanding transaction trends, user behavior, and regional transaction preferences.The project will reveal regional variations in PhonePe transactions, identifying which states and cities have the highest transaction volumes and user engagement.
                         This insight can be valuable for strategic decisions, such as marketing campaigns or service enhancements in underperforming regions.Completing this project will enhance the user's portfolio by showcasing their ability to work with large datasets, perform insightful analyses, and deliver business intelligence that can drive decision-making in the fintech space.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='PhoenPe Pulse Data',url='https://github.com/NitheshGoutham/Phonepe-Pulse-Data',use_container_width=True)

        with st.expander(':red[***Youtube Data Harvesting & Warehousing***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project will establish an automated pipeline for harvesting YouTube data (e.g., video details, comments, likes, views, and channel statistics) at scale. This system will allow for continuous, scheduled collection of large amounts of data directly from YouTube's API, providing valuable insights for content creators, marketers, and analysts.
                        The project will provide insights into key performance metrics such as viewership trends, engagement rates (likes, comments, shares), and subscriber growth for different YouTube channels and videos. This will help content creators and brands understand what drives engagement and optimize their content strategies accordingly.
                        The data pipeline and warehouse will be designed to scale with growing data needs, allowing for the integration of new data sources or metrics as YouTube evolves. This ensures the system will remain relevant and adaptable to future requirements.
                        This project will serve as a practical demonstration of the user's expertise in data engineering, warehousing, and analytics. It will showcase their ability to handle large-scale data harvesting, design data architecture, and deliver actionable insights, thus enhancing their professional portfolio and proving their skills in real-world business intelligence and analytics.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Youtube Data Harvesting',url='https://github.com/NitheshGoutham/youtube-data-harvesting-warehousing-using-streamlit',use_container_width=True)

        with st.expander(':red[***Sentinel-2 Data Processing***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project will implement a Convolutional Neural Network (CNN) to classify land cover in Sentinel-2 imagery, specifically distinguishing mangrove forests from other vegetation and land types. The CNN's ability to recognize spatial patterns will result in high accuracy for detecting and mapping mangrove regions.
                        The CNN will be used to analyze multi-temporal Sentinel-2 data, allowing for automated detection of changes in mangrove forest coverage over time. This will help monitor deforestation, regeneration, or damage caused by natural disasters or human activities.
                        The use of CNN for mangrove analysis will deliver actionable insights to conservationists and policymakers. The model’s outputs will contribute to better-informed conservation efforts, helping protect and manage vital mangrove ecosystems, which are crucial for biodiversity, coastal protection, and carbon sequestration.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Sentinel-2 Data Processing',url='https://github.com/NitheshGoutham/Sentinel-2-Data-Processing-for-Pichavaram-Mangrove-Forest-Using-CNN',use_container_width=True)
            
        with st.expander(':red[***Flask and Streamlit CRUD Application-***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>TThe project will deliver a full-stack application that enables efficient data management through a user-friendly interface. Using Flask as the backend, the application will handle CRUD (Create, Read, Update, Delete) operations, facilitating dynamic data interactions in real time. Streamlit will provide the frontend, offering a seamless and interactive user experience for managing records.
                        The project is designed for scalability and could be adapted for various applications, including employee databases, product inventories, and customer relationship management. The MySQL database is structured to securely store and manage records, while the Flask API ensures fast and reliable data processing.
                        This project will serve as a showcase of the user's skills in web development, API integration, data management, and building efficient workflows. It demonstrates proficiency in backend/frontend integration and practical expertise in deploying robust data management solutions, adding depth to the user's data engineering and application development portfolio.''',unsafe_allow_html=True)
            
            st.link_button(label='Flask and Stermalit CRUD',url='https://github.com/NitheshGoutham/Flask-and-Streamlit-CRUD-Application-',use_container_width=True)
            
        with st.expander(':red[***Face Recognition Attendance System***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The system will provide an automated solution for tracking attendance using face recognition technology. It will accurately log attendance in real-time as individuals are recognized by the system, eliminating the need for manual check-ins or sign-ins.
                        The system will incorporate security measures to ensure that face recognition data is handled securely and privately. This will include data encryption, secure storage, and compliance with privacy regulations to protect individuals' biometric information.
                        The project will showcase the user's ability to integrate cutting-edge technologies—face recognition and voice synthesis—into a cohesive system. This will demonstrate their skills in applying AI and machine learning to practical problems, enhancing their professional portfolio.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Face Recognition Attendance',url='https://github.com/NitheshGoutham/Face-recogition-attendance-system-',use_container_width=True)

        with st.expander(':red[***Bank Management System***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The system will provide a functional implementation of core banking operations, including account creation, balance checking, deposits, withdrawals, and transaction history management. These operations will be handled using basic Python data structures such as lists, dictionaries, and tuples.
                        While the system uses basic Python data structures, it will be designed with scalability in mind. The code structure will be modular, allowing for easy expansion and enhancements, such as adding new features or improving the UI.
                        By completing this project, the user will showcase their proficiency in Python programming and their ability to design and implement a functional system using basic data structures. This will enhance their portfolio and demonstrate their problem-solving skills.
                        ''',unsafe_allow_html=True)
            
            st.link_button(label='Bank Management System',url='https://github.com/NitheshGoutham/Bank-Management-System',use_container_width=True)

        with st.expander(':red[***A Study on Employees Training and Deveopment with Refernce to Saehan Stamping Limited***]'):
            st.markdown('''<h6 style='color:grey;font-size:18px'>The project investigates the impact of training and development programs on employees at Saehan Stamping Limited.
                             It examines how these initiatives enhance employee skills, performance, and job satisfaction, contributing to overall organizational growth. The study also provides recommendations to improve the effectiveness of current training practices, aiming to foster a more skilled and productive workforce.''',unsafe_allow_html=True)
            
            st.link_button(label='Employees T & D',url='https://github.com/NitheshGoutham/A-STUDY-ON-EMPLOYEES-TRAINING-AND-DEVELOPMENT-',use_container_width=True)




if selected=="Connect":

    
    st.markdown('''<h6 style='color:grey;font-size:22px'>Hi there,<br>

I’m Nithesh Goutham M, with experience in system engineering, focusing on Citrix administration, Active Directory, and service desk roles. Currently, I’m transitioning into the field of data science engineering. I have strong skills in data analysis, machine learning, and predictive modeling, and I’m continuously expanding my expertise through projects and certifications, including cloud technologies and data science tools.

I’m actively seeking opportunities in data science roles, where I can apply my analytical and problem-solving skills to drive impactful insights and solutions. Let’s connect and discuss how my experience and interests can align with your organization's goals!

Best regards,   
Nithesh Goutham M   
+919566679191   
nitheshgoutham2000@gmail.com   


                        ''',unsafe_allow_html=True)
    st.write('\n')

    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.link_button('Linkedin','https://www.linkedin.com/in/nithesh-goutham-m-0b0514205/') 
    with col2:
        st.link_button('Github','https://github.com/NitheshGoutham')
    with col3:
        st.link_button('Website','https://digital-cv-using-streamlit.onrender.com/')  
    with col4:
        st.link_button('Resume','https://drive.google.com/file/d/1JCBmLEyoyDTHa0XKjUvLaBUIqQ-PErHQ/view?usp=sharing') 


    image ="https://media.licdn.com/dms/image/C4D03AQFGL6pXJ3UwJQ/profile-displayphoto-shrink_200_200/0/1628655140308?e=2147483647&v=beta&t=kdCHSHzz9GRtptCjTFk4sdDPq0OIYbQv2q0RVtiwICI"

# Display the image with a reduced size
    st.image(image, width=200 ) 


if selected == "Skills":
    st.subheader("Skills")
    
    # Using a container
    with st.container():
        st.markdown("### :red[Programming Languages]", unsafe_allow_html=True)  # Styled heading

    # Expander for skills
    with st.expander("Programming Languages"):
        st.write('''
        - Python
        - SQL 
       ''')
    with st.container():
        st.markdown("### :red[Data Manipulation and Analysis]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Data Manipulation and Analysis"):
        st.write('''
        - Pandas (Python)
        - NumPy
        - Data Wrangling
        - Data Cleaning
        ''')
    with st.container():
        st.markdown("### :red[Statistical Analysis]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Statistical Analysis"):
        st.write('''
        - Descriptive and Inferential Statistics
        - Hypothesis Testing
        - Probability Theory
        - Regression Analysis (Linear, Logistic)
        ''')

    with st.container():
        st.markdown("### :red[Machine Learning]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Machine Learning"):
        st.write('''
        - Supervised Learning (Regression, Classification)
        - Unsupervised Learning (Clustering, Dimensionality Reduction)
        - Ensemble Methods (Random Forest, XGBoost)
        - Neural Networks (optional for deep learning)
        - Model Evaluation Metrics (Accuracy, Precision, Recall, F1-score, ROC-AUC)
        ''')
    with st.container():
        st.markdown("### :red[Data Visualization]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Data Visualization"):
        st.write('''
        - Matplotlib (Python)
        - Seaborn (Python)
        - Plotly
        - Power BI / Tableau 
        ''')
    with st.container():
        st.markdown("### :red[Database Management]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Database Management"):
        st.write('''
        - SQL (PostgreSQL, MySQL)
     ''')

    with st.container():
        st.markdown("### :red[Cloud Platforms]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Cloud Platforms"):
        st.write('''
        - Microsoft Azure 
        - Citrix
     ''')

    with st.container():
        st.markdown("### :red[Data Engineering]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Data Engineering"):
        st.write('''
        - ETL (Extract, Transform, Load) processes
        - Apache Kafka (for real-time data streaming)
     ''')

    with st.container():
        st.markdown("### :red[Natural Language Processing (NLP)]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view NLP"):
        st.write('''
        - Text Preprocessing (Tokenization, Lemmatization, etc.)
        - Word Embeddings (Word2Vec, GloVe)
        - Sentiment Analysis
     ''')
     
    with st.container():
        st.markdown("### :red[Deep Learning]", unsafe_allow_html=True)

    # Expander for skills
    with st.expander("Click to view Deep Learning"):
        st.write('''
        - TensorFlow / Keras
        - PyTorch
     ''')
     
     
    with st.container():
    
        st.markdown("### :red[Ticketing Tools]", unsafe_allow_html=True)  

    # Expander for skills
    with st.expander("Click to view Ticketing Tools"):
        st.write('''
        - Service Now 
        - NICE
        - Genesys
        ''')


    with st.container():
        st.markdown("### :red[Web]", unsafe_allow_html=True)  

    # Expander for skills
    with st.expander("Click to view Web"):
        st.write('''
        - Streamlit
        - HTML
        - CSS
        ''')

   



if selected=="Certificates":


    st.subheader("Certificates")
    
    st.subheader(':red[***Master Data Science Program***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'>The certification provides a comprehensive understanding of key data science concepts, including data analysis, machine learning, statistical modeling, and data visualization. It covers essential tools and technologies such as Python, R, SQL, and popular machine learning algorithms. 
            The program also emphasizes real-world applications, helping participants develop practical skills for solving complex data-driven problems. ''',unsafe_allow_html=True)
    st.link_button(label='Data Science',url='https://www.guvi.in/share-certificate/0497J024114L03b8V9',use_container_width=True)


   
    
    st.subheader(':red[***Microsoft Certified: Azure Fundamentals***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'>The certification provides a solid understanding of fundamental cloud computing concepts, including the benefits of cloud services, the differences between various cloud service models (IaaS, PaaS, SaaS), and deployment models (public, private, hybrid).
                        ''',unsafe_allow_html=True)
    st.link_button(label='AZ-900',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/76E4EACFAA96828B?sharingId=287514430F2C5672',use_container_width=True)


    st.subheader(':red[***Microsoft 365 Certified: Fundamentals***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'>This certification enables you to contribute to your organization’s digital transformation by implementing cloud-based solutions that improve collaboration, security, and compliance. You'll be positioned to advocate for the adoption of Microsoft 365 solutions and ensure they align with organizational goals.
                You will understand the different pricing options and licensing models for Microsoft 365 services, including business and enterprise plans. This will also cover support options and methods for resolving issues that arise within Microsoft 365.''',unsafe_allow_html=True)
    st.link_button(label='MS-900',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/4A4B03CD72235B0B?sharingId=287514430F2C5672',use_container_width=True)


    st.subheader(':red[***Microsoft Certified: Azure Administrator Associate***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'> The certification process ensures that your knowledge is current with the latest Azure technologies and best practices, which is important in the rapidly evolving field of cloud computing.
                It provides a comprehensive understanding of Azure services and administration, which is essential for working in cloud environments. This knowledge is foundational for many roles in IT and cloud computing.
                Overall, studying for and achieving the AZ-104 certification can be a significant asset in building a career in cloud computing and IT.''',unsafe_allow_html=True)
    st.link_button(label='AZ-104',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/CB82F1F614C4B016?sharingId=287514430F2C5672',use_container_width=True)


    st.subheader(':red[***Microsoft Certified: Azure Virtual Desktop Specialty***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'>This certification is beneficial for roles such as Azure Virtual Desktop Administrator or Cloud Infrastructure Engineer, where expertise in virtual desktop environments is required.
                 Azure Virtual Desktop is a key component of many organizations’ cloud strategies, so expertise in this area can be highly valuable.
                 It provides specialized skills for managing Azure Virtual Desktop environments, which are becoming increasingly important as remote work and virtualization continue to grow.''',unsafe_allow_html=True)
    st.link_button(label='AZ-140',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/784900D13054A668?sharingId=287514430F2C5672',use_container_width=True)


    st.subheader(':red[***Microsoft Certified: Security, Compliance, and Identity Fundamentals***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'>The Microsoft Certified: Security, Compliance, and Identity Fundamentals (SC-900) certification is aimed at individuals who want to understand the basics of security, compliance, and identity concepts within the Microsoft ecosystem.
                Learn about compliance principles and how Microsoft solutions can help organizations meet regulatory requirements. This includes understanding compliance frameworks and how to implement compliance solutions in Microsoft environments.
                Get an overview of how to implement and manage security, compliance, and identity solutions in Microsoft environments, including basic tasks and responsibilities.''',unsafe_allow_html=True)
    st.link_button(label='SC-900',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/C8E21911142D5B92?sharingId=287514430F2C5672',use_container_width=True)

    st.subheader(':red[***Microsoft Certified: Azure Data Fundamentals***]')
    st.markdown('''<h6 style='color:grey;font-size:18px'> The Microsoft Certified: Azure Data Fundamentals certification is designed to validate your foundational knowledge of core data concepts and how they are implemented using Microsoft Azure data services. 
                Learn about various Azure data services, including Azure SQL Database, Azure Cosmos DB, Azure Data Lake, and Azure Synapse Analytics.You'll understand how different data storage solutions work in Azure and how to choose the appropriate service for your needs.
                Get acquainted with different data processing options available in Azure, such as batch and stream processing.
                Understand the basic principles of data security and compliance in Azure, including data encryption and access controls.''',unsafe_allow_html=True)
    st.link_button(label='DP-900',url='https://learn.microsoft.com/api/credentials/share/en-us/MNitheshGoutham-3071/7F4BD48D91B6A7B?sharingId=287514430F2C5672',use_container_width=True)





