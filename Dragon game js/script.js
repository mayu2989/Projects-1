let xp = 0;
let health = 100;
let gold = 100;
let currentWeapon = 0;
let fighting;
let monsterHealth;
let inventory = ["stick"];

const button1 = document.querySelector("#button1");
const button2 = document.querySelector("#button2");
const button3 = document.querySelector("#button3");
const text = document.querySelector("#text");
const xpText = document.querySelector("#xptext");
const healthText = document.querySelector("#healthtext");
const goldText = document.querySelector("#goldtext");
const monsterStats = document.querySelector("#monsterstats");
const monsterNameText = document.querySelector("#monsternametext");
const monsterHealthText = document.querySelector("#monsterhealthtext");

const weapons = [
  { name: "stick", power: 5 },
  { name: "dagger", power: 30 },
  { name: "claw hammer", power: 50 },
  { name: "sword", power: 100 }
];

const monsters = [
  { name: "slime", level: 2, health: 15 },
  { name: "Fanged Beast", level: 8, health: 60 },
  { name: "Dragon", level: 20, health: 300 }
];

const gameLocations = [
  {
    name: "town square",
    "button text": ["Go to store", "Go to cave", "Fight dragon"],
    "button function": [goStore, goCave, fightDragon],
    text: "You are in the town square."
  },
  {
    name: "store",
    "button text": ["Buy 10 health", "Buy weapon", "Go to town square"],
    "button function": [buyHealth, buyWeapon, goTown],
    text: "You entered the store."
  },
  {
    name: "cave",
    "button text": ["Fight slime", "Fight beast", "Go to town square"],
    "button function": [fightSlime, fightBeast, goTown],
    text: "You entered the cave. Be careful!"
  },
  {
    name: "fight",
    "button text": ["Attack", "Dodge", "Run"],
    "button function": [attack, dodge, goTown],
    text: "You are fighting a monster."
  },
  {
    name: "kill monster",
    "button text": ["Go to town square", "Go to town square", "Easter Egg"],
    "button function": [goTown, goTown, easterEgg],
    text: "You defeated a monster."
  },
  {
    name: "lose",
    "button text": ["Replay", "Replay", "Replay"],
    "button function": [restart, restart, restart],
    text: "You died!"
  },
  {
    name: "win",
    "button text": ["Replay", "Replay", "Replay"],
    "button function": [restart, restart, restart],
    text: "You defeated the dragon. You won!"
  },
  {
    name: "easter egg",
    "button text": ["Two", "Eight", "Go to town square"],
    "button function": [pickTwo, pickEight, goTown],
    text:
      "You find a secret game. Pick a number. Ten numbers will be randomly chosen between 0 and 10. If the number you choose matches one, you win!"
  }
];

// Start game at the town square
update(gameLocations[0]);

function update(locationObj) {
  if (locationObj.name === "fight") {
    monsterStats.style.display = "block";
  } else {
    monsterStats.style.display = "none";
  }
  button1.innerText = locationObj["button text"][0];
  button2.innerText = locationObj["button text"][1];
  button3.innerText = locationObj["button text"][2];
  button1.onclick = locationObj["button function"][0];
  button2.onclick = locationObj["button function"][1];
  button3.onclick = locationObj["button function"][2];
  text.innerText = locationObj.text;
  updateStats();
}

function goStore() {
  update(gameLocations[1]);
}

function goCave() {
  update(gameLocations[2]);
}

function fightDragon() {
  fighting = 2;
  startFight();
}

function goTown() {
  update(gameLocations[0]);
}

function buyWeapon() {
  if (currentWeapon < weapons.length - 1) {
    if (gold >= 30) {
      gold -= 30;
      currentWeapon++;
      let newWeapon = weapons[currentWeapon].name;
      inventory.push(newWeapon);
      text.innerText = `You bought a new weapon: ${newWeapon}`;
      updateStats();
    } else {
      text.innerText = "You don’t have enough gold to buy a weapon.";
    }
  } else {
    text.innerText = "You already have the most powerful weapon.";
    button2.innerText = "Sell weapon";
    button2.onclick = sellWeapon;
  }
}

function sellWeapon() {
  if (inventory.length > 1) {
    gold += 15;
    let soldWeapon = inventory.splice(currentWeapon, 1)[0];
    currentWeapon = Math.max(0, currentWeapon - 1);
    text.innerText = `You sold your ${soldWeapon}. Inventory: ${inventory.join(", ")}`;
    updateStats();
    button2.innerText = "Buy weapon";
    button2.onclick = buyWeapon;
  } else {
    text.innerText = "Don't sell your only weapon!";
  }
}

function buyHealth() {
  if (gold >= 10) {
    gold -= 10;
    health += 10;
    text.innerText = "You bought 10 health.";
    updateStats();
  } else {
    text.innerText = "You don’t have enough gold to buy health.";
  }
}

function fightSlime() {
  fighting = 0;
  startFight();
}

function fightBeast() {
  fighting = 1;
  startFight();
}

function startFight() {
  update(gameLocations[3]);
  monsterHealth = monsters[fighting].health;
  monsterStats.style.display = "block";
  monsterNameText.innerText = monsters[fighting].name;
  monsterHealthText.innerText = monsterHealth;
}

// Helper function
function getAttackValue(level) {
  let hit = (level * 5) - Math.floor(Math.random() * xp);
  return hit > 0 ? hit : 0;
}

function isMonsterHit() {
  return Math.random() > 0.2 || health < 20;
}

function attack() {
  text.innerText = `The ${monsters[fighting].name} attacks.\nYou attack it with your ${weapons[currentWeapon].name}.`;
  if (isMonsterHit()) {
    health -= getAttackValue(monsters[fighting].level);
  } else {
    text.innerText += " You miss.";
  }
  monsterHealth -= weapons[currentWeapon].power + Math.floor(Math.random() * xp) + 1;
  updateStats();
  monsterHealthText.innerText = monsterHealth;
  if (health <= 0) {
    lose();
    return;
  } else if (monsterHealth <= 0) {
    if (fighting === 2) {
      winGame();
    } else {
      defeatMonster();
    }
    return;
  }
  // Weapon breakage, only if player has more than 1 weapon
  if (Math.random() <= 0.2 && inventory.length > 1) {
    text.innerText += "\nYour " + inventory.pop() + " breaks.";
    currentWeapon = Math.max(0, currentWeapon - 1);
  }
}

function dodge() {
  text.innerText = `You dodge the attack from the ${monsters[fighting].name}.`;
}

function defeatMonster() {
  gold += Math.floor(monsters[fighting].level * 6.7);
  xp += monsters[fighting].level;
  updateStats();
  update(gameLocations[4]);
}

function lose() {
  update(gameLocations[5]);
}

function winGame() {
  update(gameLocations[6]);
}

function restart() {
  xp = 0;
  health = 100;
  gold = 100;
  currentWeapon = 0;
  inventory = ["stick"];
  updateStats();
  goTown();
}

function updateStats() {
  xpText.innerText = "XP: " + xp;
  healthText.innerText = "Health: " + health;
  goldText.innerText = "Gold: " + gold;
}

function easterEgg() {
  update(gameLocations[7]);
}
function pickTwo() {
  pick(2);
}
function pickEight() {
  pick(8);
}
function pick(guess) {
  let numbers = [];
  while (numbers.length < 10) {
    numbers.push(Math.floor(Math.random() * 11));
  }
  text.innerText = "You picked " + guess + ". Here are the random numbers:\n";
  for (let i = 0; i < 10; i++) {
    text.innerText += numbers[i] + "\n";
  }
  if (numbers.indexOf(guess) !== -1) {
    text.innerText += "Right! You win 20 gold!";
    gold += 20;
    updateStats();
  } else {
    text.innerText += "Wrong! You lose 10 health!";
    health -= 10;
    updateStats();
    if (health <= 0) {
      lose();
    }
  }
}
