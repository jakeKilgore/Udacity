/**
 * @description Class for handling the individual cards.
 */
export default class Card {
    /**
     * @description Constructor for the Card class.
     * @param {string} icon - The name of the icon to place on the card.
     * @param {int} occurrence - The number of times a card with this icon has been added to the deck.
     */
    constructor(icon, occurrence) {
        this.icon = icon;
        this.occurrence = occurrence;
        this.$element = $(this.html);
    }

    get id() {
        return this.icon + this.occurrence;
    }

    get html() {
        return '' +
            '<div class="card" id=' + this.id + '>' +
                '<div class="card-front">' +
                    '<div class=\"icon fa fa-' + this.icon + '\">' +
                    '</div>' +
                '</div>' +
                '<div class="card-back">' +
                '</div>' +
            '</div>';
    }

    /**
     * @description Attempt to flip the card. If the card is already flipped or matched, return false.
     * @returns {boolean} flipped - Whether the card has been successfully flipped.
     */
    flip() {
        if (this.$element.hasClass('open') || this.$element.hasClass('match')) {
            return false;
        }
        this.$element.addClass('open');
        return true;
    }

    /**
     * @description Check if two cards match.
     * @param {Card} otherCard - The card to check for a match with this one.
     * @param {int} animationDelay - The delay time for certain events to account for animations.
     * @returns {boolean}
     */
    isMatch(otherCard, animationDelay) {
        if (this.icon === otherCard.icon) {
            this.setMatch();
            otherCard.setMatch();
            return true;
        }
        else {
            this.reset(animationDelay);
            otherCard.reset(animationDelay);
            return false;
        }
    }

    /**
     * @description Assign the match class to the card.
     */
    setMatch() {
        this.$element.addClass('match');
        this.$element.removeClass('open');
    }

    /**
     * @description Remove the open and match classes from the card.
     * @param {int} animationDelay - The delay time for certain events to account for animations.
     */
    reset(animationDelay) {
        setTimeout(() => {
            this.$element.removeClass('open');
            this.$element.removeClass('match');
        }, animationDelay);
    }

    /**
     * @description Represent the Card class as a string.
     * @returns {string} string - The string representation of the class.
     */
    toString() {
        return this.icon + this.occurrence;
    }
}
