import gi
import threading
from puzzle1 import Rfid_RC522

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title= "rfid_rc522.py")
        self.set_border_width(10)
        
        #Create a box with vertical orientation
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        #Create label with the right properties
        self.label= Gtk.Label(label="Please, login with your university card")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.get_style_context().add_class('login_label')
        self.box.pack_start(self.label, True, True, 0)
        
        #Create Clear button
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked_clear)
        self.box.pack_start(self.button, True, True, 0)
        
        #Use Css to style 
        self.style_provider= Gtk.CssProvider()
        self.style_provider.load_from_path("/home/carlota/puzzle2/style.css")
        self.context= Gtk.StyleContext()
        self.screen= Gdk.Screen.get_default()
        self.context.add_provider_for_screen(self.screen,self.style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        
        #Disable use of the Clear button
        self.button.set_sensitive(False)
        
        #Start the threading
        thread= threading.Thread(target=self.read_uid)
        thread.setDaemon(True)
        thread.start()
        
    def clicked_clear(self,widget):
            #Change the label text
            self.label.set_label("Please, login with your university card")
            
            #Change of color
            self.label.get_style_context().add_class('uid_label')
            
            #Restart thread
            thread= threading.Thread(target=self.read_uid)
            thread.setDaemon(True)
            thread.start()
            
            #Disable use of the Clear button
            self.button.set_sensitive(False)
        
    def read_uid(self):
        reader= Rfid_RC522()
        uid= reader.read_uid()
        self.label.get_style_context().add_class('uid_label')
        #Enable clear button to be pressed
        self.button.set_sensitive(True)
        self.label.set_label("uid: "+uid)  

window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
