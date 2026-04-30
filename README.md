# Portfolio Website

A Wagtail-based portfolio website showcasing projects and skills.

## Project Structure

```
project0/
├── manage.py
├── portfolio/
│   ├── __init__.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── settings/
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── home/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   └── models.py
│   ├── search/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   └── views.py
│   ├── site_settings/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   └── models.py
│   ├── static/
│   │   └── css/
│   │       └── portfolio.css
│   └── templates/
│       ├── base.html
│       ├── 404.html
│       ├── 500.html
│       └── search/
│           └── search.html
├── portfolio-website/
│   ├── Dockerfile
│   ├── heroku.yml
│   ├── LICENSE
│   └── README.md
└── quantstats/
    └── ... (separate package)
```

## Development Roadmap

### Phase 1: Core Setup ✅
- [x] Set up Django/Wagtail project structure
- [x] Create basic apps (home, search, site_settings)
- [x] Configure settings for dev/prod
- [x] Set up templates and static files
- [x] Implement basic search functionality

### Phase 2: Content Management
- [ ] Create portfolio page types (Project, About, Contact)
- [ ] Add image galleries and media handling
- [ ] Implement blog functionality
- [ ] Add contact form with email integration

### Phase 3: Frontend Enhancement
- [ ] Improve responsive design
- [ ] Add animations and transitions
- [ ] Implement dark/light theme toggle
- [ ] Optimize for performance

### Phase 4: Advanced Features
- [ ] Add analytics integration
- [ ] Implement SEO optimization
- [ ] Add social media sharing
- [ ] Create admin dashboard improvements

### Phase 5: Deployment & Maintenance
- [ ] Set up CI/CD pipeline
- [ ] Configure production deployment
- [ ] Add monitoring and logging
- [ ] Implement backup strategies

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run development server:
   ```bash
   python manage.py runserver
   ```

5. Access admin at: http://localhost:8000/admin/

## Technologies Used

- Django 4.0+
- Wagtail CMS
- Bootstrap 5
- Font Awesome
- Google Fonts