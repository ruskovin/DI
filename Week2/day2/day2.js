let age = parseInt(prompt("Enter your age:"))

if (age < 18) {
    alert("Sorry, you are too young to dirve this car Powering off");
}

else if (age === 18) {
    alert("Congratulations on your first year of driving . Enjoy the ride!");

}

else if (age > 18) {
    alert("Powering On. Enjoy the ride!");
}