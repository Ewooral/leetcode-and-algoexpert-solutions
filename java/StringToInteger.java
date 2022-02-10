public class StringToInteger{
    public int myAtoi(String input) {
        int sign = 1; 
        int result = 0; 
        int index = 0;
        int n = input.length();
        
        // Discard all spaces from the beginning of the input string.
        while (index < n && input.charAt(index) == ' ') { 
            index++; 
        }
        
        // sign = +1, if it's positive number, otherwise sign = -1. 
        if (index < n && input.charAt(index) == '+') {
            sign = 1;
            index++;
        } else if (index < n && input.charAt(index) == '-') {
            sign = -1;
            index++;
        }
        
        // Traverse next digits of input and stop if it is not a digit
        while (index < n && Character.isDigit(input.charAt(index))) {
            int digit = input.charAt(index) - '0';

            // Check overflow and underflow conditions. 
            if ((result > Integer.MAX_VALUE / 10) || 
                (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {     
                // If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            // Append current digit to the result.
            result = 10 * result + digit;
            index++;
        }
        
        // We have formed a valid number without any overflow/underflow.
        // Return it after multiplying it with its sign.
        return sign * result;
    }
}


/**
 * APPROACH TWO
 * 
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



enum State { q0, q1, q2, qd }

class StateMachine {
    // Store current state value.
    private State currentState;
    // Store result formed and it's sign.
    private int result, sign;

    public StateMachine() {
        currentState = State.q0;
        result = 0;
        sign = 1;
    }

    // Transition to state q1.
    private void toStateQ1(char ch) {
        sign = (ch == '-') ? -1 : 1;
        currentState = State.q1;
    }

    // Transition to state q2.
    private void toStateQ2(int digit) {
        currentState = State.q2;
        appendDigit(digit);
    }

    // Transition to dead state qd.
    private void toStateQd() {
        currentState = State.qd;
    }

    // Append digit to result, if out of range return clamped value.
    private void appendDigit(int digit) {
        if ((result > Integer.MAX_VALUE / 10) || 
            (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {
            if (sign == 1) {
                // If sign is 1, clamp result to Integer.MAX_VALUE.
                result = Integer.MAX_VALUE;
            } else {
                // If sign is -1, clamp result to Integer.MIN_VALUE.
                result = Integer.MIN_VALUE;
                sign = 1;
            }

            // When the 32-bit int range is exceeded, a dead state is reached.
            toStateQd();
        } else {
            // Append current digit to the result. 
            result = result * 10 + digit;
        }
    }

    // Change state based on current input character.
    public void transition(char ch) {
        if (currentState == State.q0) {
            // Beginning state of the string (or some whitespaces are skipped).
            if (ch == ' ') {
                // Current character is a whitespaces.
                // We stay in same state. 
                return;
            } else if (ch == '-' || ch == '+') {
                // Current character is a sign.
                toStateQ1(ch);
            } else if (Character.isDigit(ch)) {
                // Current character is a digit.
                toStateQ2(ch - '0');
            } else {
                // Current character is not a space/sign/digit.
                // Reached a dead state.
                toStateQd();
            }
        } else if (currentState == State.q1 || currentState == State.q2) {
            // Previous character was a sign or digit.
            if (Character.isDigit(ch)) {
                // Current character is a digit.
                toStateQ2(ch - '0');
            } else {
                // Current character is not a digit.
                // Reached a dead state.
                toStateQd();
            }
        }
    }
    
    // Return the final result formed with it's sign.
    public int getInteger() {
        return sign * result;
    }

    // Get current state.
    public State getState() {
        return currentState;
    }
};

class Solution {
    public int myAtoi(String s) {
        StateMachine Q = new StateMachine();
        
        for (int i = 0; i < s.length() && Q.getState() != State.qd; ++i) {
            Q.transition(s.charAt(i));
        }
        
        return Q.getInteger();
    }
}
 */