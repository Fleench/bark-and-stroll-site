/**
 * @file script.js
 * @description Handles dynamic behaviors for the Paws website, including the sticky header and cal.com embed.
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
     * @section Cal.com Embed
     * @description Initializes the Cal.com inline embed. The Cal() function is loaded
     * from an external script and will queue any calls made before it has loaded.
     */
    try {
        Cal("inline", {
            elementOrSelector: "#my-cal-inline",
            calLink: "flench04"
        });
    } catch (e) {
        console.error("Cal.com embed failed to initialize.", e);
    }

    // The iframe navigation buttons have been removed from the HTML as they are
    // non-functional due to browser cross-origin security policies.
});