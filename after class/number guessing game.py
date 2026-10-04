# ── GAME SETTINGS ──────────────────────────────────────────────
secret       = 27      # The hidden number the player must guess
max_attempts = 5

# ── SETUP ──────────────────────────────────────────────────────
count = 0
guess = 0

print("=" * 42)
print("        🎮  NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ── MAIN GAME LOOP ─────────────────────────────────────────────
# TODO: Write a while loop that keeps running as long as
#       count is less than max_attempts AND guess is not equal to secret

    # TODO: Read the player's guess using int(input())
    # TODO: Add 1 to count

    # TODO: If guess equals secret → print a win message

    # TODO: Otherwise (else):
    #   Calculate the distance (diff) between guess and secret
    #   WITHOUT using abs() — use an if/else instead

    #   Print a hint based on diff:
    #     diff >= 20  →  Ice cold
    #     diff >= 10  →  Cold
    #     diff >= 5   →  Warm
    #     else        →  Hot

    #   Calculate remaining = max_attempts - count
    #   If remaining > 0:
    #     Use a for loop to print a ❤️  for each remaining life

# ── GAME OVER CHECK ────────────────────────────────────────────
# TODO: After the loop, if guess is still not equal to secret
#       print a "Game over" message and reveal the secret number
# ── GAME SETTINGS ─────────────────────────────────────────────
secret       = 27      # Change this before distributing the boilerplate
max_attempts = 5

# ── SETUP ─────────────────────────────────────────────────────
count = 0
guess = 0

print("=" * 42)
print("        🎮  NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ── MAIN GAME LOOP ─────────────────────────────────────────────
while count < max_attempts and guess != secret:

    guess = int(input("Your guess: "))
    count = count + 1

    if guess == secret:
        print()
        print("🎉 Correct! You guessed it in", count, "attempt(s)!")
        print("Well done — you are a number wizard! 🧙")

    else:
        # Calculate distance without abs()
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        # Hint levels
        if diff >= 20:
            print("🧊 Ice cold!  You are very far away.")
        elif diff >= 10:
            print("🥶 Cold.      Still quite a distance to go.")
        elif diff >= 5:
            print("🌡️  Warm!      Getting closer...")
        else:
            print("🔥 Hot!       Almost there!")

        # Remaining lives
        remaining = max_attempts - count

        if remaining > 0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("❤️ ", end="")
            print()
        print()

# ── GAME OVER CHECK ────────────────────────────────────────────
if guess != secret:
    print("=" * 42)
    print("💀 Game over!  You used all 5 attempts.")
    print("   The secret number was:", secret)
    print("=" * 42)