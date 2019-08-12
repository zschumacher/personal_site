class Constants:
    FIRST_NAME = "Zach"
    NAME = f"{FIRST_NAME} Schumacher"
    # currently only supports syntax highlighting for strings, tuples and list.  All items in a collection currently
    # only green.
    TERMINAL_MAPPING = {
        "Zach.current_location": 'Kansas City, Missouri',
        "Zach.job": ("Software Engineer", "Quest Analytics"),
        "Zach.skills": [
            "python", "flask", "celery", "docker", "sql", "informatica", "ssis", "java", "git", "subversion"
        ],
        "Zach.interests": ["video games", "board games", "traveling", "coding", "kayaking"],
        "Zach.education": ("BSB Information Systems Technology", "University of Kansas")
    }
    NUM_TERMINAL_COMMANDS = len(TERMINAL_MAPPING)
    EMAIL_ADDRESS = "zschu15@gmail.com"
    EMAIL_LINK = f"mailto:{EMAIL_ADDRESS}"
    RESUME_FILENAME = "ZachResume.pdf"

    LINKS = {
        "LinkedIn": "https://www.linkedin.com/in/zachschumacher/",
        "GitHub": "https://www.github.com/zschumacher",
        "resume": f"/static/{RESUME_FILENAME}"
    }
    NUM_LINKS = len(LINKS)
