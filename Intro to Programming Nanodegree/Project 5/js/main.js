import Deck from './deck.js';
import Game from './game.js';

$(document).ready(function() {
    const animationDelay = 800;

    let
        deck = new Deck($('.deck')),
        game = new Game(deck, animationDelay),
        victory = false;

    /**
     * @description When the refresh button is pressed, startTimer a new game.
     */
    $('.refresh').on('click', function() {
        game.end();
        setTimeout(function() {
            game = new Game(deck, animationDelay);
        }, animationDelay);
    });

    /**
     * @description When one of the cards is clicked, make a move with that card.
     */
    $('.deck').on('click', '.card', function() {
        victory = game.makeMove(this);
    });
});
