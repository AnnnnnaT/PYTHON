# import random
# import math
# from pprint import pp


# # ✔ Какие вещи есть у всех друзей кроме одного
# # и имя того, у кого данная вещь отсутствует

# friends = {'Tom':('food', 'ball', 'pen'), 'Chris': ('ball', 'shirt', 'book'), 'Alex':('coat', 'water', 'pen')}


# everybody_took = list(set(friends['Tom']).intersection(set(friends['Chris'])).intersection(set(friends['Alex'])))
# print(f"Everyone took: {','.join(str(x) for x in everybody_took)}")

# print()

# unique_T = list(set(friends["Tom"]).difference(set(friends["Chris"]).union(set(friends["Alex"]))))
# unique_C = list(set(friends["Chris"]).difference(set(friends["Alex"]).union(set(friends["Tom"]))))
# unique_A = list(set(friends["Alex"]).difference(set(friends["Chris"]).union(set(friends["Tom"]))))
# print(f"Tom's unique things:  {','.join(str(x) for x in unique_T)}")
# print(f"Chris's unique things: {', '.join(str(x) for x in unique_C)} ")
# print(f"Alex's unique things: {', '.join(str(x) for x in unique_A)} ")

# print()

# if list((set(friends['Tom']).intersection(set(friends['Alex']))).difference(set(friends['Chris']))):
#     print(f"Chris does'n have {', '.join(str(x) for x in list((set(friends['Tom']).intersection(set(friends['Alex']))).difference(set(friends['Chris']))))}")
# if list((set(friends['Chris']).intersection(set(friends['Alex']))).difference(set(friends['Tom']))):
#     print(f"Tom does'n have {', '.join(str(x) for x in list((set(friends['Chris']).intersection(set(friends['Alex']))).difference(set(friends['Tom']))))}")
# if list((set(friends['Tom']).intersection(set(friends['Chris']))).difference(set(friends['Alex']))):
#     print(f"Alex does'n have {', '.join(str(x) for x in list((set(friends['Tom']).intersection(set(friends['Chris']))).difference(set(friends['Alex']))))}")





# 1 


# my_list = [random.randint(0,10) for _ in range(25)]
# print(my_list)
# new_list = []
# for item in my_list:
#     if my_list.count(item) > 1:
#         if item not in new_list:
#             new_list.append(item)
# print(new_list)


# 2 


# text = """
# «Хромая судьба» — роман Аркадия и Бориса Стругацких, представитель «реалистической фантастики»'\
# в их творчестве, хотя и включающий мистические элементы. Написан в течение 1982 года, журнальная публикация последовала в 1986 году. \
# Обе сюжетные линии романа посвящены взаимоотношениям человека искусства с самодостаточным всевластным государством.\
# Герой «московских» глав Феликс Сорокин — немолодой «писатель военно-патриотической темы», многие детали биографии \
# которого навеяны жизненным путём Аркадия Стругацкого. Герой рукописи Сорокина — писатель Виктор Банев — проживает в\
# неизвестном исторически и территориально государстве, и неугоден властям. Феликс Сорокин в основном занят выпивкой с \
# приятелями-писателями и работой над постылым заказным сценарием, однако в ту январскую неделю 1982 года, когда происходит\
# действие, сталкивается с людьми и ситуациями, казалось бы, сошедшими со страниц его старых рукописей. Сначала он вынужден добывать
# соседу эликсир бессмертия, потом его принимают за инопланетянина, а затем в кафе писатель сталкивается с падшим ангелом, предлагающим 
# купить партитуру труб Страшного суда. Каждый из многочисленных сюжетов обрывается и в принципе не может иметь завершения, но все эти
# события мешают Сорокину добраться до Института лингвистических исследований, куда он обязан представить свои рукописи для изучения. 
# По вечерам Феликс неизменно возвращается к «Синей папке» — главному своему, сокровенному тексту, не предназначенному для печати.
# В мире писателя Банева («Синей папке») — нескончаемый дождь и город, населённый обывателями, детей которых отчуждают от родителей «мокрецы».
# Про этих существ в масках говорят, что они генетически больны, и при этом их курирует военная разведка. Виктор Банев оказывается 
# в этом городе фактически в ссылке, поскольку лично Господином   Президентом ему предложено «перестать бренчать». 
# Банев много рассуждает о ценности  творчества и пытается активно разобраться, что же происходит в таинственном городе. Когда Сорокин                            всё-таки добирается до Института, выясняется, что там установлена электронная машина, способная измерить
# ценность писательского труда. Компьютером распоряжается некий Михаил Афанасьевич, который заявляет, что его главная миссия — добиться, 
# чтобы Синяя папка была дописана и закончена, и читает несуществующий ещё финал. Банев оказывается свидетелем конца старого мира и 
# наступления нового, солнечного и яркого, в котором спиртное и наркотики обращаются в родниковую воду, рушатся бетонные крепости и 
# ржавеет оружие. Банев счастлив увидеть всё это, но новый мир не принадлежит ему, и он должен «не забыть вернуться».
# """.lower().replace(",", " ").replace(":", " ").replace("—", " ") \
#     .replace("!", " ").replace('»', " ").replace("«", " ") \
#     .replace("(", " ").replace(')', " ").replace(".", " ").split()

# my_dict = {}
# for i in text:
#     my_dict[i] = text.count(i)
# sorted_dict = sorted(my_dict.values(), reverse = True)
# new_sort_dict = sorted_dict[:10]

# new_dict = {}
# for i in new_sort_dict:
#     for key, value in my_dict.items():
#         if value == i:
#             new_dict[key] = i
# pp(new_dict)


# 3 


# things = {"fruits" : 0.5, "ball" : 0.7, "socks" : 0.2, "book" : 0.4, "sneakers" : 0.6, "water" : 1.5, "phone" : 0.2, "laptop" : 0.8}
# lifting_capacity = float(input("Input load capacity of backpack in kg: "))
# goods = 0
# backpack = []
# for key, value in things.items():
#     if goods + value < lifting_capacity:
#         backpack.append(key) 
#         goods += value 
# print(f'{backpack} - {goods} kg')
