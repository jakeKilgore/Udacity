/**
 * Linked list implementation of a queue data structure for holding Cards.
 */
export default class Queue {
    /**
     * @description Constructor for the Queue class.
     */
    constructor() {
        this.head = null;
        this.tail = null;
        this.size = 0;
    }

    /**
     * Add a card to the queue.
     * @param {Card} card - Card to add to the queue.
     */
    enqueue(card) {
        let node = new Node(card);

        if (this.head === null) {
            this.head = node;
        }
        if (this.tail !== null) {
            this.tail.next = node;
        }

        this.tail = node;
        this.size++;
    }

    /**
     * @description Remove the first card in the queue.
     * @returns {Card} card - The card which has been removed.
     */
    dequeue() {
        if (this.size === 0) {
            return null;
        }
        let card = this.head.card;

        this.head = this.head.next;
        if (this.head === null) {
            this.tail = null;
        }

        this.size--;
        return card;
    }

    /**
     * @description Iterate through the queue and call a function on each element.
     * @param {Function} callback - Callback function to be called on each element in the queue.
     */
    forEach(callback) {
        let current = this.head;
        while (current !== null) {
            callback(current.card);
            current = current.next;
        }
    }

    /**
     * Represent the Queue data structure as a string.
     * @returns {string} string - String representation of the Queue.
     */
    toString() {
        let str = '';
        this.forEach(function(card) {
            str += card + ' -> ';
        });
        return str;
    }
}

/**
 * @description Internal class representing each element in the queue.
 *
 * The Node is made up of data (a card) and a pointer (the next Node in the Queue).
 */
class Node {
    constructor(card) {
        this.card = card;
        this.next = null;
    }
}
