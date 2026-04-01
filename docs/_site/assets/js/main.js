// TuneZ Documentation - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tabs
    initTabs();

    // Initialize copy buttons for code blocks
    initCopyButtons();

    // Initialize smooth scroll for anchor links
    initSmoothScroll();
});

/**
 * Tab functionality
 */
function initTabs() {
    const tabContainers = document.querySelectorAll('.tabs-container');

    tabContainers.forEach(container => {
        const tabs = container.querySelectorAll('.tab');
        const contents = container.querySelectorAll('.tab-content');

        tabs.forEach(tab => {
            tab.addEventListener('click', () => {
                const target = tab.dataset.tab;

                // Remove active class from all tabs
                tabs.forEach(t => t.classList.remove('active'));
                // Add active class to clicked tab
                tab.classList.add('active');

                // Hide all contents
                contents.forEach(c => c.classList.remove('active'));
                // Show target content
                const targetContent = container.querySelector(`[data-content="${target}"]`);
                if (targetContent) {
                    targetContent.classList.add('active');
                }
            });
        });
    });
}

/**
 * Copy buttons for code blocks
 */
function initCopyButtons() {
    const codeBlocks = document.querySelectorAll('pre code');

    codeBlocks.forEach(block => {
        const pre = block.parentElement;
        const wrapper = document.createElement('div');
        wrapper.className = 'code-wrapper';

        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);

        const copyButton = document.createElement('button');
        copyButton.className = 'copy-button';
        copyButton.textContent = 'Copy';
        copyButton.addEventListener('click', () => {
            navigator.clipboard.writeText(block.textContent).then(() => {
                copyButton.textContent = 'Copied!';
                setTimeout(() => {
                    copyButton.textContent = 'Copy';
                }, 2000);
            });
        });

        wrapper.appendChild(copyButton);
    });
}

/**
 * Smooth scroll for anchor links
 */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/**
 * Language switcher
 */
function switchLanguage(lang) {
    const currentPath = window.location.pathname;

    // Extract path without language prefix
    const pathParts = currentPath.split('/').filter(Boolean);

    // Check if first part is a language code
    const languageCodes = ['en', 'zh-TW', 'zh-CN'];
    if (languageCodes.includes(pathParts[0])) {
        pathParts.shift(); // Remove language code
    }

    // Build new path
    const newPath = '/' + lang + '/' + pathParts.join('/');
    window.location.href = newPath || '/' + lang + '/';
}

/**
 * Mobile menu toggle
 */
function toggleMobileMenu() {
    const nav = document.querySelector('.main-nav');
    nav.classList.toggle('mobile-open');
}

/**
 * Collapsible sections
 */
function toggleCollapsible(id) {
    const content = document.getElementById(id);
    if (content) {
        content.classList.toggle('collapsed');
    }
}

// Add CSS for collapsible sections
const style = document.createElement('style');
style.textContent = `
    .code-wrapper {
        position: relative;
    }
    
    .copy-button {
        position: absolute;
        top: 0.5rem;
        right: 0.5rem;
        padding: 0.25rem 0.5rem;
        font-size: 0.75rem;
        background-color: var(--border-color);
        border: none;
        border-radius: 4px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.2s;
    }
    
    .code-wrapper:hover .copy-button {
        opacity: 1;
    }
    
    .copy-button:hover {
        background-color: var(--text-secondary);
        color: white;
    }
    
    .collapsed {
        display: none;
    }
`;
document.head.appendChild(style);