class PersonalWebsiteManager:
    def __init__(self, bio_data, news_data, research_data):
        self.bio_data = bio_data
        self.news_data = news_data
        self.research_data = research_data

    def generate_html(self):
        news_items = "".join(
            [
                f'<li><span>{news["date"]} - {news["content"]}</span></li>'
                for news in self.news_data
            ]
        )

        research_items = "".join(
            [
                f"""
            <article class="columns">
              <div class="column is-3">
                <figure class="image">
                  <img src="path_to_research_image" alt="Research Image">
                </figure>
              </div>
              <div class="column">
                <div class="content">
                  <p><i>{research["title"]}</i><br>{research["authors"]}<br>{research["conference"]}<br>
                  <a href="{research["links"]["project"]}" target="_blank">[<u>project</u>]</a>
                  <a href="{research["links"]["paper"]}" target="_blank">[<u>paper</u>]</a>
                  <a href="{research["links"]["code"]}" target="_blank">[<u>code</u>]</a>
                  </p>
                </div>
              </div>
            </article>
            """
                for research in self.research_data
            ]
        )

        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Haoyang Li's Homepage</title>
    <!-- Bulma Version-->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    <script src="js/menuspy.js"></script>

    <!--  css-->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://pro.fontawesome.com/releases/v5.9.0/css/all.css"
            integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
    <link href="css/style.css" rel="stylesheet" type="text/css">
    <link href="css/css.css" rel="stylesheet">
    <link href="css/svg.css" rel="stylesheet" type="text/css">
</head>

<body>
    <section class="section">
    <div class="container">
        <div class="columns">
        <div class="column is-2">
            <div class="sticky">
            <figure class="image is-128x128">
                <img class="is-rounded" src="{self.bio_data["profile_image"]}">
            </figure>
            <div class="content">
                <h3>{self.bio_data["name"]}</h3>
                <h6>{self.bio_data["chinese_name"]}</h6>
                <h6>{self.bio_data["work_place"]}</h6>
                <h6>{' / '.join(self.bio_data["research_interests"])}</h6>
            </div>
            <!-- details -->
            <div class="details">
                <h3>EMAIL</h3>
                <p><a href="mailto:{self.bio_data["email"]}">{self.bio_data["email"].replace('@', '<br>[at]').replace('.', '[dot]')}</a></p>
            </div>
            <!-- social network icons -->
            <div class="social">
                <a href="{self.bio_data["github"]}" target="_blank">
                    <span class="fab fa-github fa-2x" style="display:inline; text-decoration: none"></span>
                </a>
                <a href="{self.bio_data["scholar"]}" target="_blank">
                    <span class="fab fa-google fa-2x" style="display:inline; text-decoration: none"></span>
                </a>
                <a href="{self.bio_data["twitter"]}" target="_blank">
                    <span class="fab fa-twitter fa-2x" style="display:inline; text-decoration: none"></span>
                </a>
                <a href="{self.bio_data["linkedin"]}" target="_blank">
                    <span class="fab fa-linkedin fa-2x" style="display:inline; text-decoration: none"></span>
                </a>
            </div>
            <!-- menu -->
            <div id="sidebar" class="menu sticky is-hidden-mobile">
                <p class="menu-label"><b>Quick Links</b></p>
                <ul class="menu-list">
                <li><a href="#news">News</a></li>
                <li><a href="#intro">Intro</a></li>
                <li><a href="#research">Selected Projects</a></li>
                </ul>
            </div>
            </div>
        </div>
        <div class="column">
            <div class="content">
            <!--News-->
            <h3 id="news">News</h3>
            <ul id="news-list">
                {news_items}
            </ul>

            <!--Intro-->
            <h3 id="intro">Intro</h3>
            <p>{self.bio_data["intro"]}</p>
            <p><a href="{self.bio_data["cv"]}">[CV]</a></p>

            <!--Research-->
            <h3 id="research">Selected Projects</h3>
            <div id="research-list">
                {research_items}
            </div>
            </div>
        </div>
        </div>
    </div>
    </section>

    <script>
    var elm = document.querySelector('#sidebar');
    var ms = new MenuSpy(elm, {{
        activeClass: 'is-active'
    }});
    </script>
</body>

</html>
        """

        return html_content

    def update_bio_data(self, field, value):
        if field in self.bio_data:
            self.bio_data[field] = value
        else:
            print(f"Field '{field}' not found in bio data.")

    def add_project(self, year, title, authors, conference, links):
        self.research_data.append(
            {
                "year": year,
                "title": title,
                "authors": authors,
                "conference": conference,
                "links": links,
            }
        )

    def update_project(self, index, field, value):
        if 0 <= index < len(self.research_data):
            if field in self.research_data[index]:
                self.research_data[index][field] = value
            else:
                print(f"Field '{field}' not found in project data.")
        else:
            print(f"Project index '{index}' out of range.")

    def delete_project(self, index):
        if 0 <= index < len(self.research_data):
            del self.research_data[index]
        else:
            print(f"Project index '{index}' out of range.")

    def save_html(self, filename="index.html"):
        html_content = self.generate_html()
        with open(filename, "w") as file:
            file.write(html_content)
        print(f"HTML file '{filename}' generated successfully.")


# Example usage
if __name__ == "__main__":
    # Initial data
    bio_data = {
        "name": "Haoyang Li",
        "chinese_name": "李昊洋",
        "degree": "Undergraduate Student",
        "email": "hyli1606@gmail.com",
        "github": "https://github.com/haoyangli16",
        "scholar": "https://scholar.google.com/citations?user=3KF3AIMAAAAJ&hl=en",
        "twitter": "https://x.com/Haoyang1i",
        "linkedin": "https://www.linkedin.com/in/sfhan/",
        "cv": "path_to_your_CV",
        "intro": 'I am an undergraduate student student at XYZ University, advised by Prof. <a href="https://cseweb.ucsd.edu/~haosu/" target="_blank" style="text-decoration: underline;">Hao Su</a>. During my research, I have collaborated with various institutions and professionals in the field. My research interests include robotics, 3D reconstruction, and computer vision. I have worked on projects involving active mapping in unknown environments using 3D Gaussian splatting.',
        "profile_image": "images/haoyang_website_square.jpg",
        "research_interests": ["Health Care", "Robotics", "Embodied AI"],
        "work_place": "UC San Diego",
        "icons": {
            "github": "fab fa-github fa-2x",
            "scholar": "fab fa-google fa-2x",
            "twitter": "fab fa-twitter fa-2x",
            "linkedin": "fab fa-linkedin fa-2x",
        },
    }

    news_data = [
        {
            "date": "July, 2024",
            "content": "Started a new research project on 3D reconstruction.",
        },
        {"date": "June, 2024", "content": "Published a paper in XYZ journal."},
    ]

    research_data = [
        {
            "year": 2024,
            "title": "Active Mapping in Unknown Environments using 3D Gaussian Splatting",
            "authors": "Haoyang, Collaborator Name, Another Collaborator",
            "conference": "ICRA 2024",
            "links": {
                "project": "link_to_project",
                "paper": "link_to_paper",
                "code": "link_to_code",
            },
        }
    ]

    menu_data = {
        "news": "News",
        "intro": "Intro",
        "research": "Selected Projects",
        "work": "Work Experience",
    }

    # Create an instance of PersonalWebsiteManager
    manager = PersonalWebsiteManager(bio_data, news_data, research_data)

    # Update bio data example
    manager.update_bio_data("profile_image", "images/haoyang_website.jpg")

    # Add a new project example
    manager.add_project(
        year=2025,
        title="New Project Title",
        authors="Author1, Author2, Author3",
        conference="New Conference 2025",
        links={
            "project": "new_link_to_project",
            "paper": "new_link_to_paper",
            "code": "new_link_to_code",
        },
    )

    # Update a project example
    manager.update_project(0, "title", "Updated Project Title")

    # Delete a project example
    # manager.delete_project(1)

    # Save the updated HTML content
    manager.save_html()
