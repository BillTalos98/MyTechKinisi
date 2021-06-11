from functions import function

map =function.window()
map_image=map.photo("/home/boss/PycharmProjects/App/map/map.png",390,400,0.01,0.05)
button_reset = map.app_button("Change Route",0.35,0.95)

map.run()