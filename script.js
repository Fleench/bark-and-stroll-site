/**
 * @file script.js
 * @description Handles dynamic behaviors for the Paws website, including the sticky header and iframe navigation.
 */

document.addEventListener('DOMContentLoaded', () => {

    /**
     * @section Sticky Header
     * @description Controls the visibility of the sticky header based on the user's scroll position.
     */
    const stickyHeader = document.getElementById('sticky-header');
    const titleCard = document.getElementById('title-card');

    // We show the sticky header once the user has scrolled past the main title card.
    const scrollThreshold = titleCard ? titleCard.offsetHeight : 200;

    window.addEventListener('scroll', () => {
        if (window.scrollY > scrollThreshold) {
            document.body.classList.add('scrolled');
        } else {
            document.body.classList.remove('scrolled');
        }
    });

    /**
     * @section Iframe Navigation
     * @description Adds back and forward functionality to the cal.com embed.
     */
    const iframe = document.getElementById('inlineFrameExample');
    const backButton = document.getElementById('cal-back');
    const forwardButton = document.getElementById('cal-forward');

    // Note: Cross-origin security restrictions in browsers prevent scripts from directly accessing
    // the history of an iframe from a different domain (like cal.com).
    // These buttons will use the iframe's own history navigation methods, but we cannot check
    // the state (e.g., if history.forward() is possible). This is a best-effort implementation.

    if (backButton) {
        backButton.addEventListener('click', () => {
            try {
                iframe.contentWindow.history.back();
            } catch (e) {
                console.error("Could not navigate iframe back due to security restrictions:", e);
            }
        });
    }

    if (forwardButton) {
        forwardButton.addEventListener('click', () => {
            try {
                iframe.contentWindow.history.forward();
            } catch (e) {
                console.error("Could not navigate iframe forward due to security restrictions:", e);
            }
        });
    }
});