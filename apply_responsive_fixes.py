css_path = 'css/style.css'

responsive_css = """

/* =========================================
   RESPONSIVE LAYOUT & QA FIXES 
   ========================================= */

/* 1. Global Overflow Protection */
body, html {
    overflow-x: hidden;
    width: 100%;
}

.row {
    margin-right: -15px; 
    margin-left: -15px;
    width: auto;
}

/* 2. Timeline Margin Bleed Fixes @ Mobile */
@media (max-width: 576px) {
    .timeline-box {
        padding-left: 2.5rem !important; 
    }
    .timeline-box .fa-arrow-right {
        left: -15px !important;
    }
}

/* 3. Typography Overlap & Scalability Fixes */
@media (max-width: 768px) {
    h1, .h1 {
        font-size: 2rem !important; 
    }
    .typed-text-output {
        font-size: 1.1rem !important;
        line-height: 1.4;
        word-wrap: normal;
    }
}

/* 4. Sidebar Collision & Restacking Fixes @ Tablet/Mobile */
@media (max-width: 991px) {
    .wrapper .sidebar {
        position: relative !important;
        width: 100% !important;
        float: none !important;
        margin-left: 0 !important;
        height: auto !important;
        padding-bottom: 2rem !important;
    }
    .wrapper .content {
        width: 100% !important;
        margin-left: 0 !important;
        padding: 15px !important;
    }
    .sidebar-icon {
        display: none !important;
    }
    
    /* Reveal contact info statically on mobile */
    .wrapper .sidebar-text {
        display: flex !important;
    }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(responsive_css)

print("Responsive CSS fixes appended to style.css successfully.")
