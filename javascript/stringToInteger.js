/**
 * Algorithm

Initialize two variables:
sign (to store the sign of the final result) as 1.
result (to store the 32-bit integer result) as 0.
Skip all leading whitespaces in the input string.
Check if the current character is a '+' or '-' sign:
If there is no symbol or the current character is '+', keep sign equal to 1.
Otherwise, if the current character is '-', change sign to -1.
Iterate over the characters in the string as long as the current character represents a digit or until we reach the end of the input string.
Before appending the currently selected digit, check if the 32-bit signed integer range is violated. If it is violated, then return INT_MAX or INT_MIN as appropriate.
Otherwise, if appending the digit does not result in overflow/underflow, append the current digit to the result.
Return the final result with its respective sign, sign * result.
 */

var myAtoi = function(input) {
    let sign = 1; 
    let result = 0;
    let index = 0;
    let n = input.length;
    
    let INT_MAX = Math.pow(2,31) - 1;
    let INT_MIN = -Math.pow(2, 31);
        
    // Discard all spaces from the beginning of the input string.
    while (index < n && input[index] == ' ') { 
        index++; 
    }

    // sign = +1, if it's positive number, otherwise sign = -1. 
    if (index < n && input[index] == '+') {
        sign = 1;
        index++;
    } else if (index < n && input[index] == '-') {
        sign = -1;
        index++;
    }

    // Traverse next digits of input and stop if it is not a digit. 
    // End of string is also non-digit character.
    while (index < n && input[index] >= '0' && input[index] <= '9') {
        let digit = input[index] - '0';

        // Check overflow and underflow conditions. 
        if ((result > Math.floor(INT_MAX / 10)) || 
            (result == Math.floor(INT_MAX / 10) && digit > INT_MAX % 10)) {     
            // If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
            return sign == 1 ? INT_MAX : INT_MIN;
        }

        // Append current digit to the result.
        result = 10 * result + digit;
        index++;
    }

    // We have formed a valid number without any overflow/underflow.
    // Return it after multiplying it with its sign.
    return sign * result;
};


// APPROACH TWO
/**
 * Algorithm

Initialize three variables:
currentState (to represent current state) as q0
result (to store result till now) as 0
sign (to represent the sign of the final result) as 1
For each character of the input string, if the current state is not qd:
If the current state is q0:
Stay in the same state if whitespaces occur.
If a sign occurs, change the sign variable to -1 if it's a negative sign and change the state to q1.
If a digit occurs, append the current digit to the resulting number (clamp result if needed) and change the state to q2.
If anything else occurs, then stop building the number and transition to state qd.
If the current state is q1:
If a digit occurs, append the current digit to the resulting number (clamp result if needed) and change the state to q2.
If anything else occurs, stop building the result number and transition to state qd.
If the current state is q2:
If a digit occurs, append the current digit to the resulting number (clamp result if needed) and stay in the current state.
Anything else after a digit character will not be valid; hence, stop building the number and transition to state qd.
Return the final result with the respective sign, result * sign.
 */

class StateMachine {
    // Store current state value.
    #currentState;
    // Store result formed and it's sign.
    #result; 
    #sign;
    
    State;
    #INT_MAX;
    #INT_MIN;

    constructor() {
        this.State = { q0: 1, q1: 2, q2: 3, qd: 4 };
        this.#INT_MAX = Math.pow(2,31) - 1; 
        this.#INT_MIN = -Math.pow(2, 31);
        
        this.#currentState = this.State.q0;
        this.#result = 0;
        this.#sign = 1;
    }
    
    // Transition to state q1.
    toStateQ1(ch) {
        this.#sign = (ch == '-') ? -1 : 1;
        this.#currentState = this.State.q1;
    }
    
    // Transition to state q2.
    toStateQ2(digit) {
        this.#currentState = this.State.q2;
        this.appendDigit(digit);
    }
    
    // Transition to dead state qd.
    toStateQd() {
        this.#currentState = this.State.qd;
    }
    
    // Append digit to result, if out of range return clamped value.
    appendDigit(digit) {
        if ((this.#result > Math.floor(this.#INT_MAX / 10)) || 
            (this.#result == Math.floor(this.#INT_MAX / 10) && digit > this.#INT_MAX % 10)) {
            if (this.#sign == 1) {
                // If sign is 1, clamp result to INT_MAX.
                this.#result = this.#INT_MAX;
            } else {
                // If sign is -1, clamp result to INT_MIN.
                this.#result = this.#INT_MIN;
                this.#sign = 1;
            }
            
            // When the 32-bit int range is exceeded, a dead state is reached.
            this.toStateQd();
        } else {
            // Append current digit to the result. 
            this.#result = this.#result * 10 + digit;
        }
    }

    // Change state based on current input character.
    transition(ch) {
        if (this.#currentState == this.State.q0) {
            // Beginning state of the string (or some whitespaces are skipped).
            if (ch == ' ') {
                // Current character is a whitespaces.
                // We stay in same state. 
                return;
            } else if (ch == '-' || ch == '+') {
                // Current character is a sign.
                this.toStateQ1(ch);
            } else if (ch >= '0' && ch <= '9') {
                // Current character is a digit.
                this.toStateQ2(ch - '0');
            } else {
                // Current character is not a space/sign/digit.
                // Reached a dead state.
                this.toStateQd();
            }
        } else if (this.#currentState == this.State.q1 || this.#currentState == this.State.q2) {
            // Previous character was a sign or digit.
            if (ch >= '0' && ch <= '9') {
                // Current character is a digit.
                this.toStateQ2(ch - '0');
            } else {
                // Current character is not a digit.
                // Reached a dead state.
                this.toStateQd();
            }
        }
    }
    
    // Return the final result formed with it's sign.
    getInteger() {
        return this.#sign * this.#result;
    }
    
    // Get current state.
    getState() {
        return this.#currentState;
    }
};

var myAtoiTwo = function(s) {
    let Q = new StateMachine();
        
    for (let i = 0; i < s.length && Q.getState() != Q.State.qd; ++i) {
        Q.transition(s[i]);
    }

    return Q.getInteger();
};