import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)
        self.panel = wx.Panel(self)
        self.SetMinSize((400, 600))
        self.MakeLoginPage()
        self.Centre()

    def MakeRegisterPage(self):
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        header_hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(header_hbox, flag = wx.ALIGN_CENTRE)
        title = wx.StaticText(self.panel, label = "REGISTER", style = wx.ALIGN_CENTER)
        title.SetFont(wx.Font(36, family = wx.DECORATIVE, style = wx.NORMAL, weight = wx.LIGHT))
        header_hbox.Add(title, flag = wx.EXPAND)
        
        self.panel.SetSizer(vbox)

    def MakeLoginPage(self):
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        header_hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(header_hbox, flag = wx.ALIGN_CENTRE)
        title = wx.StaticText(self.panel, label = "MEMBER", style = wx.ALIGN_CENTER)
        title.SetFont(wx.Font(36, family = wx.DECORATIVE, style = wx.NORMAL, weight = wx.LIGHT))
        header_hbox.Add(title, flag = wx.EXPAND)
        
        vbox.Add((-1, 50))
        
        body_hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(body_hbox, flag = wx.ALIGN_CENTER)
        
        body_hbox.Add((10, -1))
        
        label_vbox = wx.BoxSizer(wx.VERTICAL)
        body_hbox.Add(label_vbox)
        
        name_label = wx.StaticText(self.panel, label = 'name:')
        name_label.SetFont(wx.Font(12, family = wx.MODERN, style = wx.NORMAL, weight = wx.NORMAL))
        label_vbox.Add(name_label)
        label_vbox.Add((-1, 10))
        password_label = wx.StaticText(self.panel, label = 'password:')
        password_label.SetFont(wx.Font(12, family = wx.MODERN, style = wx.NORMAL, weight = wx.NORMAL))
        label_vbox.Add(password_label)
        label_vbox.Add((-1, 10))
        
        body_hbox.Add(20, -1)
        
        tc_vbox = wx.BoxSizer(wx.VERTICAL)
        body_hbox.Add(tc_vbox)
        
        name_tc = wx.TextCtrl(self.panel)
        name_tc.SetFont(wx.Font(8, family = wx.MODERN, style = wx.NORMAL, weight = wx.NORMAL))
        tc_vbox.Add(name_tc)
        password_tc = wx.TextCtrl(self.panel)
        password_tc.SetFont(wx.Font(8, family = wx.MODERN, style = wx.NORMAL, weight = wx.NORMAL))
        tc_vbox.Add(password_tc)

        footer_hbox = wx.BoxSizer(wx.HORIZONTAL)
        footer_hbox.Add((250, -1))
        vbox.Add(footer_hbox)
        
        login_button = wx.Button(self.panel, label = "login", size = (50, 25))
        login_button.SetFont(wx.Font(12, family = wx.ROMAN, style = wx.NORMAL, weight = wx.NORMAL))
        
        def LOGIN_ONCLICK(e):
            print(name_tc.GetValue(), '\t', password_tc.GetValue())
        
        self.Bind(wx.EVT_BUTTON, LOGIN_ONCLICK, login_button)
        footer_hbox.Add(login_button, flag = wx.ALIGN_CENTER)
        
        footer_hbox.Add((5, -1))
        
        register_button = wx.Button(self.panel, label = 'register', size = (65, 25))
        register_button.SetFont(wx.Font(12, family = wx.ROMAN, style = wx.NORMAL, weight = wx.NORMAL))
        
        def REGISTER_ONCLICK(e):
            vbox.Clear(True)
            self.MakeRegisterPage()
        self.Bind(wx.EVT_BUTTON, REGISTER_ONCLICK, register_button)
        footer_hbox.Add(register_button)
        
        self.panel.SetSizer(vbox)



def main():

    app = wx.App()
    ex = Example(None, title="LOGIN DEMO")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()