import random
import time

class Magic8Ball:
    def __init__(self):
        self.answers = [
            "As I see it, yes! 🎯",
            "Ask again when I've had my coffee ☕",
            "Better not tell you now (I'm shy) 🙈",
            "Cannot predict now (my crystal ball needs cleaning) 🔮",
            "Don't count on it (but I've been wrong before!) 🎲",
            "It is certain! (I think...) ✨",
            "Most likely (like 99.9%) 🎪",
            "My reply is no (but who am I to judge?) 🤷",
            "Outlook good (better than my weather app!) 🌈",
            "Signs point to yes (all 42 of them!) 🎯",
            "Very doubtful (like my cooking skills) 🍳",
            "Without a doubt! (I'm never wrong... except when I am) 🎭",
            "Yes, definitely! (I'm not just saying that) 🌟",
            "You may rely on it (more than my alarm clock) ⏰"
        ]

    def shake(self, question):
        print("\n🔮 Shaking the magic ball", end="")
        for _ in range(3):
            time.sleep(0.7)
            print(".", end="", flush=True)
        print("\n")
        
        time.sleep(1)
        return random.choice(self.answers)

def main():
    ball = Magic8Ball()
    
    print("🔮 Welcome to the Totally Legit Magic 8-Ball! 🔮")
    print("Where your future is totally not made up on the spot!")
    
    while True:
        print("\n👻 What would you like to do?")
        print("1. 🤔 Ask a question")
        print("2. 🚪 Exit (but your future will remain uncertain!)")
        
        choice = input("\nChoose wisely (1-2): ").strip()
        
        if choice == '2':
            print("\n✨ Remember: The future is like a pizza - sometimes it's cheesy!")
            print("Goodbye! May your bugs be few and your coffee be strong! ☕")
            break
            
        elif choice == '1':
            question = input("\n🤔 What would you like to know? ")
            
            if not question:
                print("❌ Hey! Silence may be golden, but I need actual words!")
                continue
                
            if not question.endswith('?'):
                print("📝 Pro tip: Questions usually end with a '?'")
                print("But I'll let it slide this time...")
            
            answer = ball.shake(question)
            print(f"🎱 The Magic 8-Ball says: {answer}")
            
        else:
            print("❌ That's not 1 or 2!")

if __name__ == "__main__":
    main()