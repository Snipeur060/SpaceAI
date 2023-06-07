"""
Ce programme va lancer automatiquement l'écran de démarrage
"""
from rich.console import Console


console = Console()

console.print("""
                                               _,'/
                                          _.-''._:
                                  ,-:`-.-'    .:.|
                                 ;-.''       .::.|
                  _..------.._  / (:.       .:::.|
               ,'.   .. . .  .`/  : :.     .::::.|
             ,'. .    .  .   ./    \ ::. .::::::.|
           ,'. .  .    .   . /      `.,,::::::::.;
          /  .            . /       ,',';_::::::,:_:
         / . .  .   .      /      ,',','::`--'':;._;
        : .             . /     ,',',':::::::_:'_,'
        |..  .   .   .   /    ,',','::::::_:'_,'
        |.              /,-. /,',':::::_:'_,'
        | ..    .    . /) /-:/,'::::_:',-'
        : . .     .   // / ,'):::_:',' ;
         \ .   .     // /,' /,-.','  ./
          \ . .  `::./,// ,'' ,'   . /
           `. .   . `;;;,/_.'' . . ,'
            ,`. .   :;;' `:.  .  ,'
           /   `-._,'  ..  ` _.-'
          (     _,'``------''  
           `--''

""", style="blink bold cyan")
console.print("SpaceAI - Snipeur060", style="blink bold cyan link https://github.com/Snipeur060/SpaceAI")
