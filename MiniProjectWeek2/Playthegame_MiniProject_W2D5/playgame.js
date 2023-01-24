let user_input;
let computerNumber;

function playTheGame() {

    let ask = confirm("Would you like to play the game?");

    let guesses = 0;
    let chances = 3;
    computerNumber = Math.round((Math.random() * 10));

    if (ask === false) {
        alert("No problem, Goodbye");
        return;
    }
    console.log(` You have ${chances} chances`)
    while (user_input != computerNumber) {
        if (guesses === 3) {
            alert("OUT OF CHANCES");
            break;
        }
        user_input = parseInt(prompt('Enter a number between 0 and 10'));
        if (isNaN(user_input) === true) {
            alert("Sorry not a number. Goodbye");
            return;
        }
        if (user_input < 0 || user_input > 10) {
            alert("Sorry It's not a good number, Goodbye");
            return;
        }
        compareNumbers(user_input, computerNumber);
        guesses++;
        console.log(` You have ${chances - guesses} chance(s) left`);
    }

}

function compareNumbers(user_input, computerNumber) {
    if (user_input == computerNumber) {
        alert("WINNER");
        return;
    }
    else if (user_input > computerNumber) {
        alert("Your number is bigger than the computer's,guess again");
    }
    else if (user_input < computerNumber) {
        alert("Your number is smaller than the computer's,guess again");
    }
}
