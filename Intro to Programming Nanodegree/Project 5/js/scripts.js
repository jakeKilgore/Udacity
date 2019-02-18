$(document).ready(function() {
    // JQuery selectors
   const
       $gameBoard = $('.game-board'),
       $deck = $('.deck'),
       $refresh = $('.refresh');

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
       $deck.empty();
       createBoard();
   });
   
   $(window).resize(function() {
       resizeGameBoard();
   });

   createBoard();
   resizeGameBoard();

    /**
     * @description Populate the game board with cards.
     */
   function createBoard() {
       let cards = [];
       icons.forEach(function(icon) {
           let card = '' +
               '<div class="card">' +
               '<div class=\"icon fa fa-' + icon + '\">' +
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
     * Shuffle the deck of cards
     * @param {Array} cards - Array of cards to be shuffled.
     * @return {Array} cards
     */
   function shuffle(cards) {
       for(let currentIndex = cards.length; currentIndex > 0; currentIndex--) {
            let newIndex = Math.floor(Math.random() * currentIndex);

            let temp = cards[currentIndex];
            cards[currentIndex] = cards[newIndex];
            cards[newIndex] = temp;
       }
   }
   
   function resizeGameBoard() {
       let size = .8 * Math.min($(window).innerHeight(), $(window).innerWidth());
       $gameBoard.css('width', size);
       $gameBoard.css('padding-bottom', size);
   }
});