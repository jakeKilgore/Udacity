import Queue from './queue.js';
import Score from "./score.js";

/**
 * @description Class for handling the logic of the game.
 *
 * The objective of the game is to match all 8 pairs of cards in the deck.
 */
export default class Game {
    /**
     * @description Constructor for the Game class.
     * @param {Deck} deck - Deck object representing the deck of cards used for the game.
     * @param {int} animationDelay - Delay time for certain events to account for animations.
     */
    constructor(deck, animationDelay) {
        this.deck = deck;
        this.score = new Score($('.score'));
        this.flipped = new Queue();
        this.matched = [];
        this.animationDelay = animationDelay;
        this.inProgress = true;

        this.deck.shuffle();
    }

    /**
     * @description Flip a card and check if the player has made a match.
     * @param {Element} cardElement - The card the player has clicked.
     */
    makeMove(cardElement) {
        if (!this.inProgress) {
            return;
        }
        let card = this.deck.getCard(cardElement);
        if (!card.flip()) {
            return;
        }

        if (this.score.startTime === null) {
            this.score.startTimer();
        }
        this.flipped.enqueue(card);
        this.score.makeMove(card);
        this.checkMatch();
    }

    /**
     * @description Check if two cards are a match.
     */
    checkMatch() {
        if(this.flipped.size < 2) {
            return;
        }
        let card1 = this.flipped.dequeue();
        let card2 = this.flipped.dequeue();

        if (card1.isMatch(card2, this.animationDelay)) {
            this.matched.push([card1, card2]);
        }
    }

    /**
     * @description End the game and perform clean-up.
     */
    end() {
        this.inProgress = false;
        this.flipped.forEach((card) => {
            card.reset(0);
        });
        this.matched.forEach((pair) => {
            pair.forEach((card) => {
                card.reset(0);
            });
        });
    }
}
