Terminal Commands Used

* supo apt install- install a file/program
* ls- indicates which files are in a directory
* cd- commands to go to directory
* touch- create a new file in a directory
* open- open a file in a directory
* mkdir- make directory
* rm - delete files

GIT Commands Used

* git clone- clone a repository
* git commit - commit changes
   
  
gh auth login
git clone https://github.com/KshitijThareja/TerminalWizard.git
cd TerminalWizard
mkdir codes

TerminalWizard$ ls
01  02  03  04  05  06  07  08  assets  codes  Readme.md  spellbook  Steps.md
TerminalWizard$ cd spellbook

First Challenge<br/><br/>
Directory = 06, Spell_05 : Impedimenta

TerminalWizard/spellbook$ python3 Impedimenta.py
    None (@AdarshS05), you are about to use the Impedimenta spell. Are you sure this is the right one?
    If yes, then the secret code assosciated with it is:
    aHR0cHM6Ly9naX
TerminalWizard$ cd codes
TerminalWizard$ touch Part_02.txt

 
Second Challenge<br/><br/>
Directory = 02, Spell_03 : Stupefy

TerminalWizard/spellbook$ python3 Stupefy.py


    None (@AdarshS05), you are about to use the Stupefy spell. Are you sure this is the right one?
    If yes, then the secret code assosciated with it is:
    RodWIuY29tL1RoZ
TerminalWizard$ cd codes
TerminalWizard$ touch Part_03.txt

Third Challenge<br/><br/>
TerminalWizard/spellbook$ git branch -a
* (HEAD detached at origin/defenseAgainstTheDarkArts)
  main
  remotes/origin/HEAD -> origin/main
  remotes/origin/defenseAgainstTheDarkArts
  remotes/origin/divination
  remotes/origin/herbology
  remotes/origin/historyOfMagic
  remotes/origin/main
  remotes/origin/potions
  remotes/origin/thegraveyard
  remotes/origin/transfiguration
  
TerminalWizard/spellbook$ git checkout remotes/origin/defenseAgainstTheDarkArts
HEAD is now at 866abd0 Add files from main branch

TerminalWizard/spellbook$ python3 Riddikulus.py

    None (@AdarshS05), you have found the right spell. As a part of your reward for solving the riddle,
    here is the secret code assosciated with it: Uh1bnRzbWFuNC9U
    
TerminalWizard$ cd codes
TerminalWizard$ touch Part_04.txt

Fourth Challenge<br/><br/>
TerminalWizard/spellbook$ git commit

TerminalWizard/spellbook$ git checkout remotes/origin/thegraveyard
Previous HEAD position was 866abd0 Add files from main branch
HEAD is now at 9c5ce2b Add files from main branch

TerminalWizard/spellbook$ python3 'Priori Incantatem.py' 

    None (@AdarshS05), you are about to initiate the Priori Incantatem. Are you sure it?
    If yes, then the secret code assosciated with it is:
    aGVGaW5hbFNwZWxs
    
TerminalWizard$ cd codes
TerminalWizard$ touch Part_05.txt

The End<br/><br/>
TerminalWizard/spellbook$ echo AHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs | base64 --decode
https://github.com/TheHuntsman4/TheFinalSpell

FinalSpell
git clone https://github.com/TheHuntsman4/TheFinalSpell
Cloning into 'TheFinalSpell'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
adarsh@adarsh-VirtualBox:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  snap  Templates  TerminalWizard  TheFinalSpell  Videos
$ cd TheFinalSpell
TheFinalSpell$ python3 TheOneThatEndsItAll.py

        None (@AdarshS05)

        You have just informed the wizarding world of the greatest
        threat that looms over them, that is, Voldemort. You did the right thing by informing about it to Dumbledore, 
        one of the greatest wizard of all times. He'll help you and the wizarding world in this battle against evil.
        This marks the end of the Terminal Wizard. 
        Keep up the good work!!!
        

TerminalWizard$ cd codes
TerminalWizard$ rm Part_02.txt
TerminalWizard$ rm Part_03.txt
TerminalWizard$ rm Part_04.txt
TerminalWizard$ rm Part_05.txt
TerminalWizard$ touch finalcode.txt


