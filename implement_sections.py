import os
import re

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Define HTML for Work Experience
work_experience_html = """
                <!-- Work Experience Start -->
                <div class="container bg-white py-5 mt-4">
                    <div class="row px-3">
                        <div class="col-12">
                            <h2 class="title position-relative pb-2 mb-4">Work Experience</h2>
                        </div>
                        <div class="col-12">
                            <div class="border-left border-primary pt-2 pl-4 ml-2 timeline-box">
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">[Earliest Job Title]</h5>
                                    <p class="mb-2 text-dark font-weight-bold">[Company/Organization Name] | <small>[Start Year] - [End Year]</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Major Achievements:</strong> [e.g., Successfully led the redesign of 3 internal newsletters]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Responsibilities:</strong> [e.g., Managed daily graphic asset creation]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Impact Metrics:</strong> [e.g., Increased engagement by 15%]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Relevant Skills:</strong> [e.g., Adobe Photoshop, Communication]</li>
                                    </ul>
                                </div>
                                <div class="position-relative mb-0">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">[Most Recent Job Title]</h5>
                                    <p class="mb-2 text-dark font-weight-bold">[Company/Organization Name] | <small>[Start Year] - Present</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Major Achievements:</strong> [e.g., Delivered 5 commercial motion graphic campaigns]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Responsibilities:</strong> [e.g., Directing post-production workflows]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Impact Metrics:</strong> [e.g., Campaigns generated over 10,000 views]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Relevant Skills:</strong> [e.g., Premiere Pro, After Effects]</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Work Experience End -->
"""

# Define HTML for Certifications
certifications_html = """
                <!-- Certifications Start -->
                <div class="container bg-white py-5 mt-4">
                    <div class="row px-3">
                        <div class="col-12">
                            <h2 class="title position-relative pb-2 mb-4">Certifications</h2>
                        </div>
                        <div class="col-12">
                            <div class="border-left border-primary pt-2 pl-4 ml-2 timeline-box">
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">[Earliest Certification Name]</h5>
                                    <p class="mb-2 text-dark font-weight-bold">[Issuing Organization] | <small>[Issue Date]</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Validity Period:</strong> [e.g., Valid until Dec 2028]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Credential ID:</strong> [e.g., AZ-1049583]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Verification:</strong> <a href="#" class="text-primary">[URL Link]</a></li>
                                    </ul>
                                </div>
                                <div class="position-relative mb-0">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">[Most Recent Certification Name]</h5>
                                    <p class="mb-2 text-dark font-weight-bold">[Issuing Organization] | <small>[Issue Date]</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Validity Period:</strong> [e.g., Does not expire]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Credential ID:</strong> [e.g., PR-9038475]</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i><strong>Verification:</strong> <a href="#" class="text-primary">[URL Link]</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Certifications End -->
"""

# We'll inject Work Experience and Certifications exactly after Education.
# Change "Experience & Education" title to just "Education" now that Experience is heavily separated
html = html.replace('<h2 class="title position-relative pb-2 mb-4">Experience & Education</h2>', '<h2 class="title position-relative pb-2 mb-4">Education</h2>')

target_comment = '<!-- Education End -->'
if target_comment in html:
    html = html.replace(target_comment, target_comment + '\\n' + work_experience_html + '\\n' + certifications_html)

# Now, we also update the "Projects" section formatting inside the Portfolio section to adhere to the methodology.
# In the portfolio overlay, we add placeholder areas mapping to the methodology.
old_portfolio_btn_1 = """<h4 class="text-white mb-2 font-weight-bold">2026 Showreel</h4>
                                            <p class="text-white-50 px-4 mb-3 small">A high-energy editing sizzle reel demonstrating pacing, color grading, and dynamic motion graphics.</p>"""

new_portfolio_btn_1 = """<h4 class="text-white mb-2 font-weight-bold">[Earliest Project]</h4>
                                            <p class="text-white-50 px-4 mb-1 small text-left"><strong>Scope:</strong> [e.g. 2-week turnaround]</p>
                                            <p class="text-white-50 px-4 mb-1 small text-left"><strong>Tools:</strong> [e.g. Premiere Pro]</p>
                                            <p class="text-white-50 px-4 mb-3 small text-left"><strong>Result:</strong> [e.g. 500+ organic views]</p>"""

old_portfolio_btn_2 = """<h4 class="text-white mb-2 font-weight-bold">Brand Explainer</h4>
                                            <p class="text-white-50 px-4 mb-3 small">Custom vector illustrations built in Illustrator and brought to life with complex keyframing in After Effects.</p>"""

new_portfolio_btn_2 = """<h4 class="text-white mb-2 font-weight-bold">[Recent Project]</h4>
                                            <p class="text-white-50 px-4 mb-1 small text-left"><strong>Scope:</strong> [e.g. 1-month campaign]</p>
                                            <p class="text-white-50 px-4 mb-1 small text-left"><strong>Tools:</strong> [e.g. After Effects]</p>
                                            <p class="text-white-50 px-4 mb-3 small text-left"><strong>Result:</strong> [e.g. 30% brand awareness boost]</p>"""

html = html.replace(old_portfolio_btn_1, new_portfolio_btn_1)
html = html.replace(old_portfolio_btn_2, new_portfolio_btn_2)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML structure for all sections successfully injected.")
