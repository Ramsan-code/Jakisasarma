import os
import re

html_path = 'index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new content
new_exp = """<div class="border-left border-primary pt-2 pl-4 ml-2 timeline-box">
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">G.C.E. Ordinary Level</h5>
                                    <p class="mb-2 text-dark font-weight-bold">V/Vipulananntha College | <small>2018</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Completed comprehensive foundational education covering core academic subjects</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Developed essential analytical, mathematical, and linguistic capabilities</li>
                                    </ul>
                                </div>
                                <div class="position-relative mb-4">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">G.C.E. Advanced Level (Arts)</h5>
                                    <p class="mb-2 text-dark font-weight-bold">V/Vipulananntha College | <small>2019 - 2022</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Focused on specialized subjects within the Arts and Humanities stream</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Cultivated advanced written communication, critical thinking, and research skills</li>
                                    </ul>
                                </div>
                                <div class="position-relative mb-0">
                                    <i class="fa fa-arrow-right text-primary position-absolute" style="top: 3px; left: -24px;"></i>
                                    <h5 class="mb-1 text-primary">Graphic Design</h5>
                                    <p class="mb-2 text-dark font-weight-bold">Technical College | <small>May 2022 - Oct 2022</small></p>
                                    <ul class="list-unstyled mb-0 text-muted">
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Practice workplace communication and interpersonal relations</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Apply occupational literacy and numeracy</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Work in teams</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Practice occupational health and safety measures</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Develop concept and sketches</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Design and create graphics for print/publish products</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Design and create graphics for web and other types of multimedia</li>
                                        <li class="mb-1"><i class="fa fa-check text-primary mr-2" style="font-size: 0.8rem;"></i>Handle customer care service</li>
                                    </ul>
                                </div>
                            </div>"""

# Replace in HTML using regex to handle varying whitespaces
pattern = re.compile(r'<div class="border-left border-primary pt-2 pl-4 ml-2 timeline-box">.*?</div>\s*</div>\s*</div>', re.DOTALL)
html = pattern.sub(new_exp + '\\n                        </div>\\n                    </div>', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Education section successfully implemented.")
