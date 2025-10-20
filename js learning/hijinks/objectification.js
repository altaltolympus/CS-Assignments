const character = {
    name: "Jennifer",
    maxHealth: 100,
    currentHealth: 100,
    maxMana: 100,
    currentMana: 100,
    baseDefense: 0,
    baseAttack: 0,
    baseSpellcasting: 0,
    totalDefense: 0,
    totalAttack: 0,
    totalSpellcasting: 0,
    defenseItem: "",
    attackItem: "",
    spellcastingItem: "",
};

const defenseItem1 = {
    name: "Leather Vest",
    defense: 10,
};

const defenseItem2 = {
    name: "Padded Chainmail",
    defense: 25,
};

const defenseItem3 = {
    name: "Full Plate Armour",
    defense: 50,
};

const defenseItems = [defenseItem1, defenseItem2, defenseItem3];

const attackItem1 = {
    name: "Rusty Dagger",
    attack: 10,
};

const attackItem2 = {
    name: "Arming Sword",
    attack: 25,
};

const attackItem3 = {
    name: "Bastard Sword",
    attack: 50,
};

const attackItems = [attackItem1, attackItem2, attackItem3];

const spellcastingItem1 = {
    name: "Cloudy Orb",
    spellcasting: 10,
};

const spellcastingItem2 = {
    name: "Crystal Ball",
    spellcasting: 25,
};

const spellcastingItem3 = {
    name: "Sphere of Power",
    spellcasting: 50,
};

const spellcastingItems = [spellcastingItem1, spellcastingItem2, spellcastingItem3];

function attack(target, attacker) {
    let targetDefense = target.defense;
    let attackerAttack = attacker.attack;

    let attackPower = Math.floor((Math.random() + 1) * attackerAttack);
    let attackDamage = Math.floor(attackPower / (targetDefense / 2));
    if (attackDamage > 0) target.health -= attackDamage;
    return `${attacker.name} attacked ${target.name} and dealt ${attackDamage} damage!`;
}

function damageSpell(target, attacker) {
    let targetDefense = target.defense;
    let targetSpellcasting = target.spellcasting;
    let attackerSpellcasting = attacker.spellcasting;
    let counterspell;

    let spellPower = Math.floor(Math.random() * attackerSpellcasting);
    if (counterspell) {
        let spellDamage = Math.floor(spellPower / (targetSpellcasting / 2));
    } else {
        let spellDamage = Math.floor(spellPower / (targetDefense / 2));
        s;
    }
}
