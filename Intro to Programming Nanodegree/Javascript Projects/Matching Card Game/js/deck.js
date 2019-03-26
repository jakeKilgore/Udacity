import Card from './card.js';

const icons = [
    'anchor',
    'bicycle',
    'bolt',
    'bomb',
    'cube',
    'gem',
    'leaf',
    'paper-plane',
];

/**
 * @description Class for handling the deck of cards.
 *
 * The deck is intended to contain 16 cards (8 matching pairs) which do not change throughout the game.
 * Changing the deck mid-game will lead to unexpected results.
 */
export default class Deck {
    /**
     * @description Constructor for the deck class.
     * @param {Element} $deck - JQuery DOM element representing the deck.
     */
    constructor($deck) {
        this.cards = {};
        this.keys = [];
        this.$element = $deck;

        icons.forEach((icon) => {
            this.addCard(icon, 1);
            this.addCard(icon, 2);
        });
    }

    /**
     * @description Shuffle the deck of cards.
     */
    shuffle() {
        for (let currentIndex = this.keys.length - 1; currentIndex > 0; currentIndex--) {
            let newIndex = Math.floor(Math.random() * currentIndex);

            let temp = this.keys[currentIndex];
            this.keys[currentIndex] = this.keys[newIndex];
            this.keys[newIndex] = temp;
        }

        this.refreshDeck();
    }

    /**
     * @description Empty the $deck DOM element and re-add all of the cards in order.
     *
     * The element is detached and then reattached once the changes are finished because updating the DOM repeatedly
     * is slow.
     */
    refreshDeck() {
        let $parent = this.$element.parent();
        this.$element.detach();
        this.$element.empty();
        this.keys.forEach((key) => {
            let $card = this.cards[key].$element;
            this.$element.append($card);
        });
        $parent.append(this.$element);
    }

    /**
     * @description Create a card object and add it to the deck.
     * @param {string} icon - The name of the icon to place on the card.
     * @param {int} occurrence - The number of times a card with this icon has been added to the deck.
     */
    addCard(icon, occurrence) {
        let card = new Card(icon, occurrence);
        this.keys.push(card.id);
        this.cards[card.id] = card;
    }

    /**
     * @description Return the card object that matches the card element passed in
     * @param {Element} cardElement - The DOM element representing the card
     * @returns {Card} card - The card object matching the element passed in.
     */
    getCard(cardElement) {
        let $card = $(cardElement);
        return this.cards[$card.attr('id')];
    }

    /**
     * @description Represent the Deck object as a string.
     * @returns {string} string - String representation of the object.
     */
    toString() {
        let str = '[';
        this.keys.forEach((key, index, array) => {
            if(index !== array.length - 1) {
                str += this.cards[key] + ', ';
            }
            else {
                str += this.cards[key];
            }
        });
        str += ']';
        return str;
    }
}
