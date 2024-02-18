import random
from rich.console import Console
from rich.theme import Theme

console = Console(theme=Theme({'warning': 'red on yellow'}))

rockArt = ( r"""                     
⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀       
⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀  
⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀ 
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇ 
⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿ 
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏ 
⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁  
⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋     
⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋        
                     
                     
                     
                     
""") 
paperArt = ( r"""                            
              ⣠⡴⠖⠒⢶⣄        
            ⢀⡼⠋⠀⠀⠀⢀⡿        
⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀   
⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆  
⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃  
⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁    
⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄ 
⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃ 
⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉    
⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉        
⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁           
   ⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁             
                            
""")
scissorsArt = ( r"""                              
⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀             
⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀           
⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀         
⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄  
⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆ 
⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃ 
⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀     
⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄   
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃   
                              
                              
                              
""")
youWin = ( r"""
 __   __         __      ___      _ 
 \ \ / /__ _  _  \ \    / (_)_ _ | |
  \ V / _ \ || |  \ \/\/ /| | ' \|_|
   |_|\___/\_,_|   \_/\_/ |_|_||_(_)
                                    
""")
youLose = ( r"""
 __   __          _                
 \ \ / /__ _  _  | |   ___ ___ ___ 
  \ V / _ \ || | | |__/ _ (_-</ -_)
   |_|\___/\_,_| |____\___/__/\___|
                                   
""")
youTie = ( r"""
  ___ _   _              _____ _     
 |_ _| |_( )___   __ _  |_   _(_)___ 
  | ||  _|/(_-<  / _` |   | | | / -_)
 |___|\__| /__/  \__,_|   |_| |_\___|
                                     
""")


def get_player_choice():
    choice = console.input('Please choose [bold gray66]Rock[/], [bold white]Paper[/], or [bold green]Scissors[/]: ').lower()
    if choice not in {'rock','paper','scissors'}:
        console.print(f'[bold red]{choice}[/] is not [bold gray66]Rock[/], [bold blue]Paper[/], or [bold green]Scissors[/]', style='warning')
        main()
    return choice

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def evaluate_choices(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        return 'tie'
    elif (
        playerChoice == 'rock' and computerChoice != 'paper'
        or
        playerChoice == 'paper' and computerChoice != 'scissors'
        or
        playerChoice == 'scissors' and computerChoice != 'rock'
    ):
        return 'playerWins'
    return 'computerWins'


def display(playerChoice, computerChoice, result):
    if playerChoice == 'rock':
        playerArt = rockArt
    elif playerChoice == 'paper':
        playerArt = paperArt
    else:
        playerArt = scissorsArt
    
    if computerChoice == 'rock':
        computerArt = rockArt
    elif computerChoice == 'paper':
        computerArt = paperArt
    else:
        computerArt = scissorsArt
        
    spacer = '   |   '
    for a, b, in zip(playerArt.splitlines(), computerArt.splitlines()):
        console.print(f'[green]{a}[/]{spacer}[red]{b}[/]')
    if result == 'playerWins':
        console.print(f'[green]{youWin}[/]')
    elif result == 'computerWins':
        console.print(f'[red]{youLose}[/]')
    else:
        console.print(f'[yellow]{youTie}[/]')


def play_again():
    playAgain = input('Would you like to play again? [y/n]')
    if playAgain not in {'y','n'}:
        console.print(f"{playAgain} not valid. Please only respond with 'y' or 'n'.", style='warning')
        play_again()
    elif playAgain == 'y':
        main()
    exit()


def main():
    console.clear()
    playerChoice = get_player_choice()
    computerChoice = get_computer_choice()
    result = evaluate_choices(playerChoice, computerChoice)
    display(playerChoice, computerChoice, result)
    play_again()


if __name__ == '__main__':
    main()