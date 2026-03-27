import re
import os

html_path = 'index.html'
css_path = 'css/style.css'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update <head>
html = html.replace('<title>John Doe - Personal CV Website Template</title>', '<title>Jakisasarma - Portfolio</title>')
html = html.replace('<meta content="Free Website Template" name="keywords">', '<meta content="Jakisasarma, Portfolio, Video Editing, Graphic Design, Motion Graphics" name="keywords">')
html = html.replace('<meta content="Free Website Template" name="description">', '<meta content="Portfolio of Jakisasarma, a Graphic Design student specializing in video editing and digital content creation." name="description">')

# Update fonts
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Averia+Serif+Libre:wght@400;700&family=Poppins&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">'
)

# 2. Update Sidebar
html = html.replace('alt="Image"', 'alt="Jakisasarma"')
html = html.replace('<h1 class="mt-2">John Doe</h1>', '<h1 class="mt-2 text-white">Jakisasarma</h1>')

html = html.replace(
    '<div class="typed-text d-none">Web Designer, Web Developer, Front End Developer, Apps Designer, Apps Developer</div>',
    '<div class="typed-text d-none">Video Editor, Motion Graphics Designer, Graphic Designer, Visual Storyteller, Digital Content Creator</div>'
)

html = html.replace(
    '<a href="https://htmlcodex.com/downloading/?item=1492" class="btn btn-block btn-scroll">Download Pro</a>',
    '<a href="#contact" class="btn btn-block btn-scroll">Contact Me</a>'
)

# 3. About Me section
old_about_p = '<p>Sea et gubergren justo invidunt at amet clita. Justo sit justo tempor et invidunt voluptua, lorem voluptua ipsum gubergren et est nonumy magna et vero, sit eos dolor sea sed et dolor erat et. Accusam accusam magna aliquyam eirmod amet est kasd dolore sanctus. Lorem ea vero lorem eos eos sanctus labore. Aliquyam vero ipsum dolor duo clita consetetur stet, aliquyam ipsum sea sed et magna amet dolor.</p>'
new_about_p = '<p class="lead">I am a Graphic Design student at a Technical College with a strong passion for video editing and digital content creation. I specialize in video production, motion graphics, and visual storytelling, aiming to create impactful digital experiences. My goal is to secure practical experience, collaborate on creative projects, and grow within the media and design industry. When I am not designing or editing, you can find me playing cricket or gardening to stay active and inspired.</p>'
html = html.replace(old_about_p, new_about_p)

# About Info Row
old_about_info = """<div class="row">
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Name:</h5> John Doe
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Birthday:</h5> 1 April 1990
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Degree:</h5> Master
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Experience:</h5> 10 Years
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Phone:</h5> +012 345 6789
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Email:</h5> info@example.com
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Address:</h5> 123 Street, New York, USA
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Freelance:</h5> Available
                                </div>
                            </div>"""

new_about_info = """<div class="row">
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Name:</h5> Jakisasarma
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Focus:</h5> Video Editing
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Degree:</h5> Graphic Design Student
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Interests:</h5> Cricket & Gardening
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Phone:</h5> +012 345 6789
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Email:</h5> hello@example.com
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Location:</h5> Technical College City
                                </div>
                                <div class="col-sm-6 py-1">
                                    <h5 class="d-inline text-primary">Freelance:</h5> Available
                                </div>
                            </div>"""
html = html.replace(old_about_info, new_about_info)

# 4. Skills
old_skills = """<div class="col-sm-6">
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">HTML</p>
                                    <p class="mb-2">95%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">CSS</p>
                                    <p class="mb-2">85%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-warning" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">PHP</p>
                                    <p class="mb-2">90%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-danger" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Javascript</p>
                                    <p class="mb-2">90%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-danger" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Angular JS</p>
                                    <p class="mb-2">95%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-dark" role="progressbar" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Wordpress</p>
                                    <p class="mb-2">85%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-info" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                        </div>"""

new_skills = """<div class="col-sm-6">
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Adobe Premiere Pro</p>
                                    <p class="mb-2">95%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="95" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Adobe Illustrator</p>
                                    <p class="mb-2">90%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Adobe Photoshop</p>
                                    <p class="mb-2">85%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="85" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">Adobe InDesign</p>
                                    <p class="mb-2">80%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">MS Office</p>
                                    <p class="mb-2">90%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                            <div class="skill mb-4">
                                <div class="d-flex justify-content-between">
                                    <p class="mb-2">HTML & CSS</p>
                                    <p class="mb-2">70%</p>
                                </div>
                                <div class="progress">
                                    <div class="progress-bar bg-primary" role="progressbar" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100"></div>
                                </div>
                            </div>
                        </div>"""

html = html.replace(old_skills, new_skills)

# 5. Education / Experience
html = html.replace('<h2 class="title position-relative pb-2 mb-4">Expericence</h2>', '<h2 class="title position-relative pb-2 mb-4">Experience & Education</h2>')

old_exp = """<div class="border-left border-primary pt-2 pl-4 ml-2">
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1">Web Designer</h5>
                                    <p class="mb-2">Soft Company | <small>2000 - 2050</small></p>
                                    <p>Tempor eos dolore amet tempor dolor tempor. Dolore ea magna sit amet dolor eirmod. Eos ipsum est tempor dolor. Clita lorem kasd sed ea lorem diam ea lorem eirmod duo sit ipsum stet lorem diam</p>
                                </div>
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1">Web Designer</h5>
                                    <p class="mb-2">Soft Company | <small>2000 - 2050</small></p>
                                    <p>Tempor eos dolore amet tempor dolor tempor. Dolore ea magna sit amet dolor eirmod. Eos ipsum est tempor dolor. Clita lorem kasd sed ea lorem diam ea lorem eirmod duo sit ipsum stet lorem diam</p>
                                </div>
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1">Web Designer</h5>
                                    <p class="mb-2">Soft Company | <small>2000 - 2050</small></p>
                                    <p>Tempor eos dolore amet tempor dolor tempor. Dolore ea magna sit amet dolor eirmod. Eos ipsum est tempor dolor. Clita lorem kasd sed ea lorem diam ea lorem eirmod duo sit ipsum stet lorem diam</p>
                                </div>
                            </div>"""

new_exp = """<div class="border-left border-primary pt-2 pl-4 ml-2 timeline-box">
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">Graphic Design Student</h5>
                                    <p class="mb-2 text-dark font-weight-bold">Technical College | <small>Present</small></p>
                                    <p>Studying the fundamentals and advanced techniques of graphic design, typography, and visual communication. Participating in hands-on projects and collaborating with peers to develop a strong creative foundation.</p>
                                </div>
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">Freelance Video Editor</h5>
                                    <p class="mb-2 text-dark font-weight-bold">Self-Employed | <small>2022 - Present</small></p>
                                    <p>Editing video content for local organizations, producing motion graphics, and assisting with post-production workflows. Focused on delivering compelling visual experiences for digital platforms.</p>
                                </div>
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">Digital Content Creator</h5>
                                    <p class="mb-2 text-dark font-weight-bold">Various Projects | <small>2021 - Present</small></p>
                                    <p>Creating engaging social media content, designing promotional materials, and experimenting with diverse media formats to capture audience attention and communicate key messages.</p>
                                </div>
                            </div>"""
html = html.replace(old_exp, new_exp)

# 6. Subscribe section: change Newsletter context slightly
html = html.replace('<p class="text-white">Subscribe and get my latest article in your inbox</p>', '<p class="text-white">Subscribe and get my newest design projects and video releases directly in your inbox.</p>')

# 7. Services
old_services = """<div class="col-md-6 service-item text-center mb-3">
                            <i class="fa fa-2x fa-laptop-code mx-auto mb-4"></i>
                            <h5 class="mb-2">Web Design</h5>
                            <p>Justo sit justo eos amet tempor amet clita amet ipsum eos elitr. Amet lorem lorem lorem est amet labore</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3">
                            <i class="fab fa-2x fa-android mx-auto mb-4"></i>
                            <h5 class="mb-2">Apps Development</h5>
                            <p>Justo sit justo eos amet tempor amet clita amet ipsum eos elitr. Amet lorem lorem lorem est amet labore</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3">
                            <i class="fa fa-2x fa-search mx-auto mb-4"></i>
                            <h5 class="mb-2">SEO</h5>
                            <p>Justo sit justo eos amet tempor amet clita amet ipsum eos elitr. Amet lorem lorem lorem est amet labore</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3">
                            <i class="fa fa-2x fa-edit mx-auto mb-4"></i>
                            <h5 class="mb-2">Content Creating</h5>
                            <p>Justo sit justo eos amet tempor amet clita amet ipsum eos elitr. Amet lorem lorem lorem est amet labore</p>
                        </div>"""

new_services = """<div class="col-md-6 service-item text-center mb-3 glass-card">
                            <i class="fa fa-2x fa-video mx-auto mb-4 text-primary"></i>
                            <h5 class="mb-2">Video Production</h5>
                            <p>Professional video editing and post-production services using Adobe Premiere Pro to create engaging visual stories.</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3 glass-card">
                            <i class="fa fa-2x fa-film mx-auto mb-4 text-primary"></i>
                            <h5 class="mb-2">Motion Graphics</h5>
                            <p>Enhancing videos and digital content with dynamic animations, text effects, and motion tracking.</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3 glass-card">
                            <i class="fa fa-2x fa-pencil-ruler mx-auto mb-4 text-primary"></i>
                            <h5 class="mb-2">Graphic Design</h5>
                            <p>Crafting compelling visual identities, illustrations, and print materials with Adobe Illustrator and Photoshop.</p>
                        </div>
                        <div class="col-md-6 service-item text-center mb-3 glass-card">
                            <i class="fa fa-2x fa-photo-video mx-auto mb-4 text-primary"></i>
                            <h5 class="mb-2">Content Creation</h5>
                            <p>Producing optimized multimedia content designed to capture attention and communicate effectively across platforms.</p>
                        </div>"""
html = html.replace(old_services, new_services)

# 8. Portfolio filters
html = html.replace('<li class="btn btn-outline-primary" data-filter=".first"><i class="fa fa-laptop-code mr-2"></i>Design</li>', '<li class="btn btn-outline-primary" data-filter=".first"><i class="fa fa-video mr-2"></i>Video</li>')
html = html.replace('<li class="btn btn-outline-primary" data-filter=".second"><i class="fa fa-mobile-alt mr-2"></i>Development</li>', '<li class="btn btn-outline-primary" data-filter=".second"><i class="fa fa-palette mr-2"></i>Design</li>')

# 9. Contact
html = html.replace('<h4 class="mb-4">Receive messages instantly with our PHP and Ajax contact form - available in the <a href="https://htmlcodex.com/downloading/?item=1492">Pro Version</a> only.</h4>', "<h4 class=\"mb-4\">I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision. Drop me a message below!</h4>")

# 10. Fix background classes for better contrast (make it slightly more elegant if needed)
# Add a dark mode section to Sidebar
html = html.replace('<div class="sidebar">', '<div class="sidebar bg-dark text-white">')
html = html.replace('<div class="sidebar-text d-flex flex-column h-100 justify-content-center text-center">', '<div class="sidebar-text d-flex flex-column h-100 justify-content-center text-center p-4">')
html = html.replace('<h4 class="typed-text-output d-inline-block text-body"></h4>', '<h4 class="typed-text-output d-inline-block text-white"></h4>')
# Clean up social links
html = html.replace('<a class="mx-2" href="#"><i class="fab fa-twitter"></i></a>', '<a class="mx-2 text-light" href="#"><i class="fab fa-twitter"></i></a>')
html = html.replace('<a class="mx-2" href="#"><i class="fab fa-facebook-f"></i></a>', '<a class="mx-2 text-light" href="#"><i class="fab fa-facebook-f"></i></a>')
html = html.replace('<a class="mx-2" href="#"><i class="fab fa-linkedin-in"></i></a>', '<a class="mx-2 text-light" href="#"><i class="fab fa-linkedin-in"></i></a>')
html = html.replace('<a class="mx-2" href="#"><i class="fab fa-instagram"></i></a>', '<a class="mx-2 text-light" href="#"><i class="fab fa-instagram"></i></a>')
html = html.replace('<a class="mx-2" href="#"><i class="fab fa-youtube"></i></a>', '<a class="mx-2 text-light" href="#"><i class="fab fa-youtube"></i></a>')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace fonts
css = css.replace('"Poppins", sans-serif', '"Inter", sans-serif')
css = css.replace('"Averia Serif Libre", cursive', '"Outfit", sans-serif')
css = css.replace('--primary: #78CC6D;', '--primary: #6366f1;')
css = css.replace('#78CC6D', '#6366f1')
css = css.replace('#4aaf3d', '#4f46e5') # Hover state

# Inject new UI refinements (Glassmorphism, Better Spacing, rounded corners for cards)
css_additions = """

/* --- Modern Custom Adjustments --- */
body {
    background-color: #f8fafc;
    color: #334155;
}

h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.02em;
}

.title.position-relative.pb-2.mb-4::after {
    background: #6366f1; /* Ensure underline matches primary theme */
    border-radius: 4px;
}

/* Glassmorphism Services Card */
.glass-card {
    background: rgba(255, 255, 255, 0.7);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.4);
    border-radius: 12px;
    padding: 30px 20px;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.05);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.1);
}

.service-item i {
    color: var(--primary);
    background: rgba(99, 102, 241, 0.1);
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    margin: 0 auto 20px auto;
    transition: all 0.3s ease;
}

.service-item:hover i {
    background: var(--primary);
    color: #fff;
    transform: scale(1.1);
}

/* Sidebar updates */
.sidebar {
    background: linear-gradient(135deg, #1e1e2f, #0f172a);
    box-shadow: inset -5px 0 15px rgba(0,0,0,0.1);
}
.sidebar .btn-scroll, .sidebar .border-right {
    color: #fff;
    font-weight: 500;
}
.sidebar .btn-scroll:hover, .sidebar .border-right:hover {
    background-color: rgba(255,255,255,0.1) !important;
}

/* Buttons */
.btn {
    border-radius: 6px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 10px 24px;
    transition: all 0.3s ease;
}

/* Portfolio & Images */
.portfolio-item {
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 10px 20px -5px rgba(0,0,0,0.1);
}
.portfolio-item img {
    transition: transform 0.5s ease;
}
.portfolio-item:hover img {
    transform: scale(1.05);
}

.progress {
    border-radius: 8px;
    height: 10px;
    background-color: #e2e8f0;
}
.progress-bar {
    border-radius: 8px;
}

/* Containers */
.container.bg-white {
    background-color: #ffffff !important;
    border-radius: 12px;
    box-shadow: 0 10px 40px -20px rgba(0,0,0,0.05);
    margin-bottom: 30px;
}

.content {
    background-color: #f8fafc;
}
"""

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css + css_additions)

print("Update completed successfully.")
