# Personal Information
bio_data = {
    "name": "Haoyang",
    "degree": "Undergraduate student",
    "email": "your_email@gmail.com",
    "github": "https://github.com/your_github",
    "scholar": "https://scholar.google.com/citations?user=your_scholar_id&hl=en",
    "linkedin": "https://www.linkedin.com/in/your_linkedin/",
    "cv": "path_to_your_CV",
    "intro": 'I am an undergraduate student student at XYZ University, advised by Prof. <a href="https://link_to_professor_profile" target="_blank" style="text-decoration: underline;">Professor Name</a>. During my research, I have collaborated with various institutions and professionals in the field. My research interests include robotics, 3D reconstruction, and computer vision. I have worked on projects involving active mapping in unknown environments using 3D Gaussian splatting.'
}

# News Data
news_data = [
    {"date": "July, 2024", "content": "Started a new research project on 3D reconstruction."},
    {"date": "June, 2024", "content": "Published a paper in XYZ journal."}
]

# Research Data
research_data = [
    {
        "year": 2024,
        "title": "Active Mapping in Unknown Environments using 3D Gaussian Splatting",
        "authors": "Haoyang, Collaborator Name, Another Collaborator",
        "conference": "ICRA 2024",
        "links": {
            "project": "link_to_project",
            "paper": "link_to_paper",
            "code": "link_to_code"
        }
    }
]

# Function to generate HTML content
def generate_html(bio_data, news_data, research_data):
    news_items = ''.join([f'<li><span>{news["date"]} - {news["content"]}</span></li>' for news in news_data])
    
    research_items = ''.join([
        f'''
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
        ''' for research in research_data])

    html_content = f'''
    <!DOCTYPE html>
    <html>

    <head>
      <meta charset="utf-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{bio_data["name"]}'s Homepage</title>
      <link href="css/bootstrap.css" rel='stylesheet' type='text/css' />
      <!--<link rel="shortcut icon" href="../images/fav_icon.png" type="image/x-icon">-->
      <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
      <!-- Bulma Version 0.7.5-->
      <link rel="stylesheet" href="https://unpkg.com/bulma@0.7.5/css/bulma.min.css" />
      <link href='css/style.css' rel='stylesheet' type='text/css'>
      <script defer src="font-awesome-5.9.0/js/brands.min.js"></script>
      <script defer src="font-awesome-5.9.0/js/fontawesome.min.js"></script>
      <script src="js/menuspy.js"></script>
    </head>

    <body>
      <section class="section">
        <div class="container">
          <div class="columns">
            <div class="column is-2">
              <div class="sticky">
                <figure class="image is-128x128">
                  <img class="is-rounded" src="http://hansf.me/images/sfphoto.jpg">
                </figure>
                <div class="content">
                  <h3>{bio_data["name"]}</h3>
                  <h6>{bio_data["degree"]}</h6>
                </div>
                <!-- details -->
                <div class="details">
                  <h3>EMAIL</h3>
                  <p><a href="mailto:{bio_data["email"]}">{bio_data["email"].replace('@', '[at]').replace('.', '[dot]')}</a></p>
                </div>
                <!-- social network icons -->
                <div class="social">
                  <a href="{bio_data["github"]}" target="_blank">
                    <span class="fab fa-github fa-2x" style="display:inline; text-decoration: none"></span>
                  </a>
                  <a href="{bio_data["scholar"]}" target="_blank">
                    <span class="fab fa-google fa-2x" style="display:inline; text-decoration: none"></span>
                  </a>
                  <a href="{bio_data["linkedin"]}" target="_blank">
                    <span class="fab fa-linkedin fa-2x" style="display:inline; text-decoration: none"></span>
                  </a>
                </div>

                <div id="sidebar" class="menu sticky is-hidden-mobile">
                  <p class="menu-label"><b>Quick Links</b></p>
                  <ul class="menu-list">
                    <li><a href="#news">News</a></li>
                    <li><a href="#intro">Intro</a></li>
                    <li><a href="#research">Research</a></li>
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
                <p>{bio_data["intro"]}</p>
                <p><a href="{bio_data["cv"]}">[CV]</a></p>

                <!--Research-->
                <h3 id="research">Research</h3>
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
    '''
    
    return html_content

# Generate the HTML content
html_content = generate_html(bio_data, news_data, research_data)

# Save to an HTML file
with open('index.html', 'w') as file:
    file.write(html_content)

print("HTML file generated successfully.")
