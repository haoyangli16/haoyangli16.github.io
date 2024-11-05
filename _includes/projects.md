<h2 id="projects" style="margin: 2px 0px -15px;">Projects</h2>

<div class="projects-container">
  <div class="row d-flex justify-content-between mb-5">
    {% for link in site.data.projects.main %}
      {% assign mod = forloop.index | modulo: 2 %}
      
      <div class="card d-inline-block px-0" style="width: 49%;">
        {% if link.image %}
        <img class="card-img-top" src="{{ link.image }}" alt="{{ link.title }}">
        {% endif %}
        
        <div class="card-body">
          <p class="card-text paper-title">{{ link.title }}</p>
          {% if link.description %}
          <p class="card-text">{{ link.description }}</p>
          {% endif %}
          
          {% if link.notes %}
          <p class="card-text"><strong><i style="color:#e74d3c">{{ link.notes }}</i></strong></p>
          {% endif %}
          
          <div class="links">
            {% if link.pdf %}
            <a href="{{ link.pdf }}" class="link-item">PDF</a>
            {% endif %}
            
            {% if link.code %}
            <a href="{{ link.code }}" class="link-item">Code</a>
            {% endif %}
            
            {% if link.page %}
            <a href="{{ link.page }}" class="link-item">Project Page</a>
            {% endif %}
            
            {% if link.video %}
            <a href="{{ link.video }}" class="link-item">Video</a>
            {% endif %}
          </div>
        </div>
      </div>

      {% if mod == 0 %}
        </div><div class="row d-flex justify-content-between mb-5">
      {% endif %}
    {% endfor %}
  </div>
</div>

<style>
.projects-container {
  margin-top: 30px;
}

.card {
  border: 1px solid rgba(0,0,0,.125);
  border-radius: 8px;
  transition: transform 0.2s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.card-img-top {
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  height: 200px;
  object-fit: cover;
}

.paper-title {
  font-size: 1.1rem;
  font-weight: bold;
  margin-bottom: 10px;
}

.links {
  margin-top: 15px;
}

.link-item {
  display: inline-block;
  padding: 5px 10px;
  margin: 0 5px 5px 0;
  border-radius: 4px;
  background-color: #f8f9fa;
  color: #007bff;
  text-decoration: none;
  font-size: 0.9rem;
  transition: background-color 0.2s;
}

.link-item:hover {
  background-color: #e9ecef;
  text-decoration: none;
}
</style>
