import os

html_path = 'index.html'
css_path = 'css/style.css'
js_path = 'js/main.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace existing portfolio items with new hover mechanic items
old_portfolio_content = """<div class="row portfolio-container">
                                <div class="col-md-6 mb-4 portfolio-item first">
                                    <div class="position-relative overflow-hidden mb-2">
                                        <img class="img-fluid w-100" src="img/portfolio-1.jpg" alt="">
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center">
                                            <a href="img/portfolio-1.jpg" data-lightbox="portfolio">
                                                <i class="fa fa-4x fa-plus text-white"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4 portfolio-item second">
                                    <div class="position-relative overflow-hidden mb-2">
                                        <img class="img-fluid w-100" src="img/portfolio-2.jpg" alt="">
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center">
                                            <a href="img/portfolio-2.jpg" data-lightbox="portfolio">
                                                <i class="fa fa-4x fa-plus text-white"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4 portfolio-item first">
                                    <div class="position-relative overflow-hidden mb-2">
                                        <img class="img-fluid w-100" src="img/portfolio-3.jpg" alt="">
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center">
                                            <a href="img/portfolio-3.jpg" data-lightbox="portfolio">
                                                <i class="fa fa-4x fa-plus text-white"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-6 mb-4 portfolio-item second">
                                    <div class="position-relative overflow-hidden mb-2">
                                        <img class="img-fluid w-100" src="img/portfolio-4.jpg" alt="">
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center">
                                            <a href="img/portfolio-4.jpg" data-lightbox="portfolio">
                                                <i class="fa fa-4x fa-plus text-white"></i>
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>"""

new_portfolio_content = """<div class="row portfolio-container">

                                <!-- Portfolio Item 1: Showreel (Video focus) -->
                                <div class="col-md-6 mb-4 portfolio-item first">
                                    <div class="position-relative overflow-hidden mb-2 portfolio-card">
                                        <img class="img-fluid w-100 portfolio-img" src="img/portfolio-1.jpg" alt="Showreel Thumbnail">
                                        <video class="portfolio-hover-video" muted loop playsinline preload="metadata">
                                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                                        </video>
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center flex-column text-center">
                                            <h4 class="text-white mb-2 font-weight-bold">2026 Showreel</h4>
                                            <p class="text-white-50 px-4 mb-3 small">A high-energy editing sizzle reel demonstrating pacing, color grading, and dynamic motion graphics.</p>
                                            <a href="https://www.w3schools.com/html/mov_bbb.mp4" data-lightbox="portfolio" class="btn btn-outline-light rounded-pill btn-sm">Watch Video</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Portfolio Item 2: Motion Graphics (Design focus) -->
                                <div class="col-md-6 mb-4 portfolio-item second">
                                    <div class="position-relative overflow-hidden mb-2 portfolio-card">
                                        <img class="img-fluid w-100 portfolio-img" src="img/portfolio-2.jpg" alt="Motion Graphics Vignette">
                                        <video class="portfolio-hover-video" muted loop playsinline preload="metadata">
                                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                                        </video>
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center flex-column text-center">
                                            <h4 class="text-white mb-2 font-weight-bold">Brand Explainer</h4>
                                            <p class="text-white-50 px-4 mb-3 small">Custom vector illustrations built in Illustrator and brought to life with complex keyframing in After Effects.</p>
                                            <a href="img/portfolio-2.jpg" data-lightbox="portfolio" class="btn btn-outline-light rounded-pill btn-sm">View Case Study</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Portfolio Item 3: Social Content (Video focus) -->
                                <div class="col-md-6 mb-4 portfolio-item first">
                                    <div class="position-relative overflow-hidden mb-2 portfolio-card">
                                        <img class="img-fluid w-100 portfolio-img" src="img/portfolio-3.jpg" alt="Social Campaign Edit">
                                        <video class="portfolio-hover-video" muted loop playsinline preload="metadata">
                                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                                        </video>
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center flex-column text-center">
                                            <h4 class="text-white mb-2 font-weight-bold">Vertical Ads</h4>
                                            <p class="text-white-50 px-4 mb-3 small">Fast-paced social media edits that resulted in a 40% interaction boost. Premiere Pro & InDesign assets.</p>
                                            <a href="img/portfolio-3.jpg" data-lightbox="portfolio" class="btn btn-outline-light rounded-pill btn-sm">View Case Study</a>
                                        </div>
                                    </div>
                                </div>

                                <!-- Portfolio Item 4: Personal Project (Hybrid) -->
                                <div class="col-md-6 mb-4 portfolio-item second">
                                    <div class="position-relative overflow-hidden mb-2 portfolio-card">
                                        <img class="img-fluid w-100 portfolio-img" src="img/portfolio-4.jpg" alt="Personal Project">
                                        <video class="portfolio-hover-video" muted loop playsinline preload="metadata">
                                            <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
                                        </video>
                                        <div class="portfolio-btn d-flex align-items-center justify-content-center flex-column text-center">
                                            <h4 class="text-white mb-2 font-weight-bold">Cinematic Vlog</h4>
                                            <p class="text-white-50 px-4 mb-3 small">A personal storytelling piece documenting my gardening journey, focused heavily on aesthetic color grading.</p>
                                            <a href="img/portfolio-4.jpg" data-lightbox="portfolio" class="btn btn-outline-light rounded-pill btn-sm">View Case Study</a>
                                        </div>
                                    </div>
                                </div>

                            </div>"""

if old_portfolio_content in html:
    html = html.replace(old_portfolio_content, new_portfolio_content)
else:
    print("Warning: Could not find exact block to replace in index.html. Trying fallback search.")
    # Fallback if there are minor whitespace differences
    import re
    html = re.sub(r'<div class="row portfolio-container">.*?</div>\s*</div>\s*</div>\s*</div>', new_portfolio_content + '\n                        </div>\n                    </div>\n                </div>', html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

with open(css_path, 'a', encoding='utf-8') as f:
    f.write('''
/* --- Video Hover Mechanics Portfolio --- */
.portfolio-card {
    border-radius: 12px;
    background: #000;
}

.portfolio-img {
    transition: opacity 0.4s ease, transform 0.6s ease;
    z-index: 1;
    position: relative;
}

.portfolio-hover-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    transition: opacity 0.5s ease;
    z-index: 2;
    pointer-events: none;
}

/* Hover States */
.portfolio-card:hover .portfolio-img {
    opacity: 0;
    transform: scale(1.05);
}

.portfolio-card:hover .portfolio-hover-video {
    opacity: 1;
}

.portfolio-card .portfolio-btn {
    background: rgba(15, 23, 42, 0.85); /* Indigo-tinted shadow */
    z-index: 3;
    opacity: 0;
    transition: opacity 0.4s ease;
}

.portfolio-card:hover .portfolio-btn {
    opacity: 1;
}
''')

with open(js_path, 'a', encoding='utf-8') as f:
    f.write('''

// Portfolio Video Hover Mechanics
$(document).ready(function() {
    $('.portfolio-card').each(function() {
        var card = $(this);
        var video = card.find('.portfolio-hover-video').get(0);
        
        if(video) {
            card.on('mouseenter', function() {
                var playPromise = video.play();
                if (playPromise !== undefined) {
                    playPromise.catch(function(error) {
                        // Auto-play prevented
                        console.log("Video autoplay prevented:", error);
                    });
                }
            });
            
            card.on('mouseleave', function() {
                video.pause();
                video.currentTime = 0; // Rewind the clip!
            });
        }
    });
});
''')

print("Hover mechanics implemented.")
