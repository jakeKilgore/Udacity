$(document).ready(function() {
    // JQuery selectors
    const
        $gameBoard = $('.game-deck'),
        $deck = $('.cards'),
        $moves = $('.moves'),
        $refresh = $('.refresh');

    let
        moves = 0;

    // Game pieces
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

    $refresh.on('click', function() {
        refreshCards();
        moves = 0;
        updateScore();
    });

    $deck.on('click', '.card', function() {
        makeMove(this);
    });

    $(window).resize(function() {
        resizeGameBoard();
    });

    createBoard();
    resizeGameBoard();

    /**
     * @description Populate the game deck with cards.
     */
    function createBoard() {
        let cards = [];
        icons.forEach(function(icon) {
            let card = '' +
                '<div class="card">' +
                '<div class="card-front">' +
                '<div class=\"icon fa fa-' + icon + '\">' +
                '</div>' +
                '</div>' +
                '<div class="card-back">' +
                '</div>' +
                '</div>';
            cards.push(card);
            cards.push(card);
        });
        shuffle(cards);

        cards.forEach(function(card) {
            $deck.append(card);
        });
    }

    /**
     * @description Shuffle the cards of cards.
     * @param {Array} cards - Array of cards to be shuffled.
     * @return {Array} cards
     */
    function shuffle(cards) {
        for (let currentIndex = cards.length; currentIndex > 0; currentIndex--) {
             let newIndex = Math.floor(Math.random() * currentIndex);

             let temp = cards[currentIndex];
             cards[currentIndex] = cards[newIndex];
             cards[newIndex] = temp;
        }
    }

    /**
     * @description Set the size of the deck and font based on whether the screen is larger in width or height.
     */
    function resizeGameBoard() {
        let windowWidth = $(window).innerWidth();
        let windowHeight = $(window).innerHeight();
        let boardSize = .8 * Math.min(windowWidth, windowHeight);
        $gameBoard.css('width', boardSize);
        $gameBoard.css('padding-bottom', boardSize);

        let fontSize;
        if (windowWidth < windowHeight) {
            fontSize = '1.5vh';
        } else {
            fontSize = '1.5vw';
        }
        $('.icon').css('font-size', fontSize);
    }

    /**
     * @description Flip a card and check if the player has made a match.
     * @param {Element} card - The card the player has clicked.
     */
    function makeMove(card) {
        let $card = $(card);
        if ($card.hasClass('open') || $card.hasClass('match')) {
            return;
        }
        $(card).addClass('open');
        moves++;
        updateScore();
        let match = checkMatch();
        finishMove(match);
    }

    /**
     * @description Update the move counter.
     */
    function updateScore() {
        $moves.html(moves + ' Moves');
    }

    /**
     * @description Check if the flipped cards match.
     * @returns {boolean} True if the cards match, false otherwise.
     */
    function checkMatch() {
        let cards = $('.open');
        if (cards.length < 2) {
            return false;
        }
        return $(cards[0]).html() === $(cards[1]).html();
    }

    /**
     * @description Update the classes of the cards.
     * @param {boolean} match - Whether the cards match.
     */
    function finishMove(match) {
        let cards = $('.open')
        if (cards.length < 2) {
            return;
        }
        if (match) {
            cards.addClass('match');
        }
        setTimeout(function() {
            cards.removeClass('open');
        }, 800);
    }

    /**
     * @description Reshuffle the cards.
     */
    function refreshCards() {
        $('.open').removeClass('open');
        $('.match').removeClass('match');
        setTimeout(function() {
            $deck.empty();
            createBoard();
        }, 800);
    }
});
