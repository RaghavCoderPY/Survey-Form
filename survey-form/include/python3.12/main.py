import colorama as col

col.init(autoreset=True)


# A Basic Survey form
def printc(text: str, color: str, style = col.Style.NORMAL):
    print(color + style + text)


printc("Attend this survey", color=col.Fore.YELLOW, style=col.Style.BRIGHT)
# inputs
name = input(f"Enter your name: {col.Fore.BLUE}")
email = input(f"Enter your email: {col.Fore.BLUE}")
favFood = input(f"Enter your favourite food: {col.Fore.BLUE + col.Style.DIM}")