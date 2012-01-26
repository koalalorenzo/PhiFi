#!/usr/bin/python
# -*- coding=utf-8 -*-
#
#   Copyright 2011, 2012 Lorenzo Setale
#   See: http://www.koalalorenzo.com/2011/04/13/ancora-lamerozzi/
#   Do not modify without Lorenzo's permissions.
#   THIS SOFTWARE IS NOT OPENSOURCE!
#   

class Window(object):
    """
    This class manages, builds and destroys the windows.
    """
    def __init__(self, database_path="database.sql"):
        seself.window = gtk.Window()
        self.window.set_title("NoLamer.com Client 0.1")
        self.__icon = self.window.render_icon(gtk.STOCK_ORIENTATION_PORTRAIT, gtk.ICON_SIZE_MENU)
        self.window.set_icon(self.__icon)
        self.window.set_size_request(300,400)
        self.window.set_resizable(False)
        self.window.connect("destroy", self.destroy)

        self.convert_button = gtk.ToolButton(gtk.STOCK_UPDATE)
        self.convert_button.connect("clicked", self.__convert)

        self.about_button = gtk.ToolButton(gtk.STOCK_ABOUT)
        self.about_button.connect("clicked", self.__about)
        
        self.panel_bar = gtk.Toolbar()
        self.panel_bar.add(self.convert_button)
        self.panel_bar.add(self.about_button)
        
        self.webkit = webkit.WebView()
        self.webkit.connect("populate-popup", self.__hide_menu)

        self.scroll_box = gtk.ScrolledWindow()
        self.scroll_box.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        self.scroll_box.add(self.webkit)

        self.__vbox = gtk.VBox(False, 0)
        self.__vbox.pack_start(self.scroll_box, True)
        self.__vbox.pack_start(self.panel_bar, False)
        self.window.add(self.__vbox)
        self.__disable_input()
        self.forward_button.set_sensitive(False)
        self.window.show_all()

        self.show_intro_page()


    def __hide_menu(self, view, menu):
        if not self.webkit.get_editable():
            menu.destroy()

    def __change_page(self, view=None, menu=None): self.show_page(int(self.number_entry.get_text()))
        
    def __go_back(self, view=None, menu=None):
        self.show_page(self.__number - 1)

    def __about(self, view=None, menu=None):
        about = gtk.AboutDialog()
        about.set_program_name("NoLamer.com Client")
        about.set_version("0.1")
        about.set_copyright("(c) Lorenzo Setale")
        about.set_comments("Fight the stupid spam and phish")
        about.set_website("http://nolamer.com")
        about.set_logo(self.window.render_icon(gtk.STOCK_ORIENTATION_PORTRAIT, gtk.ICON_SIZE_DIALOG))
        about.run()
        about.destroy()

    def __convert(self, view=None, menu=None): 
        return

    def __disable_input(self):
        self.webkit.set_editable(False)

    def show_page(self, anumber):
        self.__disable_input()
        self.manager.get_pages()
        if int(anumber) >= len(self.manager.pages.keys()):
            anumber = len(self.manager.pages.keys())
            self.back_button.set_sensitive(True)
            self.forward_button.set_sensitive(False)
        elif int(anumber) <= 1:
            anumber = 1
            self.back_button.set_sensitive(False)
            self.forward_button.set_sensitive(True)
        else:
            self.back_button.set_sensitive(True)
            self.forward_button.set_sensitive(True)
        self.webkit.load_string("<html>\n%s</html>" % self.manager.pages[anumber].text.replace("&amp;nbsp;"," "), "text/html", "iso-8859-15", "new-page")
        self.__number = anumber
        self.number_entry.set_text(str(anumber))

    def quit(self, widget=None, data=None):
        self.destroy()

    def destroy(self, widget=None, data=None):
        self.manager.close()
        gtk.main_quit()
