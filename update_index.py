import re

def update_html():
    with open("d:/The Road/Learning/django-rapido-mini/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Find the start of the ds-shell div
    head_end_idx = html.find('<div class="ds-shell">')
    script_start_idx = html.find('<script>', head_end_idx)

    head_content = html[:head_end_idx]
    script_content = html[script_start_idx:]

    new_body = """<div class="ds-shell">
  <aside class="ds-sidebar">
    <div class="ds-sidebar-header">
      <h1>Django<span style="font-style: normal; font-family: var(--font-code); font-size: 0.5em; display: block; margin-top: var(--sp-1);">Rapido MINI</span></h1>
      <p>Project Template 1.0</p>
      <div class="theme-toggle">
        <button class="theme-btn active" onclick="setTheme('light')">Light</button>
        <button class="theme-btn" onclick="setTheme('dark')">Dark</button>
      </div>
    </div>

    <div class="ds-nav-group">
      <div class="ds-nav-label">Getting Started</div>
      <nav>
        <a href="#overview" class="active">Overview</a>
        <a href="#quickstart">Quick Start</a>
        <a href="#commands">Commands</a>
      </nav>
    </div>
    <div class="ds-nav-group">
      <div class="ds-nav-label">Configuration</div>
      <nav>
        <a href="#structure">Structure</a>
        <a href="#database">Database</a>
        <a href="#environment">Environment</a>
      </nav>
    </div>
    <div class="ds-nav-group">
      <div class="ds-nav-label">Development</div>
      <nav>
        <a href="#docker">Docker</a>
        <a href="#auth">Authentication</a>
        <a href="#admin-ui">Admin UI</a>
      </nav>
    </div>
    <div class="ds-nav-group">
      <div class="ds-nav-label">Reference</div>
      <nav>
        <a href="#guides">Guides</a>
        <a href="#customization">Customization</a>
        <a href="#workflow">Workflow</a>
        <a href="#troubleshooting">Troubleshooting</a>
      </nav>
    </div>
  </aside>

  <main class="ds-main">
    <div class="ds-page-header">
      <div class="ds-eyebrow">Django Rapido MINI V1.0</div>
      <h1>
        <strong>Lightweight</strong>
        Project Template
        <span class="sub">Django 5.2 · REST APIs · Unfold Admin</span>
      </h1>
      <p class="ds-page-desc">A lightweight, production-ready Django project template designed for quick project setup. Perfect for smaller projects that don't need all the bells and whistles.</p>
      <div class="ds-meta">
        <span class="ds-badge">v1.0</span>
        <span class="ds-badge accent">Python 3.10+</span>
        <span class="ds-badge">Django 5.2</span>
        <span class="ds-badge">SQLite/PostgreSQL</span>
      </div>
    </div>

    <!-- OVERVIEW -->
    <section id="overview" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">01</span><span class="ds-section-tag">Overview</span></div>
      <h2>Core <em>Features</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="feature-grid">
        <div class="feature-card"><h4>Django 5.2 & DRF</h4><p>Latest Django framework along with Django REST Framework to build REST APIs quickly.</p></div>
        <div class="feature-card"><h4>Unfold Admin</h4><p>Modern, beautiful Django admin interface with dark mode support and enhanced filtering.</p></div>
        <div class="feature-card"><h4>Ready Database</h4><p>SQLite by default, ready to use out of the box. Easy switch to PostgreSQL for production.</p></div>
        <div class="feature-card"><h4>Auth & Docs</h4><p>Token-based auth with custom user model. Auto-generated API documentation with DRF Spectacular.</p></div>
      </div>
    </section>

    <!-- QUICK START -->
    <section id="quickstart" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">02</span><span class="ds-section-tag">Quick Start</span></div>
      <h2>Get <em>Started</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="section-content">
        <p><strong>Prerequisites:</strong> Python 3.10+ on Windows, macOS, or Linux.</p>
      </div>
      
      <div class="ds-sub">One-command setup</div>
      <div class="code-block"><div class="code-header"><span>bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="cm"># 1. Clone the project</span>
$ git clone &lt;your-repo-url&gt;
$ cd django-rapido-mini

<span class="cm"># 2. Initialize the project</span>
$ make init

<span class="cm"># 3. Start the development server</span>
$ make run</code></pre></div>
      
      <div class="callout note"><strong>💡 What 'make init' does</strong> <p>Creates .env, generates SECRET_KEY, runs migrations, creates a superuser, and collects static files.</p></div>
      
      <div class="ds-sub">Default Credentials</div>
      <p class="section-content">After initialization, you can log in with username: <strong>admin</strong> and password: <strong>admin123</strong>. Change these in `.env` via <code>DJANGO_SUPERUSER_USERNAME</code> and <code>DJANGO_SUPERUSER_PASSWORD</code>.</p>
    </section>

    <!-- COMMANDS -->
    <section id="commands" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">03</span><span class="ds-section-tag">Commands</span></div>
      <h2>Available <em>Commands</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <table class="data-table">
        <thead><tr><th>Command</th><th>Description</th></tr></thead>
        <tbody>
          <tr><td>make install</td><td>Install Python dependencies</td></tr>
          <tr><td>make init</td><td>Initialize project (env, key, migrations, superuser)</td></tr>
          <tr><td>make run</td><td>Start development server</td></tr>
          <tr><td>make migrate</td><td>Run database migrations</td></tr>
          <tr><td>make makemigrations</td><td>Create new migrations</td></tr>
          <tr><td>make shell</td><td>Open Django shell</td></tr>
          <tr><td>make createsuperuser</td><td>Create a new superuser</td></tr>
          <tr><td>make collectstatic</td><td>Collect static files</td></tr>
          <tr><td>make clean</td><td>Remove Python cache files</td></tr>
          <tr><td>make docker-up</td><td>Start Docker services</td></tr>
          <tr><td>make docker-down</td><td>Stop Docker services</td></tr>
        </tbody>
      </table>
    </section>

    <!-- PROJECT STRUCTURE -->
    <section id="structure" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">04</span><span class="ds-section-tag">Structure</span></div>
      <h2>Project <em>Layout</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="code-block"><div class="code-header"><span>tree</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code>django-rapido-mini/
├── accounts/              # User authentication app
├── common/                # Shared utilities & base models
├── project/               # Django project settings
│   ├── settings/
│   │   ├── base.py        # Base settings
│   │   ├── local.py       # Local development
│   │   └── production.py  # Production settings
│   └── urls.py            # Main URL configuration
├── guides/                # Documentation guides
├── .env.example           # Environment variables template
├── requirements.txt       # Python dependencies
├── Makefile               # Project commands
└── docker-compose.yml     # Docker Compose configuration</code></pre></div>
    </section>

    <!-- DATABASE -->
    <section id="database" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">05</span><span class="ds-section-tag">Database</span></div>
      <h2>Database <em>Config</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="ds-sub">SQLite (Default)</div>
      <p class="section-content">Ready to use out of the box with no additional setup needed.</p>
      
      <div class="ds-sub">PostgreSQL (Production)</div>
      <p class="section-content">To switch to PostgreSQL, edit `.env` and uncomment the PostgreSQL section in <code>project/settings/base.py</code>. The `psycopg` library is already included.</p>
      <div class="code-block"><div class="code-header"><span>env</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="cm"># .env</span>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=project_db
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432</code></pre></div>
    </section>

    <!-- ENVIRONMENT -->
    <section id="environment" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">06</span><span class="ds-section-tag">Environment</span></div>
      <h2>Environment <em>Variables</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <p class="section-content">Create a <code>.env</code> file (copy from <code>.env.example</code>):</p>
      <div class="code-block"><div class="code-header"><span>env</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="cm"># Django Settings</span>
DJANGO_ENVIRONMENT=local
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

<span class="cm"># Admin Superuser</span>
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_PASSWORD=admin123</code></pre></div>
    </section>

    <!-- DOCKER -->
    <section id="docker" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">07</span><span class="ds-section-tag">Docker</span></div>
      <h2>Docker <em>Deployment</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="two-col">
        <div class="card"><h4>Quick Start</h4><pre><code>make docker-up
# App: http://localhost:8000
# Stop: make docker-down</code></pre></div>
        <div class="card"><h4>Manual Commands</h4><pre><code>make docker-build
make docker-logs
make docker-migrate
make docker-shell</code></pre></div>
      </div>
    </section>

    <!-- AUTHENTICATION -->
    <section id="auth" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">08</span><span class="ds-section-tag">Auth</span></div>
      <h2>API <em>Authentication</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <p class="section-content">The template uses Token-based authentication.</p>
      <div class="code-block"><div class="code-header"><span>HTTP</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="cm"># 1. Get Token</span>
POST /api/auth/token/
Body: {"username": "admin", "password": "admin123"}

<span class="cm"># 2. Use Token</span>
Authorization: Token your-token-here</code></pre></div>
    </section>

    <!-- ADMIN UI -->
    <section id="admin-ui" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">09</span><span class="ds-section-tag">Admin UI</span></div>
      <h2>Admin <em>Interface</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="section-content">
        <p>Access the admin at <code>/admin</code> with <strong>Unfold</strong> - a modern Django admin theme.</p>
        <ul style="list-style-type: none; padding-left: 0;">
          <li>✨ Sleek, modern UI</li>
          <li>🌙 Dark mode support</li>
          <li>🔍 Enhanced filtering and search</li>
        </ul>
      </div>
    </section>

    <!-- GUIDES -->
    <section id="guides" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">10</span><span class="ds-section-tag">Guides</span></div>
      <h2>Documentation <em>Guides</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="checklist-group">
        <h4>Check the guides/ directory for:</h4>
        <ul class="checklist">
          <li><strong>Settings Guide</strong> - Database, email, security settings</li>
          <li><strong>Models Guide</strong> - Creating and managing models</li>
          <li><strong>Serializers Guide</strong> - DRF serializer patterns</li>
          <li><strong>Views/Permissions Guide</strong> - API views and access control</li>
          <li><strong>Unfold Admin Guide</strong> - Admin customization</li>
        </ul>
      </div>
    </section>

    <!-- CUSTOMIZATION -->
    <section id="customization" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">11</span><span class="ds-section-tag">Customization</span></div>
      <h2>Project <em>Customization</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      
      <div class="ds-sub">Creating Models</div>
      <div class="code-block"><div class="code-header"><span>python</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="kw">from</span> django.db <span class="kw">import</span> models
<span class="kw">from</span> common.models <span class="kw">import</span> TimestampedModel

<span class="kw">class</span> <span class="fn">MyModel</span>(TimestampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField()</code></pre></div>

      <div class="ds-sub">Adding API Endpoints</div>
      <ol class="section-content" style="margin-left:1.5rem">
        <li>Create serializer in <code>myapp/serializers.py</code></li>
        <li>Create view in <code>myapp/views.py</code></li>
        <li>Add URLs in <code>myapp/urls.py</code></li>
        <li>Include in main <code>project/urls.py</code></li>
      </ol>
    </section>

    <!-- WORKFLOW -->
    <section id="workflow" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">12</span><span class="ds-section-tag">Workflow</span></div>
      <h2>Development <em>Workflow</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="code-block"><div class="code-header"><span>bash</span><button class="copy-btn" onclick="copyCode(this)">Copy</button></div>
<pre><code><span class="cm"># Full setup</span>
$ make install
$ make init

<span class="cm"># Daily development</span>
$ make run

<span class="cm"># After model changes</span>
$ make makemigrations
$ make migrate</code></pre></div>
    </section>

    <!-- TROUBLESHOOTING -->
    <section id="troubleshooting" class="ds-section">
      <div class="ds-section-header"><span class="ds-section-num">13</span><span class="ds-section-tag">Troubleshooting</span></div>
      <h2>Common <em>Issues</em></h2>
      <div class="ds-section-rule"><div class="line"></div><div class="dot"></div><div class="line"></div></div>
      <div class="two-col">
        <div class="card"><h4>Migration Errors</h4><p>Reset migrations (development only):</p><pre><code>make db-reset</code></pre></div>
        <div class="card"><h4>Static Files</h4><p>If static files are not loading:</p><pre><code>make collectstatic</code></pre></div>
        <div class="card"><h4>Permission Denied</h4><p>On Linux/Mac:</p><pre><code>chmod +x manage.py</code></pre></div>
        <div class="card"><h4>App Versions</h4><p>This is the MINI version. For Celery, Redis, and more, use the full Django Rapido template.</p></div>
      </div>
    </section>

    <footer style="border-top:1px solid var(--border-light); padding:var(--sp-8) 0; margin-top:var(--sp-20); text-align:center; font-family:var(--font-code); font-size:var(--text-xs); color:var(--text-tertiary);">
      Django Rapido MINI V1.0 — Lightweight Django project template.<br>
      Licensed under MIT License.
    </footer>
  </main>
</div>
"""

    with open("d:/The Road/Learning/django-rapido-mini/index.html", "w", encoding="utf-8") as f:
        f.write(head_content + new_body + script_content)

if __name__ == "__main__":
    update_html()
