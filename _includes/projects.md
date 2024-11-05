<h2 id="projects" style="margin: 2px 0px 25px;">Projects</h2>

<div class="projects-container">
  {% for link in site.data.projects.main %}
    {% assign mod = forloop.index | modulo: 2 %}
    {% if mod == 1 %}
    <div class="row d-flex justify-content-between mb-4">
    {% endif %}
      <div class="project-card">
        {% if link.image %}
        <div class="project-image">
          <img src="{{ link.image }}" alt="{{ link.title }}">
        </div>
        {% endif %}
        <div class="project-content">
          <h3 class="project-title">{{ link.title }}</h3>
          {% if link.description %}
          <p class="project-description">{{ link.description }}</p>
          {% endif %}
          {% if link.notes %}
          <p class="project-notes"><i>{{ link.notes }}</i></p>
          {% endif %}
          <div class="project-links">
            {% if link.pdf %}
            <a href="{{ link.pdf }}" class="link-button">PDF</a>
            {% endif %}            
            {% if link.page %}
            <a href="{{ link.page }}" class="link-button">Project Page</a>
            {% endif %}
            {% if link.code %}
            <a href="{{ link.code }}" class="link-button">Code</a>
            {% endif %}
            {% if link.video %}
            <a href="{{ link.video }}" class="link-button">Video</a>
            {% endif %}
          </div>
        </div>
      </div>

    {% if mod == 0 or forloop.last %}
    </div>
    {% endif %}
  {% endfor %}
</div>

<style>
.projects-container {
  max-width: 100%;
  margin: 0 auto;
}

.row {
  display: flex;
  gap: 30px;
  margin-bottom: 40px !important;
}

.project-card {
  flex: 1;
  background: #fff;
  border: 1px solid rgba(0,0,0,0.1);
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
}

.project-image {
  width: 100%;
  height: 200px;
  overflow: hidden;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.project-content {
  padding: 20px 25px;
}

.project-title {
  font-size: 1.25rem;
  margin: 0 0 12px 0;
  color: #333;
}

.project-description {
  font-size: 0.95rem;
  color: #666;
  margin-bottom: 15px;
  line-height: 1.5;
}

.project-notes {
  color: #e74d3c;
  font-size: 0.9rem;
  margin-bottom: 15px;
}

.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.link-button {
  display: inline-block;
  padding: 5px 12px;
  background-color: #f5f5f5;
  color: #2196F3;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.link-button:hover {
  background-color: #e0e0e0;
  text-decoration: none;
}

@media (max-width: 768px) {
  .row {
    flex-direction: column;
  }
  
  .project-card {
    width: 100%;
    margin-bottom: 20px;
  }
}
</style>
