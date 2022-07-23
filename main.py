import pygame, sys, time, random, os, keyboard
import boot, webbrowser

boot.boot()

init_pos = []
posit = []
spell_correct = random.randint(0, 10)
LIVES = 10
UNHUNGRY = 10
UNTHIRSTY = 10
WEIGHT = 60
BMI = 19.5
BMI_STATUS = "normal"
COUNT = 0
BROKE = 0
B1ROKE = 0
status = "NORMAL"

xValue = random.randint(0, 20)
yValue = random.randint(0, 32)
posit.append(xValue)
posit.append(yValue)
init_pos.append(xValue)
init_pos.append(yValue)

BACKPACK = []
MEMOLIST = []
Treelist = ["Tree1", "Tree2", "Tree3", "Tree4", "Tree5", "Tree6"]
TreePosList = []

for i in range(4):
    TreePosList.append([])
    xValue = random.randint(0, 20)
    yValue = random.randint(0, 32)
    TreePosList[i].append(xValue)
    TreePosList[i].append(yValue)

def listen_move_main_world():
    print("\033[32;1m<GAME>\033[0m游戏初始化成功")
    print("\033[32;1m<GAME>\033[0m{}出生，地点为{}".format(name, init_pos))
    while True:
        move = input("\033[32;1m<GAME>\033[0m请输入方向、操作键、指令及发言：")
        if move == "w":
            posit[1] = posit[1] + 1
            print("\033[32;1m<GAME>\033[0m{}地点：{}".format(name, posit))
            if posit[1] > 32:
                """posit[1] = 31
                print("\03[32;1m<GAME>\03[0m边界限制：不能继续向上移动")"""
                print("\033[32;1m<GAME>\033[31;1m你死了！")
                print("\033[32;1m<GAME>\033[0m{}掉出了这个世界".format(name))
                break
                
        elif move == "s":
            posit[1] = posit[1] - 1
            print("\033[32;1m<GAME>\033[0m{}地点：{}".format(name, posit))
            if posit[1] < 0:
                """posit[1] = 1
                print("\03[32;1m<GAME>\03[0m边界限制：不能继续向下移动")"""
                print("\033[32;1m<GAME>\033[31;1m你死了！")
                print("\033[32;1m<GAME>\033[0m{}掉出了这个世界".format(name))
                break
                
        elif move == "a":
            posit[0] = posit[0] - 1
            print("\033[32;1m<GAME>\033[0m{}地点：{}".format(name, posit))
            if posit[0] < 0:
                """posit[0] = 1
                print("\03[32;1m<GAME>\03[0m边界限制：不能继续向左移动")"""
                print("\033[32;1m<GAME>\033[31;1m你死了！")
                print("\033[32;1m<GAME>\033[0m{}掉出了这个世界".format(name))
                break
                
        elif move == "d":
            posit[0] = posit[0] + 1
            print("\033[32;1m<GAME>\033[0m{}地点：{}".format(name, posit))
            if posit[0] > 20:
                """posit[0] = 19
                print("\03[32;1m<GAME>\03[0m边界限制：不能继续向右移动")"""
                print("\033[32;1m<GAME>\033[31;1m你死了！")
                print("\033[32;1m<GAME>\033[0m{}掉出了这个世界".format(name))
                break
                
        elif move == "i":
            try:
                if posit == TreePosList[0]:
                    if "Tree1" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵白桦树".format(name))
                elif posit == TreePosList[1]:
                    if "Tree2" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵杉树".format(name))
                elif posit == TreePosList[2]:
                    if "Tree3" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵松树".format(name))
                elif posit == TreePosList[3]:
                    if "Tree4" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵白桦树".format(name))
                elif posit == TreePosList[4]:
                    if "Tree5" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵杉树".format(name))
                elif posit == TreePosList[5]:
                    if "Tree6" in Treelist:
                        print("\033[32;1m<GAME>\033[0m{}正前方有一棵杉树".format(name))
                else:
                    print("\033[32;1m<GAME>\033[0m{}正前方没有物体".format(name))
            except IndexError:
                print("\033[32;1m<GAME>\033[0m{}正前方没有物体".format(name))
            
        elif move == "t":
            try:
                if posit == TreePosList[0]:
                    if "Tree1" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的白桦树被砍掉，获得2个白桦树皮和3个白桦树实心".format(TreePosList[0]))
                        BACKPACK.append("WHITETSUR")
                        BACKPACK.append("WHITETSUR")
                        BACKPACK.append("WHITETCUB")
                        BACKPACK.append("WHITETCUB")
                        BACKPACK.append("WHITETCUB")
                        Treelist.remove("Tree1")
                        TreePosList.remove(TreePosList[0])
                elif posit == TreePosList[1]:
                    if "Tree2" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的杉树被砍掉，获得3个杉树树皮和4个杉树木块".format(TreePosList[1]))
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        Treelist.remove("Tree2")
                        TreePosList.remove(TreePosList[1])
                elif posit == TreePosList[2]:
                    if "Tree3" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的松树被砍掉，获得4个松树树叶和2个松果".format(TreePosList[2]))
                        BACKPACK.append("SONGLEAF")
                        BACKPACK.append("SONGLEAF")
                        BACKPACK.append("SONGLEAF")
                        BACKPACK.append("SONGLEAF")
                        BACKPACK.append("SONGFRUIT")
                        BACKPACK.append("SONGFRUIT")
                        Treelist.remove("Tree3")
                        TreePosList.remove(TreePosList[2])
                elif posit == TreePosList[3]:
                    if "Tree4" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的白桦树被砍掉，获得2个白桦树皮和3个白桦树实心".format(TreePosList[3]))
                        BACKPACK.append("WHITETSUR")
                        BACKPACK.append("WHITETSUR")
                        BACKPACK.append("WHITETCUB")
                        BACKPACK.append("WHITETCUB")
                        BACKPACK.append("WHITETCUB")
                        Treelist.remove("Tree4")
                        TreePosList.remove(TreePosList[3])
                elif posit == TreePosList[4]:
                    if "Tree5" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的杉树被砍掉，获得4个杉树树皮和1个杉树木块".format(TreePosList[4]))
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        Treelist.remove("Tree5")
                        TreePosList.remove(TreePosList[4])
                elif posit == TreePosList[5]:
                    if "Tree6" in Treelist:
                        print("\033[32;1m<GAME>\033[0m位于{}的杉树被砍掉，获得2个杉树树皮和5个杉树木块".format(TreePosList[5]))
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTSUR")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        BACKPACK.append("SHANTBLO")
                        Treelist.remove("Tree6")
                        TreePosList.remove(TreePosList[5])
            except IndexError:
                pass
            else:
                pass
        elif len(BACKPACK) > 40:
            print("\033[32;1m<GAME>\033[0m您的背包过满，请清理您的背包。")
            
        elif move == "/freecreate.game.GAME@.info.treelist":
            print("\033[32;1m<@>\033[0m{}".format(TreePosList))
        
        elif move == "/freecreate.help":
            webbrowser.open("help.html")
        
        else:
            print("\033[32;1m<{}>\033[0m{}".format(name, move))
            
if spell_correct == 1:
    gname = "FreeCreat"
else:
    gname = "FreeCreate"

name = input("\033[32;1m<GAME>\033[0m欢迎游玩 %s v0.001！请输入您的姓名："%(gname))
pid = random.randint(100000, 999999)
print("\033[32;1m<GAME>\033[0m登录完毕！%s！您的ID号码为%d！"%(name, pid))
time.sleep(2)
print("\033[32;1m<GAME>\033[0m尽情享受这个世界吧！")
time.sleep(2)
listen_move_main_world()
