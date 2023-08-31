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
   
  
gh auth login<br/>
git clone https://github.com/KshitijThareja/TerminalWizard.git<br/>
cd TerminalWizard<br/>
mkdir codes<br/>

TerminalWizard$ ls<br/>
01  02  03  04  05  06  07  08  assets  codes  Readme.md  spellbook  Steps.md<br/>
TerminalWizard$ cd spellbook<br/><br/>

First Challenge<br/><br/>
Directory = 06, Spell_05 : Impedimenta<br/>

TerminalWizard/spellbook$ python3 Impedimenta.py<br/>
    None (@AdarshS05), you are about to use the Impedimenta spell. Are you sure this is the right one?
    If yes, then the secret code assosciated with it is:
    aHR0cHM6Ly9naX
TerminalWizard$ cd codes<br/>
TerminalWizard$ touch Part_02.txt<br/><br/>

 
Second Challenge<br/><br/>
Directory = 02, Spell_03 : Stupefy<br/>

TerminalWizard/spellbook$ python3 Stupefy.py<br/>


    None (@AdarshS05), you are about to use the Stupefy spell. Are you sure this is the right one?
    If yes, then the secret code assosciated with it is:
    RodWIuY29tL1RoZ
TerminalWizard$ cd codes<br/>
TerminalWizard$ touch Part_03.txt<br/>

Third Challenge<br/><br/>
TerminalWizard/spellbook$ git branch -a<br/>
* (HEAD detached at origin/defenseAgainstTheDarkArts)<br/>
  main<br/>
  remotes/origin/HEAD -> origin/main<br/>
  remotes/origin/defenseAgainstTheDarkArts<br/>
  remotes/origin/divination<br/>
  remotes/origin/herbology<br/>
  remotes/origin/historyOfMagic<br/>
  remotes/origin/main<br/>
  remotes/origin/potions<br/>
  remotes/origin/thegraveyard<br/>
  remotes/origin/transfiguration<br/>
  
TerminalWizard/spellbook$ git checkout remotes/origin/defenseAgainstTheDarkArts<br/>
HEAD is now at 866abd0 Add files from main branch<br/>

TerminalWizard/spellbook$ python3 Riddikulus.py<br/>

    None (@AdarshS05), you have found the right spell. As a part of your reward for solving the riddle,
    here is the secret code assosciated with it: Uh1bnRzbWFuNC9U
    
TerminalWizard$ cd codes<br/>
TerminalWizard$ touch Part_04.txt<br/><br/>

Fourth Challenge<br/><br/>
TerminalWizard/spellbook$ git commit

TerminalWizard/spellbook$ git checkout remotes/origin/thegraveyard<br/>
Previous HEAD position was 866abd0 Add files from main branch<br/>
HEAD is now at 9c5ce2b Add files from main branch<br/>

TerminalWizard/spellbook$ python3 'Priori Incantatem.py' <br/>

    None (@AdarshS05), you are about to initiate the Priori Incantatem. Are you sure it?
    If yes, then the secret code assosciated with it is:
    aGVGaW5hbFNwZWxs
    
TerminalWizard$ cd codes<br/>
TerminalWizard$ touch Part_05.txt<br/><br/>

The End<br/><br/>
TerminalWizard/spellbook$ echo AHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs | base64 --decode<br/>
https://github.com/TheHuntsman4/TheFinalSpell<br/><br/>

'''FinalSpell'''
git clone https://github.com/TheHuntsman4/TheFinalSpell
Cloning into 'TheFinalSpell'...<br/>
remote: Enumerating objects: 6, done.<br/>
remote: Counting objects: 100% (6/6), done.<br/>
remote: Compressing objects: 100% (6/6), done.<br/>
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0<br/>
Receiving objects: 100% (6/6), done.<br/>
adarsh@adarsh-VirtualBox:~$ ls<br/>
Desktop  Documents  Downloads  Music  Pictures  Public  snap  Templates  TerminalWizard  TheFinalSpell  Videos<br/>
$ cd TheFinalSpell<br/>
TheFinalSpell$ python3 TheOneThatEndsItAll.py<br/>

        None (@AdarshS05)

        You have just informed the wizarding world of the greatest
        threat that looms over them, that is, Voldemort. You did the right thing by informing about it to Dumbledore, 
        one of the greatest wizard of all times. He'll help you and the wizarding world in this battle against evil.
        This marks the end of the Terminal Wizard. 
        Keep up the good work!!!
        

TerminalWizard$ cd codes<br/>
TerminalWizard$ rm Part_02.txt<br/>
TerminalWizard$ rm Part_03.txt<br/>
TerminalWizard$ rm Part_04.txt<br/>
TerminalWizard$ rm Part_05.txt<br/>
TerminalWizard$ touch finalcode.txt<br/>


