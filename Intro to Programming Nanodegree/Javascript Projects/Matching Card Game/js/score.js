/**
 * @description Class handling the scoring of the game.
 *
 * There are three metrics tracked in the score.
 *      Time: The time it takes from the first move until the completion of the game.
 *      Moves: The number of times a score is flipped.
 *      Stars: The efficiency of the users' flipping. Stars startTimer at 5 and decrease based on the maximum number of
 *          times a user had to flip a unique card.
 */
export default class Score {
    constructor(score) {
        this.startTime = null;
        this.endTime = null;
        this.moves = 0;
        this.stars = 5;
        this.timesFlipped = {};
        this.maxFlipped = 0;
        this.$element = score;

        this.update();
    }

    /**
     * @description Start the game's timer
     */
    startTimer() {
        this.startTime = Date.now();
    }

    /**
     * @description Stop the timer
     */
    stopTimer() {
        this.endTime = Date.now();
    }

    /**
     * @description Update the moves and stars scores after a move.
     * @param {Card} card - The card that was flipped.
     */
    makeMove(card) {
        this.moves++;
        this.setStars(card);
        this.update();
    }

    /**
     * @description Set the number of stars based on the maximum number of times a unique card has been flipped.
     *
     * The player starts with five stars and can flip each card twice without losing one. Once a card has been flipped
     * for a third time, however, the player loses a star every additional flip.
     *
     * @param {Card} card - The card that has been flipped.
     */
    setStars(card) {
        if (!(card in this.timesFlipped)) {
            this.timesFlipped[card] = 0;
            return;
        }

        this.timesFlipped[card] = this.timesFlipped[card] + 1;
        if (this.timesFlipped[card] > this.maxFlipped) {
            this.maxFlipped = this.timesFlipped[card];
        }

        // Start with five stars, allow two flips for each card with no penalty, then subtract a star for every
        // additional flip
        this.stars = 7 - this.maxFlipped;
    }

    /**
     * @description Update the move counter on the webpage.
     */
    update() {
        this.$element.find('.moves').html(this.moves + " Moves");
    }
}
