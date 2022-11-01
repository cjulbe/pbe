import gi
import threading
from puzzle1 import Rfid_RC522

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib

reader= Rfid_RC522()

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title= "Read your UID")
        self.set_border_width(10)
        
        #Create a box with vertical orientation
        self.box= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        #Create label with the right properties
        self.label= Gtk.Label(label="Please, login with your university card")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label.get_style_context().add_class('login_label')
        self.label.set_size_request(300,80)
        self.box.pack_start(self.label, True, True, 0)
        
        #Create Clear button
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked", self.clicked_clear)
        self.box.pack_start(self.button, True, True, 0)
        
        
        #Use Css to style with colors
        self.style_provider= Gtk.CssProvider()
        self.style_provider.load_from_path("/home/carlota/puzzle2/style.css")
        self.context= Gtk.StyleContext()
        self.screen= Gdk.Screen.get_default()
        self.context.add_provider_for_screen(self.screen,self.style_provider,
                                                 Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
         
        self.button.set_sensitive(False)
        
        #Start the first thread
        thread= threading.Thread(target=self.read_uid)
        thread.setDaemon(True)
        self.thread_use=True
        thread.start()
    
    #Returns to the login screen and restarts the thread
    def clicked_clear(self,widget):
            if self.thread_use is False:
                self.thread_use=True
                #Change the label text
                self.label.set_label("Please, login with your university card")
                #Change of color
                self.label.get_style_context().remove_class('uid_label')
                self.label.get_style_context().add_class('login_label')
                
                #Create thread
                thread= threading.Thread(target=self.read_uid_queue)
                thread.setDaemon(True)
                thread.start()
            
                self.button.set_sensitive(False)
                
    #Reads the scanned uid and returns its value on screen    
    def read_uid(self):
        uid= reader.read_uid()

        self.label.get_style_context().remove_class('main_label')
        self.label.get_style_context().add_class('uid_label')
        
        #Enable clear button to be pressed
        self.button.set_sensitive(True)
        self.label.set_label("uid: "+uid)
        self.thread_use=False
        return False
    
    #Adds the function to the idle, to be called when there are not pending events
    def read_uid_queue(self):
        GLib.idle_add(self.read_uid)
        
window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
