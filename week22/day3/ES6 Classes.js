class Account {
    number;
    balance;

    constructor(number, balance) {
        this.number = number;
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
    }

    withdraw(amount) {
        if (amount > this.balance ) {
            return "Insufficient funds";
        }
        this.balance -= amount;
    }

    checkBalance() {
        return this.balance;
    }
}


class SavingAccount extends Account {


    interestRate;

    constructor(number, balance, interestRate) {
        super(number, balance);
        this.interestRate = interestRate;
    }

    addInterest() {
        this.balance = this.balance + (this.balance * this.interestRate);
    }
}


class CurrentAccount extends Account {
    minBalance;
    constructor(number, balance, minBalance) {
        super(number, balance);
        this.minBalance = minBalance;
    }

    withdraw(amount) {
        if (this.balance - amount < this.minBalance ) {
            console.log("Insufficient funds");
            return "Insufficient funds";
        }
        this.balance -= amount;
    }
}

