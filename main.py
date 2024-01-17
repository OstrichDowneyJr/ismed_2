from GUI import PressureGUI

def main():
    app_instance = App()
    gui = PressureGUI(app_instance)
    gui.run()
    app_instance.close_connection()


if __name__ == '__main__':
    main()
