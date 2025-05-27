import streamlit as st
from PIL import Image

# Page config
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="wide")

# Load profile image
#profile_pic = Image.open("assets/profile.jpg")

# Sidebar
with st.sidebar:
    #st.image(profile_pic, width=150)
    st.title("Your Name")
    st.write("📍 Location")
    st.write("📧 your.email@example.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/yourprofile)")
    st.write("🐦 [Twitter](https://twitter.com/yourhandle)")
    st.write("💻 [GitHub](https://github.com/yourusername)")

# Main Content
st.title("👨‍💼 Portfolio")

# Summary
st.header("📝 Summary")
st.write("""
Passionate and results-driven professional with experience in [your field].
Skilled in problem-solving, collaboration, and building scalable solutions.
Always eager to learn and take on new challenges.
""")

# Education
st.header("🎓 Education")
st.write("""
**Bachelor of Technology in Computer Science**  
XYZ University, 2018 – 2022  
CGPA: 8.5/10  
""")

# Experience
st.header("💼 Experience")
st.write("""
**Software Engineer** – ABC Company  
*June 2022 – Present*  
- Built scalable APIs with Flask and deployed on AWS  
- Reduced system downtime by 30% with better monitoring tools

**Intern** – DEF Startup  
*Jan 2022 – May 2022*  
- Contributed to frontend development with React  
- Automated manual processes using Python scripts
""")

# Skills
st.header("🛠️ Skills")
cols = st.columns(3)
skills = [
    ["Python", "Java", "C++"],
    ["Django", "Streamlit", "Flask"],
    ["MySQL", "MongoDB", "PostgreSQL"]
]
for col, skill_set in zip(cols, skills):
    for skill in skill_set:
        col.markdown(f"- {skill}")

# Projects
st.header("🚀 Projects")
st.subheader("Project Title 1")
st.image("assets/project1.png", width=500)
st.write("""
Built a [short description] using [technologies].  
Key features include X, Y, and Z.  
[🔗 GitHub](https://github.com/yourusername/project1)
""")

st.subheader("Project Title 2")
st.write("""
Built a [short description] using [technologies].  
Improved performance by 40%.  
[🔗 GitHub](https://github.com/yourusername/project2)
""")

# Certifications
st.header("📜 Certifications")
st.write("""
- AWS Certified Developer – Associate  
- Google Data Analytics Professional Certificate  
- Coursera: Machine Learning by Andrew Ng  
""")

# Achievements
st.header("🏆 Achievements")
st.write("""
- Top 10 Finalist at XYZ Hackathon  
- Published research paper in ABC Journal  
- Winner of CodeSprint 2023  
""")

# Hobbies
st.header("🎯 Hobbies")
st.write("""
- Playing Chess ♟️  
- Traveling & Photography 📸  
- Reading Tech Blogs 📚  
""")

# Footer
st.markdown("---")
st.caption("Created with ❤️ using Streamlit")

