import random
print("你好！这是一个异世界转生模拟器。\n")
name=input("首先告诉我你的名字吧！完成输入后按下回车，不要带标点符号哦。\n")
if name=="":
    print("虽然不知道你是手滑了还是什么情况，但总之你什么都没写！所以我现在给你随机一个名字！\n")
    name=random.choice(["无名氏","otaku","A","命定的勇者","艾丽莎"])
else:
    print("好的！正在生成中……\n")
species=["人类","精灵","天使","恶魔","龙","矮人","兽人","半兽人","地精","魔王","史莱姆","吸血鬼","猫娘","魅魔","元素精灵","龙娘","不死族"]
classes=["战士","法师","牧师","骑士","药剂师","工匠","医师","商人","神使","某人的使魔","奴隶","贵族","王族","学徒","预言的救世主","语言的诅咒之子","英雄","精神领袖","旅人","作家","艺术家"]
hairstyles=["白毛","红毛","蓝毛","灰毛","紫毛","绿毛","金发","银发","粉毛","黑毛","七彩发色","挑染","橙毛"]
eyecolors=["蓝瞳","红瞳","黑瞳","紫瞳","绿瞳","白瞳","粉瞳","金瞳","银瞳","七彩瞳色","盲眼","挡住一只眼睛","血红色眼睛"]
specie=random.choice(species)
classchosen=random.choice(classes)
hairstyle=random.choice(hairstyles)
eyecolor=random.choice(eyecolors)
print("你的异世界转生版本已经生成完毕了！\n")
print(f"你是{name}，是一个{hairstyle}{eyecolor}的{specie}，目前是{classchosen}。")