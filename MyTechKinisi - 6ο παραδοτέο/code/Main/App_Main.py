from functions import function
app_interface=function.window()
main_image=app_interface.photo('~/PycharmProjects/App/logo.png',270,250,0.15,0.05)
entry_user=app_interface.add_input(0.24,350,200,25)
entry_password=app_interface.add_input(0.24,380,200,25)
button_reset = app_interface.app_button("Login",0.40,0.75)
app_interface.run()

